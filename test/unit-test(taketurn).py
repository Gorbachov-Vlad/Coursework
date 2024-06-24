import unittest
from unittest.mock import MagicMock
from main_test import Player, takeTurns


class TestTakeTurns(unittest.TestCase):
    def test_takeTurns(self):
        # Створюємо мокові об'єкти гравців
        player1 = Player()
        player2 = Player()

        # Перевіряємо, що спочатку черга першого гравця
        self.assertTrue(player1.turn)
        self.assertFalse(player2.turn)

        # Викликаємо функцію takeTurns
        takeTurns(player1, player2)

        # Перевіряємо, що після виклику функції черга змінилася
        self.assertFalse(player1.turn)
        self.assertTrue(player2.turn)

        # Моделюємо ситуацію, коли другий гравець не змінює чергу
        player2.makeAttack = MagicMock(return_value=False)
        takeTurns(player1, player2)

        # Перевіряємо, що після виклику функції черга залишається у другого гравця
        self.assertFalse(player1.turn)
        self.assertTrue(player2.turn)


if __name__ == '__main__':
    unittest.main()
