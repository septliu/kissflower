class GameStats():
	"""follow the stats information"""
	
	def __init__(self,ai_settings):
		"""initiate stats"""
		self.ai_settings = ai_settings
		self.reset_stats()
		#active when game begin
		self.game_active = False
		self.high_score = 0
		self.level = 1
		
	def reset_stats(self):
		"""reset the changing stats"""
		self.ships_left = self.ai_settings.ship_limit
		self.score = 0
