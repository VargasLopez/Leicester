import random

from otree.api import (
    BaseConstants,
    BaseGroup,
    BasePlayer,
    BaseSubsession,
    Currency,
    Page,
    models,
)

doc = """
Encryption task
"""


class C(BaseConstants):
    NAME_IN_URL = "encrypt"
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 2
    PAYMENT_PER_CORRECT = Currency(0.10)


class Subsession(BaseSubsession):
    payment_per_correct = models.CurrencyField()

    def setup(self):
        self.payment_per_correct = C.PAYMENT_PER_CORRECT
        word = "".join(random.choices("AB", k=5))
        for player in self.get_players():
            player.word = word


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    word = models.StringField()
    response_1 = models.IntegerField()
    response_2 = models.IntegerField()
    response_3 = models.IntegerField()
    response_4 = models.IntegerField()
    response_5 = models.IntegerField()
    is_correct = models.BooleanField()

    @property
    def response_fields(self):
        return ["response_1", "response_2", "response_3", "response_4", "response_5"]

    @property
    def response_as_list(self):
        return [self.response_1, self.response_2, self.response_3,
                self.response_4, self.response_5]

    @property
    def dictionary(self):
        return {"A": 1, "B": 2}

    def compute_outcome(self):
        self.is_correct = all(
            response == self.dictionary[letter]
            for (response, letter) in zip(self.response_as_list, self.word,
                                          strict=True)
        )
        if self.is_correct:
            self.payoff = self.subsession.payment_per_correct


def creating_session(subsession):
    subsession.setup()


# PAGES
class Intro(Page):
    @staticmethod
    def is_displayed(player: Player) -> bool:
        return player.round_number == 1


class Decision(Page):
    form_model = "player"

    @staticmethod
    def get_form_fields(player):
        return player.response_fields

    @staticmethod
    def before_next_page(player, timeout_happened):
        player.compute_outcome()


class Outcome(Page):
    @staticmethod
    def is_displayed(player: Player) -> bool:
        return player.round_number == C.NUM_ROUNDS


page_sequence = [
    Intro,
    Decision,
    Outcome,
]