import pygame
from pygame.sprite import Sprite
class Ship(Sprite):
	def __init__(self,ai_settings,screen):
		"""initiate ship and position"""
		super(Ship,self).__init__()
		self.screen=screen
		self.ai_settings=ai_settings
		#upload ship image
		self.image=pygame.image.load('images/Logo.bmp')
		self.rect=self.image.get_rect()
		self.screen_rect=screen.get_rect()
		
		#let new ship park in the middle of bottom
		self.rect.centerx=self.screen_rect.centerx
		self.rect.bottom=self.screen_rect.bottom
		
		#save point on paremeter of ship
		self.center=float(self.rect.centerx)
		
		#moving mark
		self.moving_right=False
		self.moving_left=False
	def update(self):
		"""adjust the position of ship according to moving mark"""
		#update the center value not rect value
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.center += self.ai_settings.ship_speed_factor
		if self.moving_left and self.rect.left > 0:
			self.center -= self.ai_settings.ship_speed_factor	
		
		#update rect accoding self.center
		self.rect.centerx = self.center
				
	def blitme(self):
		"""draw ship at the appointed site"""
		self.screen.blit(self.image,self.rect)
		
	def center_ship(self):
		"""put the ship in the middle of bottom"""
		self.center = self.screen_rect.centerx




















