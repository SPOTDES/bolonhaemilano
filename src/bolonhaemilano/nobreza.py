
from cidade import Cidade
from jogador import Jogador


class Nobreza:

    PESO_CONSTRUCAO = 10
    PESO_SOLDADO = 2
    PESO_SERVO = 1
    HECTARES_POR_PONTO = 100

    PRESTIGIO_MINIMO = (
        0,
        400,
        550,
        700,
        850,
        1000
    )

    def calcularPrestigio(self, cidade: Cidade) -> int:

        prestigio = (
            cidade.getConstrucoes() * self.PESO_CONSTRUCAO
            + cidade.getSoldados() * self.PESO_SOLDADO
            + cidade.getServos() * self.PESO_SERVO
            + cidade.getTerras() // self.HECTARES_POR_PONTO
        )

        return prestigio

    def prestigioParaProximoTitulo(self, jogador: Jogador) -> int:

        if jogador.ehMonarca():
            return -1

        proximoNivel = jogador.getNivelTitulo() + 1

        return self.PRESTIGIO_MINIMO[proximoNivel]

    def verificarPromocao(self, cidade: Cidade) -> bool:

        dono = cidade.getDono()

        necessario = self.prestigioParaProximoTitulo(dono)

        if necessario == -1:
            return False

        prestigio = self.calcularPrestigio(cidade)

        if prestigio >= necessario:
            return dono.promover()

        return False
