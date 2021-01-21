import json
import datetime
import time
import threading
import logging
from random import randrange
from functools import wraps
from dataclasses import dataclass

logging.basicConfig(format='[%(levelname)s]:%(message)s',level=logging.INFO)
logger=logging.getLogger(__name__)

class MethodTimeoutException(Exception):
    def __init__(self,message,error_code="TIMEOUT_001"):
        super(MethodTimeoutException,self).__init__(message)
        self.message=message
        self.error_code=error_code

class AysncProcessor(threading.Thread):
    def __init__(self,func,args=None):
        super(AysncProcessor,self).__init__()
        self._func=func
        self.response=None
        self.functionState={'state':True,'message':''}
        self._args=args

    def run(self):
        try:
            self.response=self._func(*self._args)
        except Exception as e:
            self.functionState['state']=False
            self.functionState['message']=str(e)

@dataclass
class RetryProps:
    attempts:int
    timeout:int
    exception:Exception
    default_backoff:int

class LifeCycleHandler:
    def __init__(self,func,*,retry_props:RetryProps=None,exception:Exception,cleanup,force_cleanup=False):
        self._retry_props=retry_props
        self._counter=0
        self._func=func
        self._cleanup=cleanup
        self._exception=exception
        self._force_cleanup=force_cleanup

    @staticmethod
    def get_delay(attempt):
        '''Exponential backoff with jitter '''
        return randrange(1,5)+2**attempt

    def without_retry(self,*args,**kwargs):
        response=None
        try:
            response=self._func(*args,**kwargs)
        except self._exception as ex:
            logging.error(f'Exception{str(ex)} occurred while executing {self._func.__name__}')
            self._cleanup(args[0])
        finally:
            if self._cleanup:
                self._cleanup(args[0])
        return response


    def with_retry(self,*args,**kwargs):
        while True:
            try:
                if self._retry_props._timeout>0:
                    #TODO:Handling thread closure gracefully
                    process_thread=AysncProcessor(self._func,args=args)
                    process_thread.start()
                    process_thread.setDaemon(True)
                    process_thread.join(self._retry_props._timeout)
                    if process_thread.is_alive():
                        raise MethodTimeoutException(f"[{self._func.__name__}] timed out")
                    if process_thread.functionState['state']:
                        response=process_thread.response
                    else:
                        raise Exception(process_thread.functionState['message'])
                    return response
                else:
                    response=self._func(*args,**kwargs)
                    return response
            except (self._retry_props._exception,MethodTimeoutException) as e:
                logger.error(f'Exception [{str(e)}] occurred while execution')
                if self._counter<self._retry_props.attempt:
                    self._counter+=1
                    logger.warning(f'Retrying {self._func.__name__}(), retry remaining {self._retry_props.attempt-self._counter}')
                    backoff=LifeCycleHandler.get_delay(self._counter)
                    logger.warning(f'Waiting for {min(backoff,self._retry_props._default_backoff)}')
                    time.sleep(min(backoff,self._retry_props._default_backoff))
                else:
                    logger.error(f'All retry attempts were exhausted')
                    if self._cleanup:
                        self._cleanup(args[0])
                    raise e
            finally:
                if self._cleanup:
                    self._cleanup(args[0])

    def __call__(self,*args,**kwargs):
        args_repr = [repr(a) for a in args]                      
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        logger.info(f'Invoking {signature}')
        start=time.perf_counter()
        if self._retry_props:
            self.with_retry(*args,**kwargs)
        else:
            self.without_retry(*args,**kwargs)
        logger.info(f'{signature} completed....time taken {time.perf_counter()-start}s')

        
def lifecycle_handler(retry_props:RetryProps=None,exception=Exception,cleanup=None):
    def _retry_wrapper(func):
        if retry_props:
            return LifeCycleHandler(func,exception=exception,retry_props=retry_props,cleanup=cleanup)
        else:
            return LifeCycleHandler(func,exception=exception,cleanup=cleanup)
    return _retry_wrapper
