import pyttsx3
engine = pyttsx3.init()
listed = {
    "what is your name": "My name is King Jebidiah the |||, I am an adaptive AI to talk with"
}
def ask():
    que = input("What would you like to know: ")
    with open(start, "r") as file:
        newt = []
        for i in file.readlines():
            if que in i:
                engine.say(newt[-1])
                engine.runAndWait()
                break
            else:
                newt.append(i)
    choice()
def choice():
    engine.say("What would you like to do")
    engine.runAndWait()
    do = input("Enter here: ")
    if do == "teach":
        teach()
    elif do == "ask":
        ask()
    elif do == "save":
        save()

def save():
    with open(start, "a") as file:
        for i, p in listed.items():
            file.write(f"{p}\n")
            file.write(f"{i}\n")
        listed.clear()
        #engine.say(f"Listed is now {listed}")
        #engine.runAndWait()
    choice()


def teach():
    engine.say("What would be the question")
    engine.runAndWait()
    q = input("Enter question here: ")
    while q !="":
        engine.say("And the answer would be")
        engine.runAndWait()
        a = input("Enter answer here: ")
        listed[q] = a
        engine.say("What would be the question")
        engine.runAndWait()
        q = input("Enter question here: ")
    choice()

engine.say("What information file do you want to use")
engine.runAndWait()
start = input("Enter here: ")
choice()