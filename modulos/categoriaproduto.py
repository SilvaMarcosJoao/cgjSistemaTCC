from modulos.dbsqlite import BancoDados

banco = BancoDados()


class CategoriaProduto:
    def __init__(self, cod_categoria_produto: int=None, produto: list=None, desc_categoria_produto:str=None) -> None:
        self.__cod_categoria_produto = cod_categoria_produto
        self.__produto = produto
        self.__desc_categoria_produto=desc_categoria_produto
        
    def adicionarProdutoCategoria(self,produto) -> None:
        self.__produto.append(produto)

    def removerProdutoCategoria(self, produto) -> None:
        self.__produto.remove(produto)

    def get_cod_categoria_produto(self) -> int:
        return self.__cod_categoria_produto
    
    def set_cod_categoria_produto(self, cod: int) -> None:
        self.__cod_categoria_produto = cod
    
    def get_desc_categoria_produto(self) -> str:
        return self.__desc_categoria_produto

    def set_desc_categoria_produto(self, desc_categoria_produto) -> None:
        self.__desc_categoria_produto = desc_categoria_produto

    
    def cadastrarCategoria(self, desc_categoria) -> None:
        banco.conectar()
        banco.cursor.execute(f"""INSERT INTO categoria_produto (desc_categoria_produto) 
        VALUES ('{desc_categoria}')""")
        banco.conexao.commit()
        banco.desconectar()
        
    def alterarCategoria(self, cod, desc) -> None:
        banco.conectar()
        banco.cursor.execute(f"""UPDATE categoria_produto SET desc_categoria_produto = ('{desc}')
                                WHERE cod_categoria_produto = ('{cod}') """) 
        banco.conexao.commit()
        banco.desconectar()

    def listarCategoria(self) -> list:
        banco.conectar()
        categoria =banco.cursor.execute(f"""SELECT * FROM categoria_produto """).fetchall()     
        banco.desconectar()
        return categoria

    def consultarCategoria(self, cod_categoria_produto):
        banco.conectar()
        Categ = banco.cursor.execute(f"""SELECT cod_categoria_produto, desc_categoria_produto
                                FROM CategoriaPorduto
                                WHERE cod_categoria_produto='{cod_categoria_produto}' """).fetchmany()
        print(Categ)
        banco.desconectar()    
    
    def deletarCategoria(self, cod_categoria_produto):
        banco.conectar()
        banco.cursor.execute(f"""DELETE FROM categoria_produto
                                WHERE cod_categoria_produto = '{cod_categoria_produto}' """)
        banco.conexao.commit()
        banco.desconectar()
        
        






