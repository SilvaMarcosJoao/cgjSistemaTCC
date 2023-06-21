from tkinter import *
class Funcionalidades:
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
    def duplo_clique_cat(self):
        # criando função duplo clique que seleciona o registro para aparecer nos campos e  serem alterados
        self.listaCategoria.selection()
        for i in self.listaCategoria.selection():
            col1, col2 = self.listaCategoria.item(i, 'values')
            self.et_cod_categoria.insert(END, col1)
            self.et_desc_categoria.insert(END, col2)      
    
    def limpa_usuario(self):
        self.et_nova_senha.delete(0, END)
        self.et_confir_senha.delete(0, END)

    def limpa_categoria(self):
        pass

    


