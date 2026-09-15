# 📡 Telemetria IoT

Sistema de monitoramento de servidores desenvolvido em Python, com coleta de dados de utilização da CPU e memória RAM, classificação de status e visualização através de um dashboard web.

O projeto tem como objetivo demonstrar, na prática, como dados de infraestrutura podem ser coletados, processados e apresentados de forma visual para facilitar o acompanhamento da saúde dos servidores.

## 📊 Demonstração

O sistema possui um painel de telemetria que permite acompanhar as leituras recebidas dos dispositivos conectados.


### Funcionalidades

* 📈 Visualização das leituras recebidas.
* 🖥️ Monitoramento de diferentes servidores.
* ⚙️ Acompanhamento do uso da CPU.
* 💾 Acompanhamento da memória RAM utilizada.
* 🟢 Classificação das leituras em normal, atenção e crítico.
* 🕒 Registro da data e horário de cada leitura.
* 📋 Histórico das leituras recebidas.
* 🔄 Atualização periódica das informações.
* 🧹 Limpeza dos dados apresentados no painel.

## 🧠 Como o sistema funciona

O funcionamento do projeto pode ser dividido em quatro etapas principais:

```text
┌─────────────────────┐
│       SERVIDOR      │
│                     │
│   CPU + Memória RAM │
└──────────┬──────────┘
           │
           │ Coleta dos dados
           ▼
┌─────────────────────┐
│     PROCESSAMENTO   │
│                     │
│ Analisa os valores  │
└──────────┬──────────┘
           │
           │ Classificação
           ▼
┌─────────────────────┐
│       STATUS        │
│                     │
│ Normal / Atenção    │
│ / Crítico           │
└──────────┬──────────┘
           │
           │ Registro da leitura
           ▼
┌─────────────────────┐
│      DASHBOARD      │
│                     │
│ Histórico +         │
│ indicadores         │
└─────────────────────┘
```

### 1. Coleta dos dados

O sistema obtém informações relacionadas ao funcionamento dos servidores, principalmente:

* Percentual de utilização da CPU.
* Percentual de utilização da memória RAM.
* Identificação do dispositivo.
* Data e horário da leitura.

Essas informações representam a telemetria dos dispositivos monitorados.

### 2. Processamento

Depois que uma leitura é obtida, os valores são analisados pela aplicação.

A utilização dos recursos é comparada com os limites definidos pelo sistema. A partir dessa análise, a leitura recebe um status correspondente à sua condição.

### 3. Classificação dos status

O projeto utiliza três estados principais:

| Status         | Descrição                                                          |
| -------------- | ------------------------------------------------------------------ |
| 🟢 **NORMAL**  | Servidor operando dentro dos limites esperados.                    |
| 🟡 **ATENÇÃO** | Servidor apresenta utilização elevada e merece acompanhamento.     |
| 🔴 **CRÍTICO** | Servidor apresenta uma condição que necessita de atenção imediata. |

Por exemplo:

```text
SERVIDOR-001
CPU: 8.3%
RAM: 74.6%
Status: NORMAL
```

```text
SERVIDOR-002
CPU: 92.0%
RAM: 94.0%
Status: CRÍTICO
```

> Os valores acima são exemplos de leituras exibidas no painel.

### 4. Visualização

Após o processamento, as informações são apresentadas no dashboard.

O operador consegue visualizar os dados de cada servidor em uma tabela, facilitando a identificação de situações que precisam de atenção.

## 📈 Dashboard

O painel funciona como uma central de operações para acompanhamento da infraestrutura.

### Indicadores principais

| Indicador              | Função                                              |
| ---------------------- | --------------------------------------------------- |
| **Leituras recebidas** | Quantidade de leituras registradas pelo sistema.    |
| **Status normal**      | Quantidade de leituras classificadas como normais.  |
| **Alertas críticos**   | Quantidade de leituras classificadas como críticas. |

