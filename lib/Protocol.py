"""Protocol"""
from Error import *

_Successful_Code = {"300": "Public Key Recieved",
                   "301": "Game Started",
                   "302": "Game Finished"
}

ProtocolCommands = ["PUBKEY", "SEND", "LOGIN", "SIGNIN", "JOINGAME", "HELLOWORLD"]

def send(instance, PC, metadata):
    instance.send(f"{PC}({metadata})".encode("utf-8"))
