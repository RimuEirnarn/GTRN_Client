from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread
from fernet import Fernet
from Game import Settings


class Server:
    """Server Library. (for broadcast a game)"""
    def __init__(self):
        self.PUB_KEY = Fernet.generate_key()
        self.PRI_KEY = Fernet.generate_key()
        self.thread = Thread
        self.setup = Settings()
        self.host = "0.0.0.0"

    def start_game(self):
        pass
    
    def create_game(self):
        self.server = socket(AF_INET, SOCK_STREAM)
        self.server.bind((self.host, str(self.setup.raw_data["Port"])))
        self.server.listen()
        self.player2, self.p2_addr = self.server.accept()
        return True
        
