# Plano de ataque — Challenge 002 (rascunho de 10/10/2026, aguarda aprovação do Matheus)

Orçamento: 4 a 6 horas de trabalho efetivo. Cada etapa fecha com um commit.

## O que a primeira leitura mudou

O Dataset 1 (métricas) não se comporta como operação real:

| Sinal | Achado | Fonte |
|---|---|---|
| Volume | 8.469 tickets, não ~30 mil como diz o brief | `evidencias/01-primeira-leitura.txt` |
| Texto | 100% das descrições com `{product_purchased}` não substituído | idem |
| Rótulo | Assunto independe do tipo ("Refund request" aparece igual nos 5 tipos) | idem |
| Tempo | 1.365 de 2.769 fechados (49%) resolvidos *antes* da 1ª resposta | idem |
| Satisfação | CSAT plano: 1 a 5 com ~550 cada; média ~3,0 em todo canal, prioridade e tipo | idem |
| Datas | Todos os tickets entre mai–jun/2023; compras só em 2020–2021 | idem |

O Dataset 2 (texto IT) tem texto real, pré-processado (minúsculo, sem stopwords), com 47.837 linhas em 8 classes desbalanceadas (Hardware 28%, Administrative rights 4%).

13 dos 37 PRs do 002 já citam dado sintético. Notar o problema não diferencia; o diferencial é o que se faz depois.

## Etapas

1. **Diagnóstico com prova, não com opinião (D1).** Testar com estatística o que o dado sustenta: CSAT × canal/prioridade/tipo/tempo (Kruskal-Wallis, correlação, teste de permutação), tipo × assunto (qui-quadrado). Separar o que é medível (estrutura do backlog: 67% não fechados, 34% esperando o cliente) do que não é (tempo de resolução). Desperdício estimado com premissas explícitas, cada uma marcada como premissa. Fecha com "o que instrumentar nos próximos 30 dias para responder de verdade".
2. **O cruzamento.** Treinar o mesmo classificador nos dois datasets. No D1, texto → tipo deve dar ~20% (acaso), provando que os rótulos não carregam sinal. No D2, deve passar bem disso. É a prova de que o D2 é a base certa para a automação.
3. **Automação com abstenção (D2).** Classificador barato primeiro (TF-IDF + regressão logística), com curva cobertura × acurácia: rota automática só acima de um limiar de confiança; zona cinza vai para um LLM; o resto e as classes sensíveis vão para humano. "O que NÃO automatizar" justificado pela matriz de confusão e pela natureza da classe (HR Support envolve pessoa; Administrative rights envolve acesso e segurança; Miscellaneous não tem fila definida).
4. **Protótipo rodando com dado real.** Recebe o texto e devolve categoria, confiança, decisão (auto / LLM / humano) e motivo. Avaliado no conjunto de teste inteiro do D2, não em 3 exemplos. Custo por 1.000 tickets calculado por faixa.
5. **README e process log.** Template do repositório, commits por etapa, export das conversas.

## Decisões que são do Matheus

- [ ] Confirmar o challenge 002 (a recomendação de 01/10 se mantém: premia "o que não automatizar", que é a regra de produção do CRM da MarQ).
- [ ] LLM da zona cinza: só Qwen local (custo zero, roda no PC) ou Qwen + Claude comparados em amostra (mostra multimodelo e custo por token, assuntos que o João Vitor pergunta).
- [ ] Protótipo: página local simples (sem dependência nova; o C: tem ~3 GB livres) ou Streamlit.
- [ ] Onde entra a experiência real da MarQ (10 agentes no CRM, régua de humano no loop): seção "Por que essas regras" ou fora da submissão.
