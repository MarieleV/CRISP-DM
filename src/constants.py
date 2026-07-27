"""
Constantes compartilhadas pelo pipeline: listas de colunas usadas em mais
de uma fase do CRISP-DM (Entendimento dos Dados, ETL e Modelagem).

Manter essas listas em um único lugar evita duplicação e o risco de as
diferentes etapas do notebook usarem versões levemente diferentes da
mesma lista de colunas.
"""

# As 31 colunas selecionadas na Fase 2 (Entendimento dos Dados) como
# relevantes para o objetivo do projeto.
COLUNAS_DESEJADAS = [
    "CHAVE",
    "AEROPORTO",
    "MÊS",
    "TIPO DE VOO",
    "CIA AÉREA",
    "PROCESSO DE CHECK IN",
    "PROCESSO DE AQUISIÇÃO DA PASSAGEM",
    "ATENDIMENTO DA CIA. AÉREA",
    "PROCESSO DE INSPEÇÃO DE SEGURANÇA",
    "CONTROLE MIGRATÓRIO",
    "CONTROLE ADUANEIRO",
    "ESTABELECIMENTOS DE ALIMENTAÇÃO",
    "ESTABELECIMENTOS COMERCIAIS",
    "ESTACIONAMENTO",
    "LOCALIZAÇÃO E DESLOCAMENTO",
    "CONFORTO DA SALA DE EMBARQUE",
    "DISPONIBILIDADE DE ASSENTOS RESERVADOS",
    "DISPONIBILIDADE DE TOMADAS",
    "INTERNET DISPONIBILIZADA PELO AEROPORTO",
    "SANITÁRIOS",
    "LIMPEZA GERAL DO AEROPORTO",
    "PROCESSO DE RESTITUIÇÃO DE BAGAGENS",
    "ATENDIMENTO DA CIA. AÉREA2",
    "SATISFAÇÃO GERAL",
    "NACIONALIDADE",
    "GÊNERO",
    "IDADE",
    "VIAJANDO SOZINHO",
    "MOTIVO DA VIAGEM",
    "JÁ EMBARCOU/DESEMBARCOU ANTES NO AEROPORTO",
    "TEMPO DE ESPERA",
]

# Colunas de avaliação (notas de 1 a 5) relacionadas à experiência
# operacional do passageiro no aeroporto.
COLUNAS_OPERACIONAIS = [
    "PROCESSO DE CHECK IN",
    "PROCESSO DE AQUISIÇÃO DA PASSAGEM",
    "ATENDIMENTO DA CIA. AÉREA",
    "PROCESSO DE INSPEÇÃO DE SEGURANÇA",
    "CONTROLE MIGRATÓRIO",
    "CONTROLE ADUANEIRO",
    "ESTABELECIMENTOS DE ALIMENTAÇÃO",
    "ESTABELECIMENTOS COMERCIAIS",
    "ESTACIONAMENTO",
    "LOCALIZAÇÃO E DESLOCAMENTO",
    "CONFORTO DA SALA DE EMBARQUE",
    "DISPONIBILIDADE DE ASSENTOS RESERVADOS",
    "DISPONIBILIDADE DE TOMADAS",
    "INTERNET DISPONIBILIZADA PELO AEROPORTO",
    "SANITÁRIOS",
    "LIMPEZA GERAL DO AEROPORTO",
    "PROCESSO DE RESTITUIÇÃO DE BAGAGENS",
    "ATENDIMENTO DA CIA. AÉREA2",
]

# Todas as colunas de nota (as operacionais + a satisfação geral).
COLUNAS_NOTAS = COLUNAS_OPERACIONAIS + ["SATISFAÇÃO GERAL"]

# Colunas categóricas usadas no preenchimento aleatório de nulos.
COLUNAS_CATEGORICAS = [
    "AEROPORTO",
    "MÊS",
    "TIPO DE VOO",
    "CIA AÉREA",
    "NACIONALIDADE",
    "GÊNERO",
    "IDADE",
    "VIAJANDO SOZINHO",
    "MOTIVO DA VIAGEM",
    "JÁ EMBARCOU/DESEMBARCOU ANTES NO AEROPORTO",
    "TEMPO DE ESPERA",
]

# Candidatas a features numéricas para o clustering (algumas podem não
# existir após etapas de remoção de colunas — filtrar antes de usar).
NUM_FEATURES_CANDIDATAS = COLUNAS_OPERACIONAIS + [
    "SATISFAÇÃO GERAL",
    "IDADE_NUM",
    "EXPERIENCIA_MEDIA",
]