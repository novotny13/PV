import socket
import threading
import random
import datetime

class Command:
    def execute(self, server, client_socket):
        pass

class QuoteCommand(Command):
    def execute(self, server, client_socket):
        quote = random.choice(server.quotes)
        client_socket.sendall(quote.encode('utf-8'))

class DateCommand(Command):
    def execute(self, server, client_socket):
        current_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        client_socket.sendall(current_date.encode('utf-8'))

class HelpCommand(Command):
    def execute(self, server, client_socket):
        help_text = "Available commands: quote, date, help, exit, shutdown-server"
        client_socket.sendall(help_text.encode('utf-8'))

class ExitCommand(Command):
    def execute(self, server, client_socket):
        client_socket.sendall(b"Goodbye! Disconnecting...")
        client_socket.close()
        raise ConnectionClosedException()

class ShutdownCommand(Command):
    def execute(self, server, client_socket):
        client_socket.sendall(b"Shutting down the server...")
        client_socket.close()
        server.shutdown = True
        raise ConnectionClosedException()

class UnknownCommand(Command):
    def execute(self, server, client_socket):
        client_socket.sendall(b"Unknown command. Type 'help' for a list of commands.")

class ConnectionClosedException(Exception):
    pass

class Server:
    def __init__(self, host='0.0.0.0', port=12345):
        self.host = host
        self.port = port
        self.shutdown = False
        self.quotes = [
            "The only limit to our realization of tomorrow is our doubts of today. - Franklin D. Roosevelt",
            "Do not wait to strike till the iron is hot; but make it hot by striking. - William Butler Yeats",
            "Great minds discuss ideas; average minds discuss events; small minds discuss people. - Eleanor Roosevelt"
        ]
        self.commands = {
            'quote': QuoteCommand(),
            'date': DateCommand(),
            'help': HelpCommand(),
            'exit': ExitCommand(),
            'shutdown-server': ShutdownCommand()
        }

    def handle_client(self, client_socket):
        client_socket.sendall(b"Welcome to the server! Type 'help' for a list of commands.\n")
        while not self.shutdown:
            try:
                data = client_socket.recv(1024)
                if not data:
                    break

                command_name = data.decode('utf-8').strip()
                command = self.commands.get(command_name, UnknownCommand())

                try:
                    command.execute(self, client_socket)
                except ConnectionClosedException:
                    break

            except Exception as e:
                print(f"Error handling client: {e}")
                break

        client_socket.close()

    def start(self):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind((self.host, self.port))
        server_socket.listen(5)

        print(f"Server started on {self.host}:{self.port}")

        try:
            while not self.shutdown:
                client_socket, addr = server_socket.accept()
                print(f"Connection from {addr}")
                client_thread = threading.Thread(target=self.handle_client, args=(client_socket,))
                client_thread.start()
        except KeyboardInterrupt:
            print("Shutting down server...")
        finally:
            server_socket.close()

if __name__ == '__main__':
    server = Server()
    server.start()