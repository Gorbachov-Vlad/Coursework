import pygame
from main_test import updateGameScreen


def test_updateGameScreen():
    pygame.init()  # Ініціалізація Pygame
    SCREENWIDTH = 1260
    SCREENHEIGHT = 760
    GAMESCREEN = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
    GAMESTATE = 'Main Menu'
    player_win = False  # Припустимо, що гравець не виграв

    try:
        updateGameScreen(GAMESCREEN, GAMESTATE, player_win)

        # Додайте перевірки для перевірки правильності оновлення ігрового екрану
        # Наприклад, перевірка кольору певного пікселя (x, y) на екрані:
        x, y = 630, 380  # Центр екрану
        pixel_color = GAMESCREEN.get_at((x, y))

        # Припустимо, що в головному меню центральний піксель буде білим
        expected_color = (34, 35, 53, 255)  # Білий колір

        if pixel_color == expected_color:
            print(f"Тест пройшов успішно: колір пікселя на ({x}, {y}) відповідає очікуваному {expected_color}")
        else:
            print(f"Тест не пройшов: колір пікселя на ({x}, {y}) є {pixel_color}, очікувався {expected_color}")

    except Exception as e:
        print(f"Тест завершився з помилкою: {e}")

    pygame.quit()  # Завершення Pygame


test_updateGameScreen()
