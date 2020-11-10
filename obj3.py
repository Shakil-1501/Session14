from obj1 import Polygon

class Polygons:
    def __init__(self, m, R):
        if m < 3:
            raise ValueError('m must be greater than 3')
        self._m = m
        self._R = R
        self._polygons = [Polygon(i, R) for i in range(3, m+1)]
        
    def __len__(self):
        return self._m - 2
    '''
    def __repr__(self):
        return f'Polygons(m={self._m}, R={self._R})'
        
    '''    
    
    def __getitem__(self, s):
        return self._polygons[s]
    
    def __iter__(self):
        return self.PolyIter(self._m,self._R)
    
    class PolyIter():
        def __init__(self,m,R):
            self._m = m
            self._R = R
            self._polygons = [Polygon(i, R) for i in range(3, m+1)]
            self.i=len(self._polygons)-1
            
        def __iter__(self):
            return self
        
        def __next__(self):
            
            
            if self.i<=0:
                raise StopIteration
            else:
                result=self._polygons[self.i]
                self.i-=1
                return result
                
                
                
            
            
    
    @property
    def max_efficiency_polygon(self):
        sorted_polygons = sorted(self._polygons, 
                                 key=lambda p: p.area/p.perimeter,
                                reverse=True)
        return sorted_polygons[0]