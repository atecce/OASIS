class test():
    def __init__(self, value,timestamp):
        self.value = value
        self.timestamp = timestamp
        
test_dict={"one":test(1,"time_1"),"two":test(2,"time_2")}
#print test_dict
print "NOW"
#print type (test_dict["one"])
#print (type (test_dict["one"]) is 'instance')
print isinstance(test_dict["one"],test)
i=1

"""while(i):
    for key,val in test_dict.iteritems():
        print key
        print val.value
        print val.timestamp
    i=0;"""
x=True
print type(x)
print type(x) is bool
