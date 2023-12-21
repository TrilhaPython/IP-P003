from abc import ABC, abstractmethod
import statistics

class AnaliseDados(ABC):
    @abstractmethod
    def __init__(self, tipoDeDados):
        self.__tipoDeDados = tipoDeDados

    @abstractmethod
    def entradaDeDados(self):
        pass

    @abstractmethod
    def mostraMediana(self):
        pass
    
    @abstractmethod
    def mostraMenor(self):
        pass

    @abstractmethod
    def mostraMaior(self):
        pass
    
    @abstractmethod
    def listarEmOrdem(self):
        pass
    
    def mediaAritmetica(self):
        return statistics.mean(self.__tipoDeDados)

    def mediaGeometrica(self):
        return statistics.geometric_mean(self.__tipoDeDados)

    def mediaHarmonica(self):
        return statistics.harmonic_mean(self.__tipoDeDados)

    def mediana(self):
        return statistics.median(self.__tipoDeDados)

    def medianaInferior(self):
        return statistics.median_low(self.__tipoDeDados)

    def medianaSuperior(self):
        return statistics.median_high(self.__tipoDeDados)

    def desvioPadraoPopulacional(self):
        return statistics.pstdev(self.__tipoDeDados)

    def varianciaPopulacional(self):
        return statistics.pvariance(self.__tipoDeDados)

    def desvioPadraoAmostral(self):
        return statistics.stdev(self.__tipoDeDados)

    def varianciaAmostral(self):
        return statistics.variance(self.__tipoDeDados)

