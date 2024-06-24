import pygame
import unittest
from unittest.mock import MagicMock
from main_test import Player, takeTurns, EasyComputer  # Імпорт необхідних класів і функцій з вашого проекту

class TestTakeTurns(unittest.TestCase):

    def setUp(self):
        # Ініціалізація Pygame
        pygame.init()

    def tearDown(self):
        # Завершення роботи з Pygame
        pygame.quit()

    def test_takeTurns(self):
        # Створюємо мокові об'єкти гравців
        player1 = Player()
        computer = EasyComputer()

        # Встановлюємо початкову чергу гравців
        player1.turn = True
        computer.turn = False

        # Перевіряємо, що спочатку черга першого гравця
        self.assertTrue(player1.turn, "Test failed: Expected player1 turn to be True initially")
        self.assertFalse(computer.turn, "Test failed: Expected computer turn to be False initially")

        # Викликаємо функцію takeTurns
        takeTurns(player1, computer)

        # Перевіряємо, що після виклику функції черга змінилася
        self.assertTrue(player1.turn, "Test failed: Expected player1 turn to be False after takeTurns")
        self.assertFalse(computer.turn, "Test failed: Expected computer turn to be True after takeTurns")

        # Моделюємо ситуацію, коли другий гравець не змінює чергу
        computer.makeAttack = MagicMock(return_value=False)
        takeTurns(player1, computer)

        # Перевіряємо, що після виклику функції черга залишається у другого гравця
        self.assertTrue(player1.turn, "Test failed: Expected player1 turn to remain False")


        print("Test for takeTurns completed successfully.")

if __name__ == '__main__':
    unittest.main()
