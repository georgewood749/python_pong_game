from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.player1_score = 0
        self.player2_score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.setpos(0, 260)
        self.write(f"{self.player1_score} | {self.player2_score}", False, "center", ("Courier", 24, "normal"))

    def increase_player1_score(self):
        self.clear()
        self.player1_score += 1
        self.write(f"{self.player1_score} | {self.player2_score}", False, "center", ("Courier", 24, "normal"))

    def increase_player2_score(self):
        self.clear()
        self.player2_score += 1
        self.write(f"{self.player1_score} | {self.player2_score}", False, "center", ("Courier", 24, "normal"))

    def game_over(self):
        winner = ""
        self.clear()
        self.setpos(0, 0)
        if self.player1_score >= 11:
            winner = "Player 1"
        elif self.player2_score >= 11:
            winner = "Player 2"
        self.write(f"{winner} wins!", False, "center", ("Courier", 24, "normal"))
