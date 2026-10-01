# CardioIA — A Nova Era da Cardiologia Inteligente

**FIAP — Curso de Inteligência Artificial**
**Fase 1: Batimentos de Dados**

## Sobre o projeto

O CardioIA propõe simular um ecossistema cardiomédico digital, unindo Machine Learning, Processamento de Linguagem Natural, Visão Computacional e IoT em um único fluxo: triagem clínica, apoio ao diagnóstico, monitoramento remoto e estratificação de risco cardiovascular.

Nesta primeira fase — Batimentos de Dados — o foco não é construir modelos, e sim organizar e documentar a base de dados numéricos, textuais e visuais que vão sustentar as próximas etapas do projeto.

**Autoria:** Victor Henrique de Almeida — RM: 657469

> Esta fase foi feita pelo Victor ([repositório original](https://github.com/almeidavictorhenrique-glitch/CardioAI)) e serve de base para as fases seguintes. As imagens não foram copiadas por causa do tamanho; estão no link do Drive abaixo.

---

## Parte 1 — Dados Numéricos (IoT e Tabela Clínica)

Link do dataset completo: [Google Drive](https://drive.google.com/drive/folders/1espZJq5dX2Z-ZOFa7JLdZH13n8hVgt7O?usp=sharing)

### Sobre os dados

A base numérica reúne 303 registros de pacientes, com 14 variáveis clínicas e demográficas por paciente.

- **Origem:** UCI Machine Learning Repository — Heart Disease Dataset (subconjunto de Cleveland).
- **Governança e LGPD:** os dados passaram por anonimização, sem nenhuma informação pessoal identificável.
- **Distribuição do alvo (target_binary):** 164 pacientes saudáveis (54,1%) e 139 diagnosticados com doença cardíaca (45,9%).
- **Qualidade dos dados:** apenas 6 valores ausentes no total (4 em `ca`, 2 em `thal`), corrigidos por imputação da moda (`ca = 0.0`, `thal = 3.0`).

### Variáveis mais relevantes

1. **`thalach` (frequência cardíaca máxima):** útil para monitoramento via wearables, ajuda a identificar estresse miocárdico em tempo real.
2. **`trestbps` (pressão arterial em repouso):** hipertensão é uma das principais DCNTs ligadas a risco cardiovascular.
3. **`oldpeak` e `exang` (depressão de ST e angina induzida por esforço):** indicadores diretos de isquemia miocárdica.
4. **`ca` (vasos principais por fluoroscopia):** reflete o grau de aterosclerose coronariana.
5. **`age` e `sex`:** variáveis demográficas que influenciam diretamente a incidência de insuficiência cardíaca e hipertensão.

---

## Parte 2 — Dados Textuais (NLP)

Arquivos de texto para treinamento e extração de linguagem natural: [Google Drive](https://drive.google.com/drive/folders/1TQCcfs491hN-YBmndVq4uAwhV0fbjWl9?usp=sharing)

Fontes usadas: revisão fisiopatológica sobre insuficiência cardíaca (InCor/USP) e análise da PNS 2013–2019 sobre cuidado com hipertensão no SUS e na rede privada.

### Possíveis aplicações de NLP nesses dados

- **Reconhecimento de entidades (NER):** extrair termos técnicos de prontuários e literatura médica (fração de ejeção, dispneia, remodelamento ventricular, inibidores da ECA, diuréticos) para alimentar uma base de conhecimento.
- **Apoio à decisão e sumarização:** minerar artigos e diretrizes do SUS para automatizar recomendações de acompanhamento clínico.
- **Análise de sintomas relatados:** processar relatos de pacientes sobre sintomas e impacto na qualidade de vida, como fadiga e limitações funcionais (classes NYHA).

---

## Parte 3 — Dados Visuais (Visão Computacional)

Link das imagens: [Google Drive](https://drive.google.com/drive/folders/1khYUNi0oGlA9sod2gkB6wFPD_6K9Vfoy?usp=sharing)

### Sobre as imagens

O conjunto reúne 1.684 imagens médicas de eletrocardiogramas e raio-x de tórax, com boa distribuição entre classes:

- Exames normais: 858 imagens (50,95%)
- Exames com alterações: 826 imagens (49,05%)

### Aplicações possíveis

- **Classificação de padrões:** usar CNNs para diferenciar exames normais de patológicos, identificando cardiomegalia em raio-x ou arritmias/desvios de segmento ST em ECGs.
- **Segmentação anatômica:** delimitar a silhueta cardíaca e grandes vasos para calcular o índice cardiotorácico automaticamente.
- **Triagem pré-diagnóstica:** com o dataset balanceado, é possível treinar classificadores binários confiáveis para priorizar exames alterados na fila do especialista.

---

## Governança, equidade e viés nos dados

- **Equidade regional e socioeconômica:** a literatura mostra disparidades no acesso a exames e orientações sobre hipertensão e doenças cardíacas entre regiões do Brasil (com menor oferta no Norte/Nordeste) e entre classes econômicas. Isso precisa ser levado em conta para não reforçar essas desigualdades no modelo.
- **Viés demográfico:** é importante calibrar os dados por idade e sexo, já que a manifestação da doença varia bastante entre esses grupos.
- **Privacidade e LGPD:** todos os dados (clínicos, textuais e de imagem) foram anonimizados antes do uso.
