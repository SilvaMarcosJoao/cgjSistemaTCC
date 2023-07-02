from tkinter import messagebox
class Validadores:       
    def limitar_cod(self, valor):
        if valor == '': return True
        try:
            value = int(valor)
        except ValueError:
            return False
        else:
            return 0 <= value <= 100
            
        
    def limitar_tam_cod(self, val):

        if val == '': return True
        try:
            value = int(val)
        except ValueError:
            return False
        else:
            return 0 <= value <= 100000
    
    def validarString(self, texto):
        if texto.isnumeric().strip():
            messagebox.showwarning('Alerta', 'Não é permitido valores ')
            return False
        else:
            return True
        
    def validarAlphaNum(self, texto):
        pass
        
    def validaInt(self, num):
        if  num.isnumeric():
            return True
        else:
            messagebox.showwarning('Alerta','Digite um número inteiro')
            return False
            
        
    def validaDecim(self, num):
        if not num.isdecimal():
            messagebox.showwarning('Alerta','Digite um número decimal')
            return False
        else:
            return True
        
