"""
Fundamentos da Programação - Projeto 2

Francisco Salgueiro nº103345
13/11/2021
fgcdbs@gmail.com
"""

#########################################
#  2.1.1 TAD POSICAO
#########################################

# Reconhecedor


def eh_posicao(p):
    """
    Testa se o argumento é um TAD posição

    eh_posicao: universal -> booleano
    """
    return (
        isinstance(p, tuple)
        and len(p) == 2
        and isinstance(p[0], int)
        and isinstance(p[1], int)
        and p[0] >= 0
        and p[1] >= 0
        # testar explicitamente cada elemento é mais rápido
        # and all(isinstance(e, int) and e >= 0 for e in p)
    )


# Seletores


def obter_pos_x(p):
    """
    Devolve a componente x da posição p

    obter_pos_x: posicao -> int
    """
    return p[0]


def obter_pos_y(p):
    """
    Devolve a componente y da posição p

    obter_pos_y: posicao -> int
    """
    return p[1]


# Construtores


def cria_posicao(x, y):
    """
    Recebe os valores correspondentes às coordenadas de uma posição
    e devolve a posição correspondente

    cria_posicao: int x int -> posicao
    """
    pos = (x, y)
    if not eh_posicao(pos):
        raise ValueError("cria_posicao: argumentos invalidos")
    return pos


def cria_copia_posicao(p):
    """
    Recebe uma posição e devolve uma cópia nova da posição

    cria_copia_posicao: posicao -> posicao
    """
    return cria_posicao(obter_pos_x(p), obter_pos_y(p))


# Teste


def posicoes_iguais(p1, p2):
    """
    Testa se os argumentos são TADs posições iguais

    posicoes_iguais: posicao x posicao -> booleano
    """
    return p1 == p2 and eh_posicao(p1) and eh_posicao(p2)


# Transformador


def posicao_para_str(p):
    """
    Devolve a cadeia de carateres '(x, y)' que representa o seu argumento
    sendo x e y as coordenadas de p

    posicao_para_str: posicao -> str
    """
    return f"({obter_pos_x(p)}, {obter_pos_y(p)})"


# Alto Nível


def obter_posicoes_adjacentes(p):
    """
    Devolve um tuplo com as posições adjacentes à posição p,
    começando pela posição acima de p e seguindo no sentido horário

    obter_posicoes_adjacentes: posicao -> tuplo
    """
    adj = ()
    x = obter_pos_x(p)
    y = obter_pos_y(p)
    if y > 0:
        adj += (cria_posicao(x, y - 1),)  # cima
    adj += (
        cria_posicao(x + 1, y),  # direita
        cria_posicao(x, y + 1),  # baixo
    )
    if x > 0:
        adj += (cria_posicao(x - 1, y),)  # esquerda
    return adj


def ordenar_posicoes(t):
    """
    Devolve um tuplo contendo as mesmas posições do argumento,
    ordenadas de acordo com a ordem de leitura do prado

    ordenar_posicoes: tuplo -> tuplo
    """
    pos_ord = []
    for p in t:
        x = obter_pos_x(p)
        y = obter_pos_y(p)
        for i, pos in enumerate(pos_ord):
            if y < obter_pos_y(pos) or (
                y == obter_pos_y(pos) and x <= obter_pos_x(pos)
            ):
                pos_ord.insert(i, p)
                break
        else:
            pos_ord.append(p)  # caso seja a maior posição até agora
    return tuple(pos_ord)


#########################################
#  2.1.2 TAD ANIMAL
#########################################


# Reconhecedores


def eh_animal(arg):
    """
    Testa se o argumento é um TAD animal

    eh_animal: universal -> booleano
    """
    return (
        isinstance(arg, list)
        and len(arg) == 5
        and isinstance(arg[0], str)
        and len(arg[0]) > 0
        and all(isinstance(arg[i], int) and arg[i] >= 0 for i in range(2, 5))
        and isinstance(arg[1], int)
        and arg[1] > 0
    )


def eh_predador(arg):
    """
    Testa se o argumento é um TAD animal do tipo predador

    eh_predador: universal -> booleano
    """
    return eh_animal(arg) and arg[2] > 0


def eh_presa(arg):
    """
    Testa se o argumento é um TAD animal do tipo presa

    eh_presa: universal -> booleano
    """
    return eh_animal(arg) and arg[2] == 0


# Construtores


