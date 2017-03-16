#!/usr/bin/env python
# -*- coding:utf-8 -*-

from math import sin
from math import cos
from math import radians
from random import randint

__author__ = 'Damian Matyjaszek'
s = 30

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
                             
                            
                            
def gen_fraktal(dlugosc, kat, poziomy):
    '''Funkcja generująca fraktal, będący drzewem
    
    
    Argumenty:
        dlugosc (float):    Długość pnia drzewa.
        kat (float):        Początkowy kąt nachylenia gałęzi.
        poziomy (int):      Liczba poziomów gałęzi.
    
    Funkcja zwraca listę gałęzi, stanowiących drzewo.
    
    Drzewo składa się z pnia o długości 'dlugosc' znajdującego się na poziomie 0, oraz 
    gałęzi "wyrastających" po 3 z każdego końca każdej gałęzi, o grubości wynoszącej 
    2/3 + 1 grubości gałęzi poprzedzającej, o ograniczonym, względem poprzedzającej 
    gałęzi, nachyleniu. Wraz z każdym kolejnym poziomem zielona barwa gałęzi zostaje 
    zwiększona o 6.
    '''
    grubosc = dlugosc / 5
    kolor = [100, 60, 0]
    
    fraktal = galezie = [Branch([500.0, 1000.0], [500.0, 1000.0-dlugosc], grubosc, kolor)]
    
    for poziom in range(poziomy):
        dlugosc *= (2.0)/(3.0)
        grubosc = grubosc * (2.0/3.0) + 1
        kolor = [kolor[0], kolor[1] + 6, kolor[2]]
        nowe = []       # Lista przechowująca gałęzie dla nowego poziomu
        for galaz in galezie:
            # Obrót
            alfa = kat + randint(-1, 1) * randint(1, s)
            x = galaz.koniec[0] + dlugosc * cos(radians(-alfa))
            y = galaz.koniec[1] + dlugosc * sin(radians(-alfa))
        
            nowe += [Branch(galaz.koniec, [x, y], grubosc, kolor),
                     Branch(galaz.koniec, [galaz.koniec[0], y], grubosc, kolor),
                     Branch(galaz.koniec, [-x + 2*galaz.koniec[0], y], grubosc, kolor)]
                    
        fraktal += nowe     # Przechowuje wszystkie gałęzie
        galezie = nowe      # Przechowuje gałęzie ostatniego poziomu
        
    return fraktal
                                         
 
  
def gen_svg(galezie, nazwa):
    '''Funkcja generująca plik SVG
    
    Argumenty:
        galezie ([Branch, ...]):    Lista obiektów klasy Branch.
        nazwa (str):                Nazwa generowanego pliku.
       
    Funkcja tworzy plik o nazwie 'nazwa', z rozszerzeniem .svg, do którego zapisywana jest
    tekstowa reprezentacja elementów listy, składającej się z obiektów klasy Branch.
    '''
    with open(nazwa + '.svg', 'w') as plik:
        plik.write('<svg xmlns="http://www.w3.org/2000/svg" version="1.1">\n')
        for galaz in map(str, galezie):
            plik.write(galaz)
        plik.write('</svg>')
    
    
    
gen_svg(gen_fraktal(300, 30, 9), 'drzewo')
