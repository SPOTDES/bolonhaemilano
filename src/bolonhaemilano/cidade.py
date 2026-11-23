
from jogador import Jogador


class Cidade:

    # Constantes de valores iniciais
    ANO_INICIAL = 1400
    FLORINS_INICIAIS = 1000
    TERRAS_INICIAIS = 10000
    GRAOS_INICIAIS = 500
    SERVOS_INICIAIS = 200
    TAXA_IMPOSTO_INICIAL = 10
    NIVEL_JUSTICA_INICIAL = "Moderada"

    def __init__(self, nome: str, dono: Jogador) -> None:
        self.nome = nome
        self.anoAtual = self.ANO_INICIAL
        self.dono = dono

        self.florins = self.FLORINS_INICIAIS
        self.terras = self.TERRAS_INICIAIS
        self.graos = self.GRAOS_INICIAIS
        self.servos = self.SERVOS_INICIAIS

        self.taxaImposto = self.TAXA_IMPOSTO_INICIAL
        self.nivelJustica = self.NIVEL_JUSTICA_INICIAL

    def getNome(self) -> str:
        return self.nome

    def getAnoAtual(self) -> int:
        return self.anoAtual

    def getDono(self) -> Jogador:
        return self.dono

    def getFlorins(self) -> int:
        return self.florins

    def getTerras(self) -> int:
        return self.terras

    def getGraos(self) -> int:
        return self.graos

    def getServos(self) -> int:
        return self.servos

    def getTaxaImposto(self) -> int:
        return self.taxaImposto

    def setTaxaImposto(self, taxa: int) -> None:
        self.taxaImposto = taxa

    def getNivelJustica(self) -> str:
        return self.nivelJustica

    def setNivelJustica(self, nivel: str) -> None:
        self.nivelJustica = nivel

    def avancarAno(self) -> None:
        self.anoAtual += 1

    def adicionarFlorins(self, qtd: int) -> None:
        if qtd > 0:
            self.florins += qtd

    def removerFlorins(self, qtd: int) -> bool:
        if qtd <= 0 or self.florins < qtd:
            return False

        self.florins -= qtd
        return True

    def adicionarTerras(self, qtd: int) -> None:
        if qtd > 0:
            self.terras += qtd

    def removerTerras(self, qtd: int) -> bool:
        if qtd <= 0 or self.terras < qtd:
            return False

        self.terras -= qtd
        return True

    def adicionarGraos(self, qtd: int) -> None:
        if qtd > 0:
            self.graos += qtd

    def removerGraos(self, qtd: int) -> bool:
        if qtd <= 0 or self.graos < qtd:
            return False

        self.graos -= qtd
        return True

    def adicionarServos(self, qtd: int) -> None:
        if qtd > 0:
            self.servos += qtd

    def removerServos(self, qtd: int) -> bool:
        if qtd <= 0 or self.servos < qtd:
            return False

        self.servos -= qtd
        return True

    def exibirStatus(self) -> None:
        print("\n========== STATUS DA CIDADE ==========")
        print(f"Cidade: {self.nome}")
        print(f"Governante: {self.dono.getNome()}")
        print(f"Ano atual: {self.anoAtual}")
        print(f"Florins: {self.florins}")
        print(f"Terras: {self.terras} hectares")
        print(f"Grãos: {self.graos} unidades")
        print(f"Servos: {self.servos}")
        print(f"Taxa de imposto: {self.taxaImposto}%")
        print(f"Nível de justiça: {self.nivelJustica}")
        print("======================================")
