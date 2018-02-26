import cv2


def grayscale_images(filepath):

	print(filepath)

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
		file(args['-d'])
