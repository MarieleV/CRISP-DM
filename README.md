<div align="center">

# ✈️ Satisfação de Passageiros em Aeroportos

### Ciclo Completo CRISP-DM em Python

<p>
  <img src="https://img.shields.io/badge/status-concluído-success?style=for-the-badge" alt="Status: Concluído" />
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white" alt="Pandas" />
  <img src="https://img.shields.io/badge/Scikit_Learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white" alt="Scikit-Learn" />
  <img src="https://img.shields.io/badge/Jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white" alt="Jupyter" />
</p>

</div>

---

Projeto de ciência de dados aplicando o processo **CRISP-DM (Cross Industry Standard Process for Data Mining)** de ponta a ponta. Do entendimento do negócio à disponibilização dos resultados, sobre dados reais de satisfação de passageiros em aeroportos brasileiros.

<div align="center">

### 📑 Sumário

[Objetivo do Negócio](#-objetivo-do-negócio) • [Dataset](#-dataset) • [Metodologia CRISP-DM](#-metodologia-crisp-dm) • [Principais Resultados](#-principais-resultados) • [Tecnologias Utilizadas](#️-tecnologias-utilizadas) • [Estrutura do Projeto](#-estrutura-do-projeto)

</div>

---

## 🎯 Objetivo do Negócio

Representando um aeroporto fictício, o projeto busca aprender com os resultados de satisfação de outros aeroportos nacionais para identificar o que mais impacta a experiência dos passageiros e priorizar melhorias internas.

**Problemática:** gestores notaram queda na rentabilidade e na frequência de passageiros em alguns aeroportos. A análise de dados foi usada para identificar padrões que apoiem decisões de investimento e reforma.

## 📊 Dataset

-  **Nome:** Pesquisa de Satisfação dos Passageiros dos Principais Aeroportos Nacionais — Trimestral (02/2025)
-  **Fonte:** [dados.gov.br](https://dados.gov.br/dados/conjuntos-dados/pesquisa-de-satisfacao-do-passageiro-em-aeroportos) — Secretaria Nacional de Aviação Civil (SAC)
-  **Coleta:** Entrevistas presenciais nas salas de embarque/desembarque, voos domésticos e internacionais.
-  **Tamanho:** ~25.500 registros, 98 variáveis originais (reduzidas a 31 relevantes após seleção).

> ⚠️ **Nota:** O arquivo `.xlsx` original não está versionado neste repositório (ver `.gitignore`). Baixe o dataset na fonte oficial acima e salve em `data/raw/`.

## ⚙️ Metodologia CRISP-DM

| Fase | Descrição das Atividades |
|:---:|---|
|  **1. Entendimento do Negócio** | Definição de objetivos, levantamento da problemática e plano do projeto. |
|  **2. Entendimento dos Dados** | Inspeção de dimensões, tipos, nulos e estatísticas descritivas; ajuste de cabeçalho. |
|  **3. Preparação dos Dados (ETL)** | Seleção de variáveis, tratamento de nulos, criação de atributos (faixa etária, tempo de espera categorizado, experiência média por área), padronização de textos. |
|  **4. Modelagem** | Clustering com **K-Means**: seleção de features numéricas, imputação/escala, teste de K via Elbow + Silhouette. |
|  **5. Avaliação** | Interpretação dos clusters e comparação direta com os objetivos de negócio estabelecidos. |
|  **6. Disponibilização** | Plano de entrega (dashboard), sugestão de monitoramento contínuo e relatório final. |

## 💡 Principais Resultados

-  **Melhor Segmentação:** Obtida com **K = 2** (Silhouette Score de 0,0858), indicando dois perfis de passageiros com separação sutil, porém consistente — cenário comum em dados de percepção subjetiva.
-  **Cluster 0:** Passageiros com maior satisfação geral, diretamente associada a boas avaliações de conforto e atendimento.
-  **Cluster 1:** Passageiros menos satisfeitos, apontando problemas principalmente com a **infraestrutura** (internet, tomadas, restituição de bagagens).
-  **Atendimento e Limpeza:** Avaliados de forma positiva em ambos os grupos. A **infraestrutura física** é o verdadeiro gargalo.
-  **Recomendação de Negócio:** Priorizar investimentos imediatos em infraestrutura de espera e conectividade, pois são as alavancas que geram o maior ganho de satisfação percebida.

## 🛠️ Tecnologias Utilizadas

<table>
<tr>
<td width="50%" valign="top">

### Linguagem e Ferramentas
- **Python 3**
- **Jupyter Notebook** (Modelagem e Análise)
- **Git & GitHub** (Versionamento)

</td>
<td width="50%" valign="top">

### Principais Bibliotecas
- **Pandas & NumPy** — Manipulação e ETL
- **Scikit-Learn** — Modelagem (K-Means, Silhouette)
- **Matplotlib & Seaborn** — Visualização de dados

</td>
</tr>
</table>

## 📂 Estrutura do Projeto

```text
.
├── README.md
├── requirements.txt
├── .gitignore
└── data/
    └── raw/            # dataset original (.xlsx) — baixar da fonte, não versionado
