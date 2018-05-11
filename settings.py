import pygame
class Settings():
	"""save settings"""
	def __init__(self):
		"""initiation of static settings"""
		#screen setting
		self.screen_width=900
		self.screen_height=600
		self.bg_color=(66,146,108)
		
		#ship site
		self.ship_speed_factor=1.5
		
		#bullet setting
		self.bullet_speed_factor = 1
		#self.bullet_width = 3
		#self.bullet_height = 15
		#self.bullet_color = 60,60,60
		self.bullets_allowed = 3
		
		#setting alien
		self.alien_speed_factor = 0.5
		self.fleet_drop_speed = 10
		
		#self.fleet_direction 1 is move right and -1 is move left
		self.fleet_direction = 1
		self.ship_limit = 3

		#faster the game according on the velcility
		self.speedup_scale = 1.1
		#speedup score scale
		self.score_scale = 1.5
		
		self.initialize_dynamic_settings()
		
	def initialize_dynamic_settings(self):
		"""change the setting with game running"""
		self.ship_speed_factor = 1.5
		self.bullet_speed_factor = 1
		self.alien_speed_factor = 0.5
		
		#1 is to right,-1 is to left
		self.fleet_direction = 1
		
		#score
		self.alien_points = 50
		
	def increase_speed(self):
		"""increase settings and score scale"""
		self.ship_speed_factor *= self.speedup_scale
		self.bullet_speed_factor *= self.speedup_scale
		self.alien_speed_factor *= self.speedup_scale		
		
		self.alien_points = int(self.alien_points * self.score_scale)
		
		
		
		
















