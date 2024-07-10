from otree.api import (
    BaseConstants,
    BaseGroup,
    BasePlayer,
    BaseSubsession,
    Page,
)

doc = """
Encoding task
"""


class C(BaseConstants):
    NAME_IN_URL = "encoding"
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 2


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass


# PAGES
class Intro(Page):
    @staticmethod
    def is_displayed(player: Player) -> bool:
        return player.round_number == 1


class Decision(Page):
    pass


class Outcome(Page):
    @staticmethod
    def is_displayed(player: Player) -> bool:
        return player.round_number == C.NUM_ROUNDS


page_sequence = [
    Intro,
    Decision,
    Outcome,
]