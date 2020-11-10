import math

class Polygon:
    def __init__(self,n,R):
        self.edges=n
        self.circumradius = R
    
    
    @property
    def edges(self):
        return self._edges
    
    @edges.setter
    def edges(self,new_edge):
        if new_edge<=0:
            raise ValueError("edges must be positive")
        else:
            self._edges=new_edge
            self._ia = None
            self._el=  None
            self._ap=None
            self._ar=None
            self._pr=None
            
    @property
    def circumradius(self):
        return self._circumradius
    
    @circumradius.setter
    def circumradius(self,new_circumradius):
        if new_circumradius<=0:
            raise ValueError("circumradius must be positive")
        else:
            self._circumradius=new_circumradius       
            
   
    
    @property
    def interiorangle(self):
        if self._ia is None:
            print("Calculating interior angle")
            self._ia = ((self._edges-2)*(180))/self._edges
            
        return self._ia
            
            
      
    
    @property
    def edgelength(self):
        if self._el is None:
            print("Calculating edgelength")
            self._el = 2*(self._circumradius)*(math.sin(math.pi/self._edges))
            
        return self._el    
    
    
    @property
    def apothem(self):
        if self._ap is None:
            print("Calculating apothem")
            self._ap = (self._circumradius)*(math.cos(math.pi/self._edges))
        return self._ap
    
    @property
    def area(self):
        if self._ar is None:
     
            print("Calculating area")
            self._ar=(1/2)*(self._edges*self._el*self._ap)
        return self._ar
    
    
    
    @property
    def perimeter(self):
        if self._pr is None:
            print("Calculating perimeter")
            self._pr = (self._edges*self._el)
        return self._pr
        
        
        
        
            
            
     
    def __repr__(self):
        return 'Polygon({0},{1})'.format(self.edges,self.circumradius)
    def __eq__(self,other):
        if isinstance(other,Polygon):
            return self.edges==other.edges and self.circumradius==other.circumradius
    def __gt__(self,other):
        if isinstance(other,Polygon):
            return self.edges > other.edges
        else:
            return False