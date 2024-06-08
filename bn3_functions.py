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

def atira_cpu(m,coords_atiradas,coords_validas):
    letras = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10}
    bala = rd.choice(coords_validas)
    while bala in coords_atiradas:
        bala = rd.choice(coords_validas)
    l = int(bala[1:])-1
    col = letras[bala[0]]-1
    if m[l][col] == '     ':
        m[l][col] = 'water'
        estado = 'Água'
    elif m[l][col] == 'navio':
        m[l][col] = 'booom'
        estado = 'BOOM!'
    return [m,bala,estado]

def atira_plr(m,coord):
    letras = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10}
    l = int(coord[1:])-1
    col = letras[coord[0]]-1
    if m[l][col] == '     ':
        m[l][col] = 'water'
        estado = 'Água'
    elif m[l][col] == 'navio':
        m[l][col] = 'booom'
        estado = 'BOOM!'
    return[m,coord,estado]

def intersection(lst1,lst2):
    lst3 = [value for value in lst1 if value in lst2]
    return lst3

def int_batalha(m,coords_atiradas,coords_validas,coords_suspeitas):
    letras = {'null1':0,'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10,'null2':11}
    grid = ['a2','a4','a6','a8','a10',
            'b1','b3','b5','b7','b9',
            'c2','c4','c6','c8','c10',
            'd1','d3','d5','d7','d9',
            'e2','e4','e6','e8','e10',
            'f1','f3','f5','f7','f9',
            'g2','g4','g6','g8','g10',
            'h1','h3','h5','h7','h9',
            'i2','i4','i6','i8','i10',
            'j1','j3','j5','j7','j9',]
    novas_sus = []
    if len(coords_suspeitas) == 0:
        remainder = [item for item in grid if item not in coords_atiradas]
        if len(remainder) != 0:
            bala = rd.choice(remainder)
        else:
            anti_grid = [item for item in coords_validas if item not in grid]
            possiveis = [item for item in anti_grid if item not in coords_atiradas]
            bala = rd.choice(possiveis)
    else:
        bala = coords_suspeitas[-1]
        del coords_suspeitas[-1]
    
    l = int(bala[1:])-1
    col = letras[bala[0]]-1
    if m[l][col] == '     ':
        m[l][col] = 'water'
        estado = 'Água'
        novas_sus = coords_suspeitas

    elif m[l][col] == 'navio':
        m[l][col] = 'booom'
        estado = 'BOOM!'
        l_sup = l+1-1
        l_mid = l+1
        l_inf = l+1+1
        col_lft = col+1-1
        col_mid = col+1
        col_rgt = col+1+1

        for key in letras:
            if letras[key] == col_lft:
                col_lft = key
                break
        for key in letras:
            if letras[key] == col_mid:
                col_mid = key
                break
        for key in letras:
            if letras[key] == col_rgt:
                col_rgt = key
                break
        coord1 = str(col_mid) + str(l_sup)
        coord2 = str(col_rgt) + str(l_mid)
        coord3 = str(col_mid) + str(l_inf)
        coord4 = str(col_lft) + str(l_mid)
        novas_sus.append(coord1)
        novas_sus.append(coord2)
        novas_sus.append(coord3)
        novas_sus.append(coord4)

        novas_sus = intersection(novas_sus,coords_validas)
        novas_sus = [item for item in novas_sus if item not in coords_atiradas]
        # novas_sus = novas_sus + coords_suspeitas
        novas_sus = list(dict.fromkeys(novas_sus))

    return [m,bala,estado,novas_sus]

def int_batalhav2(m,coords_atiradas,coords_validas,coords_suspeitas,tentativa):
    letras = {'null1':0,'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10,'null2':11}
    grid = ['a2','a4','a6','a8','a10',
            'b1','b3','b5','b7','b9',
            'c2','c4','c6','c8','c10',
            'd1','d3','d5','d7','d9',
            'e2','e4','e6','e8','e10',
            'f1','f3','f5','f7','f9',
            'g2','g4','g6','g8','g10',
            'h1','h3','h5','h7','h9',
            'i2','i4','i6','i8','i10',
            'j1','j3','j5','j7','j9',]
    novas_sus = []
    hor = coords_suspeitas[0]
    hor = [item for item in hor if item not in coords_atiradas]
    ver = coords_suspeitas[1]
    ver = [item for item in ver if item not in coords_atiradas]

    if tentativa == 'both':
        if len(ver) == 0 and len(hor) == 0:
            remainder = [item for item in grid if item not in coords_atiradas]
            if len(remainder) != 0:
                bala = rd.choice(remainder)
            nova_tentativa = 'both'
        else:
            if len(hor) == 0:
                bala = ver[0]
                del ver[0]
                nova_tentativa = 'ver'
            else:
                bala = hor[0]
                del hor[0]
                nova_tentativa = 'hor'

    elif tentativa == 'ver':
        if len(ver) == 0 and len(hor) == 0:
            remainder = [item for item in grid if item not in coords_atiradas]
            if len(remainder) != 0:
                bala = rd.choice(remainder)
            nova_tentativa = 'both'
        elif len(ver) == 0:
            bala = hor[0]
            del hor[0]
            nova_tentativa = 'hor'
        else:
            bala = ver[0]
            del ver[0]
            nova_tentativa = 'ver'

    else:
        if len(ver) == 0 and len(hor) == 0:
            remainder = [item for item in grid if item not in coords_atiradas]
            if len(remainder) != 0:
                bala = rd.choice(remainder)
            nova_tentativa = 'both'
        elif len(hor) == 0:
            bala = ver[0]
            del ver[0]
            nova_tentativa = 'ver'
        else:
            bala = hor[0]
            del hor[0]
            nova_tentativa = 'hor'
    
    l = int(bala[1:])-1
    col = letras[bala[0]]-1
    if m[l][col] == '     ':
        m[l][col] = 'water'
        estado = 'Água'
        novas_sus = coords_suspeitas

    elif m[l][col] == 'navio':
        m[l][col] = 'booom'
        estado = 'BOOM!'
        if tentativa == 'hor':
            ver = []
        elif tentativa == 'ver':
            hor = []
        l_sup = l+1-1
        l_mid = l+1
        l_inf = l+1+1
        col_lft = col+1-1
        col_mid = col+1
        col_rgt = col+1+1

        for key in letras:
            if letras[key] == col_lft:
                col_lft = key
                break
        for key in letras:
            if letras[key] == col_mid:
                col_mid = key
                break
        for key in letras:
            if letras[key] == col_rgt:
                col_rgt = key
                break
        coord1 = str(col_mid) + str(l_sup)
        coord2 = str(col_rgt) + str(l_mid)
        coord3 = str(col_mid) + str(l_inf)
        coord4 = str(col_lft) + str(l_mid)
        
        if tentativa in ['hor','both']:
            hor.append(coord2)
            hor.append(coord4)
            hor = intersection(hor,coords_validas)
            hor = list(dict.fromkeys(hor))
            hor = [item for item in hor if item not in coords_atiradas]   
        if tentativa in ['ver','both']:
            ver.append(coord1)
            ver.append(coord3)
            ver = intersection(ver,coords_validas)
            ver = list(dict.fromkeys(ver))
            ver = [item for item in ver if item not in coords_atiradas]
        novas_sus = [hor,ver]
        
    return [m,bala,estado,novas_sus,nova_tentativa]