### Tabela de leituras

A tabela apresenta as informações de cada leitura recebida:

| Campo             | Descrição                                |
| ----------------- | ---------------------------------------- |
| **ID**            | Identificador da leitura.                |
| **Dispositivo**   | Servidor que enviou os dados.            |
| **Uso da CPU**    | Percentual de CPU utilizado.             |
| **RAM utilizada** | Percentual de memória utilizada.         |
| **Status**        | Resultado da análise da leitura.         |
| **Data / Hora**   | Momento em que a leitura foi registrada. |

## 🔄 Atualização das informações

O dashboard trabalha com atualização periódica dos dados.

Quando novas leituras são recebidas, elas são adicionadas ao histórico e os indicadores do painel são atualizados.

Isso permite acompanhar alterações no estado dos servidores sem precisar consultar manualmente cada máquina.

## 🛠️ Tecnologias utilizadas

### Python

Utilizado como linguagem principal para a implementação da lógica de monitoramento e processamento dos dados.

### Dashboard Web

Responsável pela apresentação das informações de telemetria de forma visual, permitindo acompanhar os servidores através de uma interface centralizada.

### Git e GitHub

Utilizados para versionamento e armazenamento do código-fonte.

## 🏗️ Estrutura do projeto

A estrutura principal do projeto é organizada da seguinte maneira:

```text
telemetria-IoT/
│
├── telemetria-iot/
│   ├── ...
│
└── README.md
```

> A estrutura interna detalhada deve ser atualizada conforme os arquivos presentes na versão atual do projeto.

## 🚀 Como executar

### 1. Clonar o repositório

```bash
git clone https://github.com/carlosedu2411/telemetria-IoT.git
```

### 2. Entrar na pasta do projeto

```bash
cd telemetria-IoT
```

### 3. Criar o ambiente virtual

Caso o projeto utilize um ambiente virtual Python:

```bash
python -m venv venv
```

### 4. Ativar o ambiente virtual

No Windows:

```bash
venv\Scripts\activate
```

No Linux ou macOS:

```bash
source venv/bin/activate
```

### 5. Instalar as dependências

```bash
pip install -r requirements.txt
```

### 6. Executar a aplicação

```bash
python <arquivo-principal>.py
```

> O nome exato do arquivo principal deve ser conferido na estrutura atual do projeto.

## 🎯 Objetivo do projeto

O projeto tem como objetivo demonstrar, na prática, o funcionamento de um sistema de telemetria aplicado ao monitoramento de infraestrutura.

A ideia principal é transformar dados brutos de utilização dos servidores em informações úteis para tomada de decisão.

Em vez de analisar manualmente os valores de CPU e RAM, o sistema realiza esse processamento e apresenta o resultado de maneira visual.

```text
Dados brutos
     ↓
Processamento
     ↓
Análise
     ↓
Classificação
     ↓
Dashboard
     ↓
Identificação de problemas
```

## 💡 Importância da telemetria

A telemetria permite acompanhar o comportamento de dispositivos e servidores através de dados coletados durante seu funcionamento.

Em um ambiente real, esse tipo de monitoramento pode ajudar a identificar:

* Utilização excessiva de CPU.
* Consumo elevado de memória.
* Possíveis problemas de desempenho.
* Alterações no comportamento dos servidores.
* Necessidade de manutenção ou intervenção.

Dessa forma, o sistema contribui para uma visão mais organizada da infraestrutura e facilita o acompanhamento dos recursos computacionais.


## 👨‍💻 Autor

**Carlos Eduardo**

* GitHub: [carlosedu2411](https://github.com/carlosedu2411)
* Repositório: [telemetria-IoT](https://github.com/carlosedu2411/telemetria-IoT)

## 📄 Licença

Este projeto foi desenvolvido para fins de estudo e demonstração.

---

**Telemetria IoT — Monitoramento de servidores através de dados e visualização em tempo real.**
