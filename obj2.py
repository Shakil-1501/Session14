import math
from obj1 import Polygon

class Polygons:
    def __init__(self, m, R):
        if m < 3:
            raise ValueError('m must be greater than 3')
        self._m = m
        self._R = R
        
        
    def __len__(self):
        return self._m - 2
    
    
        
        
    
    
    
    def __iter__(self):
        return self.PolyIter(self)
    
    class PolyIter():
        def __init__(self,other):
            self._index = len(other)
            self._R = other._R
            self._base = 2
            
        def __iter__(self):
            return self
        
        def __next__(self):
            
            
            if self._index<=0:
                raise StopIteration
            else:
                self._base  += 1
                self._index -= 1
                pg = Polygon( self._base, self._R)
                return pg
                
                
                
            
            
    
    