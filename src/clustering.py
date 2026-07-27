"""
Funções de modelagem por clustering (K-Means).

Extraídas do notebook `notebooks/CRISP_DM_em_Python.ipynb`, cobrindo a
Fase 4 (Modelagem) do CRISP-DM: seleção de features numéricas, imputação
e escala, busca do melhor K (Elbow + Silhouette) e ajuste do modelo final.
"""

import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.impute import SimpleImputer
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import StandardScaler


def selecionar_features_numericas(df: pd.DataFrame, candidatas: list) -> list:
    """Filtra, entre as colunas candidatas, apenas as que existem no DataFrame."""
    return [c for c in candidatas if c in df.columns]


def imputar_e_escalar(df: pd.DataFrame, features: list):
    """Imputa medianas nos ausentes e padroniza (média 0, desvio padrão 1).

    Retorna (X_scaled, imputer, scaler) — os objetos ajustados são retornados
    para permitir reaplicá-los em novos dados, se necessário.
    """
    X_num = df[features].copy()

    imputer = SimpleImputer(strategy="median")
    scaler = StandardScaler()

    X_imp = imputer.fit_transform(X_num)
    X_scaled = scaler.fit_transform(X_imp)

    return X_scaled, imputer, scaler


def testar_valores_de_k(X_scaled: np.ndarray, k_range=range(2, 11), random_state: int = 42):
    """Roda o K-Means para cada K do intervalo e retorna inertia e silhouette de cada um.

    Retorna um dict: {"k": [...], "inertia": [...], "silhouette": [...]}
    Útil para plotar o método do cotovelo (Elbow) e o Silhouette Score.
    """
    resultados = {"k": [], "inertia": [], "silhouette": []}

    for k in k_range:
        kmeans = KMeans(n_clusters=k, random_state=random_state, n_init=10)
        labels = kmeans.fit_predict(X_scaled)
        resultados["k"].append(k)
        resultados["inertia"].append(kmeans.inertia_)
        resultados["silhouette"].append(silhouette_score(X_scaled, labels))

    return resultados


def escolher_melhor_k(resultados: dict) -> int:
    """Escolhe o K com maior Silhouette Score a partir do dict de `testar_valores_de_k`."""
    idx = int(np.argmax(resultados["silhouette"]))
    return resultados["k"][idx]


def ajustar_kmeans_final(X_scaled: np.ndarray, k: int, random_state: int = 42, n_init: int = 50):
    """Treina o K-Means final com o K escolhido e retorna (labels, modelo)."""
    kmeans_final = KMeans(n_clusters=k, random_state=random_state, n_init=n_init)
    labels = kmeans_final.fit_predict(X_scaled)
    return labels, kmeans_final


def resumir_clusters(df: pd.DataFrame, features: list, coluna_cluster: str = "cluster") -> pd.DataFrame:
    """Retorna a média de cada feature por cluster, com o tamanho de cada grupo."""
    resumo = df.groupby(coluna_cluster)[features].mean().round(2)
    resumo["size"] = df[coluna_cluster].value_counts().sort_index()
    return resumo