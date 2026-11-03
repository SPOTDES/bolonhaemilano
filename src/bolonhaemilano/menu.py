import sys
from typing import Optional, TextIO

from cidade import Cidade
from jogador import Jogador
from mercado import Mercado
from agricultura import Agricultura


class Menu:

    def __init__(self) -> None:
        self.scanner: TextIO = sys.stdin
        self.emExecucao: bool = True

        self.jogador: Optional[Jogador] = None
        self.cidade: Optional[Cidade] = None

        self.mercado: Mercado = Mercado()
        self.agricultura: Agricultura = Agricultura()

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
        print("2 - Ver status da cidade")
        print("3 - Mercado")
        print("4 - Agricultura")
        print("5 - Sobre o jogo")
        print("0 - Sair")
        print("Escolha uma opção: ", end="", flush=True)

    def lerOpcao(self) -> int:
        try:
            return int(self.scanner.readline().strip())
        except ValueError:
            return -1

    def processarOpcao(self, opcao: int) -> None:
        if opcao == 1:
            self.iniciarNovoJogo()

        elif opcao == 2:
            self.exibirStatus()

        elif opcao == 3:
            self.abrirMercado()

        elif opcao == 4:
            self.abrirAgricultura()

        elif opcao == 5:
            self.exibirSobre()

        elif opcao == 0:
            self.emExecucao = False

        else:
            print("Opção inválida.")

    def iniciarNovoJogo(self) -> None:
        print("Digite o nome do jogador: ", end="", flush=True)
        nomeJogador = self.scanner.readline().strip()

        print("Digite o nome da cidade: ", end="", flush=True)
        nomeCidade = self.scanner.readline().strip()

        self.jogador = Jogador(nomeJogador)
        self.cidade = Cidade(nomeCidade, self.jogador)

        self.exibirStatus()

    def exibirStatus(self) -> None:
        if self.cidade is None:
            print("Nenhum jogo foi iniciado.")
        else:
            self.cidade.exibirStatus()

    def abrirMercado(self) -> None:
        if self.cidade is None:
            print("Nenhum jogo foi iniciado.")
            return

        noMercado = True

        while noMercado:
            print("\n========== MERCADO ==========")
            print(f"Preço do grão: {self.mercado.getPrecoGrao()} florins")
            print(f"Preço da terra: {self.mercado.getPrecoTerra()} florins")
            print(f"Florins disponíveis: {self.cidade.getFlorins()}")
            print("1 - Comprar grãos")
            print("2 - Vender grãos")
            print("3 - Comprar terras")
            print("4 - Vender terras")
            print("0 - Voltar")
            print("Escolha uma opção: ", end="", flush=True)

            opcao = self.lerOpcao()

            if opcao == 1:
                self.comprarGraos()

            elif opcao == 2:
                self.venderGraos()

            elif opcao == 3:
                self.comprarTerras()

            elif opcao == 4:
                self.venderTerras()

            elif opcao == 0:
                noMercado = False

            else:
                print("Opção inválida.")

    def lerQuantidade(self) -> int:
        print("Digite a quantidade: ", end="", flush=True)

        try:
            return int(self.scanner.readline().strip())
        except ValueError:
            return -1

    def comprarGraos(self) -> None:
        qtd = self.lerQuantidade()

        if self.mercado.comprarGraos(self.cidade, qtd):
            print("Compra de grãos realizada com sucesso!")
        else:
            print("Não foi possível comprar grãos.")

    def venderGraos(self) -> None:
        qtd = self.lerQuantidade()

        if self.mercado.venderGraos(self.cidade, qtd):
            print("Venda de grãos realizada com sucesso!")
        else:
            print("Não foi possível vender grãos.")

    def comprarTerras(self) -> None:
        qtd = self.lerQuantidade()

        if self.mercado.comprarTerras(self.cidade, qtd):
            print("Compra de terras realizada com sucesso!")
        else:
            print("Não foi possível comprar terras.")

    def venderTerras(self) -> None:
        qtd = self.lerQuantidade()

        if self.mercado.venderTerras(self.cidade, qtd):
            print("Venda de terras realizada com sucesso!")
        else:
            print("Não foi possível vender terras.")

    def abrirAgricultura(self) -> None:
        if self.cidade is None:
            print("Nenhum jogo foi iniciado.")
            return

        naAgricultura = True

        while naAgricultura:
            print("\n========== AGRICULTURA ==========")
            print(f"Terras: {self.cidade.getTerras()} hectares")
            print(f"Servos: {self.cidade.getServos()}")
            print(f"Grãos: {self.cidade.getGraos()}")
            print("1 - Colher (processar safra)")
            print("2 - Distribuir alimentos")
            print("0 - Voltar")
            print("Escolha uma opção: ", end="", flush=True)

            opcao = self.lerOpcao()

            if opcao == 1:
                self.colher()

            elif opcao == 2:
                self.distribuirAlimentos()

            elif opcao == 0:
                naAgricultura = False

            else:
                print("Opção inválida.")

    def colher(self) -> None:
        hectares = self.agricultura.processarColheita(self.cidade)

        print(f"Colheita realizada em {hectares} hectares.")

    def distribuirAlimentos(self) -> None:
        print("Digite o percentual de distribuição (20 a 80): ",
              end="", flush=True)

        percentual = self.lerOpcao()

        if self.agricultura.distribuirAlimentos(
            self.cidade,
            percentual
        ):
            print("Distribuição de alimentos realizada com sucesso!")
        else:
            print("Percentual inválido. Utilize um valor entre 20 e 80.")

    def exibirSobre(self) -> None:
        print("\nBolonha e Milano é um jogo de estratégia econômica medieval.")
        print("O jogador administra uma cidade-Estado e busca desenvolver seu território.")