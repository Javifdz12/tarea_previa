from clases.punto import punto
from clases.rectangulo import rectangulo

@staticmethod
def lanzar(self):
    p1=punto(2,3)
    p2=punto(5,5)
    p3=punto(-3,-1)
    p4=punto()
    p1.cuadrante()
    p3.cuadrante()
    p4.cuadrante()
    p1.vector(p2.x,p2.y)
    p2.vector(p1.x,p1.y)
    p1.distancia(p2.x,p2.y)
    p2.distancia(p1.x,p1.y)
    rec=rectangulo(p1,p2)
    rec.base()
    rec.altura()
    rec.area()
