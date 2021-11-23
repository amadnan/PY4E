import pyttsx3
import PyPDF2

book = open('Jana-thesis.pdf','rb')
pdfreader = PyPDF2.PdfFileReader(book)
pages = pdfreader.numPages
print(pages)

x = pyttsx3.init()

voices = x.getProperty('voices')
x.setProperty('voice', voices[1].id)

rate = x.getProperty('rate')   
print (rate)                        
x.setProperty('rate', 175)

y = pdfreader.getPage(18)
t = y.extractText()
x.say(t)
x.runAndWait()