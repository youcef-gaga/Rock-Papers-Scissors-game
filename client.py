import socket
import tkinter as tk

def main():
    host = '127.0.0.1'
    port = 5000

    s = socket.socket()
    s.connect((host, port))

    # Create the GUI
    root = tk.Tk()
    root.geometry("300x200")
    root.title("Rock, Paper, Scissors")
    tk.Label(root, text="Make your choice:").pack()
    choice = tk.StringVar(value="rock")
    tk.Radiobutton(root, text="Rock", variable=choice, value="rock").pack()
    tk.Radiobutton(root, text="Paper", variable=choice, value="paper").pack()
    tk.Radiobutton(root, text="Scissors", variable=choice, value="scissors").pack()
    result_label = tk.Label(root)
    result_label.pack()

    def on_submit():
        message = choice.get()
        s.send(message.encode('utf-8'))
        data = s.recv(1024).decode('utf-8')
        result_label.config(text="Result: " + data)

    tk.Button(root, text="Submit", command=on_submit).pack()
    root.mainloop()

    s.close()

if __name__ == '__main__':
    main()
