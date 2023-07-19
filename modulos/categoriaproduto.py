from modulos.dbsqlite import BancoDados


class CategoriaProduto:
    banco = BancoDados()
    # CONSTRUTOR
    def __init__(self, cod_categoria_produto: int=None, desc_categoria_produto:str=None) -> None:
        # ATRIBUTOS
        self.__cod_categoria_produto = cod_categoria_produto
        self.__desc_categoria_produto=desc_categoria_produto
        
    # GETTERS E SETTERS
    def get_cod_categoria_produto(self) -> int:
        return self.__cod_categoria_produto
    
    def set_cod_categoria_produto(self, cod: int) -> None:
        self.__cod_categoria_produto = cod
    
    def get_desc_categoria_produto(self) -> str:
        return self.__desc_categoria_produto

    def set_desc_categoria_produto(self, desc_categoria_produto) -> None:
        self.__desc_categoria_produto = desc_categoria_produto

    # MÉTODOS DE CRUD DA CLASSE CATEGORIA PRODUTO
    def cadastrarCategoria(self, desc_categoria:str) -> None:
        """
        Cadastra a categoria dos produtos.
        :param: desc_categoria. 
        :return: Não há retorno. 
        """
        self.banco.conectar()
        self.banco.cursor.execute(f"""INSERT INTO categoria_produto (desc_categoria_produto) 
        VALUES ('{desc_categoria}')""")
        self.banco.conexao.commit()
        self.banco.desconectar()
        
    def alterarCategoria(self, cod_categoria_produto:int, desc_categoria:str) -> None:
        """
        Altera a descrição de uma categoria.
        :param: cod_categoria_produto do tipo inteiro e desc_categoria do tipo string.
        :return: Não tem retorno
        """
        self.banco.conectar()
        self.banco.cursor.execute(f"""UPDATE categoria_produto SET desc_categoria_produto = ('{desc_categoria}')
                                WHERE cod_categoria_produto = ('{cod_categoria_produto}') """) 
        self.banco.conexao.commit()
        self.banco.desconectar()

    def listarCategoria(self) -> list:
        """
        Exibe as categorias cadastradas.
        :param: não há parâmetros.
        :return: retorna uma lista com as categorias.
        """
        self.banco.conectar()
        categoria = self.banco.cursor.execute(f"""SELECT * FROM categoria_produto """).fetchall()     
        self.banco.desconectar()
        return categoria
    
    def excluirCategoria(self, cod_categoria_produto:int) -> None:
        """
        Deleta uma categoria.
        :param: cód_categoria_produto do tipo inteiro.
        :return: Não tem retorno.
        """
        self.banco.conectar()
        self.banco.cursor.execute(f"""DELETE FROM categoria_produto
                                WHERE cod_categoria_produto = '{cod_categoria_produto}' """)
        self.banco.conexao.commit()
        self.banco.desconectar()

    def buscaQtdCodigoCategoria(self) -> int:
        self.banco.conectar()
        self.qtdcRegis = self.banco.cursor.execute(f""" SELECT count(cod_categoria_produto)  from categoria_produto""").fetchall()

        return self.qtdcRegis
    
    def codigoCategoria(self) -> int:
        self.banco.conectar()
        self.codigo = self.banco.cursor.execute(f""" SELECT cod_categoria_produto  from categoria_produto""").fetchall()
        return self.codigo