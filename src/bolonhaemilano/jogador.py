
class Jogador:

    TITULOS = (
        "Cavaleiro",
        "Barão",
        "Conde",
        "Marquês",
        "Duque",
        "Rei/Rainha"
    )

    def __init__(self, nome: str) -> None:
        self.nome = nome
        self.nivelTitulo = 0

    def getNome(self) -> str:
        return self.nome

    def getTitulo(self) -> str:
        return self.TITULOS[self.nivelTitulo]

    def getNivelTitulo(self) -> int:
        return self.nivelTitulo

    def promover(self) -> bool:
        if self.ehMonarca():
            return False

        self.nivelTitulo += 1
        return True

    def ehMonarca(self) -> bool:
        return self.nivelTitulo == len(self.TITULOS) - 1