def cria_animal(s, r, a):
    """
    Recebe os valores correspondentes à espécie, frequência de reprodução
    e frequência de alimentação, e devolve o animal

    cria_animal: str x int x int -> animal
    """
    animal = [s, r, a, 0, 0]
    if not eh_animal(animal):
        raise ValueError("cria_animal: argumentos invalidos")

    return animal


def cria_copia_animal(a):
    """
    Recebe um animal e devolve uma nova cópia do animal

    cria_copia_animal: animal -> animal
    """
    return a.copy()


# Seletores


def obter_especie(a):
    """
    Devolve a cadeia de carateres correpondente à espécie do animal

    obter_especie: animal -> str
    """
    return a[0]


def obter_freq_reproducao(a):
    """
    Devolve a frequência de reprodução do animal

    obter_freq_reproducao: animal -> int
    """
    return a[1]


def obter_freq_alimentacao(a):
    """
    Devolve a frequência de alimentação do animal

    obter_freq_alimentacao: animal -> int
    """
    return a[2]


def obter_idade(a):
    """
    Devolve a idade do animal

    obter_idade: animal -> int
    """
    return a[3]


def obter_fome(a):
    """
    Devolve a fome do animal

    obter_fome: animal -> int
    """
    return a[4]


# Modificadores


def aumenta_idade(a):
    """
    Modifica destrutivamente o animal, incrementando a sua idade por um
    e devolve o próprio animal

    aumenta_idade: animal -> animal
    """
    a[3] += 1
    return a


def reset_idade(a):
    """
    Modifica destrutivamente o animal, definindo a sua idade a zero
    e devolve o próprio animal

    reset_idade: animal -> animal
    """
    a[3] = 0
    return a


def aumenta_fome(a):
    """
    Modifica destrutivamente o animal, incrementando a sua fome por um
    e devolve o próprio animal

    aumenta_fome: animal -> animal
    """
    if obter_freq_alimentacao(a) > 0:
        a[4] += 1
    return a


def reset_fome(a):
    """
    Modifica destrutivamente o animal, definindo a sua fome a zero
    e devolve o próprio animal

    reset_fome: animal -> animal
    """
    a[4] = 0
    return a


# Teste


def animais_iguais(a1, a2):
    """
    Testa se os argumento são TAD animais, e são iguais

    animais_iguais: universal x universal -> booleano
    """
    return a1 == a2 and eh_animal(a1) and eh_animal(a2)


# Transformadores


def animal_para_char(a):
    """
    Devolve a letra correspondente ao primeiro caratere da espécie do animal

    animal_para_char: animal -> str
    """
    if eh_presa(a):
        return a[0][0].lower()
    else:
        return a[0][0].upper()


def animal_para_str(a):
    """
    Devolve a cadeia de carateres que representa o animal

    Para presas:
        'espécie [idade/freq. reprodução]'

    Para predadores:
        'espécie [idade/freq. reprodução;fome/freq. alimentação]'

    animal_para_str: animal -> str
    """
    if eh_presa(a):
        return f"{a[0]} [{a[3]}/{a[1]}]"
    else:
        return f"{a[0]} [{a[3]}/{a[1]};{a[4]}/{a[2]}]"


# Alto Nível


def eh_animal_fertil(a):
    """
    Testa se o animal atingiu a idade de reprodução

    eh_animal_fertil: animal -> booleano
    """
    return obter_idade(a) >= obter_freq_reproducao(a)


def eh_animal_faminto(a):
    """
    Testa se o animal atingiu fome igual ou superior à freq. alimentação

    eh_animal_faminto: animal -> booleano
    """
    return eh_predador(a) and obter_fome(a) >= obter_freq_alimentacao(a)


def reproduz_animal(a):
    """
    Recebe um animal e devolve um novo animal da mesma espécie
    com idade e fome iguais a 0, modificando destrutivamente o argumento
    ao alterar a sua idade para 0

    reproduz_animal: animal -> animal
    """
    reset_idade(a)
    n_animal = cria_copia_animal(a)
    reset_fome(n_animal)
    return n_animal


#########################################
#  2.1.2 TAD PRADO
#########################################


# Reconhecedores


