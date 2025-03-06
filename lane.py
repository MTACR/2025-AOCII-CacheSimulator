class Lane:
    def __init__(self):
        self.tag = 0
        self.val = False

    def get_tag(self):
        return self.tag

    def set_tag(self, tag):
        self.tag = tag

    def is_val(self):
        return self.val

    def set_val(self, val):
        self.val = val