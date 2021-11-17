"""
Fundamentos da Programação - Projeto 2

Francisco Salgueiro nº103345
13/11/2021
fgcdbs@gmail.com
"""

#########################################
#  2.1.1 TAD POSICAO
#########################################

# Construtores

def cria_posicao(x, y):
    if not(all(isinstance(e, int) and e >= 0 for e in (x, y))):
        raise ValueError("cria_posicao: argumentos invalidos")
    return (x, y)


# Seletores

def obter_pos_x(p):
    return p[0]

def obter_pos_y(p):
    return p[1]

def cria_copia_posicao(p):
    return cria_posicao(obter_pos_x(p), obter_pos_y(p))

# Reconhecedor

def eh_posicao(p):
    return isinstance(p, tuple) and len(p) == 2 and all(isinstance(e, int) and e >= 0 for e in p)

# Teste

def posicoes_iguais(p1, p2):
    return eh_posicao(p1) and eh_posicao(p2) and p1 == p2

# Transformador

def posicao_para_str(p):
    return f"({obter_pos_x(p)}, {obter_pos_y(p)})"

# Alto Nível

def obter_posicoes_adjacentes(p):
    adj = ()
    x = obter_pos_x(p)
    y = obter_pos_y(p)
    if y > 0:
        adj = adj + (cria_posicao(x, y-1),)
    adj = adj + (cria_posicao(x+1, y), cria_posicao(x, y+1),)
    if x > 0:
        adj = adj + (cria_posicao(x-1, y),)
    return adj

def ordenar_posicoes(t):
    pos_ord = []
    for p in t:
        x = obter_pos_x(p)
        y = obter_pos_y(p)
        for i in range(len(pos_ord)):
            if y < obter_pos_y(pos_ord[i]) or (y == obter_pos_y(pos_ord[i]) and x <= obter_pos_x(pos_ord[i])):
                pos_ord.insert(i, p)
                break
        else:
            pos_ord.append(p)
    return tuple(pos_ord)

#########################################
#  2.1.2 TAD ANIMAL
#########################################

# Construtores

def cria_animal(s, r, a):
    if (
        not isinstance(s, str)
        or len(s) == 0
        or not isinstance(r, int)
        or not isinstance(a, int)
        or r <= 0
        or a < 0
    ):
        raise ValueError("cria_animal: argumentos invalidos")

    return [s, r, a, 0, 0]

def cria_copia_animal(a):
    return a.copy()

# Seletores

def obter_especie(a):
    return a[0]

def obter_freq_reproducao(a):
    return a[1]

def obter_freq_alimentacao(a):
    return a[2]

def obter_idade(a):
    return a[3]

def obter_fome(a):
    return a[4]

# Modificadores

def aumenta_idade(a):
    a[3] += 1
    return a

def reset_idade(a):
    a[3] = 0
    return a

def aumenta_fome(a):
    if obter_freq_alimentacao(a)>0:
        a[4] += 1
    return a

def reset_fome(a):
    a[4] = 0
    return a

# Reconhecedores

def eh_animal(arg):
    return isinstance(arg, list) and len(arg) == 5 and isinstance(arg[0], str) and len(arg[0]) > 0 and all(isinstance(arg[i], int) and arg[i] >= 0 for i in range(2, 5)) and isinstance(arg[1], int) and arg[1]>0

def eh_predador(arg):
    return eh_animal(arg) and arg[2] > 0

def eh_presa(arg):
    return eh_animal(arg) and arg[2] == 0

# Teste

def animais_iguais(a1, a2):
    return eh_animal(a1) and eh_animal(a2) and a1 == a2

# Transformadores

def animal_para_char(a):
    if eh_presa(a):
        return a[0][0].lower()
    elif eh_predador(a):
        return a[0][0].upper()

def animal_para_str(a):
    if eh_presa(a):
        return f"{a[0]} [{a[3]}/{a[1]}]"
    elif eh_predador(a):
        return f"{a[0]} [{a[3]}/{a[1]};{a[4]}/{a[2]}]"

