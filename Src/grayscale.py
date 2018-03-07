import cv2
import os

def crop_image(img, width, height, x, y):
    startx = x//2-(width//2)
    starty = y//2-(height//2)    
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

			cv2.imwrite('grayScaledImages/gray' + str(fileNumber) + '.png', crop_image(gray_image,300,300,x,y))
			fileNumber += 1

			#numpy for cropping

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

