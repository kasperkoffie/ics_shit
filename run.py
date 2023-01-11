class Question:
    # Has the func param.
    # Func is the requirement logic
    # Func MUST return true or false
    def __init__(self, func):
        self.func = func
        self.args = {}

    # returns the boolean with the args
    def run(self):
        return self.func(self.args)
    
    # Sets one arg
    def setArg(self, argKey, argVal):
        self.args[argKey] = argVal
    
    def setArgs(self, args):
        self.args = args

def AlwaysTrue(args):
    return True

def AlwaysFalse(args):
    return False

class Interview:
    def __init__(self, questions):
        self.questions = questions

questionOne = Question(AlwaysTrue)
questionTwo = Question(AlwaysFalse)

print(questionOne.run())
print(questionTwo.run())