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
    letters = ['A','B','C','D','E','F','G','H','I','J']
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
                elif h <= 10:
                    line += m1[i-1][h-1]
                else:
                    line += m2[i-1][h-13]
        print(line)

def color_cpu(m):
    m2 = cria_mapa()
    for i in range(len(m)):
        for j in range(len(m[i])):
            if m[i][j] == 'navio':
                m2[i][j] = '     '
            elif m[i][j] == 'water':
                m2[i][j] = '\u001b[34m▇▇▇▇▇\u001b[0m'
            elif m[i][j] == 'booom':
                m2[i][j] = '\u001b[31m▇▇▇▇▇\u001b[0m'
    return m2

def color_plr(m):
    m2 = cria_mapa()
    for i in range(len(m)):
        for j in range(len(m[i])):
            if m[i][j] == 'navio':
                m2[i][j] = '\u001b[32m▇▇▇▇▇\u001b[0m' 
            elif m[i][j] == 'water':
                m2[i][j] = '\u001b[34m▇▇▇▇▇\u001b[0m'
            elif m[i][j] == 'booom':
                m2[i][j] = '\u001b[31m▇▇▇▇▇\u001b[0m'
    return m2

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
        l = rd.randint(0,len(mapa_cpu)-1)
        c = rd.choice(['a','b','c','d','e','f','g','h','i','j'])
        o = rd.choice(['v','h'])
        if posição_suporta(mapa_cpu,b,l,c,o):
            escolhido = True
    letras = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10}
    c = letras[c]-1
    for i in range(b):
        if o in ['v']:
            mapa_cpu[l+i][c] = 'navio'
        else:
            mapa_cpu[l][c+i] = 'navio'
    return mapa_cpu

def aloca_plr(m,b,l,c,o):
    mapa_plr = m
    letras = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10}
    letra = letras[c]-1
    for i in range(b):
        if o in ['v']:
            mapa_plr[l+i][letra] = 'navio'
        else:
            mapa_plr[l][letra+i] = 'navio'
    return mapa_plr

def vivo(m):
    alive = False
    for i in range(len(m)):
        for h in range(len(m[i])):
            if m[i][h] == 'navio':
                alive = True
                break
    return alive

def atira_cpu(m,coords_atiradas):
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
    letras = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10}
    bala = rd.choice(coords_validas)
    while bala in coords_atiradas:
        bala = rd.choice(coords_validas)
    l = int(bala[1:])-1
    col = letras[bala[0]]-1
    if m[l][col] == '     ':
        m[l][col] = 'water'
    elif m[l][col] == 'navio':
        m[l][col] = 'booom'
    return [m,bala]
