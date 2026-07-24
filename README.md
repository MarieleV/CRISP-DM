<div align="center">
    
# Ciclo Completo CRISP-DM em Python — Satisfação de Passageiros em Aeroportos

Projeto de ciência de dados aplicando o processo **CRISP-DM (Cross Industry Standard Process for Data Mining)** de ponta a ponta — do entendimento do negócio à disponibilização dos resultados — sobre dados reais de satisfação de passageiros em aeroportos brasileiros.
</div>

## Objetivo do Negócio

Representando um aeroporto fictício, o projeto busca aprender com os resultados de satisfação de outros aeroportos nacionais para identificar o que mais impacta a experiência dos passageiros e priorizar melhorias internas.

**Problemática:** gestores notaram queda na rentabilidade e na frequência de passageiros em alguns aeroportos. A análise de dados foi usada para identificar padrões que apoiem decisões de investimento e reforma.

## Dataset

- **Nome:** Pesquisa de Satisfação dos Passageiros dos Principais Aeroportos Nacionais — Trimestral (02/2025)
- **Fonte:** [dados.gov.br](https://dados.gov.br/dados/conjuntos-dados/pesquisa-de-satisfacao-do-passageiro-em-aeroportos) — Secretaria Nacional de Aviação Civil (SAC)
- **Coleta:** entrevistas presenciais nas salas de embarque/desembarque, voos domésticos e internacionais
- **Tamanho:** ~25.500 registros, 98 variáveis originais (reduzidas a 31 relevantes após seleção)

> O arquivo `.xlsx` não está versionado neste repositório (ver `.gitignore`). Baixe o dataset na fonte oficial acima e salve em `data/raw/`.

## Metodologia (CRISP-DM)

| Fase | O que foi feito |
|---|---|
| 1. Entendimento do Negócio | Definição de objetivos, problemática e plano do projeto |
| 2. Entendimento dos Dados | Inspeção de dimensões, tipos, nulos e estatísticas descritivas; ajuste de cabeçalho |
| 3. Preparação dos Dados (ETL) | Seleção de variáveis, tratamento de nulos, criação de atributos (faixa etária, tempo de espera categorizado, experiência média por área), padronização de textos |
| 4. Modelagem | Clustering com **K-Means**: seleção de features numéricas, imputação/escala, teste de K via Elbow + Silhouette |
| 5. Avaliação | Interpretação dos clusters, comparação com os objetivos de negócio |
| 6. Disponibilização | Plano de entrega (dashboard), monitoramento contínuo e relatório final |

## Principais Resultados

- O melhor resultado de segmentação foi obtido com **K = 2** (Silhouette Score de 0,0858), indicando dois perfis de passageiros com separação sutil, porém consistente — comum em dados de percepção subjetiva.
- **Cluster 0:** passageiros com maior satisfação geral, associada a boas avaliações de conforto e atendimento.
- **Cluster 1:** passageiros menos satisfeitos, principalmente com **infraestrutura** (internet, tomadas, restituição de bagagens).
- Aspectos de **atendimento e limpeza** foram bem avaliados de forma geral; **infraestrutura física** é o principal fator de insatisfação.
- **Recomendação de negócio:** priorizar investimentos em infraestrutura e conectividade tende a gerar o maior ganho de satisfação percebida.

## Estrutura do Repositório

```
.
├── README.md
├── requirements.txt
├── .gitignore
├── data/
│   ├── raw/            # dataset original (.xlsx) — baixar da fonte, não versionado
│   └── processed/      # dados limpos/transformados gerados pelo notebook
├── notebooks/
│   └── CRISP_DM_em_Python.ipynb   # notebook principal com todo o pipeline
├── src/                # funções reutilizáveis (em construção — ver "Próximos passos")
└── reports/
    └── figures/         # gráficos exportados para uso no README/relatório
```

## Como Executar

```bash
# 1. Clonar o repositório
git clone https://github.com/<seu-usuario>/<seu-repo>.git
cd <seu-repo>

# 2. Criar ambiente virtual (opcional, recomendado)
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 3. Instalar dependências
pip install -r requirements.txt

# 4. Baixar o dataset da fonte oficial e salvar em data/raw/

# 5. Rodar o notebook
jupyter notebook notebooks/CRISP_DM_em_Python.ipynb
```

## Limitações e Próximos Passos

- O Silhouette Score obtido (baixo em termos absolutos) sugere fronteiras pouco nítidas entre os grupos — esperado em dados de opinião.
- Testar algoritmos alternativos de clustering (DBSCAN, Gaussian Mixture Models).
- Aplicar PCA para reduzir dimensionalidade e melhorar a separação dos clusters.
- Extrair as funções de preparação de dados e clustering do notebook para `src/`, tornando o pipeline reutilizável e testável.
- Ampliar o dataset com novas variáveis comportamentais e testar modelos supervisionados para prever satisfação futura.

## Autor

Mariele V.
