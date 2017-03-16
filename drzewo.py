#!/usr/bin/env python
# -*- coding:utf-8 -*-

from math import sin
from math import cos
from math import radians
from random import randint

__author__ = 'Damian Matyjaszek'

class Branch:
    '''Klasa reprezentująca jedną ścieżkę (path) w formacie SVG
    
    Atrybuty:
        start ([float, float]):     Współrzędne początku ścieżki przechowywane w formie 
                                    dwuelementowej listy.
        koniec ([float, float]):    Współrzędne końca ścieżki przechowywane w formie 
                                    dwuelementowej listy.
        kolor ([int, int, int]):    Kolor ścieżki w formacie RGB, przechowywany w formie
                                    tablicy, której elementy odpowiadają kolejno za barwę:
                                    czerwoną, zieloną, oraz niebieską.
        grubosc (float):            Grubość ścieżki.
        '''
    def __init__(self, start, koniec, grubosc, kolor):
        '''Konstruktor klasy Branch
        
        Tworzy nowy obiekt klasy branch.
        '''
        self.start = start
        self.koniec = koniec
        self.grubosc = grubosc
        self.kolor = kolor
        
    def __str__(self):
        '''Reprezentacja klasy w formacie SVG
        
        Metoda zwraca tekst będący ścieżką w formacie SVG, z początkiem w punkcie
        wskazywanym przez atrybut 'start' i końcem przez 'koniec'. Ścieżka ma grubość
        odpowiadającą wartości atrybutu 'grubosc', oraz kolor w formacie RGB za który
        odpowiada atrybut 'kolor'.
        ''' 
        return ('    <path d="M{} {} L{} {}" stroke-width="{}" '
                'stroke="rgb({}, {}, {})"/>\n').format(
                    self.start[0], self.start[1], self.koniec[0], self.koniec[1], 
                    self.grubosc, self.kolor[0], self.kolor[1], self.kolor[2])
                             
                            
                            
def generuj_fraktal(dlugosc, kat, poziomy):
    '''Funkcja generująca fraktal, będący drzewem
    
    
    Funkcja zwraca listę gałęzi, wraz z pniem, stanowiącą drzewo.
    
    
    Argumenty:
        dlugosc (float):    Długość pnia drzewa.
        kat (float):        Początkowy kąt nachylenia gałęzi.
        poziomy (int):      Liczba poziomów gałęzi.
    '''
    kat = radians(-kat)
    grubosc = 35
    kolor = [100, 60, 0]
    start = [400, 800]
    koniec = [start[0], start[1]-dlugosc]
    fraktal = galezie = [Branch(start, koniec, grubosc, kolor)]
    
    for poziom in range(poziomy):
        dlugosc *= (2.0)/(3.0)
        grubosc = grubosc * (2.0/3.0) + 1
        kolor = [kolor[0], kolor[1] + 6, kolor[2]]
        nowe = []
        
        for galaz in galezie:
            x = galaz.koniec[0] + dlugosc * cos(kat)
            y = galaz.koniec[1] + dlugosc * sin(kat)
        
            nowe += [Branch(galaz.koniec, [x, y], grubosc, kolor),
                     Branch(galaz.koniec, [galaz.koniec[0], y], grubosc, kolor),
                     Branch(galaz.koniec, [-x + 2*galaz.koniec[0], y], grubosc, kolor)]
        
            kat += randint(-1, 1) * randint(1, 360)
                    
        fraktal += nowe
        galezie = nowe
        
    return fraktal
                                         
 
                                            
def to_svg(galezie):
    content = '<svg xmlns="http://www.w3.org/2000/svg" version="1.1">\n'
    
    for galaz in galezie:
        content += str(galaz)
        
    return content + '</svg>'
    


with open('drzewo.svg', 'w') as svg:
    svg.write(to_svg(generuj_fraktal(200, 30, 9)))
