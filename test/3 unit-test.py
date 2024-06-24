import pygame
from main_test import endScreen


def test_endScreen():
    pygame.init()  # Ініціалізація Pygame
    SCREENWIDTH = 1260
    SCREENHEIGHT = 760
    GAMESCREEN = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
    player_win = True  # Припустимо, що гравець виграв

    try:
        endScreen(GAMESCREEN, player_win)

        # Додайте перевірки для перевірки відображення екрану завершення гри
        # Наприклад, перевірка кольору певного пікселя (x, y) на екрані:
        x, y = 630, 380  # Центр екрану
        pixel_color = GAMESCREEN.get_at((x, y))
        expected_color = (148, 144, 161, 255)  # Припустимо, що зелений колір має бути на цій позиції при виграші

        if pixel_color == expected_color:
            print(f"Тест пройшов успішно: колір пікселя на ({x}, {y}) відповідає очікуваному {expected_color}")
        else:
            print(f"Тест не пройшов: колір пікселя на ({x}, {y}) є {pixel_color}, очікувався {expected_color}")

    except Exception as e:
        print(f"Тест завершився з помилкою: {e}")

    pygame.quit()  # Завершення Pygame


test_endScreen()
