
# 🏰 Bolonha e Milano

### Jogo de Estratégia Econômica e Política Medieval

**Projeto de Desenvolvimento — 4º Bimestre**  
**Instituição:** Instituto Federal de São Paulo (IFSP)  
**Disciplina:** Desenvolvimento de Sistemas  
**Professor:** Domingos Bernardo  
**Linguagem:** Python

---

## 📜 Sobre o projeto

Bolonha e Milano é um jogo de estratégia econômica e política ambientado na Itália medieval.

Cada participante governa uma cidade-Estado e precisa administrar seus recursos, desenvolver seu território, arrecadar impostos, investir em construções e organizar sua defesa.

O jogo permite de 1 a 4 participantes na mesma partida, compartilhando o mesmo terminal.

O objetivo é desenvolver a cidade, acumular prestígio e conquistar títulos de nobreza, até alcançar o título de Rei ou Rainha.

A partida termina quando algum governante alcança o título máximo ou quando se encerra o ano de 1410.

## 🎯 Objetivos do jogo

- Administrar uma cidade-Estado medieval.
- Gerenciar recursos econômicos.
- Desenvolver a agricultura e alimentar a população.
- Definir impostos e nível de justiça.
- Recrutar soldados e construir edifícios.
- Acumular prestígio e conquistar títulos de nobreza.
- Competir com outros jogadores pelo título de Rei ou Rainha.

## 👑 Progressão dos títulos

| Título | Prestígio necessário |
|---|---:|
| Cavaleiro | Inicial |
| Barão | 400 |
| Conde | 550 |
| Marquês | 700 |
| Duque | 850 |
| Rei/Rainha | 1000 |

O prestígio é calculado pela seguinte fórmula:

Prestígio = (Construções × 10) + (Soldados × 2) + Servos + (Terras ÷ 100)

Os florins não são considerados diretamente no cálculo.

## 🛠️ Tecnologias utilizadas

- Python: desenvolvimento da lógica do jogo.
- PlantUML: modelagem dos diagramas UML.
- Git: controle de versão.
- GitHub: armazenamento e acompanhamento do projeto.

## 📂 Estrutura do projeto

```text
Bolonha-e-Milano/
│
├── README.md
│
├── src/
│   └── bolonhaemilano/
│       ├── main.py
│       ├── menu.py
│       ├── jogador.py
│       ├── cidade.py
│       ├── mercado.py
│       ├── agricultura.py
│       ├── governo.py
│       ├── construcoes.py
│       ├── partida.py
│       ├── nobreza.py
│       └── testes.py
│
├── uml/
│   ├── diagramas-de-classes
│   └── diagrama-de-sequencia
│
└── casos-de-uso/
    └── diagramas-de-casos-de-uso
```

## ▶️ Como executar

É necessário ter o Python instalado.

Clone o repositório:

```bash
git clone URL_DO_REPOSITORIO
```

Acesse a pasta do projeto:

```bash
cd Bolonha-e-Milano
```

Execute o jogo:

```bash
python src/bolonhaemilano/main.py
```

## 🎮 Como jogar

### Menu principal

| Opção | Funcionalidade |
|---|---|
| 1 | Novo jogo |
| 2 | Ver status da cidade |
| 3 | Mercado |
| 4 | Agricultura |
| 5 | Governo |
| 6 | Construções |
| 7 | Encerrar turno |
| 8 | Ver classificação |
| 9 | Sobre o jogo |
| 0 | Sair |

### Mercado

Permite comprar e vender grãos e terras utilizando florins.

### Agricultura

Permite processar a colheita e distribuir alimentos à população.

A colheita pode ser realizada somente uma vez por ano em cada cidade.

### Governo

Permite arrecadar impostos, modificar a taxa de imposto e definir o nível de justiça.

A arrecadação ocorre somente uma vez por ano em cada cidade.

### Construções

Permite recrutar soldados e construir edifícios, consumindo os recursos necessários.

### Turnos e classificação

Cada jogador realiza suas ações e encerra seu turno. Quando todos finalizam, o ano é encerrado, as cidades são avaliadas e os títulos podem ser atualizados.

A classificação apresenta o prestígio de cada cidade e a meta necessária para o próximo título.

## 🧪 Como executar os testes

O projeto possui uma classe `Testes`, responsável por verificar automaticamente as regras do jogo.

Execute:

```bash
python src/bolonhaemilano/testes.py
```

Os testes verificam as classes Cidade, Mercado, Agricultura, Governo, Construções, Jogador, Nobreza e Partida.

Resultado esperado:

```text
Aprovados: 37 | Reprovados: 0
```

## 📊 Diagramas UML

Os diagramas de classes estão armazenados em `uml/`.

Os diagramas de casos de uso estão armazenados em `casos-de-uso/`.

O diagrama de sequência representa o encerramento do ano, incluindo a passagem de turno, a avaliação das cidades e as promoções de títulos.

## 📅 Etapas de desenvolvimento

| Etapa | Conteúdo |
|---|---|
| 1 | Estrutura inicial, Main e Menu |
| 2 | Classes Jogador e Cidade |
| 3 | Economia: florins, terras e grãos |
| 4 | Agricultura e população |
| 5 | Impostos e governo |
| 6 | Construções e soldados |
| 7 | Rodadas, múltiplos jogadores e vitória |
| 8 | Integração, testes e entrega final |

## 📌 Considerações finais

O projeto aplica conceitos de programação orientada a objetos, modelagem UML, integração entre classes, testes automatizados e controle de versão.

O desenvolvimento foi dividido em oito etapas incrementais, acompanhadas por diagramas e commits individuais.

**Projeto desenvolvido em Python — 4º Bimestre.**
