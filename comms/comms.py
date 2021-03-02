class display:
	def __init__(self, display_id, pinout):
		self.id = display_id
		self.pinout = pinout
	def print(self, character, sharp=False, flat=False):
		if sharp and flat:
			raise Exception("Displayed Note Cannot be Sharp and Flat")
		# TODO: Display Character