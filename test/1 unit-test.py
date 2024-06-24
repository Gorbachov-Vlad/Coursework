import pygame
from main_test import mainMenuScreen


def test_mainMenuScreen():
    pygame.init()  # Ініціалізація Pygame
    SCREENWIDTH = 1260
    SCREENHEIGHT = 760
    GAMESCREEN = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))

    try:
        mainMenuScreen(GAMESCREEN)

        # Додайте перевірки для перевірки відображення головного меню
        # Наприклад, перевірка кольору певного пікселя (x, y) на екрані:
        x, y = 100, 100
        pixel_color = GAMESCREEN.get_at((x, y))
        expected_color = (251, 233, 125, 255)  # Припустимо, що білий колір має бути на цій позиції

        if pixel_color == expected_color:
            print(f"Тест пройшов успішно: колір пікселя на ({x}, {y}) відповідає очікуваному {expected_color}")
        else:
            print(f"Тест не пройшов: колір пікселя на ({x}, {y}) є {pixel_color}, очікувався {expected_color}")

    except Exception as e:
        print(f"Тест завершився з помилкою: {e}")

    pygame.quit()  # Завершення Pygame


test_mainMenuScreen()