# Alto Nível

def eh_animal_fertil(a):
    return obter_idade(a) >= obter_freq_reproducao(a)

def eh_animal_faminto(a):
    return eh_predador(a) and obter_fome(a) >= obter_freq_alimentacao(a)

def reproduz_animal(a):
    reset_idade(a)
    n_animal = cria_copia_animal(a)
    reset_fome(n_animal)
    return n_animal

#########################################
#  2.1.2 TAD PRADO
#########################################

# Construtores

def cria_prado(d, r, a, p):
    if not (
        eh_posicao(d)
        and all(isinstance(e, tuple) for e in (r, a, p))
        and len(a) == len(p) >0
        and all(eh_animal(animal) for animal in a)
        and all(eh_posicao(pos) and 0 < obter_pos_x(pos) < obter_pos_x(d) and 0 < obter_pos_y(pos) < obter_pos_y(d) for pos in r)
        and all(eh_posicao(pos) for pos in p)
        and all(pos not in r and 0 < obter_pos_x(pos) < obter_pos_x(d) and 0 < obter_pos_y(pos) < obter_pos_y(d) for pos in p)
    ):
        raise ValueError("cria_prado: argumentos invalidos") 
    n=obter_pos_x(d)+1
    m=obter_pos_y(d)+1
    prado=[]
    for i in range(m):
        prado.append([])
        for j in range(n):
            prado[i].append([])
    for i in range(n):
        prado[0][i]="-"
        prado[m-1][i]="-"
    for j in range(m):
        prado[j][0]="-"
        prado[j][n-1]="-"
    for rochedo in r:
        prado[obter_pos_y(rochedo)][obter_pos_x(rochedo)]="@"
    for i in range(len(a)):
        prado[obter_pos_y(p[i])][obter_pos_x(p[i])]=a[i]
    return prado

def cria_copia_prado(m):
    return m.copy()

# Seletores

def obter_tamanho_x(m):
    return len(m[0])

def obter_tamanho_y(m):
    return len(m)

def obter_numero_predadores(m):
    pred=0
    for i in range(obter_tamanho_y(m)):
        for j in range(obter_tamanho_x(m)):
            if eh_predador(m[i][j]):
                pred+=1
    return pred

def obter_numero_presas(m):
    pres=0
    for i in range(obter_tamanho_y(m)):
        for j in range(obter_tamanho_x(m)):
            if eh_presa(m[i][j]):
                pres+=1
    return pres

def obter_posicao_animais(m):
    posicoes=[]
    for i in range(obter_tamanho_y(m)):
        for j in range(obter_tamanho_x(m)):
            if eh_animal(m[i][j]):
                posicoes.append(cria_posicao(i,j))
    return ordenar_posicoes(tuple(posicoes))

def obter_animal(m, p):
    return m[obter_pos_y(p)][obter_pos_x(p)]

# Modificadores

def eliminar_animal(m, p):
    m[obter_pos_y(p)][obter_pos_x(p)]=[]
    return m

def inserir_animal(m, a, p):
    m[obter_pos_y(p)][obter_pos_x(p)]=a
    return m

def mover_animal(m, p1, p2):
    animal=obter_animal(m,p1)
    eliminar_animal(m, p1)
    inserir_animal(m, animal, p2)
    return m

# Reconhecedores

def eh_prado(arg): #############################################
    return isinstance(arg, list) 

def eh_posicao_animal(m, p):
    return eh_animal(m[obter_pos_y(p)][obter_pos_x(p)])

def eh_posicao_obstaculo(m, p):
    print("p= "+str(p))
    print("x" + str(obter_pos_x(p)))
    print("y" + str(obter_pos_y(p)))
    print(m[obter_pos_y(p)][obter_pos_x(p)])
    q=m[obter_pos_y(p)][obter_pos_x(p)]
    print("q = " +str(q))
    return q=="-" or q=="@"

def eh_posicao_livre(m, p):
    return m[obter_pos_y(p)][obter_pos_x(p)]==[]

# Teste

