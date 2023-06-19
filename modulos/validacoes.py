from tkinter import messagebox

class Validadores:
    def __init__(self):
        self.caractere = None
        self.numInt = None

    def valida_string(self,texto: str) -> str:
        '''
        Esta função recebe um parâmetro qualquer para ser validado
        se é ou não uma String
        :param texto: recebe uma cadeia de caractere
        :return v: retorna a string após ser validada
        '''
        try:
            self.caractere = str(input(texto)).strip()
        except (ValueError, TypeError, FloatingPointError):
            print('\033[1;31mErro, valor digitado não é compatível com um texto\033[m')

        else:
            return self.caractere

    def valida_int(self, valor: int) -> int:
        '''
            Esta função recebe um parâmetro qualquer para ser validado
            se é ou não um valor inteiro
            :param valor: recebe um valor
            :return v: retorna o valor validado
            '''
        while True:
            try:
                self.numInt = int(input(valor))
            except ValueError:
                print('\033[1;31mValor inválido\033[m')
            except TypeError:
                print('\033[1;31mTipo de valor errado\033[m')
            else:
                return self.numInt

