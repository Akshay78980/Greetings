from greets import greetings
from translate import Translator

mytranslator = Translator(to_lang='pt')

for i in greetings:
    i = mytranslator.translate(i)
    print(i.title() + "!" + "....blaaaaaah")