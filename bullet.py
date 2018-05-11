import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
	"""manage bullet"""
	def __init__(self,ai_settings,screen,ship):
		"""create bullets near ship"""
		super(Bullet,self).__init__()
		self.screen = screen
		
		#create a rect at (0,0) and give a position to it
		#self.rect = pygame.Rect(0,0,ai_settings.bullet_width,
			#ai_settings.bullet_height)
		self.image=pygame.image.load('images/kiss.bmp')
		self.rect=self.image.get_rect()
		self.rect.centerx=ship.rect.centerx
		self.rect.top=ship.rect.top
		
		#save bullet float position
		self.y = float(self.rect.y)
		
		#self.color = ai_settings.bullet_color
		self.speed_factor = ai_settings.bullet_speed_factor
		
	def update(self):
		"""move up"""
		#update the float of bullet
		self.y -= self.speed_factor
		self.rect.y = self.y
		
	def draw_bullet(self):
		"""draw bullet on screen"""
		#pygame.draw.rect(self.screen,self.rect)
		self.screen.blit(self.image,self.rect)
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
