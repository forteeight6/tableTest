# from sys import stdin
import pandas as pd

class testeDeMesa:
    def __init__(self, number_of_variables: int) -> None:
        self.__teste_de_mesa = {}
        self.__teste_de_mesa["LINHA"] = []
        self.__lista_de_variaveis = []
        self.__number_of_variables = number_of_variables
        self.__variavel
        self.__line
        
    @property
    def __variavel(self) -> None:
        for _ in range(self.__number_of_variables):
            variavel = str(input('Digite o nome da variavel: '))
            self.__lista_de_variaveis.append(variavel)
            self.__teste_de_mesa[variavel] = []
        
    @property
    def __line(self) -> None:
        
        while True:
            linha = str(input("Digite o numero da linha: "))
            
            self.__teste_de_mesa["LINHA"].append(linha)
            self.__values()
            
            op = input("x")
            if op == "x":
                break
            
    def __values(self) -> None:
        for variavel in self.__lista_de_variaveis:
            input_or_output = str(input(f"Digite o valor da variavel {variavel}: "))
            self.__teste_de_mesa[variavel].append(input_or_output)
            
        
    def run(self):
        self.df = pd.DataFrame(data=self.__teste_de_mesa)
        return self.df
    

    def html_format(self, local=None):
        if local:
            try:
                self.__save(local, self.df.to_html())
            except e:
                raise e
        return self.df.to_html()
    
    def __save(self, local, info):
        try:    
            with open(local+'.html', 'w') as file:
                file.write(info)
        except:
            with open(local+'.html', 'a') as file:
                file.write(info)
            
        
if __name__ == "__main__":
    teste = testeDeMesa(2)
    print(teste.run())