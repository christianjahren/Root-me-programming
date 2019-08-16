import time
import socket
import base64


def connection():
    while 1:
        try:
            time.sleep(0.5)
            text = irc.recv(20400)
            print(text)

            if text.find(b"PING") != -1:
                irc.send(b"PONG " + text.split()[1] + b"\r\n")
        except:
            print("waiting..")
            break

def play():
    irc.send(b"PRIVMSG Candy :!ep2 "b"\r\n")
    time.sleep(0.5)
    while 1:
        text = irc.recv(70000)
        time.sleep(0.5)
        print(text)
        time.sleep(0.5)
        try:
            text = text[(text[1:].find(b":")) + 2:]  # slice to only get the message
            # text = text[:-2]  # if i want to stip the last characters
            print(text)
            answer = base64.b64decode(text)
            irc.send(b"PRIVMSG " + enemy + b" :!ep2 -rep " + answer + b"\r\n")  # send answer
            print("GIVE ME A PASSWORD!!")
            time.sleep(0.5)
            print(irc.recv(70000))  # Get validation password
            irc.send(b"QUIT")  # End client session
            break
        except:
            print("hmmmm... something is wrong")
            irc.send(b"QUIT")
            break


server = "irc.root-me.org"
botnick = "CboiBOT"
channel = "#root-me_challenge"
enemy = b"Candy"

# CREATE SOCKET
try:
    print("Creating socket..")
    irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    irc.connect((server, 6667))
    irc.setblocking(False)
    time.sleep(1)
except:
    print("Cannot connect..")

# CONNECT AND RUN
else:
    print("Sending username and nick..")
    irc.send(bytes("USER " + botnick + " " + botnick + " " + botnick + " :botbot \r\n", "UTF-8"))
    time.sleep(1)
    irc.send(bytes("NICK " + botnick + "\n", "UTF-8"))
    time.sleep(1)
    print("Joining the channel..")
    irc.send(bytes("JOIN " + channel + "\n", "UTF-8"))
    print("Playing ping-pong..")
    connection()
    print("Connection established, doing the challenge:")
    play()

    print("DONE..")
    irc.send(b"QUIT")
    irc.close()





