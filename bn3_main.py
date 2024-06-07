from bn3_functions import *
import random as rd
import time as t

def main():
    # estabelecendo dicionários e listas fundamentais
    paises = ['Brasil','França','Austrália','Rússia','Japão']
    d1 = {'Brasil':{'cruzador':1,'torpedeiro':2,'destroyer':1,'couraçado':1,'porta-aviões':1},
          'França':{'cruzador':3,'porta-aviões':1,'destroyer':1,'submarino':1,'couraçado':1},
          'Austrália':{'couraçado':1,'cruzador':3,'submarino':1,'porta-aviões':1,'torpedeiro':1},
          'Rússia':{'cruzador':1,'porta-aviões':1,'couraçado':2,'destroyer':1,'submarino':1},
          'Japão':{'torpedeiro':2,'cruzador':1,'destroyer':2,'couraçado':1,'submarino':1},}
    gab = {'cruzador':2,'torpedeiro':3,'destroyer':3,'couraçado':4,'porta-aviões':5,'submarino':2}
    coords_validas = ['a1','a2','a3','a4','a5','a6','a7','a8','a9','a10',
                      'b1','b2','b3','b4','b5','b6','b7','b8','b9','b10',
                      'c1','c2','c3','c4','c5','c6','c7','c8','c9','c10',
                      'd1','d2','d3','d4','d5','d6','d7','d8','d9','d10',
                      'e1','e2','e3','e4','e5','e6','e7','e8','e9','e10',
                      'f1','f2','f3','f4','f5','f6','f7','f8','f9','f10',
                      'g1','g2','g3','g4','g5','g6','g7','g8','g9','g10',
                      'h1','h2','h3','h4','h5','h6','h7','h8','h9','h10',
                      'i1','i2','i3','i4','i5','i6','i7','i8','i9','i10',
                      'j1','j2','j3','j4','j5','j6','j7','j8','j9','j10',]
    jogadas_plr = []
    jogadas_cpu = []

    # criação de mapas
    map_plr = cria_mapa()
    map_cpu = cria_mapa()

    # seleção de países
    pais_cpu = paises[rd.randint(0,4)]
    frota_cpu = d1[pais_cpu]
    escolha = input('Escolha um país: [Brasil (1) / França (2) / Austrália (3) / Rússia (4) / Japão (5)] ')
    while escolha not in ['1','2','3','4','5']:
        escolha = input('Por favor digite um número entre [1/2/3/4/5]: ')
    pais_plr = paises[int(escolha)-1]
    frota_plr = d1[pais_plr]

    # alocação
    blocos_cpu = []
    for navio in frota_cpu:
        for i in range(frota_cpu[navio]):
            blocos_cpu.append(gab[navio])
    blocos_plr = []
    for navio in frota_plr:
        for i in range(frota_plr[navio]):
            blocos_plr.append(gab[navio])
    
        # parte I - CPU
    for i in range(len(blocos_cpu)):
        map_cpu = aloca_cpu(map_cpu,blocos_cpu[i])
            
        # parte II - PLR
    for navio in frota_plr:
        print(f'Você está alocando {navio}, {frota_plr[navio]} unidades.')
        for i in range(frota_plr[navio]):
            alocado = False
            while not alocado:
                coord = input('Escolha a coordenada em que quer alocar: ')
                while coord not in coords_validas:
                    coord = input('Por favor digite uma coordenada válida: ')
                ori = input('Escolha uma orientação: ')
                while ori.lower() not in ['h','v']:
                    ori = input('Por favor digite orientação válida [v/h]: ')
                l = int(coord[1:])-1
                c = coord[0]
                if posição_suporta(map_plr,gab[navio],l,c,ori):
                    alocado = True
                    mapa_plr = aloca_plr(map_plr,gab[navio],l,c,ori)
                else:
                    print('Posição inválida! por favor escolha outra posição.')
            show_map(color_cpu(map_cpu),color_plr(map_plr))
    
    # jogo começando
    while vivo(map_cpu) and vivo(map_plr):
        t.sleep(2)
        rodada = atira_cpu(mapa_plr,jogadas_cpu)
        jogadas_cpu.append(rodada[1])
        mapa_plr = rodada[0]
        show_map(map_cpu,color_plr(map_plr))        
        for i in range(len(map_cpu)):
            print(map_cpu[i])
        t.sleep(4)
    




main()
