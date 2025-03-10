from cache_set import Cache_Set


class Cache: # Define a classe Cache
    def __init__(self, nsets, bsize, assoc, subst):
        self.nsets = nsets
        self.bsize = bsize
        self.assoc = assoc
        self.subst = subst
        self.set = [Cache_Set(assoc, subst) for _ in range(nsets)] # Cria uma lista de conjuntos (cada conjunto é um objeto da classe Cache_Set)
        self.nesp = nsets * assoc  # Calcula o número total de espaços disponíveis na cache (conjuntos * vias)
        self.cont_ocp = 0

    def load(self, end): # Calcula o índice do conjunto na cache (qual conjunto será acessado)
        ad_set = end // self.bsize # Divide o endereço pelo tamanho do bloco
        index = ad_set % self.nsets # Usa módulo para obter o índice do conjunto
        tag = ad_set // self.nsets # Calcula a tag

        returns = self.set[index].insert(tag)  # insere a tag no conjunto correspondente

        if returns == 1: # Se returns == 1, significa que foi um miss compulsório, então incrementamos os espaços ocupados
            self.cont_ocp += 1

        return returns # Retorna o tipo de acesso (hit ou miss)

    def is_full(self): #Retorna True se a cache estiver completamente cheia, caso contrário, retorna False.
        return self.cont_ocp >= self.nesp
