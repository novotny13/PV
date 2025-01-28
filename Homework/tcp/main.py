import socket

# Nastavení IP adresy a portu
server_inet_address = ("127.0.0.1", 65532)

# Vytvoření serverového socketu
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # Bind na adresu a port
    server_socket.bind(server_inet_address)
    print(f"Server spuštěn na {server_inet_address[0]}:{server_inet_address[1]}")

    # Naslouchání na portu (maximálně 5 spojení v frontě)
    server_socket.listen(5)
    print("Server čeká na připojení...")

    while True:
        # Přijetí spojení
        connection, client_inet_address = server_socket.accept()
        print(f"Připojen klient: {client_inet_address[0]}:{client_inet_address[1]}")

        try:
            # Zpráva k odeslání
            message = "HELLO\n"
            message_as_bytes = message.encode("utf-8")

            # Odeslání zprávy klientovi
            connection.send(message_as_bytes)
            print("Zpráva odeslána klientovi.")
        except Exception as e:
            print(f"Chyba při odesílání zprávy: {e}")


except Exception as e:
    print(f"Chyba na serveru: {e}")

finally:
    # Zavření serverového socketu
    server_socket.close()
    print("Server ukončen.")