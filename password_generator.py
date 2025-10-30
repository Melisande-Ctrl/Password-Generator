import tkinter as t
from tkinter import messagebox
import string
from random import choice, shuffle, sample

class Passwordgen(t.Frame):
    """Password generator"""
    def __init__(self, master=None) -> None:
        """Constructeur de la classe Passwordgen"""
        t.Frame.__init__(self, master, border=50, relief=t.SUNKEN)
        self.master.title('Password generator')

        self.len_mdp = t.IntVar()
        self.nber_mdp = t.IntVar()
        self.small_check = t.IntVar()
        self.capital_check = t.IntVar()
        self.num_check = t.IntVar()
        self.special_check = t.IntVar()
        self.accent_check = t.IntVar()

        size = t.Scale(self, from_= 1, to = 20, variable = self.len_mdp, orient = t.HORIZONTAL, label = 'Length of the password', sliderlength = 25, length = 140)
        size.pack(side=t.TOP)
        
        mdp_nber = t.Label(self, text='Enter the number of password(s)')
        mdp_nber.pack()
        enter_nber_mdp = t.Entry(self, textvariable=self.nber_mdp)
        enter_nber_mdp.pack()
        
        specifics = t.Label(self, text='Password characters : ')
        specifics.pack()
        
        n = ['Small letters', 'Capital letters', 'Numbers', 'Special symbols', 'Accented letters']
        v = [self.small_check, self.capital_check, self.num_check, self.special_check, self.accent_check]
        for i in range(5):
            check_button = t.Checkbutton(self, text=n[i], variable = v[i])
            check_button.pack()
        
        gen = t.Button(self, text='Generate', command=self.gen_mdp)
        gen.pack()

        save = t.Button(self, text='Save password(s)', command=self.save)
        save.pack()
        
        recup = t.Button(self, text='Recover password(s)', command=self.recup)
        recup.pack()
        
        delete = t.Button(self, text='Delete saved password(s)', command=self.delete)
        delete.pack()

        leave = t.Button(self, text='Quit', command=self.master.destroy)
        leave.pack(side=t.BOTTOM)
        
        self.pack()
        self.mainloop()
    
    def gen_mdp(self) -> None:
        """Method of Passwordgen that creates the password(s) following the parameters the user chose"""
        strings = []
        index = 0
        if self.small_check.get() == 1:
            small = string.ascii_lowercase
            strings.append(small)
            index += 1
        if self.capital_check.get() == 1:
            capital = string.ascii_uppercase
            strings.append(capital)
            index += 1
        if self.num_check.get() == 1:
            digits = string.digits
            strings.append(digits)
            index += 1
        if self.special_check.get() == 1:
            special = string.punctuation
            strings.append(special)
            index += 1
        if self.accent_check.get() == 1:
            accent = 'éèêëàâäùûüîïôö'
            strings.append(accent)
            index += 1
        
        self.list_passwords = []
        
        for _ in range(self.nber_mdp.get()):
            shuffle(strings)
            password = ''
            nberpertype = [0,0,0,0,0]
            for k in range(self.len_mdp.get()):
                nberpertype[k%5] += 1

            for i in range(index):
                for _ in range(nberpertype[i]):
                    password += ''.join(choice(strings[i]))
            password = ''.join(sample(password, len(password)))
            self.list_passwords.append(password)
        
        generated_passwords = '\n'.join(self.list_passwords)
        messagebox.showinfo('Password(s)', 'Password(s) generated :\n' + generated_passwords)
    
    def save(self) -> None:
        """Method of Passwordgen that writes the password(s) made in the file gen_password.txt"""
        fich = open('gen_password.txt', 'a')
        for i in range(len(self.list_passwords)):
            fich.write(self.list_passwords[i]+'\n')
        fich.close()
        messagebox.showinfo('Save', 'Password(s) saved!')

    def recup(self) -> None:
        """Method of Passwordgen that makes a list of the password(s) in the file gen_password.txt (if it isn't empty)"""
        fich = open('gen_password.txt', 'r')
        recup_mdp = fich.readlines()
        fich.close()
        if recup_mdp == []:
            messagebox.showerror('Error', 'gen_password.txt is empty.')
        else:
            recup_mdp = [password[:-1] for password in recup_mdp]
            recovered_passwords = '\n'.join(recup_mdp)
            messagebox.showinfo('Password(s) recovered', 'Password(s) in gen_password.txt :\n'+ recovered_passwords)
    
    def delete(self) -> None:
        """Method of Passwordgen that opens the file in write mode to erase any data inside"""
        fich = open('gen_password.txt', 'w')
        fich.close()
        messagebox.showinfo('Delete', 'Password(s) deleted! Your file gen_password.txt is now empty.')

Passwordgen()