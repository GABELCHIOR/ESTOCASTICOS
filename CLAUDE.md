# ESTOCASTICOS — Ross, Introduction to Probability Models (13ª ed.)

Projeto de estudo autodidata de Processos Estocásticos.
Toda a produção é **em português (pt-BR)**.

Este projeto é irmão do `MULTI` (Johnson & Wichern) e do `PP_estudo`
(Montgomery): mesma estrutura, mesmo CSS, mesmo formato de aula. Diferenças:
o tema é **vermelho-carmim**, e há **três caixas matemáticas coloridas**
(teorema / demonstração / exemplo) que os outros dois projetos não têm.

## O livro

- Arquivo: `Introduction to Probability Models -- Sheldon M. Ross -- ( WeLib.org ).pdf` (4,3 MB, 859 páginas)
- Ross, S. M. — **13ª edição**, Academic Press / Elsevier, 2024 (ISBN 978-0-443-18761-2)
- 13 capítulos + soluções dos exercícios com asterisco (PDF p. 807) + índice

**É um PDF nativo**, não escaneamento: a camada de texto é boa (prosa limpa;
fórmulas saem com as quebras de linha do LaTeX, frações e somatórios
empilhados, o que basta para localizar e conferir). As figuras são vetoriais.
Não há páginas faltando.

**Offset constante: página do PDF = página do livro + 16.** Use
`livro2pdf()` / `pdf2livro()` de `ferramentas/extrair.py` mesmo assim.

| Cap. | Título | Livro p. | PDF p. | Status |
|---|---|---|---|---|
| 1 | Introduction to Probability Theory | 3 | 19 | — (pré-requisito) |
| 2 | Random Variables | 24 | 40 | — (pré-requisito) |
| 3 | Conditional Probability and Conditional Expectation | 103 | 119 | — (pré-requisito) |
| 4 | Markov Chains | 201 | 217 | ✅ aula `04-00-cadeias-de-markov.html` + folhas `04-98-definicoes-e-resultados.html` e `04-99-guia-de-prova.html` |
| 5 | The Exponential Distribution and the Poisson Process | 300 | 316 | — |
| 6 | Continuous-Time Markov Chains | 381 | 397 | — |
| 7 | Renewal Theory and Its Applications | 436 | 452 | — |
| 8 | Queueing Theory | 516 | 532 | — |
| 9 | Reliability Theory | 600 | 616 | — |
| 10 | Brownian Motion and Stationary Processes | 649 | 665 | — |
| 11 | Simulation | 688 | 704 | — |
| 12 | Coupling | 751 | 767 | — |
| 13 | Martingales | 780 | 796 | — |

## Preferências de estudo definidas

| Item | Decisão |
|---|---|
| Objetivo | Disciplina de Processos Estocásticos. Percurso **a partir do cap. 4** (cadeias de Markov); os caps. 1–3 são pré-requisito e só entram como referência pontual. Ênfase em entender de onde vem cada resultado. |
| Demonstrações | **Manter as que agregam à disciplina** — as que usam a propriedade de Markov, Chapman–Kolmogorov, condicionamento, lei forte, TCL, variância condicional. Pura álgebra fica resumida na prosa. |
| Caixas | Enunciados (teorema/proposição/corolário/lema) em `.caixa.teorema` (azul-índigo); demonstrações em `.caixa.demonstracao` (verde-musgo); exemplos em `.caixa.exemplo` (âmbar). Cada uma tem fundo tingido — **exceção deliberada** à regra do fundo neutro do MULTI, a pedido do usuário. |
| Exemplos e exercícios | Selecionar os mais relevantes para o aprendizado, não todos. |
| Software | **R**, funções de base. Duas funções-utilitário definidas na seção 2.2 do cap. 4 e reusadas: `potencia(P, n)` e `estacionaria(P)`. |
| Formato | **Arquivos HTML locais** em `estudo/`. Offline. Matemática em **MathML nativo** (sem CDN, sem JS). |
| Idioma | Português (pt-BR). Termos técnicos com o original em inglês entre parênteses na primeira ocorrência. |

## Como trabalhar aqui

**Geração sob demanda, capítulo por capítulo.** A cada sessão o usuário escolhe
o próximo capítulo e eu gero uma página de estudo focada.

Cada página contém, nesta ordem:

1. **Objetivo da aula** — o que se deve saber fazer ao final
2. **Conceito** em português, com a matemática em MathML; teoremas, demonstrações
   e exemplos nas três caixas coloridas
3. **Figuras** recortadas do PDF e **diagramas de estados em SVG inline**
   (`<figure class="diagrama">`, cores via variáveis do tema)
4. **Exemplos do livro resolvidos passo a passo**, com o código em R e a saída
5. **Cartões de recall ativo** — pergunta com resposta escondida (`<details>`)
6. **Exercícios selecionados** do fim do capítulo, com gabarito comentado

