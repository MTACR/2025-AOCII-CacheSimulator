import random

from way import Way


class Cache_Set:
    def __init__(self, assoc, subst):
        self.ways = [Way() for _ in range(assoc)]
        self.subst = subst
        self.list = []

    def insert(self, tag):
        for i, way in enumerate(self.ways):
            if way.is_val():
                if way.get_tag() == tag:
                    if self.subst == 'L':
                        self.list.remove(i)
                        self.list.append(i)
                    return 0
            else:
                way.set_tag(tag)
                way.set_val(True)
                self.list.append(i)
                return 1

        return self.replace(tag)

    def replace(self, tag):
        if self.subst == 'R':
            n_via = random.randint(0, len(self.ways) - 1)
            self.ways[n_via].set_tag(tag)
            return 2
        elif self.subst == 'F' or self.subst == 'L':
            n_via = self.list.pop(0)
            self.list.append(n_via)
            self.ways[n_via].set_tag(tag)
            return 2
        return -1