import math
class punto:
    def __init__(self,x,y):
        if x==None:
            self.x=0
        else:
            self.x=x
        if y==None:
            self.y==0
        else:
            self.y=y
    def __str__(self):
        return f'({self.x},{self.y})'
    def cuadrante(self):
        if self.x>0 and self.y>0:
            print(f'El punto se encuentra en el primer cuadrante')
        elif self.x<0 and self.y>0:
            print(f'El punto se encuentra en el segundo cuadrante')
        elif self.x<0 and self.y<0:
            print(f'El punto se encuentra en el tercer cuadrante')
        elif self.x>0 and self.y<0:
            print(f'El punto se encuentra en el cuarto cuadrante')
        elif self.x==0 and self.y!=0:
            print('El punto esta en el eje Y')
        elif self.x!=0 and self.y==0:
            print('El punto esta en el eje X')
        else:
            print('El punto esta en el origen de coordenadas')
    def vector(self,x,y):
        print(f'el vector resultante es el ({self.x+x},{self.y+y})')
    def distancia(self,x,y):
        d=math.sqrt((x-self.x)^(2)+(y-self.y)^2)
