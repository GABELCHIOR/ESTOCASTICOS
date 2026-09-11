#!/usr/bin/env python
"""
Ferramentas de extracao do PDF do Ross (Introduction to Probability Models,
13a ed., Academic Press / Elsevier, 2024).

O PDF e NATIVO (nao e escaneamento): a camada de texto e boa e as figuras sao
desenhos vetoriais. A prosa sai limpa; as formulas saem com as quebras de
linha do LaTeX (fracoes e somatorios empilhados), o que basta para localizar e
conferir o argumento. Para figura, use `recorte` -- as poucas figuras do livro
sao pequenas e ficam nitidas a 300 dpi.

Uso:
  python extrair.py texto  217 230         -> imprime o texto das paginas 217..230 (numeracao do PDF)
  python extrair.py texto  --livro 201 214 -> idem, mas usando a numeracao impressa no livro
  python extrair.py pagina 278 saida.png   -> renderiza a pagina inteira como PNG
  python extrair.py recorte 278 115 478 305 590 saida.png   -> recorta uma regiao (x0 y0 x1 y1, em pontos)
  python extrair.py imagens 278 pasta/     -> extrai as imagens embutidas da pagina (raras: quase tudo e vetorial)
  python extrair.py buscar "Chapman"       -> lista as paginas onde o termo aparece
  python extrair.py sumario                -> imprime o sumario (bookmarks) do PDF

Offset: CONSTANTE. Pagina do PDF = pagina do livro + 16, em todo o volume
(o cap. 4 comeca na p. 201 do livro = p. 217 do PDF). Use `livro2pdf` /
`pdf2livro` mesmo assim, para o codigo continuar valendo se o PDF mudar.
"""
import sys
import os
import glob

import fitz  # PyMuPDF

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Localiza o PDF sozinho: o nome do arquivo pode mudar, a pasta nao.
_pdfs = sorted(glob.glob(os.path.join(RAIZ, "*.pdf")), key=os.path.getsize, reverse=True)
if not _pdfs:
    raise SystemExit(f"nenhum PDF encontrado em {RAIZ}")
_ross = [p for p in _pdfs if "ross" in os.path.basename(p).lower()]
PDF = (_ross or _pdfs)[0]

OFFSET = 16          # pagina do PDF = pagina do livro + 16 (constante neste PDF)


def livro2pdf(p):
    """Pagina do livro -> pagina do PDF."""
    return p + OFFSET


def pdf2livro(n):
    """Pagina do PDF -> pagina do livro (None nas paginas preliminares)."""
    return n - OFFSET if n > OFFSET else None


def abrir():
    return fitz.open(PDF)


def cmd_texto(args):
    """Imprime o texto de um intervalo de paginas."""
    if args and args[0] == "--livro":
        args = args[1:]
        ini = livro2pdf(int(args[0]))
        fim = livro2pdf(int(args[1])) if len(args) > 1 else ini
    else:
        ini = int(args[0])
        fim = int(args[1]) if len(args) > 1 else ini
    doc = abrir()
    for n in range(ini, fim + 1):
        print(f"\n{'=' * 70}\n### PDF p.{n}  (livro p.{pdf2livro(n)})\n{'=' * 70}")
        print(doc[n - 1].get_text())


def cmd_pagina(args):
    """Renderiza uma pagina inteira como PNG a 200 dpi."""
    n, saida = int(args[0]), args[1]
    doc = abrir()
    pix = doc[n - 1].get_pixmap(dpi=200)
    pix.save(saida)
    print(f"salvo: {saida}  ({pix.width}x{pix.height})")


def cmd_recorte(args):
    """Recorta uma regiao retangular da pagina em alta resolucao."""
    n = int(args[0])
    x0, y0, x1, y1 = (float(v) for v in args[1:5])
    saida = args[5]
    doc = abrir()
    rect = fitz.Rect(x0, y0, x1, y1)
    pix = doc[n - 1].get_pixmap(dpi=300, clip=rect)
    pix.save(saida)
    print(f"salvo: {saida}  ({pix.width}x{pix.height})")


def cmd_imagens(args):
    """Extrai as imagens embutidas de uma pagina."""
    n, pasta = int(args[0]), args[1]
    os.makedirs(pasta, exist_ok=True)
    doc = abrir()
    for i, info in enumerate(doc[n - 1].get_images(full=True)):
        xref = info[0]
        img = doc.extract_image(xref)
        caminho = os.path.join(pasta, f"p{n}_{i}.{img['ext']}")
        with open(caminho, "wb") as f:
            f.write(img["image"])
        print(f"salvo: {caminho}  ({img['width']}x{img['height']})")


def cmd_buscar(args):
    """Lista as paginas em que um termo aparece."""
    termo = args[0]
    doc = abrir()
    for n, page in enumerate(doc, start=1):
        if page.search_for(termo):
            print(f"PDF p.{n}  (livro p.{pdf2livro(n)})")


def cmd_sumario(args):
    """Imprime os bookmarks do PDF (capitulos e secoes, com a pagina do PDF)."""
    doc = abrir()
    for nivel, titulo, pagina in doc.get_toc():
        print(f"{'  ' * (nivel - 1)}{titulo}  ->  PDF p.{pagina}  (livro p.{pdf2livro(pagina)})")


COMANDOS = {
    "texto": cmd_texto,
    "pagina": cmd_pagina,
    "recorte": cmd_recorte,
    "imagens": cmd_imagens,
    "buscar": cmd_buscar,
    "sumario": cmd_sumario,
}

if __name__ == "__main__":
    if len(sys.argv) < 2 or sys.argv[1] not in COMANDOS:
        print(__doc__)
        sys.exit(1)
    COMANDOS[sys.argv[1]](sys.argv[2:])
