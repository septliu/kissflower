import pygame
import random
from pygame.sprite import Sprite

class Alien(Sprite):
	"""alien class"""
	
	def __init__(self,ai_settings,screen):
		"""initiate alien and position"""
		super(Alien,self).__init__()
		self.screen = screen
		self.ai_settings = ai_settings
		
		#load alien and set rect
		self.image1 = pygame.image.load('images/flower1.bmp')
		self.image2 = pygame.image.load('images/flower2.bmp')
		self.image3 = pygame.image.load('images/flower3.bmp')
		self.image4 = pygame.image.load('images/flower4.bmp')
		self.image5 = pygame.image.load('images/flower5.bmp')
		self.image6 = pygame.image.load('images/flower6.bmp')
		succulents = [self.image1,self.image2,self.image3,self.image4,
						self.image5,self.image6]
		self.image = random.choice(succulents)
		self.rect = self.image.get_rect()
		
		#every alien appear at the up-left corner
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height
		
		#save the accurate position of alien
		self.x = float(self.rect.x)
		
	def blitme(self):
		"""draw alien at one positon"""
		self.screen.blit(self.image,self.rect)

	def check_edges(self):
		"""if touch the border then reture true"""
		screen_rect = self.screen.get_rect()
		if self.rect.right >= screen_rect.right:
			return True
		elif self.rect.left <= 0:
			return True		
							
	def update(self):
		"""move right and left"""
		self.x += (self.ai_settings.alien_speed_factor*
						self.ai_settings.fleet_direction)
		self.rect.x = self.x
		

			




















		
	
