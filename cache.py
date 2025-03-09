from cache_set import Cache_Set


class Cache:
    def __init__(self, nsets, bsize, assoc, subst):
        self.nsets = nsets
        self.bsize = bsize
        self.assoc = assoc
        self.subst = subst
        self.set = [Cache_Set(assoc, subst) for _ in range(nsets)]
        self.nesp = nsets * assoc
        self.cont_ocp = 0

    def load(self, end):
        ad_set = end // self.bsize
        index = ad_set % self.nsets
        tag = ad_set // self.nsets

        returns = self.set[index].insert(tag)

        if returns == 1:
            self.cont_ocp += 1

        return returns

    def is_full(self):
        return self.cont_ocp >= self.nesp
