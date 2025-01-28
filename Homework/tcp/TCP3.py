import socket
import random
import datetime
import threading
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
        "Available commands:\n"
        "1. quote - Get a random quote\n"
        "2. date - Get the current date and time\n"
        "3. help - List all commands\n"
        "4. exit - Disconnect from server\n"
        "5. shutdown-server - Disconnect and shut down the server\n"
        "6. clients - Show the number of connected clients\n"
        "7. broadcast <message> - Send a message to all connected clients\n"
    )

# Funkce pro zpracování neznámého příkazu
def unknown_command():
    return "Error: Unknown command. Type 'help' for a list of commands."

# Command pattern - Příkazová třída
class Command:
    def execute(self, client_socket, server, args=None):
        pass

class QuoteCommand(Command):
    def execute(self, client_socket, server, args=None):
        response = get_random_quote()
        client_socket.send(response.encode('utf-8'))

class DateCommand(Command):
    def execute(self, client_socket, server, args=None):
        response = get_current_date()
        client_socket.send(response.encode('utf-8'))

class HelpCommand(Command):
    def execute(self, client_socket, server, args=None):
        response = get_help()
        client_socket.send(response.encode('utf-8'))

class ExitCommand(Command):
    def execute(self, client_socket, server, args=None):
        client_socket.send("Goodbye!\r\n".encode('utf-8'))
        client_socket.close()

class ShutdownServerCommand(Command):
    def execute(self, client_socket, server, args=None):
        client_socket.send("Server is going to shut down. Do you confirm? (yes/no)\r\n".encode('utf-8'))
        response = client_socket.recv(1024).decode('utf-8').strip().lower()
        if response == 'yes':
            server.confirm_shutdown()
        else:
            client_socket.send("Shutdown aborted.\r\n".encode('utf-8'))

class ClientsCommand(Command):
    def execute(self, client_socket, server, args=None):
        client_socket.send(f"Current number of connected clients: {len(server.clients)}\r\n".encode('utf-8'))

class BroadcastCommand(Command):
    def execute(self, client_socket, server, args=None):
        # Očekáváme, že klient posílá zprávu po zadání broadcast příkazu
        if args:
            message = args
            for client in server.clients:
                if client != client_socket:
                    client.send(f"Broadcast message: {message}\r\n".encode('utf-8'))
        else:
            client_socket.send("Error: No message provided for broadcast.\r\n".encode('utf-8'))

class UnknownCommand(Command):
    def execute(self, client_socket, server, args=None):
        response = unknown_command()
        client_socket.send(response.encode('utf-8'))

# Třída pro server
class CommandServer:
    def __init__(self, host, port):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((host, port))
        self.server_socket.listen(5)
        self.clients = []  # Seznam připojených klientů
        self.shutdown_approved = False
        self.commands = {
            'quote': QuoteCommand(),
            'date': DateCommand(),
            'help': HelpCommand(),
            'exit': ExitCommand(),
            'shutdown-server': ShutdownServerCommand(),
            'clients': ClientsCommand(),
            'broadcast': BroadcastCommand()
        }

    def start(self):
        print("Server running, waiting for connections...")
        while True:
            client_socket, client_address = self.server_socket.accept()
            print(f"Connection from {client_address}")
            self.clients.append(client_socket)
            threading.Thread(target=self.handle_client, args=(client_socket,)).start()

    def handle_client(self, client_socket):
        while True:
            try:
                data = client_socket.recv(1024)
                if not data:
                    break  # Connection closed
                command = data.decode('utf-8').strip().lower()

                # Zpracování příkazů s argumenty (pokud jsou)
                args = None
                if ' ' in command:
                    command, args = command.split(' ', 1)

                # Zpracování příkazů
                if command in self.commands:
                    self.commands[command].execute(client_socket, self, args)


            except Exception as e:
                print(f"Error: {e}")
                break
        self.clients.remove(client_socket)
        client_socket.close()

    def confirm_shutdown(self):
        # Pokud všichni klienti souhlasí, server se vypne
        self.shutdown_approved = True
        for client in self.clients:
            client.send("Shutdown in progress...\r\n".encode('utf-8'))
        sys.exit(0)  # Ukončí server

# Spuštění serveru
if __name__ == '__main__':
    host = '192.168.56.1'  # Změňte na svou IP adresu
    port = 65532
    server = CommandServer(host, port)
    server.start()