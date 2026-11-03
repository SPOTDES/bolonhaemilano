from jogador import Jogador


class Cidade:

    def __init__(self, nome: str, dono: Jogador) -> None:
        self.nome = nome
        self.anoAtual = 1400
        self.dono = dono

        self.florins = 1000
        self.terras = 10000
        self.graos = 500
        self.servos = 200

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
        print("======================================")