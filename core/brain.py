import wmi,random
from datetime import datetime
from azureTTS import *
from nltk import word_tokenize, pos_tag
import wikipedia

def processText(text):
    n,v,p,o = [],[],[],[]
    text = text.lower()
    a = pos_tag(text.split(" "))
    for i in a:
        if i[1] == "NN" or i[1]=="JJ" or i[1]=="NNS" or i[1] == "WP":
            n.append(i[0])
        elif i[1] == "VB" or i[1] == "VBD":
            v.append(i[0])
        elif i[1] == "PRP" or i[1] == "PRP$":
            p.append(i[0])
        else:
            o.append(i[0])
    return v + n + p
    
def listProcess():
    l = []
    defaultList= ['audiodg.exe','conhost.exe','csrss.exe','lsass.exe','lsm.exe','MSCamS64.exe','naPrdMgr.exe','OSPPSVC.EXE','PresentationFontCache.exe,SearchIndexer.exe','services.exe,smss.exe','spoolsv.exe','svchost.exe','svchost.exe','svchost.exe','Idle Process','UNS.exe','wininit.exe','WmiApSrv.exe','WmiPrvSE.exe','wmpnetwk.exe','WUDFHost.exe']
    for process in wmi.WMI().Win32_Process ():
        if process.name not in defaultList:
            l.append(process.Name)
    l = list( dict.fromkeys(l) )
    proc = ', '.join([str(elem) for elem in l[:7]])
    speak ("Top five processes include " + proc)

def showTime():
    speak ("It's " + datetime.now().strftime('%I hours %M %p'))

def showDate():
    speak (datetime.now().strftime('%d %h %Y'))

def greetings():
    greet=["Hi","Hello!","Hey There!","What's up?","Did you call me?"]
    speak(random.choice(greet))

def farewell():
    farewell=['I’m off','See you later', 'Talk to you Soon', 'Have a nice day', 'Bye.']
    speak(random.choice(farewell))

def wiki(topic):
    title = wikipedia.search(topic)
    content = wikipedia.summary(title[0], sentences=2)
    page = wikipedia.page(title[0])
    for i in page.images:
        if ".jpg" in i:
            pic = i
            break 
    print("<img class='wikipic' src='{}'></img>".format(pic))
    print(content.encode('utf-8'))
    speak(content)
def helper():
    speak("Well I'm happy that you asked. \n I can tell Time. Just ask 'What is the time right now?' \n If you want to know about any one, you can ask me 'Who is ', and persons name. \n I can also help you with launching applications. Say 'Launch and application name'.")
#print(processText("what can you do"))
#wiki("modi")