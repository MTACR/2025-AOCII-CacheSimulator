import random


class Cache_Set:
    def __init__(self, assoc, subst): # Inicializa um conjunto da cache
        self.ways = [{'tag': None, 'val': False} for _ in range(assoc)]
        self.subst = subst
        self.list = []

    def insert(self, tag): # Insere um novo bloco no conjunto da cache.
        for i, way in enumerate(self.ways):
            if way['val']: # Se o bloco for válido (ou seja, já contém dados)
                if way['tag'] == tag: # Se a tag já está presente na cache (hit)
                    if self.subst == 'L': # Se a política for LRU 
                        self.list.remove(i) # Remove a posição atual da lista
                        self.list.append(i) # Adiciona ao final, indicando acesso recente
                    return 0 # Retorna hit
            else: # Se encontrar um bloco inválido (vazio), insere a nova tag nele
                way['tag'] = tag
                way['val'] = True
                self.list.append(i) # Adiciona a posição do bloco na lista
                return 1 # Retorna miss compulsório

        return self.replace(tag) # Se todas as vias estavam ocupadas, aplica uma substituição

    def replace(self, tag):  # Substitui um bloco quando a cache está cheia.
        if self.subst == 'R': # Política de substituição aleatória (Random), Escolhe um bloco aleatório para ser substituído
            nway = random.randint(0, len(self.ways) - 1)
            self.ways[nway]['tag'] = tag # Atualiza a tag do bloco substituído
            return 2 # Retorna miss de capacidade/conflito
        elif self.subst == 'F' or self.subst == 'L':
            nway = self.list.pop(0) # Remove o primeiro da lista
            self.list.append(nway) # Reinsere no final, indicando novo uso
            self.ways[nway]['tag'] = tag # Substitui a tag do bloco escolhido
            return 2 # Retorna miss de capacidade/conflito
        return -1 # Caso a política de substituição seja inválida
