# TEXT TO SPEECH PROGRAM

from gtts import gTTS
import os

# text = "Hello World! My name is Suveshan Moodley. Nice to meet you!"

fh = open("test.txt", "r")
text = fh.read().replace("\n", " ")

language = "en"
output = gTTS(text=text, lang=language, slow=False)

output.save("output.mp3")
fh.close()
os.system("start output.mp3")
