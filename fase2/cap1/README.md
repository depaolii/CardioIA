# Fase 2 — Cap. 1: IA no Estetoscópio Digital

**Aluno:** Marcello De Paoli Sobrinho — RM: 567562

## Parte 1 — Extração de sintomas

| Arquivo | O que é |
|---|---|
| [frases_sintomas_pacientes.txt](parte1/frases_sintomas_pacientes.txt) | 10 relatos de pacientes |
| [mapa_conhecimento_sintomas.csv](parte1/mapa_conhecimento_sintomas.csv) | Sintomas → doença associada |
| [diagnostico_ia_final_v2.py](parte1/diagnostico_ia_final_v2.py) | Lê os relatos e sugere o diagnóstico |

Como rodar:

```bash
cd parte1
python diagnostico_ia_final_v2.py
```

O código remove acentos e pontuação e verifica se todas as palavras de um sintoma aparecem na frase. As 10 frases geram diagnóstico.

**Limitação:** uma frase pode bater com mais de uma doença ao mesmo tempo.

## Parte 2 — Classificador de risco

| Arquivo | O que é |
|---|---|
| [frases_risco.csv](parte2/frases_risco.csv) | 62 frases rotuladas como alto ou baixo risco |
| [classificador_risco.ipynb](parte2/classificador_risco.ipynb) | TF-IDF + classificação + avaliação |

Para rodar, abra o notebook no Google Colab e execute tudo. Ele pede o upload do CSV.

### Resultados

| Modelo | Acurácia no teste | Validação cruzada |
|---|---|---|
| Regressão Logística | 75% | 79% |
| Árvore de Decisão | 56% | 77% |

### Distorções observadas

- "Peito" é a palavra com mais peso. Até "minha mãe está com dor no peito" deu alto risco.
- O modelo ignora negação: "não sinto dor no peito" deu alto risco.
- Palavras como "de" e "para" entraram entre as de maior peso, o que mostra que o modelo aprendeu o jeito de escrever das frases.
- Com poucos dados, o resultado varia muito de uma divisão de teste para outra.
