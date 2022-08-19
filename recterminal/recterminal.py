#!/usr/bin/env python3

import asciinema
from .asciicast2movie import asciicast2video
import argparse
import os
import sys

def main():
	# Parse args when command was run
	parser = argparse.ArgumentParser(prog="recterminal")
	parser.add_argument("-o", "--output", help="Output location for the file", type=str, default="output.mp4")
	parser.add_argument("--fps", help="Framerate for the output video", type=int, default=24)
	parser.add_argument("--cast", help="Chose if the .cast file should be kept", action="store_true")
	parser.add_argument("-f", "--force", help="Force overwrite an existing file", action="store_true")
	args = vars(parser.parse_args())

	# TODO potentially add a check on a valid output file

	# Checks if the output file is a .mp4
	if args['output'][-4:] != ".mp4":
		print("Invalid output file extension!")
		return

	# Create variables
	print(args)
	tmpfile = args['output'][:-3] + "cast"
	outputfile = args['output']
	fps = args['fps']
	keepCast = args['cast']

	# Check if the file already exists
	if args['force'] == False and os.path.isfile(outputfile) == True:
		print("File already exists, if you want to overwrite the file add the '-f' option when running the command again!")
		return

	# Record the terminal
	print("The terminal is reccording now, to stop recording, press CTRL+D or type 'exit' in the terminal")
	asciinema.record_asciicast(tmpfile)

	# Convert asciicast to mp4
	video = asciicast2video(tmpfile, blinkingCursor=0.5, renderOptions={'fontSize':12}, continueOnLowMem=None)
	video.write_videofile(outputfile, fps=fps)

	# Remove the cast file if --cast option was not added
	if keepCast == False:
		# Checks if the file exists
		if os.path.isfile(tmpfile):
			os.remove(tmpfile)


main()

sys.exit()