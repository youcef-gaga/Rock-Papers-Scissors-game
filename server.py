import socket
import random

def main():
    host = '127.0.0.1'
    port = 5000
    server_score = 0
    client_score = 0

    s = socket.socket()
    s.bind((host, port))
    print("waiting for player")
    s.listen(1)
    c, addr = s.accept()
    print("Player connected from: " + str(addr))
    print("Start the game ")


    while True:
        data = c.recv(1024).decode('utf-8')
        if not data or data == "q":
            break

        server_choice = random.choice(["rock", "paper", "scissors"])
        print("Server chose: " + server_choice)

        if data == "rock":
            if server_choice == "rock":
                result = "tie"
            elif server_choice == "paper":
                result = "you lose"
                server_score += 1
            elif server_choice == "scissors":
                result = "you win"
                client_score += 1
        elif data == "paper":
            if server_choice == "rock":
                result = "you win"
                client_score += 1
            elif server_choice == "paper":
                result = "tie"
            elif server_choice == "scissors":
                result = "you lose"
                server_score += 1
        elif data == "scissors":
            if server_choice == "rock":
                result = "you lose"
                server_score += 1
            elif server_choice == "paper":
                result = "you win"
                client_score += 1
            elif server_choice == "scissors":
                result = "tie"
        else:
            result = "Invalid choice"

        c.send((result + ', ' + str(server_score) + ' - ' + str(client_score)).encode('utf-8'))
   

    if server_score > client_score:
        print("Server wins!")
    elif client_score > server_score:
        print("Client wins!")
    else:
        print("It's a tie!")
    c.close()

if __name__ == '__main__':
    main()
