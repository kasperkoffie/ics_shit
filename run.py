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
access_control_suggestions = []

external_systems = booleanQuestion("Are there any external systems or networks connected to your ICS (e.g. remote access for maintenance and support, third-party vendors)?")

dmz_protection = booleanQuestion("Are the important resources protected by a DMZ?")
if not dmz_protection:
    access_control_suggestions.append("It is imporant to isolate critical resoures by a DMZ. Think about which resources are critical for operation (e.g. a Database) and encapsulate them in a DMZ.")

wireless = booleanQuestion("Are there any wireless networks in use in your factory?")

if wireless:
    wireless_types = multipleQuestion("What type of wireless technology is used?", ["WiFi", "Zigbee", "LoRa", "NB-IoT", "LTE"])
    if "WiFi" in wireless_types:
        wifi_necessary = booleanQuestion("Is the WiFi network neccessary for operations?")
        if not wifi_necessary:
            access_control_suggestions.append("Consider disabling the wireless access functionality if it is not neccessary for operations. You could also only enable the wireless network when neccessary and disable it by default.")
        wifi_secure = booleanQuestion("Is the WiFi network properly secured with WPA2 or WPA3 and optionally WPA enterprise?")
        if not wifi_secure:
            access_control_suggestions.append("It is very critical to have good wireless encryption. If devices do not support a secure wireless protection standard, disable their wireless functionality and/or replace them.")
        wifi_isolation = booleanQuestion("Is the WiFi network isolated from critical infrastructure?")
        if not wifi_isolation:
            access_control_suggestions.append("The wireless network is a common attack vector and routers often have security vulnerabilities. To limit the impact from a compromised WiFi, separate it from other devices on a network level. If possible for operations, also enable client isolation.")

password_bruteforce = booleanQuestion("Are there any measures in place to protect against brute force password attacks?")
if not password_bruteforce:
    access_control_suggestions.append("Install protection measures against bruteforce attacks, such as fail2ban on SSH servers. This applies to internal as well as outwards-facing devices.")
password_2fa = booleanQuestion("Is two-factor-authentication used for all possible user accounts and devices?")
if not password_2fa:
    access_control_suggestions.append("Enable two-factor-authentication with a smart card, security token or other means for user account login. Where this is not possible, make sure that strong passwords are used.")

remote_access = booleanQuestion("Are there remote access requirements?")
if remote_access:
    remote_access_how = multipleQuestion("How is the remote access established?", ["Internet", "Dial-Up", "Site LAN"])
    if "Internet" in remote_access_how:
        vpn = booleanQuestion("Is the access from the internet limited to VPN access (or similar services)?")
        if not vpn:
            access_control_suggestions.append("Consider using a secure VPN standard to access your infrastructure from outside. This protects against insecure protocols possibly used by servers and avoids exposing application vulnerabilites to outside attackers.")
    remote_access_firewall = booleanQuestion("Is there firewall protection for remote access/outwards facing servers?")
    if not remote_access_firewall:
        access_control_suggestions.append("Install a firewall between internet facing servers and the internet. Configure the firewall to only allow neccessary connections, e.g. only VPN. This limits the attack surface if the server is improperly configured or has unknown vulnerabililites.")
    
user_available = booleanQuestion("Are separate user accounts used for each employee and access to devices?")
user_passwords = booleanQuestion("Is there a password policy in place to ensure secure user passwords?")
if user_available:
    user_roles = booleanQuestion("Is there role-based access control for the usrers?")
    if user_roles:
        user_least_privilege = booleanQuestion("Is the least-privilege principle enforced for those roles and user accounts?")

security_technology = multipleQuestion("What types of security devices and technologies are used in you factory?", ["Firewalls", "Intrusion Detection Systems", "SIEM Systems"])

print("Initializing Section 2: System Integrity")
time.sleep(1)
# System Integrity Section
system_integrity_suggestions = []

protocols = multipleQuestion("What are the main communication protocols used in your factory?", ["Ethernet/IP", "Modbus", "OPC UA", "MQTT"])
incident_response = booleanQuestion("Are there any incident response plans and procedures in place in case of security incidents or breaches?")
monitoring_systems = booleanQuestion("Are there any monitoring systems in place to track and detect security incidents?")
connections = multipleQuestion("How are your ICS and IT systems connected?", ["dedicated networks", "shared networks", "cloud-systems"])
pentesting = booleanQuestion("Are regular security assessments and penetration tests done?")
process_monitoring = multipleQuestion("What types of software are used to control and monitor your industrial processes?", ["custom software", "commercial off-the-shelf software"])


