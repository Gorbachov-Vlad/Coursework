import pygame
from main_test import deploymentScreen


def test_deploymentScreen():
    pygame.init()  # Ініціалізація Pygame
    SCREENWIDTH = 1260
    SCREENHEIGHT = 760
    GAMESCREEN = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))

    try:
        deploymentScreen(GAMESCREEN)

        # Додайте перевірки для перевірки відображення екрану розстановки кораблів
        # Наприклад, перевірка кольору певного пікселя (x, y) на екрані:
        x, y = 200, 200
        pixel_color = GAMESCREEN.get_at((x, y))
        expected_color = (37, 79, 143, 255)

        if pixel_color == expected_color:
            print(f"Тест пройшов успішно: колір пікселя на ({x}, {y}) відповідає очікуваному {expected_color}")
        else:
            print(f"Тест не пройшов: колір пікселя на ({x}, {y}) є {pixel_color}, очікувався {expected_color}")

    except Exception as e:
        print(f"Тест завершився з помилкою: {e}")

    pygame.quit()  # Завершення Pygame


test_deploymentScreen()
