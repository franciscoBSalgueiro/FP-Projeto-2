import timeit

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


def obter_posicoes_adjacentes1(p):
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

def eh_posicao_animal1(m, p):
    for e in m[3]:
        if posicoes_iguais(p,e):
            return True
    return False

def eh_posicao_animal2(m, p):
    return any(posicoes_iguais(p,e) for e in m[3])

def eh_presa(p):
    return True
if __name__ == "__main__":
    import timeit
    print(timeit.timeit("len([a for a in ((3,5),(4,4),(6,7)) if eh_presa(a)])", setup="from __main__ import obter_pos_x, obter_pos_y, cria_posicao, posicoes_iguais, eh_presa, eh_posicao, eh_posicao_animal2"))
    print(timeit.timeit("len(tuple(filter(eh_presa,((3,5),(4,4),(6,7)))))", setup="from __main__ import obter_pos_x, obter_pos_y, cria_posicao, posicoes_iguais, eh_presa, eh_posicao, eh_posicao_animal2"))