**Tom das aulas:** professor dando aula, não resumo. Explicar o *porquê*,
mostrar as derivações, ligar cada conceito a onde ele reaparece nos capítulos
seguintes.

**Regra dos números:** todo resultado numérico é *calculado* (numpy no
scratchpad), nunca copiado de memória, e conferido contra o livro. As saídas de
R nas páginas são escritas à mão a partir dos números conferidos em Python —
**R não está instalado no PATH**. Mantê-las simples, com poucas casas.

**Divergências encontradas no livro (cap. 4):** o Exemplo 4.24 imprime
π₀ = 0,07; o valor é 0,0624 → 0,06. Anotado na `.nota` do fim da página.

**Ganchos plantados pelo capítulo 4** (retomar quando o capítulo chegar):

- "ciclos i.i.d. entre visitas + lei forte" (Prop. 4.4) é a renovação em
  miniatura → **cap. 7**
- distribuição de equilíbrio da idade da lâmpada, `π_i = P{L ⩾ i}/E[L]`
  (Ex. 4.40) → **cap. 7**
- "adivinhar a estacionária e verificar que se reproduz" (Ex. 4.27, hotel
  Poisson) → redes de filas, **cap. 8**
- balanço detalhado e cadeia reversa → CTMC reversíveis, **cap. 6**
- identidade de Wald aparece disfarçada no Ex. 4.20 e na duração da ruína
  (Exerc. 59) → **caps. 7 e 13**
- falta de memória da exponencial usada no Ex. 4.43 (Gibbs) → **cap. 5**
- limites `Pⁿᵢⱼ → πⱼ` ficaram sem prova (acoplamento) → **cap. 12**
- tempo de parada, mencionado no Ex. 4.20 → **cap. 13**

## Ferramentas

`ferramentas/extrair.py` — localiza o PDF sozinho na raiz (prioridade ao nome
que contém "ross") e converte a numeração com `livro2pdf`/`pdf2livro`.
Redirecionar a saída de `texto` para arquivo quebra no Windows (`cp1252`): use
`PYTHONIOENCODING=utf-8`. Tem também `sumario` (bookmarks do PDF).
`ferramentas/figuras.py` — aglomera os traçados vetoriais da página em caixas
e aponta a legenda "Figure N.M" mais próxima (`minimo_grupo` descarta as
frações e chaves das fórmulas).

```bash
python ferramentas/extrair.py texto --livro 201 214
python ferramentas/extrair.py recorte 278 115 478 305 590 fig.png
python ferramentas/extrair.py buscar "Chapman"
python ferramentas/extrair.py sumario
python ferramentas/figuras.py listar 278
```

Dependências: `pymupdf` (instalado). Python 3.13.

O cap. 4 tem uma única figura (Fig. 4.1, PDF p. 278, recorte
`115 478 305 590`). Os demais diagramas de estados são SVG desenhados na aula.

## Folhas de consulta

Cada capítulo pode ter, além da aula, **duas** folhas para levar impressas na
prova. O modelo foi um guia de MS512 que o usuário trouxe — A4, duas colunas,
densa, caixas coloridas com barra de título.

| Arquivo | O que é | Cap. 4 |
|---|---|---|
| `NN-98-definicoes-e-resultados.html` | **só enunciados**: definição, teorema, proposição, corolário e fórmula numerada, na ordem do livro, com hipóteses explícitas e a página do Ross em cada caixa. **Sem exemplo, sem exercício** — é a cola para consultar no meio de uma questão. | 5 pág. |
| `NN-99-guia-de-prova.html` | guia de estudo: mapa de decisão, receitas, exemplos numéricos, "fato ou fake", fórmulas de bolso. | 6 pág. |

As duas usam o mesmo `guia.css`; mudam as classes de caixa e a legenda.

**Ela não usa `estilo.css`.** Carrega `tema.css` + **`assets/guia.css`**, que é
o layout próprio da folha: uma coluna na tela, `columns: 2` A4 na impressão,
corpo 8,2 pt. Cinco caixas, cada uma com `--cor`/`--cor-fundo` próprias:

| Classe | Cor | Uso |
|---|---|---|
| `.bloco.teo` | azul-índigo | definição, teorema, proposição, corolário |
| `.bloco.dem` | verde-musgo | por que é verdade (demonstração curta) |
| `.bloco.ex` | âmbar | exemplo numérico de fixação |
| `.bloco.rec` | carmim | receita: passo a passo para a prova |
| `.bloco.arm` | roxo-uva | armadilha, "fato ou fake", erro clássico |

