class Score:

    def __init__(self):
        self.reset()

    def reset(self):
        self.value = 0
        self.high_score = 0

    def add(self, points=1):

        self.value += points

        if self.value > self.high_score:
            self.high_score = self.value