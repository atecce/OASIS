import global_test
import test2

global_test.dict_test["five"]=5
global_test.dict_test["six"]=6
test2.new_stuff();

def print_bullshit():
    print "we here"
    print global_test.dict_test
def test2_abcd():
    print " Phase two"
    print global_test.dict_test




