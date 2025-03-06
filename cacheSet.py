import random
from collections import deque
from lane import Lane

class CacheSet:
    def __init__(self, assoc, subst):
        self.lanes = [Lane() for _ in range(assoc)]
        self.subst = subst
        self.list = deque(maxlen=assoc)

    def insert(self, tag):
        for i, lane in enumerate(self.lanes):
            if lane.is_val():
                if lane.get_tag() == tag:
                    if self.subst == 'L':
                        if i in self.list:
                            self.list.remove(i)
                        self.list.append(i)
                    return 0
            else:
                lane.set_tag(tag)
                lane.set_val(True)
                if i not in self.list:
                    self.list.append(i)
                return 1

        return self.replace(tag)

    def replace(self, tag):
        if self.subst == 'R':
            n_lane = random.randint(0, len(self.lanes) - 1)
            self.lanes[n_lane].set_tag(tag)
            return 2

        if self.subst in ('F', 'L'):
            if not self.list:
                n_lane = 0
            else:
                n_lane = self.list.popleft()
            self.list.append(n_lane)
            self.lanes[n_lane].set_tag(tag)
            return 2

        return -1