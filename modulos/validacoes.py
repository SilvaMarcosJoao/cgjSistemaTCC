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
        if texto.isnumeric():
            messagebox.showwarning('Alerta', 'Não é permitido valores ')
            return False
        else:
            return True
        
    def validaInt(self, num):
        if num.isnumeric():
            return True
        else:
            messagebox.showwarning('Alerta','Digite um número inteiro')
            return False