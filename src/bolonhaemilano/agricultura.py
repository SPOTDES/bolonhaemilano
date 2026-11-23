from cidade import Cidade


class Agricultura:

    HECTARES_POR_SERVO = 5
    RENDIMENTO_POR_HECTARE = 2
    SERVOS_POR_GRAO = 5
    CRESCIMENTO_PERCENTUAL = 5
    PERCENTUAL_MINIMO = 20
    PERCENTUAL_MAXIMO = 80


    def processarColheita(self, cidade: Cidade) -> int:

        if cidade.isColheitaFeita():
            return -1

        hectares = min(
            cidade.getTerras(),
            cidade.getServos() * self.HECTARES_POR_SERVO
        )

        sementes = hectares // 2

        if sementes > cidade.getGraos():
            hectares = cidade.getGraos() * 2
            sementes = hectares // 2

        cidade.removerGraos(sementes)

        producao = hectares * self.RENDIMENTO_POR_HECTARE

        cidade.adicionarGraos(producao)

        cidade.marcarColheitaFeita()

        return hectares


    def distribuirAlimentos(
        self,
        cidade: Cidade,
        percentual: int
    ) -> bool:

        if (
            percentual < self.PERCENTUAL_MINIMO
            or percentual > self.PERCENTUAL_MAXIMO
        ):
            return False

        alimentoDistribuido = (
            cidade.getGraos() * percentual
        ) // 100

        cidade.removerGraos(alimentoDistribuido)

        necessidade = cidade.getServos() // self.SERVOS_POR_GRAO

        if alimentoDistribuido >= necessidade:

            crescimento = (
                cidade.getServos() * self.CRESCIMENTO_PERCENTUAL
            ) // 100

            cidade.adicionarServos(crescimento)

        else:

            deficit = necessidade - alimentoDistribuido

            cidade.removerServos(
                min(deficit, cidade.getServos())
            )

        return True