A folha `NN-98` usa outras três classes sobre as mesmas paletas: `.def`
(azul, definição), `.res` (carmim, teorema/proposição/corolário/fórmula) e
`.obs` (roxo, as *Remarks* do próprio livro).

**O título da caixa tem estrutura fixa** — o `h4` é `display:flex` e precisa de
**exatamente dois filhos**:

```html
<h4><span class="tit">Proposição 4.4</span><span class="pg">livro 224</span></h4>
```

Sem o `.tit`, um `<math>` dentro do título vira um item de flex à parte e o
`gap` rasga a frase no meio. (O `.pg` já foi `float: right` e sumia em título
longo: o float ia para a segunda linha e o `overflow: hidden` da caixa o
cortava.)

Outras peças: `.chave` (destaque carmim inline), `.miudo` (corpo menor para o
detalhe), `.rot-e`/`.rot-s` (Enunciado./Solução.), `.qed`, `.so-tela` (aviso
que some no papel), `.legenda` (a tira de cores do cabeçalho).

**Conteúdo do cap. 4** (o molde para os próximos): mapa de decisão "o que a
questão pede × que ferramenta usar" → montar a cadeia → *n* passos → classificação
→ longo prazo → absorção → ramificação → reversibilidade → MCMC → MDP/HMM →
"fato ou fake" + checklist → fórmulas de bolso. Poucos exercícios, muitos
exemplos curtos: foi o pedido explícito do usuário ("não precisa ter tantos
exercícios, nem uma prova toda corrigida").

### Gerar o PDF

O Chrome está instalado e faz a impressão sem abrir janela:

```powershell
# servir a pasta (ou use .claude/launch.json) e imprimir sem abrir janela
& "C:\Program Files\Google\Chrome\Application\chrome.exe" --headless=new --disable-gpu `
  --no-pdf-header-footer --print-to-pdf="estudo\cap04\04-98-definicoes-e-resultados.pdf" `
  "http://localhost:8765/estudo/cap04/04-98-definicoes-e-resultados.html"
```

**Espere ~4 s** antes de ler o arquivo: o Chrome devolve o prompt antes de
terminar de escrever o PDF.

Precisa ser por **http://**, não `file://` (o CSS relativo não carrega no
headless a partir de file). Os PDFs ficam **fora do git** (`*.pdf` no
`.gitignore`) — são artefatos derivados. Entregue-os também em
`C:\Users\gabri\Downloads\`, que é onde o usuário guarda esse tipo de
guia (e onde estava o MS512 que serviu de modelo).

**Armadilha da impressão:** no papel nada rola. `overflow-x: auto` (código,
`.rolagem`, `math[display="block"]`) vira *conteúdo cortado* no PDF. O
`@media print` do `guia.css` já neutraliza os três, mas **equação larga demais
continua vazando para fora da coluna** — a correção é quebrar a equação em duas
linhas ou encurtar os rótulos, não mexer no CSS. Confira sempre o PDF página a
página (renderize com pymupdf e leia as imagens).

## Convenção de nomes

Igual ao MULTI. **Números sempre com dois dígitos**, minúsculas, sem acento,
hífen entre palavras.

| O quê | Padrão | Exemplo |
|---|---|---|
| Pasta do capítulo | `capNN/` | `cap04/` |
| Página do capítulo inteiro | `NN-00-titulo.html` | `cap04/04-00-cadeias-de-markov.html` |
| Folha só de enunciados | `NN-98-definicoes-e-resultados.html` | `cap04/04-98-definicoes-e-resultados.html` |
| Guia de prova do capítulo | `NN-99-guia-de-prova.html` (`9x` = apêndice, ordena por último) | `cap04/04-99-guia-de-prova.html` |
| Figura | `img/fig-NN-MM.png` | `cap04/img/fig-04-01.png` |

Ao criar uma aula nova, acrescentar o link em **três** lugares de
`estudo/index.html`: a lista da barra lateral (trocar o `<li class="adiante">`
por um `<li>` com link — com folha de consulta, vira `<details class="sub">`
com os dois links, como no cap. 4), o cartão em "Aulas disponíveis" (trocar o
`<span class="cartao pendente">` por `<a class="cartao">`) e a linha da tabela
da seção **"Menu"**. A folha de consulta ganha ainda um cartão na seção
**"Folhas de consulta"**, e um link no `.extras` e no `.nav-rodape` da aula. E acertar o `.nav-rodape` (anterior/próxima) da aula
vizinha — o do cap. 4 hoje diz "Cap. 5 … (em breve)" sem link.

## Layout das páginas

O CSS está separado em dois arquivos e essa separação é para valer:

- `estudo/assets/tema.css` — **única** fonte de cores, fontes e medidas, com
  bloco `@media (prefers-color-scheme: dark)`. Tema: **vermelho-carmim**. Regra
  geral: superfícies neutras, cor só em tipografia e filetes. **Exceção:** as
  variáveis `--teorema/--teorema-fundo`, `--demo/--demo-fundo`,
  `--exemplo/--exemplo-fundo` dão fundo tingido às três caixas matemáticas.
  `--ambar` (avisos) aqui é roxo-uva, porque o âmbar de verdade ficou para os
  exemplos.
- `estudo/assets/estilo.css` — só estrutura, copiado do MULTI e acrescido de:
  `.teorema`, `.demonstracao`, `.exemplo` (caixas), `.qed` (o ∎ à direita),
  `.teorema + .demonstracao { margin-top: -0.9rem }` (a demonstração cola no
  enunciado que prova), e `figure.diagrama` com as classes de SVG `.no`,
  `.no-abs` (estado absorvente, sombreado), `.seta`, `.rot`, `.est`, `.ponta`.
  **Nunca escrever cor literal aqui.**

O `<head>` de toda página de aula:

```html
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow">
<title>Cap. N — Título</title>
<link rel="stylesheet" href="../assets/tema.css?v=1">
<link rel="stylesheet" href="../assets/estilo.css?v=1">
```

Tudo o mais (grade de quebra de coluna, `.topo + .objetivo`, barra lateral
fixa com `<details class="sub">`, `h3` com `id="{h2}-{k}"`, `td.txt`,
`?v=` a incrementar ao mexer no CSS) é idêntico ao MULTI — ver o CLAUDE.md
de lá se precisar do detalhe.

**Diagramas SVG.** Cada `<svg>` define o seu próprio `<marker id="pontaN">`
(ids únicos por página: `ponta1`, `ponta2`, …) e as setas usam
`style="marker-end:url(#pontaN)"`. Auto-laços são `path` cúbicos que saem e
voltam ao mesmo círculo.

**MathML — armadilhas já encontradas:**

- Espaço nas bordas de `<mtext>` é descartado (`<mtext>para algum </mtext>`
  cola na letra seguinte). Use `<mspace width="0.35em"/>` fora do `<mtext>`.
- `<mfrac linethickness="0">` para coeficientes binomiais.
- Um `Write` só não cabe: a aula tem ~1 900 linhas. Escrever em partes no
  scratchpad e concatenar com `cat >>`; validar o aninhamento com um
  `html.parser` a cada passada.

## Preview local

O painel de navegador do Claude Code serve `file://` como snapshot (`data:`) e
não carrega o CSS relativo. Use `.claude/launch.json` (fora do git), que sobe
`python -m http.server 8765`, e abra
`http://localhost:8765/estudo/cap04/04-00-cadeias-de-markov.html`.

