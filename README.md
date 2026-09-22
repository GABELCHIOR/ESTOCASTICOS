# Processos Estocásticos — caderno de estudo

Caderno de estudo autodidata de **Processos Estocásticos**, em português, montado
a partir de Ross, S. M., *Introduction to Probability Models*, 13ª edição
(Academic Press / Elsevier, 2024). Começa pelo capítulo 4 (cadeias de Markov),
onde começa a matéria nova; os capítulos 1–3 são a probabilidade que a
disciplina supõe conhecida.

São páginas HTML locais, sem dependência de rede: abrem direto no navegador,
funcionam offline, e a matemática é **MathML nativo** — sem CDN, sem JavaScript
de renderização.

👉 **Comece por [`estudo/index.html`](estudo/index.html).**

## O que já existe

| Cap. | Título | Conteúdo |
|---|---|---|
| 4 | [Cadeias de Markov](estudo/cap04/04-00-cadeias-de-markov.html) | A propriedade de Markov e a matriz `P`; Chapman–Kolmogorov com demonstração e `P⁽ⁿ⁾ = Pⁿ`; a cadeia `Wₙ` para "entrar num conjunto até o tempo m"; classes, recorrência e transiência (Prop. 4.1, Cor. 4.2, com as demonstrações) e o **passeio aleatório via Stirling**; proporções de longo prazo, `πⱼ = 1/mⱼ` pela lei forte, Teorema 4.1 e as três leituras de `π` (proporção, estacionária, limite); ruína do jogador, estados transientes `S = (I − P_T)⁻¹`, ramificação, reversibilidade e o critério de Kolmogorov, Hastings–Metropolis e Gibbs, processos de decisão e cadeias ocultas (forward, backward, Viterbi). 37 exemplos, 24 demonstrações, 15 cartões de recall e 18 blocos de exercícios resolvidos. |

Além da aula, o capítulo 4 tem uma
[**folha de consulta para a prova**](estudo/cap04/04-99-guia-de-prova.html):
a matéria inteira condensada — mapa de decisão "o que a questão pede × que
ferramenta usar", enunciados, as demonstrações curtas, um exemplo numérico por
ideia, "fato ou fake" e as fórmulas de bolso. Abre em uma coluna na tela e sai
em **duas colunas A4** (6 páginas) ao imprimir com Ctrl+P.

Cada aula traz o objetivo, o conceito com as derivações, os **enunciados,
demonstrações e exemplos em caixas de cores distintas** (azul, verde e âmbar),
figuras do livro e diagramas de estados, os exemplos resolvidos passo a passo
com código em **R**, cartões de recall ativo e uma seleção de exercícios com
gabarito comentado. **Todo resultado numérico foi recalculado**, não copiado.

## Estrutura

```
├── index.html              redireciona para estudo/
├── estudo/
│   ├── index.html          painel do percurso
│   ├── assets/
│   │   ├── tema.css        cores, fontes e medidas (tema vermelho-carmim)
│   │   ├── estilo.css      estrutura e layout das aulas
│   │   └── guia.css        layout da folha de consulta (A4, duas colunas)
│   └── capNN/
│       ├── NN-00-titulo.html      a aula
│       ├── NN-99-guia-de-prova.html   a folha de consulta
│       └── img/            figuras recortadas do PDF
└── ferramentas/
    ├── extrair.py          texto, páginas e recortes do PDF
    └── figuras.py          detecção automática de figuras
```

Trocar de tema é trocar `assets/tema.css`: todas as cores e medidas do site
estão ali, em variáveis CSS, e `estilo.css` nunca traz cor literal. Há suporte a
modo claro e escuro pelo `prefers-color-scheme`.

## Sobre o PDF do livro

O PDF **não** está no repositório — é obra protegida por direitos autorais. As
ferramentas o localizam sozinhas se você colocar a sua própria cópia na raiz da
pasta. É um PDF nativo (não escaneado): a camada de texto é boa e a numeração
é constante, **página do PDF = página do livro + 16**.

## Uso das ferramentas

```bash
python ferramentas/extrair.py texto --livro 201 214      # texto pela numeração do livro
python ferramentas/extrair.py recorte 278 115 478 305 590 fig.png
python ferramentas/extrair.py buscar "Chapman"
python ferramentas/extrair.py sumario
python ferramentas/figuras.py listar 278
```

Requer Python 3 e `pymupdf`.

## Aviso

Material de estudo pessoal. As páginas reproduzem figuras e enunciados da obra
original para fins de estudo; todas trazem `noindex, nofollow` e o repositório
inclui um `robots.txt` restritivo. Não é substituto do livro — é um caderno de
quem está lendo o livro.
