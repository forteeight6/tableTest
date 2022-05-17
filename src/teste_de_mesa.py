# from sys import stdin
import pandas as pd

# df = pd.DataFrame(data=teste_de_mesa)
class testeDeMesa:
    def __init__(self, number_of_variables: int) -> None:
        self.__teste_de_mesa = {
            "LINHAS": []
        }
        
        self.__lista_de_variaveis = []
        self.__number_of_variables = number_of_variables
        self.__process
        
    @property
    def __process(self) -> None:

        for _ in range(self.__number_of_variables):
            variavel = str(input('Digite o nome da variavel: '))
            self.__lista_de_variaveis.append(variavel)
            self.__teste_de_mesa[variavel] = []
        
        while True:
            linha = str(input("Digite o nummero da linha: "))
            self.__teste_de_mesa["LINHAS"].append(linha)
            for variavel in self.__lista_de_variaveis:
                input_or_output = str(input(f"Digite o valor da variavel {variavel}: "))
                self.__teste_de_mesa[variavel].append(input_or_output)
                
            op = input("x")
            if op == "x":
                break
            
        
    def run(self):
        df = pd.DataFrame(data=self.__teste_de_mesa)
        return df
            
        
if __name__ == "__main__":
    teste = testeDeMesa(2)
    print(teste.run())
    print('Isto é um segundo teste')