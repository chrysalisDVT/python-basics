import boto3
import re
from  hvac_util import access_key,access_secret

def filter_services(service):
    """
    Filters the service list from aws to help the user to create a client

    List being filtered
    [apigateway,apigatewayv2,s3,....]

    Sample Input: 
        api
    
    Sample Output:
        [apigateway,apigatewayv2]
    """
    pattern=re.compile("{0}*".format(service_key))
    if pattern.match(service):
        return True
    else:
        return False
    
#Creating the aws session
aws_session=boto3.Session(aws_access_key_id=access_key,aws_secret_access_key=access_secret)
services=aws_session.get_available_services()

while True:
    service_key=input("Please provide the service name which you want to monitor?")
    #filtering the list based on the user input
    filtered_service_list=filter(filter_services,services)
    for service in filtered_service_list:
        print(service)
    if input("Do you received your service ?(Y/N)") is 'Y' or 'y':
        try:
            aws_service_client=aws_session.client(service_key)
            break
        except Exception as error:
            print("The service does not exist, please select again....\n {0}".format(error))
            continue


print(aws_service_client.list_buckets())
#Creating the aws client for the service selected by the user


