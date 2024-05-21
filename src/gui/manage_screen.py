import tkinter as tk
from tkinter import messagebox

class Managescreen:
    def __init__(self, interface) -> None:
        self.interface=interface
        self.root = tk.Tk()
        
        self.root.geometry("400x300")
        
        self.frame = tk.Frame(self.root)
        self.listbox = tk.Listbox(self.frame)

        self.btn = tk.Button(self.frame, text="Excluir", command=self.delete_person)
        
        self.listbox.pack()
        self.btn.pack()
        self.frame.pack()
        self.show_names()
    
    def show_names(self):
        self.names = self.interface.get_names()
        self.listbox.delete(0, tk.END)
        i=0
        
        for name in self.names:
            self.listbox.insert(i, name)
            i+=1
        self.frame.update()
    async def open(self):
        self.root.mainloop()
    
    def delete_person(self):
        i=self.listbox.curselection()[0]
        if messagebox.askyesno("Are you sure?", message="Deseja deletar?", parent=self.root):
            self.interface.delete_on_index(i)
            self.interface.refresh_names()
            self.show_names()
        
    def close(self):
        self.close()