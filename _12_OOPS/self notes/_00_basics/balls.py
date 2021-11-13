class Ball:
    def __init__(self, type, game, name="cricketball"):
        self.type = type
        self.game = game
        self.name = name

cricket_ball = Ball("hard", "cricket")

print((cricket_ball))