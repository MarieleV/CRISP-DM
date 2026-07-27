"""
Funções de visualização.

Extraídas do notebook `notebooks/CRISP_DM_em_Python.ipynb`, cobrindo os
gráficos repetidos na Fase 2 (Análise Exploratória) e na Fase 5
(interpretação dos clusters). Cada função recebe os dados já prontos e
apenas desenha o gráfico — a lógica de preparação continua em
`data_prep.py` / `clustering.py`.
"""

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.decomposition import PCA


def configurar_estilo():
    """Aplica o estilo visual padrão usado em todo o notebook."""
    sns.set(style="whitegrid", palette="viridis", font_scale=1.1)


def plot_distribuicao_satisfacao(df: pd.DataFrame, coluna: str = "SATISFAÇÃO GERAL"):
    """Countplot da distribuição geral das notas de satisfação."""
    plt.figure(figsize=(8, 5))
    sns.countplot(x=coluna, data=df)
    plt.title("Distribuição da Satisfação Geral dos Passageiros")
    plt.xlabel("Nota de Satisfação (1 a 5)")
    plt.ylabel("Quantidade de Avaliações")
    plt.show()


def plot_media_por_categoria_barh(
    df: pd.DataFrame,
    coluna_categoria: str,
    coluna_valor: str = "SATISFAÇÃO GERAL",
    titulo: str = None,
    cor: str = None,
    top_n: int = None,
):
    """Barra horizontal com a média de `coluna_valor` agrupada por `coluna_categoria`.

    Útil para "satisfação média por aeroporto", "por companhia aérea" etc.
    Use `top_n` para mostrar apenas os N piores (ex.: aeroportos com menor satisfação).
    """
    medias = df.groupby(coluna_categoria)[coluna_valor].mean().sort_values()
    if top_n is not None:
        medias = medias.head(top_n)

    plt.figure(figsize=(10, 6))
    medias.plot(kind="barh", color=cor)
    plt.title(titulo or f"{coluna_valor} Média por {coluna_categoria}")
    plt.xlabel("Nota Média")
    plt.ylabel(coluna_categoria)
    plt.show()


def plot_media_por_categoria_barras(
    df: pd.DataFrame,
    coluna_categoria: str,
    coluna_valor: str = "SATISFAÇÃO GERAL",
    titulo: str = None,
    figsize: tuple = (8, 5),
    rotacao_x: int = 0,
):
    """Barras verticais com a média de `coluna_valor` por `coluna_categoria` (com barra de erro oculta)."""
    plt.figure(figsize=figsize)
    sns.barplot(x=coluna_categoria, y=coluna_valor, data=df, estimator="mean", errorbar=None)
    plt.title(titulo or f"{coluna_valor} Média por {coluna_categoria}")
    plt.xlabel(coluna_categoria)
    plt.ylabel("Nota Média")
    plt.xticks(rotation=rotacao_x)
    plt.show()


def plot_boxplot_por_categoria(df: pd.DataFrame, coluna_categoria: str, coluna_valor: str):
    """Boxplot de `coluna_valor` segmentado por `coluna_categoria` (ex.: satisfação por tipo de voo)."""
    plt.figure(figsize=(8, 5))
    sns.boxplot(x=coluna_categoria, y=coluna_valor, data=df)
    plt.title(f"Distribuição de {coluna_valor} por {coluna_categoria}")
    plt.show()


def plot_medias_por_area(df: pd.DataFrame, colunas_avaliacoes: list):
    """Barras com a média de satisfação para cada área/aspecto avaliado (ordenadas)."""
    medias = df[colunas_avaliacoes].mean().sort_values()
    plt.figure(figsize=(10, 5))
    sns.barplot(x=medias.values, y=medias.index)
    plt.title("Médias de Satisfação por Área Avaliada")
    plt.xlabel("Nota Média")
    plt.ylabel("Aspecto do Aeroporto")
    plt.show()


def plot_elbow_e_silhouette(resultados: dict):
    """Plota lado a lado o método do cotovelo (inertia) e o Silhouette Score por K.

    `resultados` é o dict retornado por `clustering.testar_valores_de_k`.
    """
    plt.figure(figsize=(12, 4))

    plt.subplot(1, 2, 1)
    plt.plot(resultados["k"], resultados["inertia"], "-o")
    plt.xlabel("K")
    plt.ylabel("Inertia")
    plt.title("Elbow: Inertia x K")

    plt.subplot(1, 2, 2)
    plt.plot(resultados["k"], resultados["silhouette"], "-o")
    plt.xlabel("K")
    plt.ylabel("Silhouette Score")
    plt.title("Silhouette Score x K")

    plt.tight_layout()
    plt.show()


def plot_comparativo_clusters(
    df: pd.DataFrame, features: list, coluna_cluster: str = "cluster", titulo: str = None
):
    """Barras comparando a média de cada feature entre os clusters."""
    resumo = df.groupby(coluna_cluster)[features].mean().T
    resumo.plot(kind="bar", figsize=(14, 6))
    plt.title(titulo or "Comparativo das Médias de Avaliação por Cluster")
    plt.ylabel("Média de Satisfação (0–5)")
    plt.xlabel("Aspectos Avaliados")
    plt.xticks(rotation=90)
    plt.show()


def plot_clusters_pca(X_scaled, labels, random_state: int = 42):
    """Projeta os dados em 2D via PCA e colore os pontos pelo cluster atribuído."""
    pca = PCA(n_components=2, random_state=random_state)
    X_pca = pca.fit_transform(X_scaled)

    plt.figure(figsize=(8, 6))
    scatter = plt.scatter(X_pca[:, 0], X_pca[:, 1], c=labels, cmap="tab10", s=15)
    plt.legend(*scatter.legend_elements(), title="cluster")
    plt.title("Clusters (visualização em 2D via PCA)")
    plt.xlabel("PC1")
    plt.ylabel("PC2")
    plt.show()


def plot_heatmap_correlacao(df: pd.DataFrame, colunas: list, titulo: str = "Correlação"):
    """Heatmap de correlação entre as colunas informadas."""
    plt.figure(figsize=(10, 6))
    sns.heatmap(df[colunas].corr(), annot=True, cmap="coolwarm")
    plt.title(titulo)
    plt.show()