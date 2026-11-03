import sys
from typing import TextIO


class Menu:

    def __init__(self) -> None:
        self.scanner: TextIO = sys.stdin
        self.emExecucao: bool = True

    def executar(self) -> None:
        while self.emExecucao:
            self.exibirOpcoes()
            opcao = self.lerOpcao()
            self.processarOpcao(opcao)

        self.scanner.close()

    def exibirOpcoes(self) -> None:
        print("\n==========================================")
        print("              BOLONHA E MILANO")
        print("   Um jogo de estratégia econômica medieval")
        print("==========================================")
        print("1 - Novo jogo")
        print("2 - Sobre o jogo")
        print("0 - Sair")
        print("Escolha uma opção: ", end="")

    def lerOpcao(self) -> int:
        try:
            return int(self.scanner.readline().strip())
        except ValueError:
            return -1

    def processarOpcao(self, opcao: int) -> None:
        if opcao == 1:
            print("\nNovo jogo será implementado na Etapa 2.")

        elif opcao == 2:
            self.exibirSobre()

        elif opcao == 0:
            self.emExecucao = False

        else:
            print("Opção inválida.")

    def exibirSobre(self) -> None:
        print("\nBolonha e Milano é um jogo de estratégia econômica medieval.")
        print("O jogador administra uma cidade-Estado e busca desenvolver seu território.")