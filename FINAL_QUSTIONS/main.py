def askYesNoQuestion(question):
        YesNoAnswer = input(question).upper()
        if YesNoAnswer == "YES" or YesNoAnswer == "NO":
            return YesNoAnswer
        else:
            return askYesNoQuestion(question)

def askYesNoQuestion(question):
        YesNoAnswer = input(question).upper()
        if YesNoAnswer == "YES" or YesNoAnswer == "NO":
            return YesNoAnswer
        else:
            return askYesNoQuestion(question)