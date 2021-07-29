import socket
import threading
import datetime
from queue import Queue
from time import sleep

target = input("Hedef Server: ")
lock = threading.Lock()
s_thread = int(input("Kullanılacak Thread Sayısı: "))
mod = input("Mod (1:1024 port 2: Tüm portlar): ")

def c_banner():
    print("-" * 40)
    print("Bitiş: " + str(datetime.datetime.now()))
    print("""
░░░░░░░░▄▀█▀█▄██████████▄▄
░░░░░░░▐██████████████████▌
░░░░░░░███████████████████▌
░░░░░░▐███████████████████▌
░░░░░░█████████████████████▄
░░░▄█▐█▄█▀█████████████▀█▄█▐█▄
░▄██▌██████▄█▄█▄█▄█▄█▄█████▌██▌
▐████▄▀▀▀▀████████████▀▀▀▀▄███
▐█████████▄▄▄▄▄▄▄▄▄▄▄▄██████▀
░░░▀▀████████████████████         
            """)
    print("-" * 40)
    sleep(2)
    input("Çıkış için [ENTER]")
    
    

def banner():
    print("""
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░▄▄▄▄▄▄▄░░░░░░░░░
░░░░░░░░░▄▀▀▀░░░░░░░▀▄░░░░░░░
░░░░░░░▄▀░░░░░░░░░░░░▀▄░░░░░░
░░░░░░▄▀░░░░░░░░░░▄▀▀▄▀▄░░░░░
░░░░▄▀░░░░░░░░░░▄▀░░██▄▀▄░░░░
░░░▄▀░░▄▀▀▀▄░░░░█░░░▀▀░█▀▄░░░
░░░█░░█▄▄░░░█░░░▀▄░░░░░▐░█░░░
░░▐▌░░█▀▀░░▄▀░░░░░▀▄▄▄▄▀░░█░░
░░▐▌░░█░░░▄▀░░░░░░░░░░░░░░█░░
░░▐▌░░░▀▀▀░░░░░░░░░░░░░░░░▐▌░
░░▐▌░░░░░░░░░░░░░░░▄░░░░░░▐▌░
░░▐▌░░░░░░░░░▄░░░░░█░░░░░░▐▌░
░░░█░░░░░░░░░▀█▄░░▄█░░░░░░▐▌░
░░░▐▌░░░░░░░░░░▀▀▀▀░░░░░░░▐▌░
░░░░█░░░░░░░░░░░░░░░░░░░░░█░░
░░░░▐▌▀▄░░░░░░░░░░░░░░░░░▐▌░░
░░░░░█░░▀░░░░░░░░░░░░░░░░▀░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░""")
    print("-"*40)
    print(f"{target} Taranıyor...")
    print("Başlangıç: " + str(datetime.datetime.now()))
    print("-"*40)

def portscanner(port):
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    try:
        try:
            
            s.connect((target,port))
            banner = s.recv(1024)
            print(f"{port} OPEN BANNER: {banner}")
        except:
            pass
        s.connect((target,port))
        with lock:
            print(f"{port} OPEN Banner: {banner}")
    except:
        pass

def threader():
    while True:
        worker = q.get()
        portscanner(worker)
        q.task_done()
q = queue.Queue()

def main():
    for x in range(s_thread):
        t = threading.Thread(target=threader)
        t.daemon = True
        t.start()
    if mod == "1":
        for w in range(1,1024):
            q.put(w)
    elif mod =="2":
        for w in range(1,65535):
            q.put(w)
    q.join()

def bannergrab():
    pass


banner()
main()
c_banner()