def eh_prado(arg):
    """
    Testa se o argumento é um TAD prado

    eh_prado: universal -> booleano
    """
    if not (isinstance(arg, list) and len(arg) == 4):
        return False
    d, r, a, p = arg[0], arg[1], arg[2], arg[3]
    return (
        eh_posicao(d)
        and all(isinstance(e, tuple) for e in (r, a, p))
        and len(a) == len(p) > 0
        and all(eh_animal(animal) for animal in a)
        and all(
            eh_posicao(pos)
            and 0 < obter_pos_x(pos) < obter_pos_x(d)
            and 0 < obter_pos_y(pos) < obter_pos_y(d)
            for pos in r
        )
        and all(eh_posicao(pos) for pos in p)
        and all(
            not any(posicoes_iguais(pos, e) for e in r)
            and 0 < obter_pos_x(pos) < obter_pos_x(d)
            and 0 < obter_pos_y(pos) < obter_pos_y(d)
            for pos in p
        )
    )


def eh_posicao_animal(m, p):
    """
    Testa se a posição p está ocupada por um animal no prado m

    eh_posicao_animal: prado x posicao -> booleano
    """
    for e in m[3]:
        if posicoes_iguais(p,e):
            return True
    return False


def eh_posicao_obstaculo(m, p):
    """
    Testa se a posição p está ocupada por um obstáculo no prado m

    eh_posicao_obstaculo: prado x posicao -> booleano
    """
    return (
        obter_pos_y(p) == 0
        or obter_pos_y(p) == obter_tamanho_y(m) - 1
        or obter_pos_x(p) == 0
        or obter_pos_x(p) == obter_tamanho_x(m) - 1
        or any(posicoes_iguais(p, e) for e in m[1])
    )


def eh_posicao_livre(m, p):
    """
    Testa se a posição p corresponde a um espaço livre no prado m

    eh_posicao_livre: prado x posicao -> booleano
    """
    return not (eh_posicao_animal(m, p) or eh_posicao_obstaculo(m, p))


# Construtores


def cria_prado(d, r, a, p):
    """
    Recebe os valores correspondentes à dimensão, posições de obstáculos,
    animais, e posições de animais, e devolve o prado

    cria_prado: posicao x tuplo x tuplo x tuplo -> prado
    """
    prado = [d, r, a, p]
    if not eh_prado(prado):
        raise ValueError("cria_prado: argumentos invalidos")

    return prado


def cria_copia_prado(m):
    """
    Recebe um prado e devolve uma nova cópia do prado

    cria_copia_prado: prado -> prado
    """
    return m.copy()


# Seletores


def obter_tamanho_x(m):
    """
    Devolve o valor correspondente à dimensão x do prado

    obter_tamanho_x: prado -> int
    """
    return obter_pos_x(m[0]) + 1


def obter_tamanho_y(m):
    """
    Devolve o valor correspondente à dimensão y do prado

    obter_tamanho_y: prado -> int
    """
    return obter_pos_y(m[0]) + 1


def obter_numero_predadores(m):
    """
    Devolve o número de animais predadores no prado

    obter_numero_predadores: prado -> int
    """
    return len([a for a in m[2] if eh_predador(a)])


def obter_numero_presas(m):
    """
    Devolve o número de animais presas no prado

    obter_numero_presas: prado -> int
    """
    return len([a for a in m[2] if eh_presa(a)])


def obter_posicao_animais(m):
    """
    Devolve um tuplo contendo as posições do prado ocupadas por animais,
    ordenadas pela ordem de leitura do prado

    obter_posicao_animais: prado -> tuplo posicoes
    """
    return ordenar_posicoes(m[3])


def obter_animal(m, p):
    """
    Devolve o animal do prado m que se encontra na posição p

    obter_animal: prado x posicao -> animal
    """
    for i, pos in enumerate(m[3]):
        if posicoes_iguais(pos, p):
            return m[2][i]


# Modificadores


def eliminar_animal(m, p):
    """
    Modifica destrutivamente o prado m, eliminando o animal da posição p
    e devolve o próprio prado

    eliminar_animal: prado x posicao -> prado
    """
    for i, pos in enumerate(m[3]):
        if posicoes_iguais(pos, p):
            m[2] = m[2][:i] + m[2][i + 1:]
            m[3] = m[3][:i] + m[3][i + 1:]
            return m


def inserir_animal(m, a, p):
    """
    Modifica destrutivamente o prado m, acrescentando na posição p
    do prado, o animal a, e devolve o próprio prado

    inserir_animal: prado x animal x posicao -> prado
    """
    m[2] = m[2] + (a,)
    m[3] = m[3] + (p,)
    return m


def mover_animal(m, p1, p2):
    """
    Modifica destrutivamente o prado m, movimentando o animal da posição p1
    para a posição p2

    mover_animal: prado x posicao x posicao -> prado
    """
    animal = obter_animal(m, p1)
    eliminar_animal(m, p1)
    inserir_animal(m, animal, p2)
    return m


