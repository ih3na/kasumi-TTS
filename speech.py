# imports
import os
import gtts
import PyPDF2
from playsound import  playsound
import argparse

# arguments
parse = argparse.ArgumentParser()
parse.add_argument("-f")
parse.add_argument("-p")
args = parse.parse_args()

# print arguments
print('file: ',args.f)

filename=args.f

txt=".txt"
pdf=".pdf"

if txt in filename :
	# text
	file=open(args.f, 'r')
	text=file.read()


elif pdf in filename:
	# pdf
	pdf=open(args.f, 'rb')
	pgnum= int(args.p)
	reader=PyPDF2.PdfReader(pdf)
	page=reader.pages[pgnum]
	text=page.extract_text()
	print(text)
else:
	print("Invalid filetype")




# tts
tts=gtts.gTTS(text, lang="en")
tts.save("out.mp3")
playsound("out.mp3")
