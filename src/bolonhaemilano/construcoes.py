
from cidade import Cidade


class Construcoes:

    PRECO_SOLDADO = 5
    SERVOS_POR_SOLDADO = 1
    PRECO_CONSTRUCAO = 20

    def recrutarSoldados(
        self,
        cidade: Cidade,
        qtd: int
    ) -> bool:

        if qtd <= 0:
            return False

        custo = qtd * self.PRECO_SOLDADO

        servosNecessarios = qtd * self.SERVOS_POR_SOLDADO

        # Validar os dois recursos antes de alterar qualquer um.
        if (
            cidade.getFlorins() < custo
            or cidade.getServos() < servosNecessarios
        ):
            return False

        # Depois de validar, realizar as alterações.
        cidade.removerFlorins(custo)
        cidade.removerServos(servosNecessarios)
        cidade.adicionarSoldados(qtd)

        return True

    def construir(self, cidade: Cidade, qtd: int) -> bool:

        if qtd <= 0:
            return False

        custo = qtd * self.PRECO_CONSTRUCAO

        if not cidade.removerFlorins(custo):
            return False

        cidade.adicionarConstrucoes(qtd)

        return True

    def getPrecoSoldado(self) -> int:
        return self.PRECO_SOLDADO

    def getPrecoConstrucao(self) -> int:
        return self.PRECO_CONSTRUCAO
