"""
Funções de carregamento, limpeza e engenharia de atributos.

Extraídas do notebook `notebooks/CRISP_DM_em_Python.ipynb`, cobrindo as
Fases 2 (Entendimento dos Dados) e 3 (Preparação dos Dados / ETL) do
CRISP-DM. Cada função corresponde a um passo do pipeline e pode ser
testada/reaproveitada de forma independente.
"""

import re

import numpy as np
import pandas as pd

from src.constants import COLUNAS_CATEGORICAS, COLUNAS_OPERACIONAIS


def carregar_dataset(caminho: str, header: int = 2) -> pd.DataFrame:
    """Lê o arquivo .xlsx da pesquisa de satisfação.

    O dataset original tem linhas de cabeçalho extras (usadas apenas para
    agrupamento visual das categorias no Excel), por isso o cabeçalho real
    das colunas está na linha de índice 2 (terceira linha).
    """
    return pd.read_excel(caminho, header=header)


def selecionar_colunas(df: pd.DataFrame, colunas: list) -> pd.DataFrame:
    """Retorna apenas as colunas relevantes para a análise."""
    colunas_existentes = [c for c in colunas if c in df.columns]
    return df[colunas_existentes].copy()


def converter_colunas_para_numerico(df: pd.DataFrame, colunas: list) -> pd.DataFrame:
    """Converte colunas de avaliação (texto, com valores como "NS") para numérico.

    Valores que não podem ser convertidos (ex.: "NS") viram NaN.
    """
    df = df.copy()
    colunas_existentes = [c for c in colunas if c in df.columns]
    df[colunas_existentes] = df[colunas_existentes].apply(pd.to_numeric, errors="coerce")
    return df


def remover_linhas_com_nulos_essenciais(df: pd.DataFrame, colunas_essenciais: list) -> pd.DataFrame:
    """Remove linhas com nulo em qualquer uma das colunas essenciais informadas."""
    return df.dropna(subset=colunas_essenciais)


def preencher_valores_faltantes(
    df: pd.DataFrame,
    colunas_numericas: list = COLUNAS_OPERACIONAIS + ["SATISFAÇÃO GERAL"],
    colunas_categoricas: list = COLUNAS_CATEGORICAS,
    random_state: int | None = None,
) -> pd.DataFrame:
    """Preenche valores ausentes com dados simulados.

    - Numéricas: amostra de uma normal com média/desvio padrão da própria coluna.
    - Categóricas: amostra aleatória dos valores válidos já existentes na coluna.

    Essa estratégia mantém o volume do dataset sem distorcer as distribuições
    originais — indicada quando o volume de nulos é grande e a exclusão das
    linhas reduziria demais a amostra.
    """
    if random_state is not None:
        np.random.seed(random_state)

    df = df.copy()

    for col in colunas_numericas:
        if col not in df.columns:
            continue
        df[col] = pd.to_numeric(df[col], errors="coerce")
        media = df[col].mean()
        std = df[col].std()
        nulos = df[col].isnull()
        n_nulos = nulos.sum()
        if n_nulos > 0:
            valores_aleatorios = np.random.normal(loc=media, scale=std, size=n_nulos)
            df.loc[nulos, col] = valores_aleatorios

    for col in colunas_categoricas:
        if col not in df.columns:
            continue
        valores_possiveis = df[col].dropna().unique()
        nulos = df[col].isnull()
        n_nulos = nulos.sum()
        if n_nulos > 0 and len(valores_possiveis) > 0:
            valores_aleatorios = np.random.choice(valores_possiveis, size=n_nulos)
            df.loc[nulos, col] = valores_aleatorios

    return df


