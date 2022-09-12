from ast import For
from unittest import TestResult, result
import iperf3
import time
from multiprocessing import Process

def firstClient(server: str, port: int):
    client = iperf3.Client()
    client.duration = 10
    client.server_hostname = server
    client.port = port
    result = client.run()
    if result.error:
        print(result.error)
    else:
        ### Gibt die Mbit mit 2 nachkommastellen aus 
        ### print kann mit einer variable ersetzt werden für csv implementiereung
        #print("{:.2f}".format(float(result.received_Mbps)))
        result_value = "{:.2f}".format(float(result.received_Mbps))
        result_cl1.append("{:.2f}".format(float(result.received_Mbps)))
        result_cl1.append(result_value)
        result_cl1.append()

def secondClient(server: str, port: int):
    client2= iperf3.Client()
    client2.duration = 10
    client2.server_hostname = server
    client2.port = port
    result2 = client2.run()
    if result2.error:
        print(result2.error)
    else:
        ### Gibt die Mbit mit 2 nachkommastellen aus 
        ### print kann mit einer variable ersetzt werden für csv implementiereung
        print("{:.2f}".format(float(result2.received_Mbps)))
        result_cl2.append("{:.2f}".format(float(result2.received_Mbps)))

def thirdClient(server: str, port: int):
    client3= iperf3.Client()
    client3.duration = 10
    client3.server_hostname = server
    client3.port = port
    result3 = client3.run()
    if result3.error:
        print(result3.error)
    else:
        ### Gibt die Mbit mit 2 nachkommastellen aus 
        ### print kann mit einer variable ersetzt werden für csv implementiereung
        print("{:.2f}".format(float(result3.received_Mbps)))
        result_cl3.append("{:.2f}".format(float(result3.received_Mbps)))
## Inputs für IP und Port der Server
if __name__ == '__main__':
    result_cl1 = []
    result_cl2 = []
    result_cl3 = []
    '''
    server_first = input("IP für Server 1: ?\n")
    port_first = int(input("Port für Server 1: ? \n"))
    server_second = input("IP für Server 2: ?\n")
    port_second = int(input("Port für Server 1: ? \n"))
    server_third = input("IP für Server 3: ?\n")
    port_third = int(input("Port für Server 1: ? \n"))'''
    loopCheck = ""
    while(loopCheck != "exit"):
        #clProcess1 = Process(target=firstClient, args=(server_first,port_first))
        #clProcess2 = Process(target=secondClient, args=(server_second,port_second))
        #clProcess3 = Process(target=thirdClient, args=(server_third,port_third))
        clProcess1 = Process(target=firstClient, args=("127.0.0.1",5000))
        clProcess2 = Process(target=secondClient, args=("127.0.0.1",5001))
        clProcess3 = Process(target=thirdClient, args=("127.0.0.1",5002))
        clProcess1.start()
        clProcess2.start()
        clProcess3.start()
        clProcess1.join()
        clProcess2.join()
        clProcess3.join()
        loopCheck = input("exit = exit\nEnter = continue\n")
        if(loopCheck != "exit" and ""):
            loopCheck = input("exit = exit\nEnter = continue\n")
    for i in range(len(result_cl1)):
        print(f"Liste 1: {result_cl1[i]}")
        print(f"Liste 2: {result_cl2[i]}")
        print(f"Liste 3: {result_cl3[i]}")
    print(result_cl1)