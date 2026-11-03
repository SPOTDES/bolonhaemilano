from jogador import Jogador


class Cidade:

    def __init__(self, nome: str, dono: Jogador) -> None:
        self.nome = nome
        self.anoAtual = 1400
        self.dono = dono

    def avancarAno(self) -> None:
        self.anoAtual += 1

    def exibirStatus(self) -> None:
        print("\n--- Status da cidade ---")
        print(f"Cidade: {self.nome}")
        print(f"Governante: {self.dono.getNome()}")
        print(f"Ano atual: {self.anoAtual}")