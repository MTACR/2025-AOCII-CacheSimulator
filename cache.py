from cacheSet import CacheSet

class Cache:
    def __init__(self, n_sets, b_size, assoc, subst):
        self.n_sets = n_sets
        self.b_size = b_size
        self.assoc = assoc
        self.subst = subst

        self.conj = [CacheSet(assoc, subst) for _ in range(n_sets)]
        self.n_esp = n_sets * assoc
        self.cont_occupied = 0

    def load(self, end):
        end_conj = end // self.b_size
        index = end_conj % self.n_sets
        tag = end_conj // self.n_sets

        returns = self.conj[index].insert(tag)

        if returns == 1:
            self.cont_occupied += 1

        return returns

    def is_full(self):
        return self.cont_occupied >= self.n_esp