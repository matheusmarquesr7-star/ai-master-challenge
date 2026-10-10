# Diário do processo

Registro cronológico de como o trabalho foi feito: o que pedi à IA, o que ela fez, onde desconfiei e o que decidi.
Ferramenta principal: Claude Code (Opus 5.5) no VS Code, orquestrando scripts Python locais.

---

## 10/10/2026 — Preparação

**O que pedi:** preparar o começo do desafio a partir do que já tinha levantado sobre o processo seletivo em 01–02/10 (escolha do challenge, régua das revisões publicadas nos PRs).

**O que a IA fez:**
1. Clonou o repositório e releu README, guia de submissão, CONTRIBUTING e o brief do 002.
2. Baixou os dois datasets do Kaggle pela URL pública (sem conta) e escreveu `scripts/baixar_dados.py` para qualquer pessoa reproduzir.
3. Antes de qualquer análise, rodou uma leitura só com a biblioteca padrão para ver se o dado tem sinal (`scripts/01_primeira_leitura.py` → `evidencias/01-primeira-leitura.txt`).

**O que apareceu:** o Dataset 1 tem 8.469 linhas (o brief fala em ~30 mil), o texto vem com placeholder não substituído em 100% das linhas, metade dos tickets fechados termina antes da primeira resposta e a satisfação é uniforme de 1 a 5 em qualquer recorte. O Dataset 2 tem texto real em 8 classes.

**Checagem de contexto:** a IA leu os 181 PRs abertos. 37 são do 002 e 13 deles já falam em dado sintético. Conclusão: apontar o problema é o mínimo, não o diferencial.

**Decisões pendentes (minhas):** ver `docs/plano.md`, seção "Decisões que são do Matheus".

<!-- Próximas entradas: uma por etapa, com o prompt, o erro da IA quando houver, a correção e a decisão tomada. -->
