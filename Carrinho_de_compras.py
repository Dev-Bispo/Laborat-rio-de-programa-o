class Carrinho_de_compras:
    def __init__(self):
        self.total_preco = 0.0
        self.quantidade = 0
        self.compra = False
        self.finalizado = 0
        self.mercadoria = 0        
        self.mercado =  {"feijao":5.50,"arroz":25.00,"oleo":18.00,"farinha":14.60,"miojo":3.40,"macarrao":5.00, "suco":2.40 }          
        self.adicao = False   
        self.retirada = False
           
    def operacao(self):
        print("Produtos disponiveis:\n")
        
        for pro, pre in self.mercado.items():            
            print( f"{pro} : {pre} " )
          
        self.confirmacao1 = input("Deseja comprar algo?(s/n):" )  
          
        if self.confirmacao1 == "s":
            self.execucao = True   
                   
            while self.execucao is True:
                
                self.escolhas = {}
                self.produtos = input("Digite o produto que deseja: ")
                self.quantidade = input("quantidade: ")
                self.escolhas[self.produtos] = self.quantidade
                self.confirmacao2 = input("gostaria de mais algo?s/n")
                 
                if self.confirmacao2 == "n": 
                    self.retirada = False   
                    self.execucao = False  
                    self.adicao = False
                    self.compra = True  
                            
                         
                    
                   
                    
                elif self.confirmacao2 == "s":
                        self.confirmacao2 = int(input("Adicionar mais item(1)\nRetirar item(2)\nFinalizar compra(3)"))
                        if self.confirmacao2 == 1:
                            self.retirada = False  
                            self.execucao = False  
                            self.adicao = True
                            self.compra = False 
                        
                        elif self.confirmacao2 == 2:
                            self.retirada = True  
                            self.execucao = False  
                            self.adicao = False
                            self.compra = False 
                            
                        elif self.confirmacao2 == 3:
                         
                             self.retirada = False   
                             self.execucao = False  
                             self.adicao = False
                             self.compra = True       
                          
                
                   
        else: 
            self.execucao = False                           
            
          
     
    def retirar(self): 
        
            if self.retirada == True:
                
                while self.retirada is not False: 

                    self.tirar = input("Qual item deseja retirar?")
                    
                    for pro, pre in self.mercado.items():
                        
                        if self.tirar.lower() == pro:                                 
                            self.quantidade_retirada = int(input("Quantos deseja retirar?"))
                            self.escolhas[self.produtos]  = int(self.escolhas.get(self.produtos, (self.quantidade)))- int(self.quantidade_retirada) 
                            
                    self.confirmacao3 = input("Deseja retirar mais algo?s/n")       
                    if self.confirmacao3 == "n":
                        self.confirmacao4 = int(input("Adicionar mais item(1)\n Retirar item(2)\n Finalizar compra(3)\n\n"))
                     
                        if self.confirmacao4 == 1:
                           self.adicao = True
                           self.compra = False
                           self.retirada = False
                           
                        elif self.confirmacao4 == 2:
                           self.adicao = False
                           self.compra = False
                           self.retirada = True
                           
                        elif self.confirmacao4 == 3:
                           self.adicao = False
                           self.compra = True
                           self.retirada = False        
                         
                    else:
                         self.adicao = False
                         self.compra = False
                         self.retirada = True
                        
               
                                       
    def adicionar(self):
        
        if self.adicao == True:
            
            while self.adicao is not False:
                     
                       self.produtos = input("Digite o produto que deseja: ")
                       self.quantidade = input("quantidade: ")
                       self.escolhas[self.produtos] = self.quantidade   
                       self.confirmacao4 = int(input("Adicionar mais item(1)\n Retirar item(2)\n Finalizar compra(3)\n\n"))
                       
                       if self.confirmacao4 == 1:
                           self.adicao = True
                           self.compra = False
                           self.retirada = False
                           
                       elif self.confirmacao4 == 2:
                           self.adicao = False
                           self.compra = False
                           self.retirada = True
                           
                       elif self.confirmacao4 == 3:
                           self.adicao = False
                           self.compra = True
                           self.retirada = False        
                         
    def confirmacao(self):
        
        if self.compra == True:
            for it, to in self.escolhas.items():
                        
                        for pro, pre in self.mercado.items():
                            
                            if it == pro:
                                print(to, pre)
                                self.total_preco = float(to) * float(pre) 
 
            print(f"Compra finalizada\n Valor da compra:{self.total_preco:.2f}\n Itens: {self.escolhas}  ")  
            self.execucao = False
            self.adicao = False
            self.compra = False
            self.retirada = False                      
                            
                      
                                           
              
                                     
           
                               
                           
             
            
                
            
carrinho = Carrinho_de_compras()
carrinho.operacao()
carrinho.retirar() 
carrinho.adicionar()
carrinho.confirmacao()    
            
           
      
    