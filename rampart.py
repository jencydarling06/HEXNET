import socket
import threading
import time
import os
import numpy as np
import pygame
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Configuration for the beep sound
FREQUENCY = 4000  # Increased frequency
DURATION = 1000   # Duration in milliseconds
VOLUME = 1.0      # Volume level (1.0 is max)

def title(message):
    print(message)

def warning(message):
    print(f"Stay sharp—this is your warning to take action now!: {message}")

def play_beep():
    try:
        pygame.mixer.init(frequency=44100, size=-16, channels=2)  # Initialize pygame mixer with stereo sound
        sample_rate = 44100
        t = np.linspace(0, DURATION / 1000, int(sample_rate * DURATION / 1000), endpoint=False)
        
        # Generate stereo beep sound (left and right channels)
        left_channel = (VOLUME * np.sin(2 * np.pi * FREQUENCY * t) * 32767).astype(np.int16)
        right_channel = left_channel
        stereo_samples = np.stack([left_channel, right_channel], axis=1)
        
        sound = pygame.sndarray.make_sound(stereo_samples)
        sound.play()
        pygame.time.wait(DURATION)  # Wait for the sound to finish
    except Exception as e:
        print(f"Oops! Sound Playback Hit a Snag—Let's Get It Going!: {e}")

def send_email_report(report_file, recipient_email):
    try:
        sender_email = "rampartinhexnet@gmail.com"
        password = "nvaucsqyszudovsl"  # Replace with the actual password

        # Create the email
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = "Intruder Spotted! HeXNet Rampart Sounds the Alarm!"

        with open(report_file, "r") as file:
            report_content = file.read()

        msg.attach(MIMEText(report_content, 'plain'))

        # Send the email
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, password)
        text = msg.as_string()
        server.sendmail(sender_email, recipient_email, text)
        server.quit()

        print(f"\nSuccess! Report Delivered to{recipient_email}.\n")
    except Exception as e:
        print(f"\n Uh-oh! Report Email Delivery Unsuccessful!: {e}\n")

def ramconfig(port, message, sound, log, logname):
    try:
        # Create a TCP server
        tcpserver = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tcpserver.bind(("0.0.0.0", port))
        tcpserver.listen(5)

        print(f"\n  RAMPART ENGAGED ON PORT—Shielding in Full Force!{port} ({time.strftime('%Y-%m-%d %H:%M:%S')})\n")

        if log.lower() == "y":
            try:
                with open(logname, "a") as logf:
                    logf.write(f"#################### HeXNet RamPart log\n")
                    logf.write(f"\n  RAMPART ACTIVATED ON PORT {port} ({time.strftime('%Y-%m-%d %H:%M:%S')})\n")
            except FileNotFoundError:
                print("\n Saving log error: No such file or directory.\n")

        while True:
            # Accept incoming connections
            socket_client, addr = tcpserver.accept()
            time.sleep(1)  # To mitigate possible DoS attacks

            def handle_client(sock):
                remote_ip, remote_port = addr
                print(f"\n  ALERT! INTRUSION ATTEMPT SPOTTED--ACTION REQUIRED! from {remote_ip}:{remote_port} ({time.strftime('%Y-%m-%d %H:%M:%S')})")
                print(" -----------------------------")
                reciv = sock.recv(1000).decode()
                print(reciv)
                if sound.lower() == "y":
                    play_beep()  # Play beep sound

                # Generate the report
                report_filename = f"rampart_report_{time.strftime('%Y%m%d_%H%M%S')}.txt"
                with open(report_filename, "w") as report_file:
                    report_file.write(f"Alert! Intrusion Attempt Spotted—Action Required:\n")
                    report_file.write(f"Remote IP: {remote_ip}\n")
                    report_file.write(f"Remote Port: {remote_port}\n")
                    report_file.write(f"Date: {time.strftime('%Y-%m-%d')}\n")
                    report_file.write(f"Time: {time.strftime('%H:%M:%S')}\n")
                    report_file.write(f"Details:\n{reciv}\n")
                    print(f"\nBoom! Your report is hot off the press and ready for you!: {report_filename}\n")

                # Log the intrusion details
                if log.lower() == "y":
                    try:
                        with open(logname, "a") as logf:
                            logf.write(f"\n ALERT! INTRUSION ATTEMPT SPOTTED--ACTION REQUIRED! from {remote_ip}:{remote_port} ({time.strftime('%Y-%m-%d %H:%M:%S')})\n")
                            logf.write("########################\n")
                            logf.write(reciv)
                    except FileNotFoundError:
                        print("\n Saving log error: No such file or directory.\n")

                # Send the report via email
                user_email = os.getenv('USER_EMAIL', 'default@example.com')
                send_email_report(report_filename, user_email)

                time.sleep(2)  # Sticky honeypot
                sock.sendall(message.encode())
                sock.close()

            threading.Thread(target=handle_client, args=(socket_client,)).start()

    except PermissionError:
        print("\n Error: Oops! Rampart Needs Root Privileges to Proceed!\n")
    except OSError as e:
        if e.errno == 98:  # Address already in use
            print("\n Error:Hold Up! This Port’s Already in Action!\n")
        else:
            print(f"\n Unknown error: {e}\n")

def main():
    print("\nGet ready to fortify your defenses with Rampart!\n")
    print(" ")
    print(" _____________________  _________________________________ ")
    print(" ___  __ \__    |__   |/  /__  __ \__    |__  __ \__  __/ ")
    print(" __  /_/ /_  /| |_  /|_/ /__  /_/ /_  /| |_  /_/ /_  /    ")
    print(" _  _, _/_  ___ |  /  / / _  ____/_  ___ |  _, _/_  /     ")
    print(" /_/ |_| /_/  |_/_/  /_/  /_/     /_/  |_/_/ |_| /_/      ")
    print("                                                          ")

    warning("Heads Up! HexNet Needs Root Privileges to Launch!..\n")
    print(" Choose Your Option and Let’s Dive In!\n")

    print("Take Control with Manual Configuration—(y/n) \n")
    print("")
    configuration = input("   -> ").strip()

    if configuration == "y":
        port = input("\nEnter the Port to Unlock and Get Started! \n\n   -> ").strip()
        message = input("\n Enter a Custom Message to Display—Get Creative!\n\n   -> ").strip()
        log = input("\n Keep a log of detected intrusions?\n\n (y/n)   -> ").strip()
        logname = ""
        if log.lower() == "y":
            logname = input("\n What's the Name for Your Log File? Let’s Make It Count! (incremental)\n\nDefault: */hexnet/tools/network/log.txt \n\n   -> ").strip()
            if not logname:
                logname = os.path.join(os.path.dirname(__file__), "../../other/log_honeypot.txt")
        sound = input("\n  Set Off the Beep() Alert for Intrusions—Get Notified in Style!?\n\n (y/n)   -> ").strip()
        
        ramconfig(int(port), message, sound, log, logname)
    else:
        print("\n Oops! That’s an Invalid Option—Try Again!\n")
        print("")

if __name__ == "__main__":
    main()
