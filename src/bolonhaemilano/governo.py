
from cidade import Cidade


class Governo:

    TAXA_MAXIMA = 50

    MULTIPLICADOR_JUSTA = 0.8
    MULTIPLICADOR_MODERADA = 1.0
    MULTIPLICADOR_SEVERA = 1.3

    def arrecadarImpostos(self, cidade: Cidade) -> int:

        base = (
            cidade.getServos() *
            cidade.getTaxaImposto()
        ) // 100

        multiplicador = self.multiplicadorPara(
            cidade.getNivelJustica()
        )

        arrecadado = int(base * multiplicador)

        cidade.adicionarFlorins(arrecadado)

        return arrecadado

    def definirTaxaImposto(
        self,
        cidade: Cidade,
        taxa: int
    ) -> bool:

        if taxa < 0 or taxa > self.TAXA_MAXIMA:
            return False

        cidade.setTaxaImposto(taxa)

        return True

    def definirJustica(
        self,
        cidade: Cidade,
        nivel: str
    ) -> bool:

        niveisValidos = ["Justa", "Moderada", "Severa"]

        if nivel not in niveisValidos:
            return False

        cidade.setNivelJustica(nivel)

        return True

    def multiplicadorPara(self, nivel: str) -> float:

        if nivel == "Justa":
            return self.MULTIPLICADOR_JUSTA

        elif nivel == "Moderada":
            return self.MULTIPLICADOR_MODERADA

        elif nivel == "Severa":
            return self.MULTIPLICADOR_SEVERA

        return self.MULTIPLICADOR_MODERADA
