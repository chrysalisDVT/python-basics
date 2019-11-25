class VariableScopeTest:
    x=10

    def test_local_scope(self):
        global x
        x='hello'
        print('The value of x:{0}'.format(x))
    
    def test_non_local_scope(self):
        x="hello world"
        def nested_func():
            nonlocal x
            print("Nonlocal x:{0}".format(x))
        nested_func()

def test_var_scope():
    var_test=VariableScopeTest()
    var_test.test_local_scope()
    var_test.test_non_local_scope()

if __name__ =="__main__":
    test_var_scope()
