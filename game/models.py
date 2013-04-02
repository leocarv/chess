from django.db import models
from chess import Board


class Game(models.Model):
    white_player = models.PositiveIntegerField()
    black_player = models.PositiveIntegerField()
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(null=True)
    last_move_date = models.DateTimeField(null=True)
    fen = models.CharField(max_length=100)

    def __unicode__(self):
        return self.id

    def move(self, move):
        try:
            # inicializa o board com o fen atual
            myBoard = Board(self.fen)
            # aplica o movimento
            myBoard.move_algebraic(move)
            # modifica o atributo FEN
            self.fen = myBoard.get_fen()
            # salva registro
            self.save()

            #for debugger
            print myBoard.to_ascii_art()

        except Exception, e:
            print e
            return False
        return True
