from array import array
import time

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

def booleanQuestion(question: str) -> bool:
    while True:
        answer = input(question + " [y/n]:").lower()
        if answer in ["y", "yes"]:
            return True
        elif answer in ["n", "no"]:
            return False
        else:
            print("Invalid Answer, please try again!")

def integerQuestion(question: str) -> int:
    while True:
        try:
            answer = int(input(question))
            if answer > 0:
                return answer
            else:
                print("Number must be positive")
        except:
           print("Please input a not negative integer value!")

def multipleQuestion(question: str, answers: list[str]) -> list[str]:
    while True:
        try:
            print(question)
            [print(f"{a} [{i}]") for i, a in enumerate(answers)]
            answer = input("Type numbers comma-separated (e.g. 1,2,3) to select:").split(",")
            answer = [int(i) for i in answer]
            if len(list(filter((lambda a : (a < 0) or (a > (len(answers) - 1))), answer))) > 0:
                print("Not all inputs in correct range, please try again!")
                continue
            else:
                return [answers[i] for i in answer]
        except:
            print("Please only input integer values!")
            

questionOne = Question(AlwaysTrue)
questionTwo = Question(AlwaysFalse)

print(questionOne.run())
print(questionTwo.run())

print("ICS Security Suggestion System Version 0x1337")
print("Initializing Section 1: Access Control")
time.sleep(1)

external_systems = booleanQuestion("Are there any external systems or networks connected to your ICS (e.g remote access for maintenance and support, third-party vendors)?")
if external_systems:
    external_systems_firewall = booleanQuestion("Is there a firewall installed which limits the accessible ports?")
    external_systems_vpn = booleanQuestion("Is there a VPN used to access the system from outside?")
    print(external_systems)
    print(external_systems_firewall)
    print(external_systems_vpn)

protocols = ["HTTP", "MQTT", "TCP Modbus", "SSH"]
multiple_answer = multipleQuestion("Which protocols are used inside your ICS?", protocols)
print(multiple_answer)
