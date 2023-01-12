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
            
print("ICS Security Suggestion System Version 0x1337")
print("Initializing Section 1: Access Control")
time.sleep(1)

# We specify our questions and immediatily get the answer
# with question_answer = boolean/integer/multipleQuestion(question here)

# Acess Control Section
external_systems = booleanQuestion("Are there any external systems or networks connected to your ICS (e.g. remote access for maintenance and support, third-party vendors)?")

dmz_protection = booleanQuestion("Are the important resources protected by a DMZ?")

wireless = booleanQuestion("Are there any wireless networks in use in your factory?")

if wireless:
    wireless_types = multipleQuestion("What type of wireless technology is used?", ["WiFi", "Zigbee", "LoRa", "NB-IoT", "LTE"])
    if "WiFi" in wireless_types:
        wifi_necessary = booleanQuestion("Is the WiFi network neccessary for operations?")
        wifi_security = booleanQuestion("Is the WiFi network properly secured with WPA2 or WPA3 and optionally WPA enterprise?")
        wifi_isolation = booleanQuestion("Is the WiFi network isolated from critical infrastructure?")

password_bruteforce = booleanQuestion("Are there any measures in place to protect against brute force password attacks?")
password_2fa = booleanQuestion("Is two-factor-authentication used for all possible user accounts and devices?")

remote_access = booleanQuestion("Are there remote access requirements?")
if remote_access:
    remote_access_how = multipleQuestion("How is the remote access established?", ["Internet", "Dial-Up", "Site LAN"])
    remote_access_firewall = booleanQuestion("Is there firewall protection for remote access?")
    remote_access_authentication = booleanQuestion("Is there sufficient authentication for remote access?")

