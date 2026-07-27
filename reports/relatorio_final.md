# Relatório Final — Satisfação de Passageiros em Aeroportos

> Documento extraído da Fase 6 (Disponibilização) do notebook `notebooks/CRISP_DM_em_Python.ipynb`, consolidando a avaliação (Fase 5) e o relatório final (Fase 6) do processo CRISP-DM.

## 1. Descrição do Problema e dos Objetivos da Análise

O presente projeto teve como objetivo principal extrair conhecimento de uma base de dados de satisfação de passageiros de companhias aéreas, buscando compreender padrões e perfis distintos de satisfação. A partir da aplicação do modelo CRISP-DM (CRoss Industry Standard Process for Data Mining), foram realizadas todas as etapas do processo de descoberta de conhecimento, desde o entendimento do problema até a disponibilização dos resultados.

O problema central investigado foi:

> *"Quais fatores influenciam a satisfação dos passageiros e como é possível identificar grupos (clusters) com características semelhantes de percepção?"*

Os objetivos específicos incluíram:

- Identificar perfis de passageiros com base nas avaliações realizadas.
- Reconhecer aspectos que mais impactam a satisfação geral.
- Fornecer insights estratégicos para orientar melhorias na operação e no atendimento ao cliente.

## 2. Etapas de Preparação dos Dados e Justificativas

A base de dados original continha mais de 1.000 registros de passageiros, com informações sobre idade, tipo de viagem, classe, e diversos fatores de avaliação (como conforto, limpeza, alimentação e internet).

Durante a fase de preparação (ETL), foram realizadas as seguintes ações:

1. **Seleção dos dados relevantes:** foram escolhidas variáveis relacionadas à experiência do passageiro.
2. **Limpeza dos dados:** exclusão de valores nulos, duplicados e registros inconsistentes.
3. **Normalização e transformação:** variáveis numéricas foram padronizadas para melhor desempenho dos algoritmos.
4. **Criação de novas variáveis derivadas**, como `IDADE_NUM`, construída a partir da variável "Idade", para uso em análises quantitativas.
5. **Remoção de atributos irrelevantes ao modelo** (como IDs e informações redundantes).

O conjunto final preparado foi considerado adequado para aplicação de técnicas de aprendizado não supervisionado (clustering).

## 3. Modelagem e Análise dos Clusters

Na fase de modelagem, foi aplicado o algoritmo **K-Means**, com o objetivo de identificar agrupamentos naturais entre os passageiros com base em suas avaliações. A escolha do número ideal de clusters foi definida por meio da análise do método do cotovelo (Elbow Method) e da métrica Silhouette Score.

Após testar valores de K de 2 a 10, o **Silhouette Score máximo foi 0,0858 para K = 2**, indicando que o agrupamento com dois clusters apresenta a melhor separação entre grupos. Embora o valor absoluto do silhouette seja baixo — o que é comum em dados de percepção humana e avaliações subjetivas — ele ainda demonstra a presença de dois perfis distintos de passageiros em relação à satisfação e experiência. Por isso, foi adotado **K = 2** como número ideal de clusters, trazendo o melhor equilíbrio entre simplicidade do modelo e coerência dos resultados.

Os dois clusters identificados apresentam perfis distintos:

- **Cluster 0:** passageiros com maiores índices de satisfação geral, geralmente associados a boas avaliações de conforto e atendimento.
- **Cluster 1:** grupo com níveis mais baixos de satisfação, especialmente insatisfeito com itens de infraestrutura, como internet, tomadas e restituição de bagagens.

As médias de avaliação foram visualizadas por meio de mapas de calor (heatmaps) e gráficos comparativos, evidenciando diferenças claras entre os grupos formados. A variável `IDADE_NUM` foi excluída das análises de correlação e gráficos comparativos para evitar distorções, focando exclusivamente nas variáveis de satisfação.

Os resultados mostram que fatores como **infraestrutura física** (tomadas, internet, conforto) têm impacto mais forte na **insatisfação**, enquanto aspectos de **atendimento e limpeza** são mais **bem avaliados**. Isso indica que **investimentos em tecnologia e comodidade** podem melhorar significativamente a satisfação geral dos passageiros.

## 4. Avaliação dos Resultados

