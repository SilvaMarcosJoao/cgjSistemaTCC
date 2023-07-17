from modulos.dbsqlite import BancoDados


class Produto:
    banco = BancoDados()
    # CONSTRUTOR
    def __init__(self,cod_produto: int=None, desc_produto: str=None, modelo_produto:str=None ,preco_compra_produto:float=None, preco_venda_produto: float=None, qtd : int=None, categoria_produto :int=None):
        # ATRIBUTOS
        self.__cod_produto=cod_produto
        self.__desc_produto=desc_produto
        self.__modelo_produto=modelo_produto
        self.__preco_compra_produto=preco_compra_produto
        self.__preco_venda_produto=preco_venda_produto
        self.__qtd =qtd 
        self.__categoria_produto=categoria_produto

    # GETTERS E SETTERS
    def get_cod_produto(self) -> int:
        return self.__cod_produto

    def get_desc_produto(self) -> str:
        return self.__desc_produto

    def get_modelo_produto(self) -> str:
        return self.__modelo_produto

    def get_preco_compra_produto(self) -> float:
        return self.__preco_compra_produto

    def get_preco_venda_produto(self) -> float:
        return self.__preco_venda_produto

    def get_qtd(self) -> int:
        return self.__qtd

    def get_cod_categoria_produto(self) -> int:
        return self.__categoria_produto

    def set_cod_produto(self, cod_produto:int) -> None:
        self.__cod_produto = cod_produto

    def set_desc_produto(self, desc_produto:str) -> None:
        self.__desc_produto = desc_produto

    def set_modelo_produto(self, modelo_produto:str) -> None:
        self.__modelo_produto = modelo_produto

    def set_preco_compra_produto(self, preco_compra_produto:float) -> None:
        self.__preco_compra_produto = preco_compra_produto

    def set_preco_venda_produto(self, preco_venda_produto:float) -> None:
        self.__preco_venda_produto = preco_venda_produto

    def set_qtd(self, qtd:int) -> None:
        self.__qtd = qtd

    def set_cod_categoria_produto(self, cod_categoria_produto:int) -> None:
        self.__cod_produto = cod_categoria_produto


    # MÉTODOS DE CRUD DA CLASSE PRODUTO
    def cadastrarProduto(self, desc_produto:str, mod_produto:str, preco_compra:float, preco_venda:float, cod_categoria:int) -> None:
        """
        """
        self.banco.conectar()
        self.banco.cursor.execute(f"""INSERT INTO produto (desc_produto, modelo_produto,
                          preco_compra_produto, preco_venda_produto, cod_categoria_produto) 
                           VALUES ('{desc_produto}','{mod_produto}',
                           '{preco_compra}','{preco_venda}','{cod_categoria}') """)
        self.banco.conexao.commit()
        self.banco.desconectar()
       
    def alterarProduto(self, cod_produto:int, desc_produto:str, modelo_produto:str, preco_compra_produto:float, preco_venda_produto:float) -> None:
        """
        """
        self.banco.conectar()
        self.banco.cursor.execute(f"""UPDATE produto
                                SET desc_produto =('{desc_produto}'),
                                modelo_produto =('{modelo_produto}'),
                                preco_compra_produto =('{preco_compra_produto}'),
                                preco_venda_produto =('{preco_venda_produto}')
                                WHERE cod_produto =('{cod_produto}')""")
        self.banco.conexao.commit()
        self.banco.desconectar()
   
    def listarProdutos(self) -> list:
        """
        """
        self.banco.conectar()
        self.produtos = self.banco.cursor.execute("""SELECT cod_produto, desc_produto, modelo_produto, preco_compra_produto,
                                      preco_venda_produto, qtd_estoque, categoria_produto.desc_categoria_produto 
                                      FROM categoria_produto, produto 
                                      WHERE produto.cod_categoria_produto = categoria_produto.cod_categoria_produto""").fetchall()
        self.banco.desconectar()
        return self.produtos
        
    def consultarProduto(self, desc_produto:str) -> list: 
        """
        """
        self.banco.conectar()
        produto = self.banco.cursor.execute(f"""SELECT cod_produto, desc_produto, modelo_produto,
                          preco_compra_produto, preco_venda_produto, categoria_produto.desc_categoria_produto 
                          FROM categoria_produto, produto
                            WHERE produto.cod_categoria_produto = categoria_produto.cod_categoria_produto and desc_produto like '{desc_produto[0]}%'""").fetchall()
        self.banco.desconectar()  
        return produto

    def excluirProduto(self, cod_produto:int) -> None:
        """
        """
        self.banco.conectar()
        self.banco.cursor.execute(f"""DELETE FROM produto
                                WHERE cod_produto='{cod_produto}'""")
        self.banco.conexao.commit()
        self.banco.desconectar()

    def atualizaEstoqueProd(self, cod_produto:int, qtd:int) -> None:
        self.banco.conectar()
        self.banco.cursor.execute(f"""UPDATE produto SET qtd_estoque=qtd_estoque + ('{qtd}') 
                    WHERE cod_produto = {cod_produto} """)
        self.banco.conexao.commit()
        self.banco.desconectar()


# Métodos personalizados para telaCliente
    def listaperProduto(self):
        self.banco.conectar()
        self.produtos = self.banco.cursor.execute(f"""SELECT cod_produto, desc_produto, modelo_produto,
                                      preco_venda_produto, qtd_estoque
                                      FROM PRODUTO """).fetchall()
        self.banco.desconectar()                              
        return self.produtos
        
    def consultaProdutoVenda(self) -> list:
        """
        """
        self.banco.conectar()
        self.produto = self.banco.cursor.execute(f"""SELECT cod_produto, desc_produto,
                                         modelo_produto, preco_venda_produto FROM PRODUTO 
                                         """).fetchall()   
        self.banco.desconectar()
        return self.produto