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

# Checking for network redundancy
# If the number of routers is smaller than 2, that means you have either a single point of failure or no routers whatsoever. Having at least two or more guarantees redundancy
number_of_routers = integerQuestion("How many routers is your system protected by?")

# Checking for backup recovery functionality
# If there is no backup recovery in place, or the back-up is either unscheduled or missing something, give advice to add RAID / regular
# If not tested, give advice to test
# If not in an offsite location, store it in an offsite location
backup_recovery = booleanQuestion("Are there backup and disaster recovery measures in place for your ICS and IT environment?")
if backup_recovery:
    backup_recovery_how = multipleQuestion("What measures are in place?", ["Regular unscheduled back-up (manual)", "Regular scheduled back-up", "RAID integration"])
    backup_recovery_tested = booleanQuestion("Have these back-up systems been proven to work in realistic test scenarios?")
    backup_location_offsite = booleanQuestion("Are back-ups made stored in an off-site location inaccessible through the host network?")

# Checks if external services are used. If they're used, check if they're highly available & relatively safe.
# If either of those are not, recommend to use different services.
external_apis_used = booleanQuestion("Are any external services (such as API's) used?")
if external_apis_used:
    external_apis_available = booleanQuestion("Are these external services often available?")
    external_apis_safe = booleanQuestion("Are these external API's cyber-secure to a reasonable level?")

# If not, suggest redundancy
critical_hardware_redudancy = booleanQuestion("Is critical hardware structured redundandly? (i.e. critical database mirrored in two or more instances)")

# If shared networks, recommend to either segment it properly or to use secure cloud providers
how_connected = multipleQuestion("How are your ICS and IT systems connected?", ["Dedicated segmented networks", "Shared networks", "Cloud-based systems from secure providers"])

