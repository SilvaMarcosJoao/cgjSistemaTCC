from modulos.dbsqlite import BancoDados
from modulos.categoriaproduto import CategoriaProduto

categoria_produto = CategoriaProduto()
categoria_produto.get_desc_categoria_produto()
banco = BancoDados()


class Produto:
    def __init__(self,cod_produto: int=None, desc_produto: str=None, modelo_produto:str=None ,preco_compra_produto:float=None, preco_venda_produto: float=None, qtd : int=None, categoria_produto :CategoriaProduto=None):

        self.__cod_produto=cod_produto
        self.__desc_produto=desc_produto
        self.__modelo_produto=modelo_produto
        self.__preco_compra_produto=preco_compra_produto
        self.__preco_venda_produto=preco_venda_produto
        self.__qtd =qtd 
        self.__categoria_produto=categoria_produto


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

    def get_cod_categoria_produto(self) -> CategoriaProduto:
        return self.__categoria_produto

    def set_cod_produto(self, cod_produto):
        self.__cod_produto = cod_produto

    def set_desc_produto(self, desc_produto):
        self.__desc_produto = desc_produto

    def set_modelo_produto(self, modelo_produto):
        self.__modelo_produto = modelo_produto

    def set_preco_compra_produto(self, preco_compra_produto):
        self.__preco_compra_produto = preco_compra_produto

    def set_preco_venda_produto(self, preco_venda_produto):
        self.__preco_venda_produto = preco_venda_produto

    def set_qtd(self, qtd):
        self.__qtd = qtd

    def set_cod_categoria_produto(self, cod_categoria_produto):
        self.__cod_produto = cod_categoria_produto

     #cadastra os produtos 
    def cadastrarProduto(self):
        banco.conectar()
        banco.cursor.execute(f"""Insert into Produto(cod_produto, desc_produto, modelo_produto,
                          preco_compra_produto, preco_venda_produto, qtd, cod_categoria_produto) 
                          values('{self.__cod_produto }','{self.__desc_produto }','{self.__modelo_produto }','{self.__preco_compra_produto}','{self.__preco_venda_produto }','{self.__qtd }','{self.__categoria_produto }')""")
        banco.conexao.commit()
        banco.desconectar()
    
    #Atualizar produto    
    def alterarProduto(self, cod_produto, desc_produto, modelo_produto, preco_compra_produto, preco_venda_produto, qtd , cod_categoria_produto):
        banco.conectar()
        banco.cursor.execute(f"""UPDATE Produto
                                SET desc_produto = ('{desc_produto }') ,
                                modelo_produto = ('{modelo_produto }'),
                                preco_compra_produto = ('{preco_compra_produto }'),
                                preco_venda_produto = ('{preco_venda_produto }'),
                                qtd = ('{qtd }'),
                                cod_categoria_produto = ('{cod_categoria_produto }'), 
                                WHERE cod_produto='{cod_produto}'""")
        banco.conexao.commit()
        banco.desconectar()
   
               
    #mostra todos os produtos
    def listarProduto(self):
        banco.conectar()
        Produto=banco.cursor.execute(f"""SELECT * FROM PRODUTO""").fetchall()   
        print(Produto)   
        banco.desconectar()
        
    #procura um produto   
    def consultarProduto(self, cod_produto): 
        banco.conectar()
        prod = banco.cursor.execute(f"""SELECT cod_produto, desc_produto, modelo_produto,
                          preco_compra_produto, preco_venda_produto, qtd , cod_categoria_produto FROM Produto
                                WHERE cod_produto='{cod_produto}'""").fetchmany()
        print(prod)
        banco.desconectar()  

    #apaga produtos
    def deletarProduto(self, cod_produto):
        banco.conectar()
        banco.cursor.execute(f"""DELETE FROM Produto
                                WHERE cod_produto='{cod_produto}'""")
        banco.conexao.commit()
        banco.desconectar()
        
       
produto2 = Produto('1', 'capa', 'xs max', '20,00', '50,00', 12, 34245)

#fetchall = todos
#fetchmany = alguns