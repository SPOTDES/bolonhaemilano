# 🏰 Bolonha e Milano

### Jogo de Estratégia Econômica Medieval

**Projeto de Desenvolvimento — 4º Bimestre**  
**Disciplina:** Desenvolvimento de Sistemas  
**Professor:** Domingos Bernardo  
**Linguagem de programação:** Python

---

## 📜 Sobre o projeto

Bolonha e Milano é um jogo de estratégia econômica e política ambientado na Itália medieval. O jogador assume o papel de governante de uma cidade-Estado e precisa administrar seus recursos, desenvolver seu território e tomar decisões estratégicas para conquistar títulos de nobreza.

Ao longo do jogo, será necessário equilibrar aspectos como agricultura, alimentação, economia, comércio, impostos, construções e defesa territorial.

O objetivo final é desenvolver a cidade e conquistar progressivamente os títulos de nobreza, chegando ao título de **Rei ou Rainha**.

O projeto será desenvolvido de maneira incremental, dividido em oito etapas, aplicando conceitos de programação orientada a objetos, modelagem UML e organização de código com Git e GitHub.

## 🎯 Objetivos do jogo

- Administrar uma cidade-Estado medieval.
- Gerenciar recursos e desenvolver o território.
- Tomar decisões econômicas e políticas.
- Equilibrar produção agrícola, população e comércio.
- Investir em construções e defesa.
- Evoluir na hierarquia de títulos de nobreza.
- Alcançar o título de Rei ou Rainha.

## ⚔️ Recursos administrados

Durante o desenvolvimento do jogo, serão trabalhados recursos como:

| Recurso | Função |
|---|---|
| Florins | Financiar compras, investimentos e construções. |
| Grãos | Alimentar a população e reservar sementes para a agricultura. |
| Terras | Determinar o espaço disponível para produção agrícola. |
| Servos | Fornecer mão de obra. |
| Soldados | Manter a capacidade de defesa. |
| Mercadores | Participar das atividades comerciais. |
| Clero | Fortalecer a influência religiosa. |
| Nobres | Fortalecer o prestígio político. |
| Mercados | Expandir o comércio. |
| Moinhos de lã | Desenvolver a atividade produtiva. |
| Palácios | Aumentar o prestígio político. |
| Catedrais | Ampliar a influência religiosa. |

## 👑 Progressão dos títulos

A evolução política do governante acontece por meio de oito títulos:

1. Cavaleiro
2. Barão
3. Conde
4. Marquês
5. Duque
6. Grão-Duque
7. Príncipe
8. Rei / Rainha

A conquista dos títulos estará relacionada ao desenvolvimento geral do território e aos requisitos estabelecidos pelas regras do jogo.

## 🛠️ Tecnologias utilizadas

- **Python:** desenvolvimento da lógica e funcionamento do jogo.
- **PlantUML:** criação dos diagramas UML.
- **Git:** controle de versão do projeto.
- **GitHub:** armazenamento e acompanhamento do desenvolvimento.

## 📂 Estrutura do projeto

```text
Bolonha-e-Milano/
│
├── README.md
│
├── src/
│   └── bolonhaemilano/
│       ├── main.py
│       └── menu.py
│
├── uml/
│   └── etapa-1-diagrama-de-classes.puml
│
└── casos-de-uso/
```

### Organização das pastas

- **src/bolonhaemilano/:** contém os arquivos Python e as classes responsáveis pelo funcionamento do jogo.
- **uml/:** armazena os diagramas de classes desenvolvidos em PlantUML.
- **casos-de-uso/:** destinada aos diagramas de casos de uso.
- **README.md:** documentação geral do projeto.

## 📅 Etapas de desenvolvimento

O projeto será desenvolvido em oito etapas incrementais:

| Etapa | Desenvolvimento |
|---|---|
| 1 | Estrutura inicial, Main e Menu |
| 2 | Classes Jogador e Cidade |
| 3 | Economia: florins, terras e grãos |
| 4 | Agricultura e população |
| 5 | Impostos e governo |
| 6 | Construções e soldados |
| 7 | Rodadas, múltiplos jogadores e vitória |
| 8 | Integração, testes e entrega final |

Cada etapa acrescentará novas funcionalidades ao projeto, mantendo a estrutura e os diagramas UML atualizados.

## 💻 Etapa 1 — Estrutura inicial, Main e Menu

Nesta primeira etapa, foi desenvolvida a estrutura inicial do programa, estabelecendo o ponto de entrada e o menu principal.

Foram implementadas duas classes:

**Main**
- Responsável pelo ponto de entrada do programa.
- Cria um objeto da classe Menu.
- Chama o método responsável por executar o menu.

**Menu**
- Apresenta as opções disponíveis no terminal.
- Realiza a leitura e validação das entradas.
- Controla o laço principal de execução.
- Processa as opções escolhidas pelo usuário.
- Apresenta informações sobre o jogo.
- Encerra a execução quando o usuário seleciona a opção de saída.

### Menu principal

```text
==========================================
              BOLONHA E MILANO
   Um jogo de estratégia econômica medieval
==========================================
1 - Novo jogo
2 - Sobre o jogo
0 - Sair
Escolha uma opção:
```

Nesta etapa, a opção Novo jogo apresenta uma mensagem informando que sua implementação será realizada na Etapa 2.

O menu permanece em execução até que o usuário escolha a opção de saída. Entradas inválidas são tratadas sem interromper o funcionamento do programa.

## ▶️ Como executar o projeto

É necessário ter o Python instalado na máquina.

Clone o repositório:

```bash
git clone URL_DO_REPOSITORIO
```

Acesse a pasta do projeto:

```bash
cd Bolonha-e-Milano
```

Execute o programa:

```bash
python src/bolonhaemilano/main.py
```

O menu principal será apresentado diretamente no terminal.

## 📊 Diagramas UML

Os diagramas UML acompanham o desenvolvimento incremental do projeto.

A cada etapa, os diagramas correspondentes serão atualizados e adicionados ao repositório, documentando a estrutura das classes e as funcionalidades do sistema.

Os arquivos são armazenados no formato `.puml`, permitindo sua visualização e edição utilizando ferramentas compatíveis com PlantUML.

## 📌 Considerações finais

O projeto Bolonha e Milano busca aplicar, na prática, os conceitos de programação orientada a objetos, organização de sistemas, modelagem UML e controle de versão.

O desenvolvimento será realizado progressivamente, respeitando os requisitos e as funcionalidades estabelecidos para cada etapa.

**Projeto em desenvolvimento — 4º Bimestre.**