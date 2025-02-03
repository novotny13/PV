import socket

# Třídy pro stavy serveru
class State:
    def handle_input(self, input_data):
        raise NotImplementedError

class StateKnowNothing(State):
    def handle_input(self, input_data):
        if input_data.startswith("U="):
            return StateKnowU(float(input_data[2:]))
        elif input_data.startswith("R="):
            return StateKnowR(float(input_data[2:]))
        elif input_data.startswith("I="):
            return StateKnowI(float(input_data[2:]))
        else:
            return self, "Chyba: Neplatný vstup. Očekává se U=, R= nebo I=."

class StateKnowU(State):
    def __init__(self, U):
        self.U = U

    def handle_input(self, input_data):
        if input_data.startswith("R="):
            return StateKnowUandR(self.U, float(input_data[2:]))
        elif input_data.startswith("I="):
            return StateKnowUandI(self.U, float(input_data[2:]))
        elif input_data == "U=?":
            return self, f"U={self.U}V"
        else:
            return self, "Chyba: Neplatný vstup. Očekává se R=, I= nebo U=?."

class StateKnowR(State):
    def __init__(self, R):
        self.R = R

    def handle_input(self, input_data):
        if input_data.startswith("U="):
            return StateKnowUandR(float(input_data[2:]), self.R)
        elif input_data.startswith("I="):
            return StateKnowRandI(self.R, float(input_data[2:]))
        elif input_data == "R=?":
            return self, f"R={self.R}Ω"
        else:
            return self, "Chyba: Neplatný vstup. Očekává se U=, I= nebo R=?."

class StateKnowI(State):
    def __init__(self, I):
        self.I = I

    def handle_input(self, input_data):
        if input_data.startswith("U="):
            return StateKnowUandI(float(input_data[2:]), self.I)
        elif input_data.startswith("R="):
            return StateKnowRandI(float(input_data[2:]), self.I)
        elif input_data == "I=?":
            return self, f"I={self.I}A"
        else:
            return self, "Chyba: Neplatný vstup. Očekává se U=, R= nebo I=?."

class StateKnowUandR(State):
    def __init__(self, U, R):
        self.U = U
        self.R = R

    def handle_input(self, input_data):
        if input_data == "I=?":
            I = self.U / self.R
            return StateKnowUandI(self.U, I), f"I={I}A"
        else:
            return self, "Chyba: Neplatný vstup. Očekává se I=?."

class StateKnowUandI(State):
    def __init__(self, U, I):
        self.U = U
        self.I = I

    def handle_input(self, input_data):
        if input_data == "R=?":
            R = self.U / self.I
            return StateKnowUandR(self.U, R), f"R={R}Ω"
        else:
            return self, "Chyba: Neplatný vstup. Očekává se R=?."

class StateKnowRandI(State):
    def __init__(self, R, I):
        self.R = R
        self.I = I

    def handle_input(self, input_data):
        if input_data == "U=?":
            U = self.R * self.I
            return StateKnowUandR(U, self.R), f"U={U}V"
        else:
            return self, "Chyba: Neplatný vstup. Očekává se U=?."

# Server
def start_server(host='0.0.0.0', port=12345):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    print(f"Server naslouchá na {host}:{port}...")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Připojen klient: {client_address}")
        state = StateKnowNothing()  # Počáteční stav

        while True:
            data = client_socket.recv(1024).decode().strip()
            if not data:
                break

            print(f"Přijat příkaz: {data}")
            if data == "CALCULATEOHM":
                state = StateKnowNothing()
                response = "OK"
            else:
                state, response = state.handle_input(data)

            client_socket.send(response.encode())

        client_socket.close()
        print(f"Klient {client_address} odpojen.")

# Spuštění serveru
if __name__ == "__main__":
    start_server()
