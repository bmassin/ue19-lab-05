import requests
import re

r = requests.get("https://official-joke-api.appspot.com/random_joke", auth=('user', 'pass'))
texte = r.text
regex = rf'.*"setup":"(.*)","punchline":"(.*)",.*'
match = re.search(regex, texte)
if match:
    question = match.group(1)
    rep = match.group(2)
    print(question)
    #answer = input("Answer ? ")
    #if rep == answer:
        #print("Exactly !")
    #else:
        #print("No ! The answer is :")
    print(rep)
