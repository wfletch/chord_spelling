#TODO: Load Config
#TODO: Set Up Displays
#TODO: Welcome Screen
#TODO: Get Difficulty (Software)
#TODO: Get Difficulty (Hardware)
#TODO: Save Scores

# hello_psg.py

import zmq

class master_node():
	context= zmq.Context()
	def __init__(self):
		self.sink_socket =  self.context.socket(zmq.PUB)


if __name__ == "__main__":
	cn = master_node()