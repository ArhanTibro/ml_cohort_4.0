class Rectangle:
    def __init__(self,l,b):
        self.l=l
        self.b=b
    def calculate(self):
        return self.l* self.b

L=float(input('enter length of the rectangle : '))
B=float(input('enter breadth of the rectangle : '))
rec=Rectangle(L,B)
area=f'area of the rectangle is : {rec.calculate()}'
print(area)


    