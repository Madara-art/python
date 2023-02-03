import numpy as np

class NumPyCreator:
    # @staticmethod
    def from_list(self,lst):
        if not isinstance(lst,list): #or not (all([isinstance(x,list) or isinstance(x,int) for x in lst])) or len(set([type(x) for x in lst])) != 1 :
            return None
        if lst and isinstance(lst[0],list):
            l = len(lst[0])
            for i in lst:
                if len(i) != l: #or not all([isinstance(x,int) for x in i]):
                    return None
        return np.array(lst)

    # @staticmethod
    def from_tuple(self,tpl):
        if not isinstance(tpl,tuple): # or not (all([isinstance(x,tuple) or isinstance(x,int) for x in tpl])) or len(set([type(x) for x in tpl])) != 1 :
            return None
        if tpl and isinstance(tpl[0],tuple):
            l = len(tpl[0])
            for i in tpl:
                if len(i) != l:# or not all([isinstance(x,int) for x in i]):
                    return None
        return np.array(tpl)

    # @staticmethod
    def from_iterable(self,itr):
        try:
            iter(itr)
            return np.array([x for x in itr])
        except:
            return None
    # @staticmethod
    def from_shape(self,shape, value = 0):
        if not isinstance(shape,tuple):
            return None
        return np.full(shape,value)
    # @staticmethod
    def random(self,shape):
        if not isinstance(shape,tuple):
            return None
        return np.random.rand(shape[0],shape[1])
    # @staticmethod
    def identity(self,n):
        if not isinstance(n,int):
            return None
        return np.identity(n)






