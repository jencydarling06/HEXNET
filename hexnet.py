#!/usr/bin/env python3

# Copyright (C) 2012, 2013, 2014
# Minzsec
# www.facebook.com/rootnameshadow
#
# PenTBox (Penetration Testing Box)
#
# This file is part of PenTBox.
#
# PenTBox is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# PenTBox is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with PenTBox.  If not, see <http://www.gnu.org/licenses/>.

import os
import signal
import random
import time
import sys
import re

# Email validation function
def is_valid_email(email):
    # Simple regex for email validation
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

# Get user's email ID with validation
def get_user_email():
    while True:
        email = input("Share Your Email Address Here—Let’s Stay Connected!:").strip()
        print(" ")
        if is_valid_email(email):
            return email
        else:
            print("Oops! That email doesn’t seem right. Give it another go!")
            print(" ")

# Store user's email in environment variable or configuration
user_email = get_user_email()
os.environ['USER_EMAIL'] = user_email  # or use a configuration file

rampart_directory = r'/home/kali/Int/rampart.py'
sys.path.append(rampart_directory)

from rampart import ramconfig, main as rampart_main

###########################
##  BASIC CONFIGURATION  ##
###########################

pb_log_enabled = False
pb_log_file = os.path.join(os.path.dirname(__file__), "other/log/pentbox_log_" + os.getenv('USER', 'default') + ".log")

protected_mode = True
text_color = True

###########################

def pb_write_log(message, module):
    if pb_log_enabled:
        with open(pb_log_file, 'a') as log_file:
            log_file.write(f"[{time.strftime('%Y-%m-%d %H:%M:%S')} - {module} - {os.getenv('USER', 'default')}] {message}\n")

def title(text):
    if text_color:
        print(f"\033[1;34m{text}\033[0m")
    else:
        print(text)

def has_permission():
    return os.geteuid() == 0

def get_input(prompt):
    return input(prompt)

def main():
    version = "1.8"

    def signal_handler(sig, frame):
        print("")
        print("[*] Signing Off—Catch You on the Flip Side..")
        print("")
        pb_write_log("exiting", "Core")
        exit(0)

    signal.signal(signal.SIGINT, signal_handler)

    pb_write_log("HEXNET loaded", "Core")

    random.seed(time.time())
    banner = random.randint(0, 2)

    print("")
    title(f" HeXNeT {version} ")

    if banner == 0:
        print("                                         ")
        print("                                         ")
        print("                  ▓▓▒▓▓                  ")
        print("                ▓       ▓                ")
        print("              ▓▓         ▓▓              ")
        print("             ▓    𝐇𝐄𝐗𝐍𝐄𝐓   ▓             ")
        print("             ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓            ")
        print("            ▓▓▓▓▓▒▒▓▓▓▓▒▓▓▓▓▓            ")
        print("            ▓▓             ▓▓            ")
        print("             ▓▓           ▓▓             ")
        print("          ▓▓   ▓ ▓▓▓▓▓▓▓ ▓   ▓▓          ")
        print("         ▓                     ▓         ")
        print("        ▓                       ▓        ")
        print("        ▓  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓  ▓        ")
        print("       ▓   ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓   ▓       ")
        print("       ▓   ▓▓▓▓▓▓▓▓▒▒▓▓▓▓▓▓▓▓▓   ▓       ")
        print("       ▓   ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓   ▓       ")
        print("       ▓▓  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓  ▓▓       ")
        print("         ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓         ")
        print("            ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓            ")
        print("                                         ")

    elif banner == 1:
        print("                               ")
        print("                               ")
        print("             ░░▒▒▓▓▓▓▓▒▒░░     ")               
        print("        ▒██▓░░$$$$$$$$░░░░▒██▒ ")           
        print("         ▓▒$$$$$$$$$$$$$$$$$▒▓  ")          
        print("         ▓▒$$$$$$$$$$$$$$$$$▒▓  ")          
        print("         ▓▒$$$$$$$$$$$$$$$$$▒▓  ")          
        print("         ▓▒$$$$ ℝ𝔸𝕄ℙ𝔸ℝ𝕋 $$$$▒▓  ")          
        print("         ▒▓$$$$$$$$$$$$$$$$░▓▒ ")           
        print("         ░▓░$$$$$$$$$$$$$$░░▓░  ")          
        print("          ▒▓░$$$$$$$$$$$$$░▓▒░  ")          
        print("          ░▒█░░$$$$$$$$$░░█▒░   ")          
        print("            ░▓▓░░$$$$$░░▓▓░    ")           
        print("              ░▒█▓░$░▒█▒░░    ")            
        print("                 ░░▒▒░      ")
    elif banner == 2:
        print("    _   _   _____  __  __  _   _   _____   _____   ")
        print("   | | | | | ____| \ \/ / | \ | | | ____| |_   _|   ")
        print("   | |_| | |  _|    \  /  |  \| | |  _|     | |       ")
        print("   |  _  | | |___   /  \  | |\  | | |___    | |       ")
        print("   |_| |_| |_____| /_/\_\ |_| \_| |_____|   |_|        ")

    time.sleep(0.25)
    option1 = ""

    while option1 != "8":
        module_exec = True
        print("")
        print("====================================================")
        print("")
        
        print("Network Powerhouse Tool—Unleash Its Potential (y/n)")
        print("")
        print("")
        option1 = get_input("   -> ")
        print("")

        if option1 == "y":
            print("")
            print("Get ready to fortify your defenses with Rampart!(y/n)")
            print("")
            print("")
            option2 = get_input("   -> ")
            if option2 == "n":
                module_exec = False
            elif option2 == "y":
                print(" ")
                print("Rampart Setup—Get Ready to Customize Your Defense!")
                print("")
                print("####################")
                print(" ")
                rampart_main()
                # Implement Honeypot
                pass
            else:
                module_exec = False
                print("")
                print("Oops! That’s an Invalid Option—Try Again!")
                print("")
        elif option1 == "n":
            module_exec = False
            os.kill(os.getpid(), signal.SIGINT)

        if module_exec:
            print("")
            print("[*] Module Execution Wrapped Up—All Set and Done!")
            print("")

if __name__ == "__main__":
    main()
