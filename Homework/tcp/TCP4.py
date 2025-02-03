class OhmState:
    def __init__(self):
        self.voltage = None
        self.current = None
        self.resistance = None
        
    def set_value(self, value_type, value):
        raise NotImplementedError()
        
    def calculate(self, target_type):
        raise NotImplementedError()

class KnowNothingState(OhmState):
    def set_value(self, value_type, value):
        if value_type.lower() == 'u':
            return KnowUState(value)
        elif value_type.lower() == 'r':
            return KnowRState(value)
        elif value_type.lower() == 'i':
            return KnowIState(value)
        raise ValueError("Neplatný typ hodnoty")

class KnowUState(OhmState):
    def __init__(self, voltage):
        super().__init__()
        self.voltage = float(voltage)
        
    def set_value(self, value_type, value):
        if value_type.lower() == 'r':
            return KnowURState(self.voltage, float(value))
        elif value_type.lower() == 'i':
            return KnowUIState(self.voltage, float(value))
        raise ValueError("Napřed nastavte odpor nebo proud")
    
    def calculate(self, target_type):
        raise ValueError("Chybí potřebné hodnoty pro výpočet")

# Další stavy podobně...

class OhmServer:
    def __init__(self):
        self.state = KnowNothingState()
        
    def handle_command(self, command):
        parts = command.split('=')
        
        if len(parts) == 2:
            # Příkaz pro nastavení hodnoty
            value_type, value = parts
            try:
                self.state = self.state.set_value(value_type.strip(), value.strip())
                return "OK"
            except ValueError as e:
                return f"Chyba: {str(e)}"
        elif command.endswith('?'):
            # Příkaz pro výpočet
            target_type = command[:-1].strip()
            try:
                result = self.state.calculate(target_type)
                return f"{target_type.upper()}={result}"
            except ValueError as e:
                return f"Chyba: {str(e)}"
        else:
            return "Neplatný příkaz"

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 12345))
    server_socket.listen(1)
    
    ohm_server = OhmServer()
    
    print("Čekám na připojení...")
    conn, addr = server_socket.accept()
    print(f"Připojen klient z {addr}")
    
    while True:
        try:
            command = conn.recv(1024).decode().strip()
            if not command:
                break
                
            response = ohm_server.handle_command(command)
            conn.sendall(f"{response}\n".encode())
            
        except Exception as e:
            print(f"Chyba: {str(e)}")
            conn.sendall("Chyba při zpracování příkazu\n".encode())
            break
    
    conn.close()
    server_socket.close()

if __name__ == "__main__":
    main()
