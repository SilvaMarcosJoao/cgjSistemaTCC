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
        