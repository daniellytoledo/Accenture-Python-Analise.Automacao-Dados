# 🤖 Módulo 1 — Onboarding com IA: NotebookLM aplicado à Análise de Dados

> **Bootcamp:** Accenture - Python para Análise e Automação de Dados · Plataforma DIO  
> **Módulo:** 1 — Inteligência Artificial como Ferramenta de Estudo  
> **Ferramenta principal:** [Google NotebookLM](https://notebooklm.google.com/)

---

## 📌 Sobre este módulo

Neste módulo, o objetivo foi utilizar o **NotebookLM** — uma ferramenta de IA desenvolvida pelo Google que permite treinar um modelo com fontes personalizadas (vídeos, artigos, PDFs e links) — para extrair conhecimento estruturado sobre a área de **Análise de Dados**.

O processo envolveu:
1. Selecionar e inserir fontes no NotebookLM
2. Formular **perguntas estratégicas** para extrair insights relevantes
3. Criar **prompts eficazes** para guiar as respostas do modelo
4. Gerar um **mapa mental** visual com os conceitos-chave
5. Documentar todo o aprendizado neste README

---

## 🗂️ Fontes utilizadas para treinar o NotebookLM

As fontes escolhidas foram vídeos de profissionais experientes em análise de dados e um roadmap de referência da comunidade:

| # | Título | Link |
|---|--------|------|
| 1 | How I'd Become a Data Analyst in 2026 (the full roadmap) | [YouTube](https://www.youtube.com/watch?v=hGCKdMsfU7g) |
| 2 | How I'd become a data analyst (if i had to start over) in 2026 | [YouTube](https://www.youtube.com/watch?v=dJA7k58zlA8) |
| 3 | This is how you'll become a REMOTE Data Analyst in 2026 (FULL Guide) | [YouTube](https://www.youtube.com/watch?v=q5MOKiZzSFA) |
| 4 | How I Would Learn to be a Data Analyst | [YouTube](https://www.youtube.com/watch?v=TFFzNjWkhDk) |
| 5 | Fastest way to become a self taught data analyst and get a job | [YouTube](https://www.youtube.com/watch?v=sF5FyLeSR-8) |
| 6 | Data Analyst Roadmap | [roadmap.sh](https://roadmap.sh/data-analyst) |

> **Por que essas fontes?** Todas são produzidas por analistas ou ex-analistas com experiência de mercado real. A diversidade de perspectivas permitiu cruzar informações e identificar consensos sobre o caminho mais eficiente para entrar na área.

---

## ❓ Perguntas estratégicas e respostas do NotebookLM

As perguntas foram formuladas de forma progressiva — do geral ao específico — para mapear o campo de conhecimento da análise de dados.

---

### 1. Quais são as ferramentas fundamentais para um analista de dados?

As ferramentas fundamentais podem ser divididas em quatro categorias principais:

**📊 1. Planilhas (Excel ou Google Sheets)**  
O Microsoft Excel é o ponto de partida ideal e a ferramenta de BI mais popular do mundo. Conceitos-chave: fórmulas (`VLOOKUP`, `SUM`, `IF`), tabelas dinâmicas (pivot tables) e gráficos.

**🗄️ 2. Bancos de Dados (SQL)**  
O SQL é a linguagem padrão para se comunicar com bancos de dados e a habilidade técnica mais exigida em processos seletivos. Dialetos recomendados: PostgreSQL, MySQL ou Microsoft SQL Server.

**📈 3. Ferramentas de Visualização (BI)**  
Permitem criar dashboards interativos. As líderes de mercado são:
- **Power BI** — alta integração com o ecossistema Microsoft
- **Tableau** — valorizado por sua interface intuitiva e capacidade visual

**🐍 4. Linguagens de Programação**  
- **Python** — preferido pela versatilidade (Pandas, NumPy, Matplotlib, Seaborn)
- **R** — voltado para estatística e pesquisa acadêmica

**🔧 Ferramentas complementares:** Git, DBT, Hadoop, Spark, Loom (comunicação assíncrona), Slack

---

### 2. Qual o nível de SQL necessário para uma vaga júnior?

Para o nível júnior, é esperado um **nível intermediário** de SQL — não é necessário ser um especialista avançado.

**Fundamentos exigidos:**
- `SELECT`, `FROM`, `WHERE`, `GROUP BY`, `HAVING` (DQL)
- `JOIN` entre múltiplas tabelas
- `UPDATE`, `DELETE` (DML básico)

**Nível intermediário recomendado:**
- CTEs (Common Table Expressions) e Subqueries
- Window Functions
- Limpeza de dados: valores ausentes, duplicatas, transformações

**Preparação para processos seletivos:**
- Praticar questões de nível fácil/médio no LeetCode ou HackerRank
- Tempo estimado: 1–2 meses para a base, até 3,5 meses para conforto pleno

---

### 3. Quais conhecimentos de estatística são indispensáveis para um analista de dados júnior?

**Estatística Descritiva:**
- Medidas de tendência central: média, mediana, moda
- Medidas de dispersão: amplitude, variância, desvio padrão
- Distribuições: assimetria (skewness) e curtose (kurtosis)

**Análise de Relacionamentos e Inferência:**
- Correlação entre variáveis
- Regressão linear
- Testes de hipótese
- Conceitos básicos de probabilidade

**Aplicações práticas:**
- Identificação de outliers na limpeza de dados
- Testes A/B (diferencial para marketing)
- Modelagem preditiva básica

> Tempo de estudo sugerido: 1 a 2 meses de estudo focado.

---

### 4. O que as empresas mais procuram em um analista de dados júnior?

**🛠️ Habilidades técnicas essenciais ("S-Tier"):**
- SQL — aparece em 1 de cada 2 vagas
- Excel — nível intermediário (Pivot Tables, VLOOKUP, funções de agregação)
- Power BI ou Tableau — criação de dashboards interativos

**🧠 Conhecimento de domínio (Business Intuition):**
- Background em vendas, marketing, finanças ou operações é um diferencial crítico
- Capacidade de entender os desafios da equipe e alinhar a análise à estratégia

**🗣️ Comunicação e Storytelling:**
- Traduzir números em decisões e ações
- Documentar processos com clareza (Slack, Loom)

**📁 Portfólio com problemas reais:**
- Projetos que usem dados "sujos" para responder perguntas de negócio
- Narrativa completa: coleta → limpeza → análise → recomendação

**🚀 Atitude e mentalidade:**
- Fazer as perguntas certas durante processos seletivos
- Capacidade de aprendizado contínuo

---

### 5. Se eu for começar hoje a estudar, quais os primeiros passos devo tomar?

O caminho consensual entre as fontes leva de **6 a 12 meses**. A ordem recomendada:

| Etapa | Conteúdo | Tempo estimado |
|-------|----------|----------------|
| 1 | Excel — funções básicas, Pivot Tables, gráficos | 1–3 semanas |
| 2 | SQL — DQL, JOINs, CTEs, Window Functions | 1–2 meses |
| 3 | Estatística — média, desvio padrão, testes de hipótese | 1–2 meses |
| 4 | Power BI ou Tableau — dashboards interativos | 1–2 meses |
| 5 | Portfólio — projetos com dados reais + storytelling | Contínuo |

**Diferenciais críticos para 2026:**
- Aproveitar experiência anterior (vendas, marketing, etc.)
- Comunicação clara e documentação de processos
- Networking ativo — indicações valem mais do que candidaturas frias

---

## 🗺️ Mapa Mental gerado pelo NotebookLM

O NotebookLM gerou automaticamente um **mapa mental** com base nas fontes inseridas, organizando os conceitos em quatro grandes eixos temáticos. As imagens abaixo foram exportadas e salvas no projeto:

### Conceitos Fundamentais da Análise de Dados
<img src="Modulo1-Onboarding-IA/imgs/conceitos.png" alt="Mapa Mental - Conceitos Fundamentais" width="700"/>

### Diferenciais do Profissional de Dados
<img src="Modulo1-Onboarding-IA/imgs/diferencial.png" alt="Mapa Mental - Diferenciais" width="700"/>

### Matemática e Estatística Necessárias
<img src="Modulo1-Onboarding-IA/imgs/estatistica.png" alt="Mapa Mental - Estatística" width="700"/>

### Linguagens de Programação para Análise de Dados
<img src="Modulo1-Onboarding-IA/imgs/linguagens.png" alt="Mapa Mental - Linguagens" width="700"/>

---

## 💡 Prompts para pesquisas futuras
 
Os prompts abaixo foram desenvolvidos para aprofundar o estudo de análise de dados em sessões futuras com IAs como o NotebookLM ou o Claude.
 
---
 
### Prompt 1 — Diagnóstico de lacunas e plano de estudo personalizado
 
```
Você é um mentor especialista em análise de dados com experiência em
contratação e desenvolvimento de profissionais júnior. Analise as fontes
disponíveis e atue como um orientador de carreira.
 
Com base no perfil abaixo:
- Nível atual: [iniciante / tem base em Excel / já conhece SQL básico]
- Disponibilidade de estudo: [X horas por semana]
- Background profissional anterior: [ex: vendas, administrativo, TI]
- Objetivo: conseguir a primeira vaga de analista de dados em [X meses]
 
Faça o seguinte:
 
1. DIAGNÓSTICO: Identifique quais habilidades das fontes são mais urgentes
para o meu perfil específico e quais posso deixar para depois.
 
2. PLANO SEMANAL: Monte um cronograma semana a semana com tópicos,
recursos e metas mensuráveis — considerando minha disponibilidade.
 
3. MARCOS DE VALIDAÇÃO: Defina 3 checkpoints ao longo do plano onde eu
consiga avaliar se estou no ritmo certo ou preciso ajustar.
 
4. PROJETOS PRÁTICOS: Sugira 2 projetos de portfólio alinhados ao meu
background anterior que eu possa construir enquanto aprendo, com dados
reais e uma pergunta de negócio clara para cada um.
 
5. ARMADILHAS: Liste os 3 erros mais comuns que iniciantes cometem nessa
jornada e como evitá-los com base nas fontes.
 
Seja direto e específico. Evite recomendações genéricas.
```
 
> **Como usar:** Preencha os campos entre colchetes com o seu perfil real antes de enviar. Quanto mais específico você for, mais personalizada será a resposta.
 
---
 
### Prompt 2 — Simulação de processo seletivo técnico
 
```
Você é um recrutador técnico sênior de uma empresa de médio porte que
está contratando um analista de dados júnior. Seu papel é conduzir uma
entrevista técnica realista e dar feedback construtivo ao final.
 
Contexto da vaga simulada:
- Setor da empresa: [ex: varejo / financeiro / saúde / tecnologia]
- Stack de dados da empresa: SQL + Power BI + Excel
- Time: 3 analistas, relatórios diretos ao gerente de operações
 
Conduza a simulação em 4 etapas:
 
1. PERGUNTAS COMPORTAMENTAIS (2 perguntas): Foque em situações onde o
candidato precisou resolver um problema com dados ou comunicar resultados
para alguém não técnico.
 
2. DESAFIO TÉCNICO DE SQL: Apresente um cenário de negócio do setor
escolhido e peça para eu escrever uma query. Corrija e explique os erros
se houver, apontando o que o recrutador esperaria ver.
 
3. INTERPRETAÇÃO DE DASHBOARD: Descreva um dashboard hipotético com 3
métricas e peça para eu identificar um insight e sugerir uma ação para
o negócio com base nele.
 
4. FEEDBACK FINAL: Avalie minha performance simulada com:
   - Pontos fortes demonstrados
   - Lacunas críticas a corrigir antes de entrevistas reais
   - Uma nota de 0 a 10 com justificativa
   - Os próximos 2 tópicos que devo estudar com prioridade
 
Seja exigente mas justo. O objetivo é me preparar para a realidade
do mercado, não me poupar de críticas construtivas.
```
 
> **Como usar:** Substitua o campo `[setor da empresa]` pelo setor em que você quer trabalhar. Use este prompt após ter estudado SQL e BI para simular uma entrevista real e identificar pontos cegos antes de processos seletivos.
 
---

## ⚠️ Dificuldades encontradas durante o processo

Durante o uso do NotebookLM, foi identificada uma **limitação importante relacionada às fontes**:

> Por utilizar 5 vídeos produzidos por profissionais experientes, o modelo apresentou dificuldade em fornecer respostas direcionadas ao nível **júnior**. Ao perguntar sobre conhecimentos básicos de estatística para um analista de dados júnior, a resposta foi praticamente idêntica à de uma pergunta genérica sobre estatística para analistas — independentemente do nível especificado no prompt.

**Causa identificada:** As fontes, em sua maioria, abordam o tema de forma avançada e convergente. O NotebookLM se limitou ao que estava disponível nas fontes, sem inferir distinções de nível que não estavam explicitamente mapeadas.

**Aprendizado:** A qualidade e diversidade das fontes impacta diretamente a profundidade e especificidade das respostas. Para tópicos muito específicos (ex: nível júnior vs. sênior), é recomendável incluir fontes que abordem explicitamente essas distinções.

---

## 📚 Glossário de Conceitos

| Termo | Definição |
|-------|-----------|
| **SQL** | Structured Query Language — linguagem padrão para consulta e manipulação de bancos de dados relacionais |
| **DQL** | Data Query Language — subconjunto do SQL focado em consultas (`SELECT`) |
| **DML** | Data Manipulation Language — subconjunto do SQL para manipulação de dados (`INSERT`, `UPDATE`, `DELETE`) |
| **JOIN** | Operação SQL que combina linhas de duas ou mais tabelas com base em uma coluna relacionada |
| **CTE** | Common Table Expression — expressão de tabela temporária que simplifica queries complexas |
| **Window Function** | Função SQL que realiza cálculos sobre um conjunto de linhas relacionadas sem colapsar o resultado |
| **Pivot Table** | Tabela dinâmica que reorganiza e resume dados para facilitar a análise |
| **VLOOKUP / PROCV** | Função do Excel para buscar valores em uma tabela com base em uma chave |
| **BI (Business Intelligence)** | Conjunto de tecnologias e processos para transformar dados brutos em informações acionáveis |
| **Power BI** | Ferramenta de visualização de dados da Microsoft para criação de dashboards interativos |
| **Tableau** | Ferramenta de visualização de dados amplamente utilizada no mercado corporativo |
| **Python** | Linguagem de programação versátil muito usada em análise de dados (Pandas, NumPy, Matplotlib) |
| **Pandas** | Biblioteca Python para manipulação e análise de dados tabulares |
| **NumPy** | Biblioteca Python para computação numérica e operações com arrays |
| **Matplotlib / Seaborn** | Bibliotecas Python para criação de visualizações e gráficos |
| **Git** | Sistema de controle de versão distribuído para rastrear mudanças em código |
| **DBT** | Data Build Tool — ferramenta de transformação de dados no pipeline de engenharia de dados |
| **Outlier** | Valor atípico em um conjunto de dados que se distancia significativamente dos demais |
| **Desvio Padrão** | Medida de dispersão que indica o quanto os valores se afastam da média |
| **Teste de Hipótese** | Método estatístico para validar se uma descoberta é significativa ou fruto do acaso |
| **Teste A/B** | Experimento controlado que compara duas versões de algo para determinar qual performa melhor |
| **Correlação** | Medida estatística que indica o grau de relação entre duas variáveis |
| **Regressão** | Técnica estatística para modelar a relação entre variáveis e fazer previsões |
| **Storytelling com Dados** | Capacidade de comunicar insights de dados de forma clara e narrativa para audiências não técnicas |
| **Dashboard** | Painel visual interativo que exibe métricas e KPIs em tempo real |
| **KPI** | Key Performance Indicator — indicador-chave de desempenho de um processo ou negócio |
| **Hadoop** | Framework de código aberto para processamento distribuído de grandes volumes de dados |
| **Spark** | Motor de processamento de dados em larga escala, mais rápido que o Hadoop para certas operações |
| **NotebookLM** | Ferramenta de IA do Google que permite criar um assistente personalizado a partir de fontes próprias |
| **Loom** | Ferramenta de gravação de vídeo assíncrona usada para comunicação e documentação em times remotos |

---

## 🛠️ Tecnologias e ferramentas utilizadas neste módulo

![NotebookLM](https://img.shields.io/badge/Google-NotebookLM-4285F4?style=for-the-badge&logo=google&logoColor=white)
![YouTube](https://img.shields.io/badge/YouTube-Fontes-FF0000?style=for-the-badge&logo=youtube&logoColor=white)
![Claude](https://img.shields.io/badge/Anthropic-Claude-D97757?style=for-the-badge&logo=anthropic&logoColor=white)
![Markdown](https://img.shields.io/badge/Markdown-README-000000?style=for-the-badge&logo=markdown&logoColor=white)

---

*Documentação gerada como parte do Bootcamp Accenture - Python para Análise e Automação de Dados · DIO*