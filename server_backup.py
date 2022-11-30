# ref: https://docs.python.org/3/library/socketserver.html?highlight=requesthandlerclass#socketserver.BaseServer.RequestHandlerClass
import socketserver
from pymongo import MongoClient

mongo_client = MongoClient("mongo")
db = mongo_client["cse312"]
logs_collection = db["logs"]

class MyTCPHandler(socketserver.BaseRequestHandler):

    def handle(self):
        received_data = self.request.recv(2048)

        client_id = self.client_address[0] + ":" + str(self.client_address[1])
        logs_collection.insert_one({"client": client_id})
        
        print(client_id + " is sending data:")
        print(len(received_data))
        print(received_data.decode())

        print("\n\n")
           
        self.request.sendall("HTTP/1.1 200 OK\r\nContent-Length: 5\r\nContent-Type: text/plain; charset=utf-8\r\n\r\nhello".encode())



if __name__ == "__main__":
    host = "0.0.0.0"
    port = 8000

    server = socketserver.ThreadingTCPServer((host, port), MyTCPHandler)
    server.serve_forever()
