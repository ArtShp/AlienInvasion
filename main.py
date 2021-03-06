import pygame
from pygame.sprite import Group
from files.settings import Settings
from files.game_stats import GameStats
from files.scoreboard import Scoreboard
from files.button import Button
from files.ship import Ship
from files import game_functions as gf


def run_game():
    # Инициализирует pygame, settings и объект экрана.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption('Alien Invasion')

    # Создание кнопки Play.
    play_button = Button(ai_settings, screen, 'Play')

    # Создание экземпляров GameStats и Scoreboard.
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    # Создание корабля, группы пришельцев и группы пуль.
    ship = Ship(ai_settings, screen)
    aliens = Group()
    bullets = Group()

    # Создание флота пришельцев.
    gf.create_fleet(ai_settings, screen, ship, aliens)

    gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)
    # Запуск основного цикла игры.
    while True:
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)
        if stats.game_active:
            ship.update()
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)


run_game()
