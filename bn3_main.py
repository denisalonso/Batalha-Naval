from bn3_functions import *
import random as rd

mp = [['     ','     ']]


def main():
    paises = ['Brasil','França','Austrália','Rússia','Japão']
    d1 = {'Brasil':{'cruzador':1,'torpedeiro':2,'destroyer':1,'couraçado':1,'porta-aviões':1},
          'França':{'cruzador':3,'porta-aviões':1,'destroyer':1,'submarino':1,'couraçado':1},
          'Austrália':{'couraçado':1,'cruzador':3,'submarino':1,'porta-aviões':1,'torpedeiro':1},
          'Rússia':{'cruzador':1,'porta-aviões':1,'couraçado':2,'destroyer':1,'submarino':1},
          'Japão':{'torpedeiro':2,'cruzador':1,'destroyer':2,'couraçado':1,'submarino':1},}
    gab = {'cruzador':2,'torpedeiro':3,'destroyer':3,'couraçado':4,'porta-aviões':5,'submarino':2}
    jogadas_plr = []
    jogadas_cpu = []

    map_player = cria_mapa()
    map_cpu = cria_mapa()


    while vivo(map_player) and vivo(map_cpu):

main()