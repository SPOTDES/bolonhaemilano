import sys
from typing import Optional, TextIO

from cidade import Cidade
from jogador import Jogador


class Menu:

    def __init__(self) -> None:
        self.scanner: TextIO = sys.stdin
        self.emExecucao: bool = True
        self.jogador: Optional[Jogador] = None
        self.cidade: Optional[Cidade] = None

    def executar(self) -> None:
        while self.emExecucao:
            self.exibirOpcoes()
            opcao = self.lerOpcao()
            self.processarOpcao(opcao)

        self.scanner.close()

    def iniciarNovoJogo(self) -> None:
        print("Digite o nome do jogador: ", end="")
        nomeJogador = self.scanner.readline().strip()

        print("Digite o nome da cidade: ", end="")
        nomeCidade = self.scanner.readline().strip()

        self.jogador = Jogador(nomeJogador)
        self.cidade = Cidade(nomeCidade, self.jogador)

        self.cidade.exibirStatus()

    def exibirOpcoes(self) -> None:
        print("\n==========================================")
        print("              BOLONHA E MILANO")
        print("   Um jogo de estratégia econômica medieval")
        print("==========================================")
        print("1 - Novo jogo")
        print("2 - Ver status da cidade")
        print("3 - Sobre o jogo")
        print("0 - Sair")
        print("Escolha uma opção: ", end="")

    def lerOpcao(self) -> int:
        try:
            return int(self.scanner.readline().strip())
        except ValueError:
            return -1

    def processarOpcao(self, opcao: int) -> None:
        if opcao == 1:
            self.iniciarNovoJogo()

        elif opcao == 2:
            if self.cidade is None:
                print("Nenhum jogo foi iniciado.")
            else:
                self.cidade.exibirStatus()

        elif opcao == 3:
            self.exibirSobre()

        elif opcao == 0:
            self.emExecucao = False

        else:
            print("Opção inválida.")

    def exibirSobre(self) -> None:
        print("\nBolonha e Milano é um jogo de estratégia econômica medieval.")
        print("O jogador administra uma cidade-Estado e busca desenvolver seu território.")