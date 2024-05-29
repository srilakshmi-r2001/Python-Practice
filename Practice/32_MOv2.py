class GeoShapes:
    def area(self,a=None,b=None):
        if(a!=None and b!=None):
            print("Area of Rectangle:",a*b)
        
        elif(a!=None and b==None):
            print("Area of Square:",a*a)

        else:
            return 0
        
GS=GeoShapes()
val=GS.area()
print(val)
GS.area(5)
GS.area(5,6)