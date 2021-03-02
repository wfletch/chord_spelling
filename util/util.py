
class chord_quality:
	def __init__(self, name, intervals):
		self.name = name
		self.intervals = intervals
	def __len__(self):
		return len(intervals)

class chord:
	def __init__(self, root, chord_quality, basic=True):
		self.root = root
		self.chord_quality = chord_quality
		self.length = len(chord_quality)
	
	def __len__(self):
		return self.length
	def get_component(self, component)


class note:
	def __init__(self, value, enharmonic):
		self.value = value
		self.enharmonic = enharmonic

	def getEnharmonic(self):
		return self.enharmonic
