class key_quality:
	def __init__(self, name, intervals):
		self.name = name
		self.intervals = intervals

class key:
	def __init__(self,root, key_quality):
		self.modes = []
		self.root = root
		self.

class chord_quality:
	def __init__(self, name, intervals):
		self.name = name
		self.intervals = intervals

	def __len__(self):
		return len(intervals)

	def getIntervals(self):
		return self.intervals

class chord:
	def __init__(self, root, chord_quality):
		self.root = root
		self.chord_quality = chord_quality
		self.length = len(chord_quality)
		self.spelling = self.buildSpelling()

	def buildSpelling(self):
		recipe = self.chord_quality.getIntervals()
		root = self.root
	def __len__(self):
		return self.length

	def get_component(self, component):


class note:
	def __init__(self, value, modifier=None):
		self.value = value
		self.modifier = modifier
