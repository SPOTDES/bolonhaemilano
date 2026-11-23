
from typing import Optional

from cidade import Cidade
from nobreza import Nobreza


class Partida:

    MAXIMO_JOGADORES = 4
    ANO_FINAL = 1410

    def __init__(self) -> None:
        self.cidades: list[Cidade] = []
        self.indiceAtual: int = 0

    def adicionarCidade(self, cidade: Cidade) -> bool:

        if len(self.cidades) >= self.MAXIMO_JOGADORES:
            return False

        self.cidades.append(cidade)

        return True

    def getCidades(self) -> list[Cidade]:
        return self.cidades

    def getCidadeAtual(self) -> Optional[Cidade]:

        if not self.cidades:
            return None

        return self.cidades[self.indiceAtual]

    def getAnoAtual(self) -> int:

        if not self.cidades:
            return 1400

        return self.cidades[0].getAnoAtual()

    def getAnoFinal(self) -> int:
        return self.ANO_FINAL

    def passarTurno(self) -> bool:

        if not self.cidades:
            return False

        self.indiceAtual += 1

        if self.indiceAtual >= len(self.cidades):
            self.indiceAtual = 0
            return True

        return False

    def encerrarAno(self, nobreza: Nobreza) -> list[Cidade]:

        promovidas = []

        for cidade in self.cidades:

            cidade.avancarAno()

            if nobreza.verificarPromocao(cidade):
                promovidas.append(cidade)

        return promovidas

    def terminou(self) -> bool:

        for cidade in self.cidades:
            if cidade.getDono().ehMonarca():
                return True

        return self.getAnoAtual() > self.ANO_FINAL

    def determinarVencedor(
        self,
        nobreza: Nobreza
    ) -> Optional[Cidade]:

        if not self.cidades:
            return None

        vencedor = self.cidades[0]

        for cidade in self.cidades[1:]:

            nivelAtual = cidade.getDono().getNivelTitulo()
            nivelVencedor = vencedor.getDono().getNivelTitulo()

            if nivelAtual > nivelVencedor:
                vencedor = cidade

            elif nivelAtual == nivelVencedor:

                prestigioAtual = nobreza.calcularPrestigio(cidade)
                prestigioVencedor = nobreza.calcularPrestigio(vencedor)

                if prestigioAtual > prestigioVencedor:
                    vencedor = cidade

        return vencedor
