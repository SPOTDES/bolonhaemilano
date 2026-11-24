
import sys

from jogador import Jogador
from cidade import Cidade
from mercado import Mercado
from agricultura import Agricultura
from governo import Governo
from construcoes import Construcoes
from nobreza import Nobreza
from partida import Partida


class Testes:

    aprovados = 0
    reprovados = 0

    @staticmethod
    def verificar(descricao: str, condicao: bool) -> None:

        if condicao:
            Testes.aprovados += 1
            print(f"[OK]    {descricao}")
        else:
            Testes.reprovados += 1
            print(f"[FALHA] {descricao}")

    @staticmethod
    def novaCidade() -> Cidade:
        return Cidade("Bolonha", Jogador("Teste"))

    @staticmethod
    def testarCidade() -> None:

        print("\n-- Cidade --")

        cidade = Testes.novaCidade()

        Testes.verificar(
            "cidade nasce com 1000 florins",
            cidade.getFlorins() == 1000
        )

        Testes.verificar(
            "cidade nasce no ano 1400",
            cidade.getAnoAtual() == 1400
        )

        saldoInicial = cidade.getFlorins()

        resultado = cidade.removerFlorins(2000)

        Testes.verificar(
            "removerFlorins acima do saldo devolve false",
            resultado is False
        )

        Testes.verificar(
            "remocao recusada nao altera o saldo",
            cidade.getFlorins() == saldoInicial
        )

        cidade.marcarColheitaFeita()
        cidade.marcarImpostosArrecadados()

        cidade.avancarAno()

        Testes.verificar(
            "avancarAno soma 1 ao ano",
            cidade.getAnoAtual() == 1401
        )

        Testes.verificar(
            "avancarAno libera colheita e impostos novamente",
            not cidade.isColheitaFeita()
            and not cidade.isImpostosArrecadados()
        )

    @staticmethod
    def testarMercado() -> None:

        print("\n-- Mercado --")

        cidade = Testes.novaCidade()
        mercado = Mercado()

        resultado = mercado.comprarGraos(cidade, 100)

        Testes.verificar(
            "comprar 100 graos da certo",
            resultado is True
        )

        Testes.verificar(
            "comprar 100 graos custa 200 florins",
            cidade.getFlorins() == 800
        )

        Testes.verificar(
            "comprar 100 graos soma 100 unidades",
            cidade.getGraos() == 600
        )

        Testes.verificar(
            "comprar quantidade negativa e recusado",
            mercado.comprarGraos(cidade, -10) is False
        )

        cidadeSemSaldo = Testes.novaCidade()
        cidadeSemSaldo.removerFlorins(900)

        Testes.verificar(
            "comprar sem florins suficientes e recusado",
            mercado.comprarGraos(cidadeSemSaldo, 100) is False
        )

    @staticmethod
    def testarAgricultura() -> None:

        print("\n-- Agricultura --")

        cidade = Testes.novaCidade()
        agricultura = Agricultura()

        hectares = agricultura.processarColheita(cidade)

        Testes.verificar(
            "primeira colheita cultiva 1000 hectares",
            hectares == 1000
        )

        Testes.verificar(
            "colheita deixa 2000 graos",
            cidade.getGraos() == 2000
        )

        Testes.verificar(
            "segunda colheita no mesmo ano devolve -1",
            agricultura.processarColheita(cidade) == -1
        )

        Testes.verificar(
            "distribuir 10 por cento e recusado",
            agricultura.distribuirAlimentos(cidade, 10) is False
        )

    @staticmethod
    def testarGoverno() -> None:

        print("\n-- Governo --")

        cidade = Testes.novaCidade()
        governo = Governo()

        Testes.verificar(
            "taxa de 60 por cento e recusada",
            governo.definirTaxaImposto(cidade, 60) is False
        )

        Testes.verificar(
            "justica Branda e recusada",
            governo.definirJustica(cidade, "Branda") is False
        )

        governo.definirJustica(cidade, "Severa")

        arrecadado = governo.arrecadarImpostos(cidade)

        Testes.verificar(
            "200 servos, 10 por cento, Severa arrecada 26 florins",
            arrecadado == 26
        )

        Testes.verificar(
            "segunda arrecadacao no mesmo ano devolve -1",
            governo.arrecadarImpostos(cidade) == -1
        )

    @staticmethod
    def testarConstrucoes() -> None:

        print("\n-- Construcoes --")

        cidade = Testes.novaCidade()
        construcoes = Construcoes()

        # Deixa somente 50 servos disponíveis.
        cidade.removerServos(150)

        resultado = construcoes.recrutarSoldados(cidade, 100)

        Testes.verificar(
            "recrutar 100 soldados com apenas 50 servos e recusado",
            resultado is False
        )

        Testes.verificar(
            "recrutamento recusado nao debita florins pela metade",
            cidade.getFlorins() == 1000
        )

        resultadoConstrucao = construcoes.construir(cidade, 10)

        Testes.verificar(
            "construir 10 construcoes da certo",
            resultadoConstrucao is True
        )

        Testes.verificar(
            "construir 10 custa 200 florins",
            cidade.getFlorins() == 800
        )

    @staticmethod
    def testarJogadorENobreza() -> None:

        print("\n-- Jogador e Nobreza --")

        jogador = Jogador("Teste")
        cidade = Cidade("Bolonha", jogador)
        nobreza = Nobreza()

        Testes.verificar(
            "jogador comeca como Cavaleiro",
            jogador.getTitulo() == "Cavaleiro"
        )

        Testes.verificar(
            "prestigio inicial e 300",
            nobreza.calcularPrestigio(cidade) == 300
        )

        Testes.verificar(
            "com prestigio 300 nao sobe de titulo",
            nobreza.verificarPromocao(cidade) is False
        )

        cidade.adicionarConstrucoes(50)

        resultado = nobreza.verificarPromocao(cidade)

        Testes.verificar(
            "com 50 construcoes sobe de titulo",
            resultado is True
        )

        Testes.verificar(
            "promocao sobe somente para Barao",
            jogador.getTitulo() == "Barão"
        )

        # Promove até chegar ao último título.
        while jogador.promover():
            pass

        Testes.verificar(
            "promover alem de Rei/Rainha e recusado",
            jogador.promover() is False
        )

    @staticmethod
    def testarPartida() -> None:

        print("\n-- Partida --")

        partida = Partida()
        nobreza = Nobreza()

        jogador1 = Jogador("Ana")
        jogador2 = Jogador("Beto")

        cidade1 = Cidade("Bolonha", jogador1)
        cidade2 = Cidade("Milano", jogador2)

        partida.adicionarCidade(cidade1)
        partida.adicionarCidade(cidade2)

        Testes.verificar(
            "primeiro turno e de Bolonha",
            partida.getCidadeAtual() is cidade1
        )

        Testes.verificar(
            "passar turno de Bolonha nao fecha o ano",
            partida.passarTurno() is False
        )

        Testes.verificar(
            "agora e a vez de Milano",
            partida.getCidadeAtual() is cidade2
        )

        Testes.verificar(
            "passar turno de Milano fecha o ano",
            partida.passarTurno() is True
        )

        partida.encerrarAno(nobreza)

        Testes.verificar(
            "encerrarAno avanca todas as cidades",
            cidade1.getAnoAtual() == 1401
            and cidade2.getAnoAtual() == 1401
        )

        Testes.verificar(
            "partida ainda nao terminou em 1401",
            partida.terminou() is False
        )

        jogador2.promover()

        vencedor = partida.determinarVencedor(nobreza)

        Testes.verificar(
            "vencedor parcial e Milano pelo titulo mais alto",
            vencedor is cidade2
        )

        partidaLimite = Partida()

        for nome in ["Ana", "Beto", "Jogador 3", "Jogador 4"]:
            partidaLimite.adicionarCidade(
                Cidade(nome, Jogador(nome))
            )

        Testes.verificar(
            "quinta cidade e recusada (maximo 4)",
            partidaLimite.adicionarCidade(
                Cidade("Roma", Jogador("Jogador 5"))
            ) is False
        )

    @staticmethod
    def main(args: list[str] | None = None) -> None:

        Testes.aprovados = 0
        Testes.reprovados = 0

        print("===== TESTES BOLONHA E MILANO =====")

        Testes.testarCidade()
        Testes.testarMercado()
        Testes.testarAgricultura()
        Testes.testarGoverno()
        Testes.testarConstrucoes()
        Testes.testarJogadorENobreza()
        Testes.testarPartida()

        print("\n===================================")
        print(
            f"Aprovados: {Testes.aprovados} | "
            f"Reprovados: {Testes.reprovados}"
        )

        if Testes.reprovados > 0:
            raise SystemExit(1)


if __name__ == "__main__":
    Testes.main(sys.argv[1:])
