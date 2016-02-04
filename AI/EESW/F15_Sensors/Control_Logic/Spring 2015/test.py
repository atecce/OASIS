def case1():
    print "one"
    return
def case2():
    print "two"
    return
test_dict={}
test_dict[case1]=case1
test_dict[case2]=case2

test_dict[case1]()
