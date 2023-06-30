import unittest
from card import Card
from card_game import CardGame

class TestCardGame(unittest.TestCase):

    def setUp(self):
        self.card = Card(suit='clubs', value=3)
        self.game = CardGame()
        self.card1 = Card(suit='diamonds',value=10)
        self.card2 = Card(suit='clubs', value=5)
        self.cards = [self.card1, self.card2]

    def test_check_for_ace_with_non_ace_card(self):
        result = self.game.check_for_ace(self.card)

        self.assertEqual(False, result)

    def test_highest_card_with_card1_having_higher_value(self):
        result = self.game.highest_card(self.card1, self.card2)

        self.assertEqual(result, self.card1)

    def test_cards_total_with_multiple_cards(self):
        result = self.game.cards_total(self.cards)

        self.assertEqual("You have a total of 15", result)
    

if __name__ == '__main__':
    unittest.main()