from cncClass import server_connection
from handler import handler

if __name__=="__main__":
    s=server_connection()
    s.create_connection(ip="",port=7777)
    print("[+] Listening for connections")
    conn_sock, conn_address=s.accept_connection()
    # s.send_data("never gonna give you up never gonna let you down never gonna run around and desert you")
    # print(s.recieve_data())
    handler(s)
    
    s.sock.close()
    conn_sock.close()