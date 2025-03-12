import random


class Cache_Set:
    def __init__(self, assoc, subst):
        self.ways = [{'tag': None, 'val': False} for _ in range(assoc)]
        self.subst = subst
        self.list = []

    def insert(self, tag):
        for i, way in enumerate(self.ways):
            if way['val']:  # se for True
                if way['tag'] == tag:
                    if self.subst == 'L':
                        self.list.remove(i)
                        self.list.append(i)
                    return 0  # hit
            else:
                way['tag'] = tag
                way['val'] = True
                self.list.append(i)
                return 1  # miss compulsório

        return self.replace(tag)

    def replace(self, tag):
        if self.subst == 'R':
            nway = random.randint(0, len(self.ways) - 1)
            self.ways[nway]['tag'] = tag
            return 2  # miss de capacidade/conflito
        elif self.subst == 'F' or self.subst == 'L':
            nway = self.list.pop(0)
            self.list.append(nway)
            self.ways[nway]['tag'] = tag
            return 2  # miss de capacidade/conflito
        return -1  # erro no tag
