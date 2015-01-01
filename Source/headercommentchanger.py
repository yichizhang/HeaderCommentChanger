'''
 Copyright (c) 2015 Yichi Zhang
 https://github.com/yichizhang
 zhang-yi-chi@hotmail.com
 
 Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
 
 The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
 
 THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
'''

import os
import sys
import argparse

C_SINGLE_LINE_COMMENT = "//"
C_MULTI_LINE_COMMENT_BEGIN = "/*"
C_MULTI_LINE_COMMENT_END = "*/"

def newstringbychangingheader (originalstring, newheader):
	newstring = ""
	
	loc1 = originalstring.find(C_SINGLE_LINE_COMMENT)
	loc2 = originalstring.find(C_MULTI_LINE_COMMENT_BEGIN)
	
	if (loc1 == 0):
		words = originalstring.split('\n')

		newstring = newheader
		firstblockofcomments = True

		for word in words:
			if (word.startswith(C_SINGLE_LINE_COMMENT) == True and (firstblockofcomments == True)):
				# First few lines of single line comments;
				# Original comments; no need to copy.
				# Therefore, pass;
				pass
			else: 
				# Copy all the rest of lines;
				firstblockofcomments = False
				newstring = newstring + word + "\n" 

			# First line that do not start with //
			if (word.startswith(C_SINGLE_LINE_COMMENT) == False):
				firstblockofcomments = False
				
	elif (loc2 == 0):
		endlocation = originalstring.find(C_MULTI_LINE_COMMENT_END)
		trimlocation = endlocation + len(C_MULTI_LINE_COMMENT_END)
		newstring = newheader + originalstring[trimlocation:]
	else:
		newstring = newheader + originalstring
		
	return newstring

def processfile (filepath, newheader):
	outputpath = filepath
	newstring = ""
	
	fin = open(filepath, 'r')
	originalstring = fin.read()
	fin.close()
	
	newstring = newstringbychangingheader(originalstring, newheader)
	
	fout = open(outputpath, 'w')
	fout.write(newstring)
	fout.close()		

	return	
		
def shouldprocessfile (filename):
	flag = False
	if filename.startswith('._'):
		flag = False
	else:
		if (filename.endswith('.swift') or filename.endswith('.h') or filename.endswith('.m')):
			flag = True
	
	return flag

# Main program

def main (rootdir, newheaderpath):

	k = raw_input("\n--------------------------------------------\n                  WARNING\n--------------------------------------------\nYour files will be modified; YOU MIGHT LOSE IMPORTANT INFORMATION.\nYou should backup or commit your files before continuing.\n\nPress ENTER to continue\nIf you wish to abort, press Control + C")

	f = open(newheaderpath, 'r')
	newheader = f.read()
	f.close()

	for subdir, dirs, files in os.walk(rootdir):
		for file in files:
			if shouldprocessfile (file):
				filepath = os.path.join(subdir, file)
				processfile(filepath, newheader)
	return

if __name__ == "__main__":
	parser = argparse.ArgumentParser()

	#parser.add_argument('dir', help="directory of the files to be changed")
	#parser.add_argument('newheaderfile', help="path of the new header file to be added to the files in the directory")
	parser.add_argument('-d', '--dir', help="directory of the files to be changed")
	parser.add_argument('-f', '--newheaderfile', help="path of the new header file to be added to the files in the directory")

	args = parser.parse_args()

	if args.dir is None:
		rootdir = os.path.dirname(os.path.realpath(__file__))
		print "No directory specified; using: " + rootdir
	else:
		rootdir = args.dir

	if args.newheaderfile is None:
		newheaderpath = "newheader.txt"
		print "No new header file specified; looking for: " + newheaderpath
	else:
		newheaderpath = args.newheaderfile

	main(rootdir, newheaderpath)