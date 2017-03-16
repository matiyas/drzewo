#!/usr/bin/env python
# -*- coding:utf-8 -*-

from math import sin
from math import cos
from math import radians
from random import randint


class Branch:
    def __init__(self, a, b, szerokosc, kolor):
        self.a = a
        self.b = b
        self.szerokosc = szerokosc
        self.kolor = kolor
        
    def __str__(self):
        return ('<path d="M{} {} L{} {}" stroke-width="{}" '
                'stroke="rgb({}, {}, {})"/>\n').format(
                    self.a[0], self.a[1], self.b[0], self.b[1], self.szerokosc,
                    self.kolor[0], self.kolor[1], self.kolor[2])
                             
                            
                             
def generuj_fraktal(dlugosc, kat, poziomy):
    kat = radians(-kat)
    grubosc = 35
    kolor = [100, 60, 0]
    a = [400, 800]
    b = [a[0], a[1]-dlugosc]
    fraktal = galezie = [Branch(a, b, grubosc, kolor)]
    
    for poziom in range(poziomy):
        dlugosc *= (2.0)/(3.0)
        grubosc = grubosc * (2.0/3.0) + 1
        kolor = [kolor[0], kolor[1] + 6, kolor[2]]
        nowe = []
        
        for galaz in galezie:
            x = galaz.b[0] + dlugosc * cos(kat)
            y = galaz.b[1] + dlugosc * sin(kat)
        
            nowe.append(Branch(galaz.b, [x, y], grubosc, kolor))
            nowe.append(Branch(galaz.b, [galaz.b[0], y], grubosc, kolor))
            nowe.append(Branch(galaz.b, [-x + 2*galaz.b[0], y], grubosc, kolor))
                    
            #kat = kat + randint(-1, 1) * randint(1, 10)
                    
        fraktal += nowe
        galezie = nowe
        
    return fraktal
                                         
 
                                            
def to_svg(galezie):
    content = '<svg xmlns="http://www.w3.org/2000/svg" version="1.1">\n'
    
    for galaz in galezie:
        content += str(galaz)
        
    return content + '</svg>'
    


with open('drzewo.svg', 'w') as svg:
    svg.write(to_svg(generuj_fraktal(200, 30, 2)))
