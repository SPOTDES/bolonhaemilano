
import sys
from typing import Optional, TextIO

from cidade import Cidade
from jogador import Jogador
from mercado import Mercado
from agricultura import Agricultura
from governo import Governo
from construcoes import Construcoes
from nobreza import Nobreza
from partida import Partida


class Menu:

    def __init__(self) -> None:
        self.scanner: TextIO = sys.stdin
        self.emExecucao: bool = True

        self.partida: Optional[Partida] = None
        self.cidade: Optional[Cidade] = None

        self.mercado: Mercado = Mercado()
        self.agricultura: Agricultura = Agricultura()
        self.governo: Governo = Governo()
        self.construcoes: Construcoes = Construcoes()
        self.nobreza: Nobreza = Nobreza()

    def executar(self) -> None:
        while self.emExecucao:
            self.exibirOpcoes()
            opcao = self.lerOpcao()
            self.processarOpcao(opcao)

        self.scanner.close()

    def exibirOpcoes(self) -> None:
        print("\n==========================================")
        print("              BOLONHA E MILANO")

        if self.partida is not None and self.cidade is not None:
            jogador = self.cidade.getDono()

            print(f"Ano atual: {self.partida.getAnoAtual()}")
            print(
                f"Vez de: {jogador.getNome()} "
                f"({jogador.getTitulo()}), "
                f"de {self.cidade.getNome()}"
            )
        else:
            print("Nenhuma partida em andamento.")

        print("==========================================")
        print("1 - Novo jogo")
        print("2 - Ver status da cidade")
        print("3 - Mercado")
        print("4 - Agricultura")
        print("5 - Governo")
        print("6 - Construções")
        print("7 - Encerrar turno")
        print("8 - Ver classificação")
        print("9 - Sobre o jogo")
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
            self.abrirGoverno()

        elif opcao == 6:
            self.abrirConstrucoes()

        elif opcao == 7:
            self.encerrarTurno()

        elif opcao == 8:
            self.exibirClassificacao()

        elif opcao == 9:
            self.exibirSobre()

        elif opcao == 0:
            self.emExecucao = False

        else:
            print("Opção inválida.")

    def iniciarNovoJogo(self) -> None:
        print("Quantos jogadores (1 a 4)? ", end="", flush=True)

        quantidadeJogadores = self.lerOpcao()

        if quantidadeJogadores < 1 or quantidadeJogadores > 4:
            quantidadeJogadores = 2

        cidadesPadrao = [
            "Bolonha",
            "Milano",
            "Florença",
            "Veneza"
        ]

        novaPartida = Partida()

        for i in range(quantidadeJogadores):

            numeroJogador = i + 1

            print(
                f"Nome do jogador {numeroJogador}: ",
                end="",
                flush=True
            )

            nomeJogador = self.scanner.readline().strip()

            if not nomeJogador:
                nomeJogador = f"Jogador {numeroJogador}"

            print(
                f"Nome da cidade de {nomeJogador} "
                f"(Enter = {cidadesPadrao[i]}): ",
                end="",
                flush=True
            )

            nomeCidade = self.scanner.readline().strip()

            if not nomeCidade:
                nomeCidade = cidadesPadrao[i]

            jogador = Jogador(nomeJogador)
            cidade = Cidade(nomeCidade, jogador)

            novaPartida.adicionarCidade(cidade)

        self.partida = novaPartida
        self.cidade = self.partida.getCidadeAtual()

        print("\nNovo jogo iniciado!")
        print(
            "Ano 1400. A partida vai ate o fim de 1410 "
            "ou ate alguem virar Rei/Rainha."
        )

        jogadorInicial = self.cidade.getDono()

        print(
            f"Comeca: {jogadorInicial.getNome()} "
            f"({jogadorInicial.getTitulo()}), "
            f"de {self.cidade.getNome()}."
        )

        self.exibirStatus()

    def exibirStatus(self) -> None:
        if self.partida is None:
            print("Nenhum jogo em andamento.")
            return

        self.cidade = self.partida.getCidadeAtual()
        self.cidade.exibirStatus()

    def abrirMercado(self) -> None:
        if self.partida is None:
            print("Nenhum jogo em andamento.")
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
        if self.partida is None:
            print("Nenhum jogo em andamento.")
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

        if hectares == -1:
            print("A colheita deste ano já foi realizada.")
        else:
            print(f"Colheita realizada em {hectares} hectares.")

    def distribuirAlimentos(self) -> None:
        print(
            "Digite o percentual de distribuição (20 a 80): ",
            end="",
            flush=True
        )

        percentual = self.lerOpcao()

        if self.agricultura.distribuirAlimentos(
            self.cidade,
            percentual
        ):
            print("Distribuição de alimentos realizada com sucesso!")
        else:
            print("Percentual inválido. Utilize um valor entre 20 e 80.")

    def abrirGoverno(self) -> None:
        if self.partida is None:
            print("Nenhum jogo em andamento.")
            return

        noGoverno = True

        while noGoverno:
            print("\n========== GOVERNO ==========")
            print(f"Florins disponíveis: {self.cidade.getFlorins()}")
            print(f"Taxa de imposto: {self.cidade.getTaxaImposto()}%")
            print(f"Nível de justiça: {self.cidade.getNivelJustica()}")
            print("1 - Arrecadar impostos")
            print("2 - Definir taxa de imposto")
            print("3 - Definir nível de justiça")
            print("0 - Voltar")
            print("Escolha uma opção: ", end="", flush=True)

            opcao = self.lerOpcao()

            if opcao == 1:
                self.arrecadarImpostos()

            elif opcao == 2:
                self.definirTaxaImposto()

            elif opcao == 3:
                self.definirJustica()

            elif opcao == 0:
                noGoverno = False

            else:
                print("Opção inválida.")

    def arrecadarImpostos(self) -> None:
        arrecadado = self.governo.arrecadarImpostos(self.cidade)

        if arrecadado == -1:
            print("Os impostos deste ano já foram arrecadados.")
        else:
            print(f"Impostos arrecadados: {arrecadado} florins.")

    def definirTaxaImposto(self) -> None:
        print(
            "Digite a taxa de imposto (0 a 50): ",
            end="",
            flush=True
        )

        taxa = self.lerOpcao()

        if self.governo.definirTaxaImposto(self.cidade, taxa):
            print("Taxa de imposto atualizada com sucesso!")
        else:
            print("Taxa inválida. Utilize um valor entre 0 e 50.")

    def definirJustica(self) -> None:
        print("\nEscolha o nível de justiça:")
        print("1 - Justa")
        print("2 - Moderada")
        print("3 - Severa")
        print("Escolha uma opção: ", end="", flush=True)

        opcao = self.lerOpcao()

        niveis = {
            1: "Justa",
            2: "Moderada",
            3: "Severa"
        }

        nivel = niveis.get(opcao)

        if nivel is None:
            print("Opção de justiça inválida.")
            return

        if self.governo.definirJustica(self.cidade, nivel):
            print("Nível de justiça atualizado com sucesso!")

    def abrirConstrucoes(self) -> None:
        if self.partida is None:
            print("Nenhum jogo em andamento.")
            return

        naConstrucoes = True

        while naConstrucoes:
            print("\n========== CONSTRUÇÕES ==========")
            print(f"Florins: {self.cidade.getFlorins()}")
            print(f"Servos: {self.cidade.getServos()}")
            print(f"Soldados: {self.cidade.getSoldados()}")
            print(f"Construções: {self.cidade.getConstrucoes()}")
            print("1 - Recrutar soldados")
            print("2 - Construir")
            print("0 - Voltar")
            print("Escolha uma opção: ", end="", flush=True)

            opcao = self.lerOpcao()

            if opcao == 1:
                self.recrutarSoldados()

            elif opcao == 2:
                self.construir()

            elif opcao == 0:
                naConstrucoes = False

            else:
                print("Opção inválida.")

    def recrutarSoldados(self) -> None:
        qtd = self.lerQuantidade()

        if self.construcoes.recrutarSoldados(self.cidade, qtd):
            print("Soldados recrutados com sucesso!")
        else:
            print("Não foi possível recrutar soldados.")

    def construir(self) -> None:
        qtd = self.lerQuantidade()

        if self.construcoes.construir(self.cidade, qtd):
            print("Construção realizada com sucesso!")
        else:
            print("Não foi possível construir.")


    def encerrarTurno(self) -> None:
        if self.partida is None:
            print("Nenhum jogo em andamento.")
            return

        anoTerminou = self.partida.passarTurno()

        if anoTerminou:

            anoEncerrado = self.partida.getAnoAtual()

            promovidas = self.partida.encerrarAno(self.nobreza)

            print(f"\n========== FIM DO ANO {anoEncerrado} ==========")

            for cidadePromovida in promovidas:
                dono = cidadePromovida.getDono()

                print(
                    f"{dono.getNome()}, de {cidadePromovida.getNome()}, "
                    f"agora é {dono.getTitulo()}!"
                )

            self.exibirClassificacao()

            if self.partida.terminou():
                self.encerrarPartida()
                return

            print(f"\nComeça o ano {self.partida.getAnoAtual()}.")

        else:
            print("\nTurno encerrado.")

        self.cidade = self.partida.getCidadeAtual()

        jogador = self.cidade.getDono()

        print(
            f"Agora é a vez de {jogador.getNome()} "
            f"({jogador.getTitulo()}), de {self.cidade.getNome()}."
        )


    def exibirClassificacao(self) -> None:
        if self.partida is None:
            print("Nenhum jogo em andamento.")
            return

        print("\n----------- CLASSIFICAÇÃO -----------")

        for cidade in self.partida.getCidades():

            dono = cidade.getDono()

            prestigio = self.nobreza.calcularPrestigio(cidade)

            proximoTitulo = (
                self.nobreza.prestigioParaProximoTitulo(dono)
            )

            print(
                f"{cidade.getNome()} | "
                f"{dono.getNome()} ({dono.getTitulo()}) | "
                f"prestígio {prestigio}"
            )

            if proximoTitulo == -1:
                print("    Título máximo alcançado.")
            else:
                faltam = max(0, proximoTitulo - prestigio)

                print(
                    f"    Próximo título com {proximoTitulo} "
                    f"(faltam {faltam})"
                )

        print("-------------------------------------")

    def encerrarPartida(self) -> None:

        vencedor = self.partida.determinarVencedor(self.nobreza)

        print("\n========== FIM DE JOGO ==========")

        if vencedor is not None:

            dono = vencedor.getDono()

            prestigio = self.nobreza.calcularPrestigio(vencedor)

            print(f"Vencedor: {dono.getNome()}")
            print(f"Cidade: {vencedor.getNome()}")
            print(f"Título: {dono.getTitulo()}")
            print(f"Prestígio: {prestigio}")

        print("================================")

        self.partida = None
        self.cidade = None

    def exibirSobre(self) -> None:
        print("\nBolonha e Milano é um jogo de estratégia econômica medieval.")
        print("Cada jogador governa uma cidade-Estado.")
        print("O objetivo é desenvolver sua cidade e conquistar títulos de nobreza.")
        print("A partida termina quando alguém chega a Rei/Rainha ou ao fim de 1410.")