def prados_iguais(p1, p2):
    return p1 == p2 and eh_prado(p1) and eh_prado(p2)

# Transformador

def prado_para_str(m):
    s = ""
    x = obter_tamanho_x(m)
    y = obter_tamanho_y(m)
    for i in range(y):
        if i == 0:
            s += "+"+(x-2)*"-"+"+\n"
            continue
        if i == y-1:
            s += "+"+(x-2)*"-"+"+"
            continue
        for j in range(x):
            if j == 0:
                s += "|"
            elif j == x-1:
                s += "|\n"
            else:
                pos = cria_posicao(j, i)
                if eh_posicao_animal(m, pos):
                    s += animal_para_char(obter_animal(m, pos))
                elif eh_posicao_obstaculo(m, pos):
                    s += "@"
                else:
                    s += "."
    return s

# Alto Nível

def obter_valor_numerico(m, p):
    return obter_tamanho_x(m)*obter_pos_y(p) + obter_pos_x(p)

def obter_movimento(m, p):
    adj = obter_posicoes_adjacentes(p)
    adj_novo = []
    existe_presa = False
    for pos in adj:
        if eh_posicao_livre(m, pos) and not existe_presa:
            adj_novo.append(pos)
        elif eh_posicao_animal(m, pos) and eh_predador(obter_animal(m, p)) and eh_presa(obter_animal(m, pos)):
            if not existe_presa:
                adj_novo = []
                existe_presa = True
            adj_novo.append(pos)
    if len(adj_novo) == 0:
        return cria_copia_posicao(p)
    return cria_copia_posicao(adj_novo[obter_valor_numerico(m, p) % len(adj_novo)])

#########################################
#  2.2 Funções Adicionais
#########################################

def geracao(m):
    y = obter_tamanho_y(m)
    x = obter_tamanho_x(m)
    ja_se_moveram = []
    for i in range(y):
        for j in range(x):
            pos = cria_posicao(j, i)
            if eh_posicao_animal(m, pos) and pos not in ja_se_moveram:
                animal = cria_copia_animal(obter_animal(m, pos))
                aumenta_idade(animal)
                mov = obter_movimento(m, pos)
                if eh_predador(animal):
                    if eh_posicao_animal(m, mov) and eh_presa(obter_animal(m, mov)):
                        reset_fome(animal)
                        eliminar_animal(m, mov)
                    else:
                        aumenta_fome(animal)

                eliminar_animal(m,pos)
                inserir_animal(m,animal,pos)

                if not posicoes_iguais(mov,pos):
                    mover_animal(m, pos, mov)
                if eh_animal_fertil(animal):
                    if not posicoes_iguais(mov,pos):
                        inserir_animal(m, reproduz_animal(animal), pos)
                if eh_animal_faminto(animal) and eh_predador(animal):
                    eliminar_animal(m, mov)
                ja_se_moveram.append(mov)
    return m

def simula_ecossistema(f, g, v):
    with open(f, mode="r") as file:
        config = file.readlines()
    d = cria_posicao(eval(config[0])[0], eval(config[0])[1])
    r = ()
    for rochedo in eval(config[1]):
        r = r + (cria_posicao(rochedo[0], rochedo[1]),)
    a = ()
    p = ()
    for i in range(2, len(config)):
        animal = eval(config[i])
        a = a + (cria_animal(animal[0], animal[1], animal[2]),)
        p = p + (cria_posicao(animal[3][0], animal[3][1]),)
    m = cria_prado(d, r, a, p)
    for i in range(g+1):
        if i == 0 or ((v and (obter_numero_predadores(m) != predadores_ant or obter_numero_presas(m) != presas_ant)) or (i == g and not v)):
            print(f"Predadores: {obter_numero_predadores(m)} vs Presas: {obter_numero_presas(m)} (Gen. {i})")
            print(prado_para_str(m))
        if i == g:
            return obter_numero_predadores(m), obter_numero_presas(m)
        predadores_ant = obter_numero_predadores(m)
        presas_ant = obter_numero_presas(m)
        m = geracao(m)
