class RecordScore:
    """Class to track a game's maximum score"""

    def __init__(self):
        self.score = 0

    def __call__(self, score):
        if score > self.score:
            self.score = score
        return self.score
