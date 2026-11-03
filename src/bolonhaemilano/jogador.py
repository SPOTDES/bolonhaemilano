class Jogador:

    def __init__(self, nome: str) -> None:
        self.nome = nome
        self.titulo = "Cavaleiro"

    def getNome(self) -> str:
        return self.nome

    def getTitulo(self) -> str:
        return self.titulo

    def setTitulo(self, titulo: str) -> None:
        self.titulo = titulo