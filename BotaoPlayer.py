import tkinter as tk

janela = tk.Tk()
janela = title("Player")
janela.geometry("300x200")

janela.mainloop()

def play():
    print("Play")

btn = tk.button(janela, text="Play", command=play)
btn.pack()
janela.mainloop()