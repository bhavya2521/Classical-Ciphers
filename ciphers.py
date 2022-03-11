from tkinter import *
import re

class MyWindow:
    def __init__(self, win):
        self.lbl1 = Label(win, text='Mode', font=("Comic Sans MS", 13))
        self.lbl2 = Label(win, text='Message', font=("Comic Sans MS", 13))
        self.lbl4 = Label(win, text='Key', font=("Comic Sans MS", 13))
        self.lbl3 = Label(win, text='Result', font=("Comic Sans MS", 13))
        self.info1 = Label(win, text="Type 'e' or 'E' to encrypt and 'd' or 'D' to decrypt.",
                           font=("Comic Sans MS", 13))
        self.einfo = StringVar(win)
        self.error = Label(win, textvariable=self.einfo, font=("Comic Sans MS", 15))
        self.scrollbar = Scrollbar(orient=VERTICAL)
        self.t1 = Entry(bd=3, xscrollcommand=self.scrollbar.set, font=("Comic Sans MS", 13))
        self.t2 = Text(bd=3, font=("Comic Sans MS", 13))
        self.t4 = Entry(bd=3, font=("Comic Sans MS", 13))
        self.t3 = Text(bd=3, font=("Comic Sans MS", 13))
        self.t3.config(state='disabled')
        self.info1.place(x=100, y=10)
        self.lbl1.place(x=100, y=40)
        self.t1.place(x=200, y=40, width=350, )
        self.lbl2.place(x=100, y=80)
        self.t2.place(x=200, y=80, width=350, height=180)
        self.lbl4.place(x=100, y=270)
        self.t4.place(x=200, y=270, width=350)
        self.b1 = Button(win, text='Caesar', font=("Comic Sans MS", 13), command=self.caesar)
        self.b2 = Button(win, text='Substitution', font=("Comic Sans MS", 13), command=self.substitution)
        self.b3 = Button(win, text='Affine', font=("Comic Sans MS", 13), command=self.affine)
        self.b4 = Button(win, text='Vigenere', font=("Comic Sans MS", 13), command=self.vigenere)
        self.b5 = Button(win, text='Permutation', font=("Comic Sans MS", 13), command=self.permutation)
        self.b6 = Button(win, text='Play Fair', font=("Comic Sans MS", 13), command=self.playfair)
        self.b1.place(x=210, y=305)
        self.b2.place(x=290, y=305)
        self.b3.place(x=410, y=305)
        self.b4.place(x=210, y=355)
        self.b5.place(x=300, y=355)
        self.b6.place(x=420, y=355)
        self.lbl3.place(x=100, y=400)
        self.t3.place(x=200, y=400, width=350, height=180)
        self.error.place(x=100, y=600)

    def clear(self):
        self.t3.config(state='normal')
        self.t3.delete('1.0', 'end')
        self.t3.config(state='disabled')

    def set(self, res):
        self.t3.config(state='normal')
        self.t3.delete('1.0', 'end')
        self.t3.insert(END, str(res))
        self.t3.config(state='disabled')

    def getMode(self):
        mode = self.t1.get().lower()
        if mode == "e" or mode == "d":
            return mode
        else:
            self.clear()
            self.einfo.set("Error: Invalid Mode!! Enter either 'e' or 'd' or 'E' or 'D'.")

    def getMessage(self):
        message = self.t2.get('1.0', 'end')
        return str(message)

    def getKey(self):
        key = self.t4.get()
        return key

    def getValue(self, ch):
        if ch.isupper():
            return ord(ch) - 65
        else:
            return ord(ch) - 97

    def egcd(self, a, b):
        x, y, u, v = 0, 1, 1, 0
        while a != 0:
            q, r = b // a, b % a
            m, n = x - u * q, y - v * q
            b, a, x, y, u, v = a, r, u, v, m, n
        gcd = b
        return gcd, x, y

    def invalue(self, n):
        gcd, x, y = self.egcd(n, 26)
        if gcd != 1:
            return None
        else:
            return x % 26

    def caesar(self):
        mode = self.getMode()
        if mode == "e" or mode == "d":
            self.einfo.set("")
            message = self.getMessage()
            try:
                key = int(self.getKey())
            except:
                self.clear()
                self.einfo.set("Error: Invalid Key!! Enter a key between 1 and 26")
                return
            if 1 <= key <= 26:
                self.einfo.set("")
                if mode == 'd':
                    key = -key
                res = ''
                for symbol in message:
                    if symbol.isalpha():
                        if symbol.isupper():
                            res += chr((ord(symbol) + key - 65) % 26 + 65)
                        elif symbol.islower():
                            res += chr((ord(symbol) + key - 97) % 26 + 97)
                    else:
                        res += symbol
                self.set(res)
            else:
                self.clear()
                self.einfo.set("Error: Invalid Key!! Enter a key between 1 and 26")

    def substitution(self):
        mode = self.getMode()
        if mode == 'e' or mode == 'd':
            self.einfo.set("")
            message = self.getMessage()
            key = self.getKey()
            letters = 'abcdefghijklmnopqrstuvwxyz'
            s=""
            for i in key:
                if(i not in s):
                    s+=i
            key=s
            if(len(key)!=26):
                self.clear()
                self.einfo.set("Error: Invalid Key!! Enter a permutation of a to z alphabets of length 26")
            else:
                dict1 = {}
                for i in range(26):
                    dict1[letters[i]] = key[i]
                dict2 = {}
                for i in range(26):
                    dict2[key[i]] = letters[i]
                self.einfo.set("")
                res = ""
                if mode == 'd':
                    for i in message:
                        if i.isalpha():
                            if(i.isupper()):
                                res += dict2[i.lower()].upper()
                            else:
                                res += dict2[i.lower()]
                        else:
                            res += i
                else:
                    for i in message:
                        if i.isalpha():
                            if (i.isupper()):
                                res += dict1[i.lower()].upper()
                            else:
                                res += dict1[i.lower()]
                        else:
                            res += i
                self.set(res)

    def affine(self):
        mode = self.getMode()
        if mode == 'e' or mode == 'd':
            self.einfo.set("")
            message = self.getMessage()
            key = self.getKey()
            key = key.split(",")
            a = int(key[0])
            b = int(key[1])
            res = ""
            if self.invalue(a) is not None:
                if mode == 'e':
                    for i in message:
                        if i.isalpha():
                            x = (self.getValue(i) * a + b) % 26
                            if i.isupper():
                                res += chr(x + 65)
                            else:
                                res += chr(x + 97)
                        else:
                            res += i
                else:
                    for i in message:
                        if i.isalpha():
                            x = (self.invalue(a) * (self.getValue(i) - b)) % 26
                            if i.isupper():
                                res += chr(x + 65)
                            else:
                                res += chr(x + 97)
                        else:
                            res += i
                self.set(res)
            else:
                self.clear()
                self.einfo.set("Error: Invalid Key!! Enter a key which is co-prime to 26")

    def vigenere(self):
        mode = self.getMode()
        if mode == 'e' or mode == 'd':
            self.einfo.set("")
            message = self.getMessage()
            key = self.getKey()
            key = list(key)
            n = len(message)
            for i in range(n - len(key)):
                key.append(key[i % len(key)])
            key = "".join(key)
            res = ""
            if mode == 'e':
                c = 0
                for i in range(n):
                    if message[i].isalpha():
                        x = (ord(message[i]) + self.getValue(key[c]))
                        if message[i].isupper():
                            if x < 65:
                                x += 26
                            elif x > 90:
                                x -= 26
                        if message[i].islower():
                            if x < 97:
                                x += 26
                            elif x > 122:
                                x -= 26
                        res += chr(x)
                        c += 1

                    else:
                        res += message[i]
            else:
                c = 0
                for i in range(n):
                    if message[i].isalpha():
                        x = (ord(message[i]) - self.getValue(key[c]))
                        if message[i].isupper():
                            if x < 65:
                                x += 26
                            elif x > 90:
                                x -= 26
                        if message[i].islower():
                            if x < 97:
                                x += 26
                            elif x > 122:
                                x -= 26
                        res += chr(x)
                        c += 1

                    else:
                        res += message[i]
            self.set(res)

    def permutation(self):
        mode = self.getMode()
        if mode == 'e' or mode == 'd':
            self.einfo.set("")
            message = self.getMessage()
            key = self.getKey().split(",")
            n = len(key)
            res = ""
            message = message.strip()
            if mode == 'e':
                text = ""
                for i in range(len(message)):
                    text += message[i]
                    if len(text) == n or i == len(message) - 1:
                        text += 'x' * (n - len(text))
                        for k in key:
                            res += text[int(k) - 1]
                        text = ""
            else:
                l = [0] * len(key)
                for i in range(len(key)):
                    l[int(key[i]) - 1] = i + 1
                key = l

                text = ""
                for i in range(len(message)):
                    text += message[i]
                    if len(text) == n or i == len(message) - 1:
                        text += 'x' * (n - len(text))
                        for k in key:
                            res += text[int(k) - 1]
                        text = ""
            self.set(res)

    def playfair(self):
        mode = self.getMode()
        if mode == 'e' or mode == 'd':
            self.einfo.set("")
            msg = self.getMessage()
            key = self.getKey()
            key = key.replace(" ", "")
            key = key.upper()
            message = msg.upper()
            message = 'X'.join(re.findall(r"(?i)\b[a-z]+\b", message))

            result = []
            for c in key:
                if c not in result:
                    if c == 'J':
                        result.append('I')
                    else:
                        result.append(c)
            flag = 0
            for i in range(65, 91):
                if chr(i) not in result:
                    if i == 73 and chr(74) not in result:
                        result.append("I")
                        flag = 1
                    elif flag == 0 and i == 73 or i == 74:
                        pass
                    else:
                        result.append(chr(i))

            my_matrix = [[0 for i in range(5)] for j in range(5)]
            k = 0
            for i in range(5):
                for j in range(5):
                    my_matrix[i][j] = result[k]
                    k += 1

            def locindex(c):
                loc = list()
                if c == 'J':
                    c = 'I'
                for i, j in enumerate(my_matrix):
                    for k, l in enumerate(j):
                        if c == l:
                            loc.append(i)
                            loc.append(k)
                            return loc

            res = ""
            i = 0
            if mode[0] == 'e':
                for s in range(0, len(message) + 1, 2):
                    if s < len(message) - 1:
                        if message[s] == message[s + 1]:
                            message = message[:s + 1] + 'X' + message[s + 1:]
                if len(message) % 2 != 0:
                    message = message[:] + 'X'
                while i < len(message):
                    loc = locindex(message[i])
                    loc1 = locindex(message[i + 1])
                    if loc[1] == loc1[1]:
                        res += my_matrix[(loc[0] + 1) % 5][loc[1]]
                        res += my_matrix[(loc1[0] + 1) % 5][loc1[1]]
                    elif loc[0] == loc1[0]:
                        res += my_matrix[loc[0]][(loc[1] + 1) % 5]
                        res += my_matrix[loc1[0]][(loc1[1] + 1) % 5]
                    else:
                        res += my_matrix[loc[0]][loc1[1]]
                        res += my_matrix[loc1[0]][loc[1]]
                    i = i + 2
                res = res.lower()

            else:
                while i < len(message):
                    loc = locindex(message[i])
                    loc1 = locindex(message[i + 1])
                    if loc[1] == loc1[1]:
                        res += my_matrix[(loc[0] - 1) % 5][loc[1]]
                        res += my_matrix[(loc1[0] - 1) % 5][loc1[1]]
                    elif loc[0] == loc1[0]:
                        res += my_matrix[loc[0]][(loc[1] - 1) % 5]
                        res += my_matrix[loc1[0]][(loc1[1] - 1) % 5]
                    else:
                        res += my_matrix[loc[0]][loc1[1]]
                        res += my_matrix[loc1[0]][loc[1]]
                    i = i + 2
                res = res.lower()
            self.set(res)


window = Tk()
mywin = MyWindow(window)
window.title('Classical Ciphers')
window.geometry("650x650+10+10")
window.resizable(width=False, height=False)
window.mainloop()
