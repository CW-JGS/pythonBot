import pyautogui, time, json 

configJson = open("config.json")
config = json.load(configJson)
wordListJSON = open("wordlist.json")
wordlist = json.load(wordListJSON)
repetitions = config["repetitions"]
def printWordsFromWordlist():
    for i in wordlist:
        pyautogui.typewrite(i)
        time.sleep(0.25)
        pyautogui.press("enter")
        time.sleep(0.25)

def main():
    if(repetitions == "0" ):
        while true:
            printWordsFromWordlist()
    else:
        for i in range(repetitions):
            printWordsFromWordlist()

if(__name__) == "__main__":
    main()
