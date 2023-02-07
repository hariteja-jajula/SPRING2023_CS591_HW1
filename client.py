# Name : Hari Teja Jajula
# Section : CS-591
# SPRING 2023
# HOMEWORK - 1 



import socket, select, string, sys

#Helper function (formatting)
def display() :
        you="\33[33m\33[1m"+" You: "+"\33[0m"
        sys.stdout.write(you)
        sys.stdout.flush()

def main():

    if len(sys.argv)<2:
        host = input("Enter host ip address: ")
    else:
        host = sys.argv[1]

    port =int(input("Enter port number :  "))

    #asks for user name
    name=input("\33[34m\33[1m CREATING NEW ID:\n Enter username: \33[0m")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2)

    # connecting host
    try :
        s.connect((host, port))
    except :
        print ("\33[31m\33[1m Can't connect to the server \33[0m")
        sys.exit()

    #if connected
    s.send(name.encode())
    display()
    while 1:
        socket_list = [sys.stdin, s]

        # Get the list of sockets which are readable
        rList, wList, error_list = select.select(socket_list , [], [])

        for sock in rList:
            #incoming message from server
            if sock == s:
                data = sock.recv(4096)
                if not data :
                    print ('\33[31m\33[1m \rDISCONNECTED!!\n \33[0m')
                    sys.exit()
                else :
                    sys.stdout.write(data.decode())
                    display()

            #user entered a message
            else :
                msg=sys.stdin.readline()
                s.send(msg.encode())
                display()

if __name__ == "__main__":
    main()
                