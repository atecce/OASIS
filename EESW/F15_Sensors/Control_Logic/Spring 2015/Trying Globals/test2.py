import global_test
#import test

def abcd():
    print global_test.dict_test
    global_test.dict_test["seven"]=7
def new_stuff():
    global_test.dict_test={}
    global_test.dict_test["eight"]=8
    print "We are also here"
    test.test2_abcd()
    
    
    