# Teste


def prados_iguais(p1, p2):
    """
    Testa se os argumentos são TAD prados e são iguais

    prados_iguais: universal x universal -> booleano
    """
    return p1 == p2 and eh_prado(p1) and eh_prado(p2)


# Transformador


def prado_para_str(m):
    """
    Devolve uma cadeia de carateres que representa o prado

    prado_para_str: prado -> str
    """
    s = ""
    x = obter_tamanho_x(m)
    y = obter_tamanho_y(m)
    for i in range(y):
        if i == 0:
            s += "+" + (x - 2) * "-" + "+\n"
            continue
        if i == y - 1:
            s += "+" + (x - 2) * "-" + "+"
            continue
        for j in range(x):
            if j == 0:
                s += "|"
            elif j == x - 1:
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
    """
    Devolve o valor da posição p correspondente à ordem de leitura do prado m

    obter_valor_numerico: prado x posicao -> int
    """
    return obter_tamanho_x(m) * obter_pos_y(p) + obter_pos_x(p)


def obter_movimento(m, p):
    """
    Devolve a posição seguinte do animal na posição p dentro do prado m
    de acordo com as regras de movimento dos animais

    obter_movimento: prado x posicao -> posicao
    """
    adj = obter_posicoes_adjacentes(p)
    adj_novo = []
    existe_presa = False
    for pos in adj:
        if eh_posicao_livre(m, pos) and not existe_presa:
            adj_novo.append(pos)
        elif (
            eh_posicao_animal(m, pos)
            and eh_predador(obter_animal(m, p))
            and eh_presa(obter_animal(m, pos))
        ):
            if not existe_presa:
                adj_novo = []
                existe_presa = True
            adj_novo.append(pos)
    if len(adj_novo) == 0:
        return cria_copia_posicao(p)
    return cria_copia_posicao(
        adj_novo[obter_valor_numerico(m, p) % len(adj_novo)]
    )


#########################################
#  2.2 Funções Adicionais
#########################################


def geracao(m):
    """
    Modifica o prado m de acordo com a evolução correspondente a uma geração
    completa. Isto é, seguindo a ordem de leitura do prado, cada animal
    realiza o seu turno de ação de acordo com as regras definidas

    geracao: prado -> prado
    """
    ja_se_moveram = []
    pos_animais = obter_posicao_animais(m)
    for pos in pos_animais:
        if not any(posicoes_iguais(pos, p) for p in ja_se_moveram):
            animal = cria_copia_animal(obter_animal(m, pos))
            aumenta_idade(animal)
            mov = obter_movimento(m, pos)
            if eh_predador(animal):
                if eh_posicao_animal(m, mov) and eh_presa(
                    obter_animal(m, mov)
                ):
                    reset_fome(animal)
                    eliminar_animal(m, mov)
                    ja_se_moveram.append(mov)
                else:
                    aumenta_fome(animal)

            eliminar_animal(m, pos)

            if not posicoes_iguais(mov, pos) and eh_animal_fertil(animal):
                inserir_animal(m, reproduz_animal(animal), pos)
            if not eh_animal_faminto(animal):
                inserir_animal(m, animal, mov)
    return m


def simula_ecossistema(f, g, v):
    """
    Simula a evolução do prado inicial definido pelo ficheiro de configuração f
    ao longo de g gerações, com ou sem modo verboso dependendo do booleano v

    simula_ecossistema: str x int x booleano -> tuplo
    """
    def mostra_dados_geracao(pred, presas, geracao, prado):
        print(f"Predadores: {pred} vs Presas: {presas} (Gen. {geracao})")
        print(prado_para_str(prado))

    with open(f, mode="r", encoding="utf-8") as file:
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
    for i in range(g + 1):
        if i == 0:  # 1ª geração
            pred = obter_numero_predadores(m)
            presas = obter_numero_presas(m)
            mostra_dados_geracao(pred, presas, 0, m)
            if v:
                pred_ant = pred
                presas_ant = presas
        elif v:  # modo verboso
            pred = obter_numero_predadores(m)
            presas = obter_numero_presas(m)
            if pred != pred_ant or presas != presas_ant:
                mostra_dados_geracao(pred, presas, i, m)
            pred_ant = pred
            presas_ant = presas
        if i == g:  # última geração
            if not v:
                pred = obter_numero_predadores(m)
                presas = obter_numero_presas(m)
                mostra_dados_geracao(pred, presas, g, m)
            return pred, presas
        m = geracao(m)
