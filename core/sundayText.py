import sys
from azureTTS import *
from brain import *

cmds = [['hi','hello','hey'],['time'],['day','date','month','year'],['list','processes','process'],['bye','stop','exit'],['wiki', 'who', 'what'],['who', 'you'],['do', 'what', 'you']]

def think(text):
    processed = processText(text)        
    if any(i in cmds[0] for i in processed):
        return greetings()
    elif cmds[6] == processed:
        speak("Hello, I am Sunday your personal Assistant. I was created to help you in all your needs. To know more about what i can do ask \'what can you do\'")
    elif cmds[7] == processed:
        return helper()
    elif any(i in cmds[1] for i in processed):
        return showTime()
    elif any(i in cmds[2] for i in processed):
        return showDate()
    elif any(i in cmds[3] for i in processed):
        return listProcess()
    elif any(i in cmds[4] for i in processed):
        return farewell()
    elif any(i in cmds[5] for i in processed):
        return wiki(" ".join(processed[1:]))
    else:
        speak("Sorry I didn't quite catch that!")

think(sys.argv[1])