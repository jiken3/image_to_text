# imports
import os
from subprocess import call

# main
if __name__ == "__main__":

	# input path ('resource' folder)
	_input = os.path.abspath("resource")

	# check if _input exists
	if os.path.exists(_input) == True:

		# check for some file(s) inside the '_input' path
		for image in os.listdir(_input):
			file = os.path.join(_input, image)
			output = os.path.join("text_from_image")

			call(["tesseract", file, output])

			print("Done")

	# if _input doesn't exists
	else:
		print("No resource found")