def criar_faixa_etaria(df: pd.DataFrame, coluna_idade: str = "IDADE") -> pd.DataFrame:
    """Cria IDADE_NUM (idade numérica extraída do texto) e FAIXA_ETÁRIA a partir da coluna de idade.

    A coluna original contém intervalos textuais (ex.: "26 a 35 anos"); extrai-se
    o primeiro número como idade aproximada e depois categoriza-se em faixas.
    """
    df = df.copy()
    df["IDADE_NUM"] = df[coluna_idade].astype(str).str.extract(r"(\d+)").astype(float)
    df["FAIXA_ETÁRIA"] = pd.cut(
        df["IDADE_NUM"],
        bins=[0, 18, 30, 45, 60, 100],
        labels=["Até 18", "19-30", "31-45", "46-60", "60+"],
    )
    return df


def _categorizar_tempo(tempo: str):
    """Classifica um texto de tempo de espera (ex.: "1h30min a 2h") em Curto/Médio/Longo."""
    if pd.isnull(tempo):
        return np.nan
    match = re.search(r"(\d+)h", tempo)
    if not match:
        return np.nan
    horas = int(match.group(1))
    if horas < 1:
        return "Curto"
    elif 1 <= horas <= 2:
        return "Médio"
    return "Longo"


def categorizar_tempo_espera(df: pd.DataFrame, coluna: str = "TEMPO DE ESPERA") -> pd.DataFrame:
    """Cria TEMPO_ESPERA_CATEGORIZADO (Curto/Médio/Longo) a partir da coluna de tempo de espera."""
    df = df.copy()
    df["TEMPO_ESPERA_CATEGORIZADO"] = df[coluna].apply(_categorizar_tempo)
    return df


def calcular_experiencia_media(
    df: pd.DataFrame, colunas_operacionais: list = COLUNAS_OPERACIONAIS
) -> pd.DataFrame:
    """Cria EXPERIENCIA_MEDIA: a média das notas operacionais do passageiro."""
    df = df.copy()
    colunas_existentes = [c for c in colunas_operacionais if c in df.columns]
    df["EXPERIENCIA_MEDIA"] = df[colunas_existentes].mean(axis=1)
    return df


def binarizar_sim_nao(df: pd.DataFrame, coluna: str, nova_coluna: str) -> pd.DataFrame:
    """Converte uma coluna Sim/Não em binária (Sim=0, Não=1) em uma nova coluna."""
    df = df.copy()
    df[nova_coluna] = df[coluna].map({"Sim": 0, "Não": 1})
    return df


def remover_colunas_redundantes(df: pd.DataFrame, colunas: list) -> pd.DataFrame:
    """Remove colunas originais já substituídas por versões derivadas/tratadas."""
    colunas_existentes = [c for c in colunas if c in df.columns]
    return df.drop(columns=colunas_existentes)


def limitar_notas(df: pd.DataFrame, colunas_notas: list, minimo: int = 1, maximo: int = 5) -> pd.DataFrame:
    """Garante que as notas de avaliação fiquem dentro da escala original [minimo, maximo]."""
    df = df.copy()
    colunas_existentes = [c for c in colunas_notas if c in df.columns]
    df[colunas_existentes] = df[colunas_existentes].clip(minimo, maximo)
    return df


def padronizar_textos(df: pd.DataFrame) -> pd.DataFrame:
    """Normaliza espaços e capitalização de colunas de texto (companhia aérea e mês)."""
    df = df.copy()
    if "CIA AÉREA" in df.columns:
        df["CIA AÉREA"] = df["CIA AÉREA"].str.strip().str.title()
    if "MÊS" in df.columns:
        df["MÊS"] = df["MÊS"].str.capitalize()
    return df


def padronizar_motivo_viagem(
    df: pd.DataFrame,
    coluna: str = "MOTIVO DA VIAGEM",
    categorias_principais: tuple = ("Trabalho", "Lazer"),
) -> pd.DataFrame:
    """Agrupa motivos de viagem fora das categorias principais em "Outros"."""
    df = df.copy()
    df["MOTIVO_VIAGEM_PAD"] = df[coluna].apply(
        lambda x: x if x in categorias_principais else "Outros"
    ).astype("category")
    return df