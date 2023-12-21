# Classe ListaNotas

class ListaNotas(AnaliseDados):
    
    def __init__(self, lista_notas=None):
        super().__init__(type(float))
        if lista_notas is None:
            lista_notas = []
        self.__lista = np.array(lista_notas)
    
    def entradaDeDados(self, nota):
        self.__lista = np.append(self.__lista, nota)

    def mostraMediana(self):
        mediana = np.median(self.__lista)
        return mediana

    def mostraMenor(self):
        menor = np.min(self.__lista)
        return menor

    def mostraMaior(self):
        maior = np.max(self.__lista)
        return maior

    def listarEmOrdem(self):
        lista_ordenada = np.sort(self.__lista)
        return lista_ordenada

    def __iter__(self):
        return iter(self.__lista)

    def __str__(self):
        return '\n'.join(str(nota) for nota in self.__lista)
