def cria_mapa():
    mapa = []
    for i in range(10):
        mapa.append([])
    for i in range(10):
        for j in range(10):
            mapa[i].append('     ')
    return mapa

m1 = cria_mapa()
m2 = cria_mapa()

letters = ['A','B','C','D','E','F','D','H','I','J']
numbers = ['1','2','3','4','5','6','7','8','9','10']

for i in range(12):
    if i in [0,11]:
        line = '   '
        for i in range(20):
            if i in [10]:
                line += '      '
            if i > 9:
                line += f'  {letters[i-10]}  '
            else: 
                line += f'  {letters[i-10]}  '
    else:
        line = ''
        for h in range(24):
            if h in [0,11,12,23]:
                if i in [10]:
                    line += numbers[i-1]
                    line += ' '              
                else:
                    line += ' '
                    line += numbers[i-1]
                    line += ' '
            elif h < 10:
                line += m1[i-1][h]
            else:
                line += m2[i-1][h-13]
    print(line)
