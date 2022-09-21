import punto
class rectangulo:
    def __init__(self,punto1,punto2):
        self.punto1 = punto1
        self.punto2 = punto2
    def base(self):
        punto1=punto(self.punto1.x,self.punto1.y)
        punto2=punto(self.punto2.x,self.punto1.y)
        print(f'la base va desde {punto1} hasta {punto2}')
    def longitud_base(self):
        punto1=punto(self.punto1.x,self.punto1.y)
        punto2=punto(self.punto2.x,self.punto1.y)
        return punto1.distancia(punto2.x,punto2.y)
    def altura(self):
        punto1=punto(self.punto1.x,self.punto1.y)
        punto2=punto(self.punto1.x,self.punto2.y)
        print(f'la base va desde {punto1} hasta {punto2}')
    def longitud_altura(self):
        punto1=punto(self.punto1.x,self.punto1.y)
        punto2=punto(self.punto1.x,self.punto2.y)
        return punto1.distancia(punto2.x,punto2.y)
    def area(self):
        a=(self.longitud_base()*self.longitud_altura())/2
        print(f'el area es: {a}')