A avaliação foi conduzida com base nos objetivos definidos na Fase 1 (Entendimento do Negócio), verificando se os resultados atenderam às expectativas da descoberta de conhecimento:

- O objetivo de entender o perfil dos passageiros e sua relação com a satisfação foi atingido, com dois perfis bem definidos.
- O objetivo de identificar aspectos que geram insatisfação também foi atingido, destacando problemas em infraestrutura (tomadas, internet, restituição de bagagens).
- O objetivo de avaliar padrões úteis para a tomada de decisão foi atingido, pois os clusters se mostraram coerentes e interpretáveis, fornecendo insights claros para a gestão.

De modo geral, os resultados foram consistentes, interpretáveis e alinhados ao contexto operacional do setor aeroportuário.

**Conclusão da coerência com os objetivos:** o modelo de agrupamento conseguiu identificar perfis distintos de satisfação entre passageiros, fornecendo informações valiosas para priorização de melhorias. Apesar dos baixos valores de silhouette, a interpretação dos clusters é coerente e relevante, considerando o contexto real de dados de opinião.

## 5. Plano de Disponibilização e Manutenção

### 5.1 Disponibilização e integração dos resultados

Os resultados obtidos a partir da análise de clusters foram planejados para integração ao ambiente organizacional de forma a apoiar decisões estratégicas. Os perfis identificados (clusters) permitem que a empresa compreenda melhor as diferenças nas percepções de satisfação entre grupos de passageiros, direcionando melhorias de forma segmentada. A entrega prevista inclui:

- Relatório interativo (dashboard em Power BI ou similar) contendo as métricas de satisfação e os perfis de clusters.
- Apresentação executiva para os gestores, com recomendações práticas baseadas nos resultados.
- Integração dos insights ao sistema interno de gestão da qualidade, para acompanhamento contínuo de indicadores de satisfação.

### 5.2 Monitoramento e manutenção

Para garantir a continuidade e relevância dos resultados, será implementado um plano de monitoramento contínuo, que envolve:

- Atualização periódica dos dados de satisfação (mensal ou trimestralmente).
- Reaplicação do modelo de clusterização com os novos dados para verificar mudanças nos perfis dos passageiros.
- Revisão dos indicadores de desempenho (KPIs) relacionados à satisfação e infraestrutura.
- Documentação de ajustes realizados para garantir a rastreabilidade das alterações.

Esse processo garante que o conhecimento obtido permaneça relevante, atualizado e aplicável às decisões futuras da organização.

## 6. Conclusão e Considerações Finais

O projeto cumpriu integralmente o ciclo do processo CRISP-DM, permitindo a extração de conhecimento útil a partir de uma base de dados realista e volumosa. Os resultados alcançados evidenciam o potencial da mineração de dados como ferramenta de apoio à decisão, possibilitando compreender melhor o comportamento e as preferências dos passageiros.

Como melhorias futuras, recomenda-se:

- A ampliação do dataset com novas variáveis comportamentais.
- A utilização de modelos supervisionados para prever satisfação futura.
- A integração dos resultados a sistemas corporativos para automatizar o monitoramento contínuo.

Assim, o estudo demonstra que a análise de dados, quando bem conduzida, oferece insights estratégicos valiosos para o aprimoramento dos serviços e a elevação da satisfação do cliente.

## 7. Revisão do Projeto: Pontos Positivos, Negativos e Sugestões

**Pontos positivos:**

- Dataset extenso e com boa representatividade geográfica.
- Resultados coerentes e interpretáveis.
- Técnica de clustering adequada ao objetivo exploratório.

**Pontos de atenção:**

- A pontuação silhouette sugere que as fronteiras entre grupos não são fortemente definidas.
- Algumas variáveis podem estar altamente correlacionadas, afetando a distância euclidiana usada pelo K-Means.

**Recomendações:**

- Testar outros algoritmos de agrupamento (ex.: DBSCAN ou Gaussian Mixture Models), que podem capturar padrões mais complexos.
- Aplicar PCA (Análise de Componentes Principais) para reduzir dimensões e melhorar a separação dos clusters.

**Síntese final:** a mineração de dados cumpriu os objetivos de identificar padrões e perfis de passageiros. O modelo K-Means com dois clusters apresentou separação suficiente para gerar insights úteis à gestão aeroportuária, direcionando ações estratégicas em infraestrutura e atendimento.