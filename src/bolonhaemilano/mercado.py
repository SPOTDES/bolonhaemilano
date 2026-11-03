from cidade import Cidade


class Mercado:

    # Valores provisórios para permitir os testes.
    # Os slides exigem preços fixos, mas não informam
    # os valores numéricos oficiais.
    PRECO_GRAO = 2
    PRECO_TERRA = 10

    def getPrecoGrao(self) -> int:
        return self.PRECO_GRAO

    def getPrecoTerra(self) -> int:
        return self.PRECO_TERRA

    def comprarGraos(self, cidade: Cidade, qtd: int) -> bool:
        if qtd <= 0:
            return False

        custo = qtd * self.PRECO_GRAO

        if not cidade.removerFlorins(custo):
            return False

        cidade.adicionarGraos(qtd)
        return True

    def venderGraos(self, cidade: Cidade, qtd: int) -> bool:
        if qtd <= 0:
            return False

        if not cidade.removerGraos(qtd):
            return False

        receita = qtd * self.PRECO_GRAO
        cidade.adicionarFlorins(receita)

        return True

    def comprarTerras(self, cidade: Cidade, qtd: int) -> bool:
        if qtd <= 0:
            return False

        custo = qtd * self.PRECO_TERRA

        if not cidade.removerFlorins(custo):
            return False

        cidade.adicionarTerras(qtd)
        return True

    def venderTerras(self, cidade: Cidade, qtd: int) -> bool:
        if qtd <= 0:
            return False

        if not cidade.removerTerras(qtd):
            return False

        receita = qtd * self.PRECO_TERRA
        cidade.adicionarFlorins(receita)

        return True