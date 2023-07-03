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
        
    def validarAlphaNum(self, texto):
        pass
        
    def validaInt(self, num):
        if num == '': return True
        try:
            value = int(num)
        except:
            return False
        else:
            return value
            
        
    def validaDecim(self, num):
        if num == '': return True
        try:
            value = float(f'{num:.2f}')
        except:
            return False
        else:
            return value
        
    
        
