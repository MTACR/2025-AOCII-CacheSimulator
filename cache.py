from cache_set import Cache_Set


class Cache:  # Define a classe Cache e seus parâmetros
    def __init__(self, nsets, bsize, assoc, subst):
        self.nsets = nsets
        self.bsize = bsize
        self.assoc = assoc
        self.subst = subst
        self.set = [Cache_Set(assoc, subst) for _ in
                    range(nsets)]  # Cria uma lista de conjuntos (cada conjunto é um objeto da classe Cache_Set)
        self.nesp = nsets * assoc  # Calcula o número total de espaços disponíveis na cache (conjuntos * vias)
        self.cont_ocp = 0

    def load(self, ad):  # Calcula o índice do conjunto na cache (qual conjunto será acessado)
        offset = self.bsize.bit_length() - 1
        index_bits = self.nsets.bit_length() - 1
        tag = ad >> (offset + index_bits)
        index = (ad >> offset) & (2**index_bits - 1)

        returns = self.set[index].insert(tag)

        if returns == 1:
            self.cont_ocp += 1

        return returns

    def is_full(self):  # Retorna True se a cache estiver completamente cheia, caso contrário, retorna False.
        return self.cont_ocp >= self.nesp
