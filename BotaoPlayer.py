import tkinter as tk

def play():
    print("Play")

janela = tk.Tk()
janela.title("Player")
janela.geometry("300x200")

btn = tk.Button(janela, text="Play", command=play)
btn.pack()

janela.mainloop()