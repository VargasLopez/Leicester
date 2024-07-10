from otree.api import *

doc = """
A simple Tullock contest game with possibly different costs of effort.
"""


class C(BaseConstants):
    NAME_IN_URL = 'contest'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 2
    ENDOWMENT = 20


class Subsession(BaseSubsession):
    is_paid = models.BooleanField()


    def setup(self):
        self.is_paid = (self.round_number == 1)

class Group(BaseGroup):
    pass


class Player(BasePlayer):
    endowment = models.IntegerField()
    cost_per_ticket = models.IntegerField()
    tickets_purchased = models.IntegerField()
    is_winner = models.BooleanField()
    earnings = models.IntegerField()


def creating_session(subsession):
    subsession.setup()

# PAGES
class Intro(Page):
    pass


class SetupRound(WaitPage):
    pass


class Decision(Page):
    pass


class WaitForDecisions(WaitPage):
    pass


class Results(Page):
    pass


class EndBlock(Page):
    pass


page_sequence = [
    Intro,
    SetupRound,
    Decision,
    WaitForDecisions,
    Results,
    EndBlock,
]
