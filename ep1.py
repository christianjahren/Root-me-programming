import time
import socket
import math

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
    irc.send(b"PRIVMSG Candy :!ep1 "b"\r\n")
    time.sleep(0.5)
    while 1:
        text = irc.recv(70000)
        time.sleep(0.5)
        print(text)
        time.sleep(0.5)
        if text.find(b"/") > -1:  # to make sure we recieve the correct answer
            try:
                text = text[(text[1:].find(b":")) + 2:]  # strip the message to look
                text = text[:text.find(b".")]            # like number1/number2
                print(text)
                nb1 = int(text[:text.find(b"/")])  # get number1
                print(nb1)
                nb2 = int(text[(text.find(b"/")) + 1:])  # get number2
                print(nb2)
                answer = round(math.sqrt(nb1)*nb2,2)
                answer = bytes(str(answer).encode("ASCII"))
                print(nb1,"*",0.5,"*",nb2,"=",answer) #calculate
                irc.send(b"PRIVMSG "+enemy+b" :!ep1 -rep "+answer+b"\r\n")  # send answer
                print("GIVE ME A PASSWORD!!")
                time.sleep(0.5)
                print(irc.recv(70000))  # Get validation password
                irc.send(b"QUIT :bye..!")  # End up client session
                break
            except:
                print("hmmmm... something is wrong")

server = "irc.root-me.org"
botnick = "CboiBOT"
channel = "#root-me_challenge"
enemy = b"Candy"

# CREATE SOCKET
try:
    print("Creating socket..")
    irc = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    irc.connect((server,6667))
    irc.setblocking(False)
    time.sleep(1)
except:
    print("Cannot connect..")

# CONNECT AND RUN
else:
    print("Sending username and nick..")
    irc.send(bytes("USER " +botnick+" "+botnick+" "+botnick+" :botbot \r\n","UTF-8"))
    time.sleep(1)
    irc.send(bytes("NICK "+botnick+"\n","UTF-8"))
    time.sleep(1)
    print("Joining the channel..")
    irc.send(bytes("JOIN "+channel+"\n","UTF-8"))
    print("Playing ping-pong..")
    connection()
    print("Connection established, doing the challenge:")
    play()

    print("DONE..")
    irc.close()