## Estrutura

```
ESTOCASTICOS/
├── Introduction to Probability Models -- ... .pdf   (fora do git: .gitignore)
├── index.html              redireciona para estudo/ — serve ao GitHub Pages
├── README.md               documentação pública do repositório
├── CLAUDE.md               este arquivo
├── .gitignore  .gitattributes  robots.txt
├── ferramentas/
│   ├── extrair.py
│   └── figuras.py
└── estudo/
    ├── index.html          painel com o percurso
    ├── assets/
    │   ├── tema.css        cores, fontes, medidas (vermelho-carmim)
    │   ├── estilo.css      estrutura e layout das aulas
    │   └── guia.css        layout da folha de consulta (A4, 2 colunas)
    └── cap04/
        ├── 04-00-cadeias-de-markov.html
        ├── 04-98-definicoes-e-resultados.html   (+ .pdf, fora do git)
        ├── 04-99-guia-de-prova.html             (+ .pdf, fora do git)
        └── img/fig-04-01.png
```

O repositório está em <https://github.com/GABELCHIOR/ESTOCASTICOS> (remoto
`origin`, branch `main`). O PDF fica de fora pelo `.gitignore`. Para o GitHub
Pages servir o site, ativar em Settings → Pages → branch `main`, pasta `/`
(raiz); a `index.html` da raiz redireciona para `estudo/`.

## Progresso

**Capítulo 4 pronto** (2026-09-11): aula completa. **Duas folhas de consulta
do cap. 4 prontas** (2026-09-22): `04-99-guia-de-prova.html` (6 pág.) e
`04-98-definicoes-e-resultados.html` (5 pág., só enunciados — pedido explícito
do usuário: "uma cola rápida para olhar se esquecer algo durante a resolução
do exercício").

Próximo: capítulo 5 (The Exponential Distribution and the Poisson Process,
livro 300–380, PDF 316–396). Ao gerar, retomar os ganchos: falta de memória
(usada no Ex. 4.43), e a distribuição de equilíbrio do Ex. 4.40 como aperitivo
da renovação. Gerar **aula + folha** para cada capítulo daqui em diante.
