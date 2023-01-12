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


print("Initializing Section 3: Confidentiality")
time.sleep(1)

confidentiality_suggestions = []

# Checks if encryption is  used
# If encryption is not used, or 'other' is selected, recommend AES / RSA encryption
encryption_used = booleanQuestion("Are any modern encryption methods used?")
if encryption_used:
    encryption_type = multipleQuestion("What types of encryption are used?" ["AES", "RSA", "Other"])
    if encryption_type == "Other":
        confidentiality_suggestions.append("You should integrate AES or RSA")
else:
    confidentiality_suggestions.append("You should integrate AES or RSA")

# If no, recommend measures.
portable_security = booleanQuestion("Are there measures in place to protect against portable device security?")
if not portable_security:
    confidentiality_suggestions.append("You should put measures in place to protect portable devices")

# Checks if security patches are regularly installed. If not, recommend to do so.
is_the_system_patched = booleanQuestion("Are software updates and patches installed regularly for your ICS and IT systems?")
if not is_the_system_patched:
    confidentiality_suggestions.append("You should implement a regular patching cycle")

# If not, recommend to do so
firewalls_or_dmzs = booleanQuestion("Are the different layers of the network separated firewalls or DMZs?")
if not firewalls_or_dmzs:
    confidentiality_suggestions.append("You should separate the different layers of networks with firewalls and/or DMZs")

print("Initializing Section 4: Availability")
time.sleep(1)

availability_suggestions = []

# Checking for network redundancy
# If the number of routers is smaller than 2, that means you have either a single point of failure or no routers whatsoever. Having at least two or more guarantees redundancy
number_of_routers = integerQuestion("How many routers is your system protected by?")
if number_of_routers < 2:
    availability_suggestions.append("You should have at least 2 or more routers in your network in order to guarantee network redundancy.")


# Checking for backup recovery functionality
# If there is no backup recovery in place, or the back-up is either unscheduled or missing something, give advice to add RAID / regular
# If not tested, give advice to test
# If not in an offsite location, store it in an offsite location
backup_recovery = booleanQuestion("Are there backup and disaster recovery measures in place for your ICS and IT environment?")
if backup_recovery:
    backup_recovery_how = multipleQuestion("What measures are in place?", ["Regular unscheduled back-up (manual)", "Regular scheduled back-up", "RAID integration"])
    if backup_recovery_how == "Regular unscheduled back-up (manual)":
        availability_suggestions.append("Please implement either a regularly scheduled back-up, RAID integration, or both!")
    backup_location_offsite = booleanQuestion("Are back-ups made stored in an off-site location inaccessible through the host network?")
    if not backup_location_offsite:
        availability_suggestions.append("Please locate the back-ups off-site inaccessible through the host-network!")
else:
    availability_suggestions.append("You should have a regularly scheduled back-up cycle and/or RAID integration in your system!")


# Checks if external services are used. If they're used, check if they're highly available & relatively safe.
# If either of those are not, recommend to use different services.
external_apis_used = booleanQuestion("Are any external services (such as API's) used?")
if external_apis_used:
    external_apis_available = booleanQuestion("Are these external services often available?")
    if not external_apis_available:
        availability_suggestions.append("Please pick other services / API's with a reasonable uptime!")
    external_apis_safe = booleanQuestion("Are these external API's cyber-secure to a reasonable level?")
    if not external_apis_available:
        availability_suggestions.append("Please pick different services that are reasonably cyber-secure!")

# If not, suggest redundancy
critical_hardware_redudancy = booleanQuestion("Is critical hardware structured redundandly? (i.e. critical database mirrored in two or more instances)")
if not critical_hardware_redudancy:
    availability_suggestions.append("Please implement critical hardware reduncancy through hardware mirroring!")

# If shared networks, recommend to either segment it properly or to use secure cloud providers
how_connected = multipleQuestion("How are your ICS and IT systems connected?", ["Dedicated segmented networks", "Shared networks", "Cloud-based systems from secure providers"])
if how_connected == "Shared networks":
    availability_suggestions.append("Please implement either network segmentation or cloud architecture!")