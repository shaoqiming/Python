
def checkIndex(key):
    if not isinstance(key,(int,long)):raise TypeError
    if key<0:raise IndexError


class ArithmeticSequence:
    def __init__(self,start=0,step=1):
        self.start=start
        self.step=step
        self.changed={}
    def __getitem__(self,key):
        checkIndex(key)
        try:return self.changed[key]
        except KeyError:
            return self.start+key*self.step
    def __setitem__(self,key,value):      
        checkIndex(key)
        self.changed[key]=value


s=ArithmeticSequence(1,2);
print s[4]



#子类化
class CountList(list):
    def __init__(self,*args):
        super(CountList,self).__init__(*args)
        self.counter=0
    def __getitem__(self,index):
        self.counter+=1
        return super(CountList,self).__getitem__(index)