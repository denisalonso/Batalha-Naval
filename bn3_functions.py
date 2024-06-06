import random as rd

def cria_mapa():
    mapa = []
    for i in range(10):
        mapa.append([])
    for i in range(10):
        for j in range(10):
            mapa[i].append('     ')
    return mapa

def show_map(m1,m2):
    letters = ['A','B','C','D','E','F','D','H','I','J']
    numbers = ['1','2','3','4','5','6','7','8','9','10']
    for i in range(12):
        if i in [0,11]:
            line = '   '
            for i in range(20):
                if i in [10]:
                    line += '       '
                if i > 9:
                    line += f'  {letters[i-10]}  '
                else: 
                    line += f'  {letters[i-10]}  '
        else:
            line = ''
            for h in range(24):
                if h in [0,12]:
                    if i in [10]:
                        line += numbers[i-1]
                        line += ' '              
                    else:
                        line += ' '
                        line += numbers[i-1]
                        line += ' '                
                elif h in [11,23]:
                    line += ' '
                    if i in [10]:
                        line += numbers[i-1]
                        line += ' '              
                    else:
                        
                        line += numbers[i-1]
                        line += ' '
                        line += ' '
                elif h < 10:
                    line += m1[i-1][h]
                else:
                    line += m2[i-1][h-13]
        print(line)

def color_map(m):
    mapa = m
    for i in range(len(m)):
        for j in range(len(mapa[i])):
            if mapa[i][j] == ' ':
                mapa[i][j] = '   '
            elif mapa[i][j] == 'N':
                mapa[i][j] = '\u001b[32m▇▇▇\u001b[0m' 
            elif mapa[i][j] == 'A':
                mapa[i][j] = '\u001b[34m▇▇▇\u001b[0m'
            elif mapa[i][j] == 'X':
                mapa[i][j] = '\u001b[31m▇▇▇\u001b[0m'
    return mapa

def posição_suporta(m,b,l,c,o):
    letras = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10}
    letra = letras[c]-1
    if m[l][letra] in ['navio']:
        return False
    for i in range(b):
        if o in ['v']:
            if l + i > len(m)-1:
                return False
            if m[l+i][letra] in ['navio']:
                return False
        else:
            if letra + i > len(m)-1:
                return False
            if m[l][letra+i] in ['navio']:
                return False
    return True

def aloca_cpu(m,b):
    mapa_cpu = m
    escolhido = False
    while not escolhido:
        l = rd.randint(0,len(mapa_cpu-1))
        c = rd.randint(0,len(mapa_cpu-1))
        o = rd.choice('v','h')
        if posição_suporta(mapa_cpu,b,l,c,o):
            escolhido = True
    for i in range(b):
        if o in ['v']:
            mapa_cpu[l+i][c] = 'navio'
        else:
            mapa_cpu[l][c+i] = 'navio'
    return mapa_cpu

def aloca_plr(m,b,l,c,o):
    mapa_plr = m
    letras = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10}
    letra = letras[c]-2
    for i in range(b):
        if o in ['v']:
            mapa_plr[l+i][letra] = 'navio'
        else:
            mapa_plr[l][letra+i] = 'navio'
    return mapa_plr