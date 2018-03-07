import cv2
import os

class imageChunk:
	def __init__(self, totalWhite, x, y):
		self.totalWhite = totalWhite
		self.x = x
		self.y = y


def crop_image(img, width, height, x, y):
	"""Split image into 16x16 chunks, then find the highest light value possible. Get R,G,B and add each of the pixels in the 16x16 area. The shiniest pixels are the cancer cells"""

	imageY,imageX = img.shape
	cropImageChunks = []
	"""First split image into chunks"""
	for chunkX in range(0,imageX%16):
		for chunkY in range(0,imageY%16):
			grayVal = 0

			"""Analyze pixels in chunk"""
			for pixelX in range(chunkX*16, chunkX*16+16):
				for pixelY in range(chunkY*16, chunkY*16+16):
					grayVal += img[pixelX,pixelY]

			chunk = imageChunk(grayVal, chunkX*16+8, chunkY*16+8)
			cropImageChunks.append(chunk)

	lowWhite = 0
	startx = x//2-200
	starty = y//2-200

	for item in cropImageChunks:
		if lowWhite < 5500:
			if item.x > startx:
				if item.y > starty:
					lowWhite = item.totalWhite
					startx = item.x
					starty = item.y



	return img[starty:starty+height,startx:startx+width]

def grayscale_images(filepath):

	"""TO DO: CROP IMAGE"""
	directory = "grayScaledImages"
	if not os.path.exists(directory):
		os.makedirs(directory)


	fileNumber = 0
	for subdir, dirs, files in os.walk(filepath):
		for file in files:
			"""Files in filepath, all of them in all sub directories."""
			print(os.path.join(subdir,file))

			while os.path.isfile('grayScaledImages/gray' + str(fileNumber) + '.png'):
				fileNumber+=1

			image = cv2.imread(os.path.join(subdir,file))
			gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

			y,x = gray_image.shape

			cv2.imwrite('grayScaledImages/gray' + str(fileNumber) + '.png', crop_image(gray_image,400,400,x,y))
			fileNumber += 1

def opt(argv):
	opts = {}
	while argv:
		if argv[0][0] == '-':
			opts[argv[0]] = argv[1]
		argv = argv[1:]
	return opts

if __name__ == "__main__":
	from sys import argv
	args = opt(argv)
	if '-d' in args: 
		grayscale_images(args['-d'])

