# from sys import stdin
import pandas as pd

# df = pd.DataFrame(data=teste_de_mesa)
class testeDeMesa:
    def __init__(self, number_of_variables: int) -> None:
        self.__teste_de_mesa = {}
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
        self.__teste_de_mesa["LINHAS"] = []
        while True:
            linha = str(input("Digite o numero da linha: "))
            
            self.__teste_de_mesa["LINHAS"].append(linha)
            self.__values()
            
            op = input("x")
            if op == "x":
                break
            
    def __values(self) -> None:
        for variavel in self.__lista_de_variaveis:
            input_or_output = str(input(f"Digite o valor da variavel {variavel}: "))
            self.__teste_de_mesa[variavel].append(input_or_output)
            
        
    def run(self):
        df = pd.DataFrame(data=self.__teste_de_mesa)
        return df
            
        
if __name__ == "__main__":
    teste = testeDeMesa(2)
    print(teste.run())