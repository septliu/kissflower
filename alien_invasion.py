import pygame
from pygame.sprite import Group
from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship
import game_functions as gf

def run_game():
	#initiation game and create a screen
	pygame.init()
	ai_settings=Settings()
	screen=pygame.display.set_mode(
		(ai_settings.screen_width,ai_settings.screen_height))
	pygame.display.set_caption('Kiss Flower')
	
	#create button
	play_button = Button(ai_settings, screen, "Play")
	
	#create one event for saving game stats and scoreboard
	stats = GameStats(ai_settings)
	sb = Scoreboard(ai_settings,screen,stats)
	
	#create a ship
	ship=Ship(ai_settings,screen)
	
	#create a group for saving bullets
	bullets = Group()
	
	#create a group for alien 
	aliens = Group()
	
	#crate aliens
	gf.create_fleet(ai_settings,screen,ship,aliens)
	
	#begin main cycle
	while True:
		gf.check_events(ai_settings,screen,stats,sb,play_button,
			ship,aliens,bullets)
		if stats.game_active:
			ship.update()
			gf.update_bullets(ai_settings,screen,stats,sb,ship,aliens,
								bullets)
			gf.update_aliens(ai_settings,stats,screen,sb,ship,aliens,
								bullets)
		gf.update_screen(ai_settings,screen,stats,sb,ship,aliens,bullets, 
			play_button)
run_game()

