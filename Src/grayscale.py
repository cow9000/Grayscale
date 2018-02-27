import cv2
import os

def grayscale_images(filepath):
	directory = "grayScaledImages"
	if not os.path.exists(directory):
		os.makedirs(directory)


	fileNumber = 0
	for subdir, dirs, files in os.walk(filepath):
		for file in files:
			"""Files in filepath, all of them in all sub directories."""
			print(os.path.join(subdir,file))
			image = cv2.imread(os.path.join(subdir,file))
			gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
			cv2.imwrite('grayScaledImages/gray' + str(fileNumber) + '.png', gray_image)
			fileNumber += 1

def getopts(argv):
	opts = {}  # Empty dictionary to store key-value pairs.
	while argv:  # While there are arguments left to parse...
		if argv[0][0] == '-':  # Found a "-name value" pair.
			opts[argv[0]] = argv[1]  # Add key and value to the dictionary.
		argv = argv[1:]  # Reduce the argument list by copying it starting from index 1.
	return opts

if __name__ == "__main__":
	from sys import argv
	args = getopts(argv)
	if '-d' in args: 
		grayscale_images(args['-d'])

