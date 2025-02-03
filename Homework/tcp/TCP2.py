import socket
import random
import datetime
import sys

# Citáty pro náhodný výběr
quotes = [
    "The only way to do great work is to love what you do. – Steve Jobs",
    "Life is what happens when you're busy making other plans. – John Lennon",
    "To be yourself in a world that is constantly trying to make you something else is the greatest accomplishment. – Ralph Waldo Emerson",
    "The purpose of life is not to be happy. It is to be useful, to be honorable, to be compassionate, to have it make some difference that you have lived and lived well. – Ralph Waldo Emerson"
]

# Funkce pro příkaz 'quote'
def get_random_quote():
    return random.choice(quotes)

# Funkce pro příkaz 'date'
def get_current_date():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Funkce pro příkaz 'help'
def get_help():
    return (
        "Available commands: 1. quote - Get a random quote"
        " 2. date - Get the current date and time"
        " 3. help - List all commands"
        " 4. exit - Disconnect from server"
        " 5. shutdown-server - Disconnect and shut down the server"



    )

# Funkce pro zpracování neznámého příkazu
def unknown_command():
    return "Error: Unknown command. Type 'help' for a list of commands."

# Command pattern - Příkazová třída
class Command:
    def execute(self, client_socket):
        pass

class QuoteCommand(Command):
    def execute(self, client_socket):
        response = get_random_quote()
        client_socket.send(response.encode('utf-8'))

class DateCommand(Command):
    def execute(self, client_socket):
        response = get_current_date()
        client_socket.send(response.encode('utf-8'))

class HelpCommand(Command):
    def execute(self, client_socket):
        response = get_help()
        client_socket.send(response.encode('utf-8'))

class ExitCommand(Command):
    def execute(self, client_socket):
        client_socket.send("Goodbye!\r\n".encode('utf-8'))
        client_socket.close()

class ShutdownServerCommand(Command):
    def execute(self, client_socket):
        client_socket.send("Server shutting down.\r\n".encode('utf-8'))
        client_socket.close()
        sys.exit(0)  # Ukončí server

class UnknownCommand(Command):
    def execute(self, client_socket):
        response = unknown_command()
        client_socket.send(response.encode('utf-8'))

class CommandServer:
    def __init__(self, host, port):
        self.server_socket = socket.socket()
        self.server_socket.bind((host, port))
        self.server_socket.listen(5)
        self.commands = {
            'quote': QuoteCommand(),
            'date': DateCommand(),
            'help': HelpCommand(),
            'exit': ExitCommand(),
            'shutdown-server': ShutdownServerCommand()
        }

    def start(self):
        print("Server running, waiting for connections...")
        while True:
            client_socket, client_address = self.server_socket.accept()
            print(f"Connection from {client_address}")
            self.handle_client(client_socket)

    def handle_client(self, client_socket):
        while True:
            try:
                data = client_socket.recv(1024)
                if not data:
                    break
                command = data.decode('utf-8').strip().lower()


                if command in self.commands:
                    self.commands[command].execute(client_socket)


            except Exception as e:
                print(f"Error: {e}")
                break
        client_socket.close()

# Spuštění serveru
if __name__ == '__main__':
    host = '127.0.0.1'  # Změňte na svou IP adresu
    port = 65532
    server = CommandServer(host, port)
    server.start()
