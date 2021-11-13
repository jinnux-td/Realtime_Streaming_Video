class VideoStream:
	def __init__(self, filename):
		self.filename = filename
		try:
			self.file = open(filename, 'rb')
		except:
			raise IOError
		self.frameNum = 0
		self.totalFrame = 0

	def totalFrame(self):
		data = self.file.read(5) # Get the framelength from the first 5 bits
		if data: 
			framelength = int(data)
			self.file.read(framelength)
			self.totalFrame += 1

		while data:
			data = self.file.read(5)
			framelength = int(data)
			data = self.file.read(framelength)
			self.totalFrame += 1
		
		return self.totalFrame
		
	def nextFrame(self):
		"""Get next frame."""
		data = self.file.read(5) # Get the framelength from the first 5 bits
		if data: 
			framelength = int(data)
							
			# Read the current frame
			data = self.file.read(framelength)
			self.frameNum += 1
		return data
		
	def frameNbr(self):
		"""Get frame number."""
		return self.frameNum
	
	