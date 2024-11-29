class Carro:
    def _init_(self, marca, modelo, ano, cor, preco):
        self._marca = marca
        self._modelo = modelo
        self._ano = ano
        self._cor = cor
        self._preco = preco
    
    def get_marca(self):
        return self._marca
    
    def set_marca(self, nova_marca):
        self._marca = nova_marca

    def get_modelo(self):
        return self._modelo
    
    def set_modelo(self, nova_modelo):
        self._modelo = nova_modelo

    def get_ano(self):
        return self._ano
    
    def set_ano(self, nova_ano):
        self._ano = nova_ano

    def get_cor(self):
        return self._cor
    
    def set_cor(self, nova_cor):
        self._cor = nova_cor

    def get_preco(self):
        return self._preco
    
    def set_preco(self, nova_preco):
        self._preco = nova_preco

meu_carro = Carro("Toyotta", "carolla", 2020, "preto", 50000) 

print("Marca:", meu_carro.get_marca())
print("Modelo:", meu_carro.get_modelo())
print("Ano:", meu_carro.get_ano())
print("Cor:", meu_carro.get_cor())
print("Preço:", meu_carro.get_preco())

meu_carro.set_modelo('camry')
meu_carro.set_ano(2021)
meu_carro.get_cor('branco')
meu_carro.get_preco('55000')