#!/usr/bin/env python
"""
Localiza as regioes de figura numa pagina do PDF do Ross.

Este PDF e nativo: as figuras sao desenhos vetoriais (linhas, circulos, texto),
nao bitmaps. O que se faz aqui e aglomerar os tracados (`get_drawings`) em
caixas contiguas e apontar a legenda "Figure N.M" mais proxima. Atencao: as
chaves e barras de fracao das formulas tambem sao tracados vetoriais, por isso
o filtro `minimo` descarta o cisco e so sobram as caixas grandes.

  python figuras.py listar 278            -> candidatos na pagina 278 do PDF
  python figuras.py salvar 278 saida.png  -> salva o maior candidato

O capitulo 4 tem uma unica figura (Fig. 4.1, PDF p. 278). Quando o resultado
sair torto, recorte a mao com `extrair.py recorte`, que e sempre confiavel.
"""
import re
import sys
import os

import fitz

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from extrair import abrir, pdf2livro

LEGENDA = re.compile(r"^\s*(Figure|Table)\s+\d", re.I)


def caixas(page, margem=8.0, minimo=10.0, minimo_grupo=2000.0):
    """Agrupa os tracados vetoriais em caixas contiguas.

    Os tracados de uma figura sao pequenos (segmentos de reta, circulos dos
    nos), por isso `minimo` e baixo; o que separa figura de formula e o
    tamanho do GRUPO depois de aglomerado (`minimo_grupo`, em pontos²).
    """
    itens = [fitz.Rect(b["bbox"]) for b in page.get_image_info()]
    itens += [d["rect"] for d in page.get_drawings()]
    grupos = []
    for r in itens:
        if r.is_empty or r.width * r.height < minimo:
            continue
        alvo = fitz.Rect(r) + (-margem, -margem, margem, margem)
        juntar = [g for g in grupos if g.intersects(alvo)]
        for g in juntar:
            grupos.remove(g)
            r = fitz.Rect(r) | g
        grupos.append(fitz.Rect(r))
    mudou = True
    while mudou:
        mudou = False
        for i in range(len(grupos)):
            for j in range(i + 1, len(grupos)):
                a = grupos[i] + (-margem, -margem, margem, margem)
                if a.intersects(grupos[j]):
                    grupos[i] |= grupos[j]
                    del grupos[j]
                    mudou = True
                    break
            if mudou:
                break
    grupos = [g for g in grupos if g.width * g.height >= minimo_grupo]
    return sorted(grupos, key=lambda r: -(r.width * r.height))


def expandir(page, rect, folga=14.0):
    """Cresce a caixa para abarcar os rotulos da figura (nos, pesos, eixos).

    Nunca engole a legenda: "Figure N.M" marca o fim.
    """
    r = fitz.Rect(rect)
    mudou = True
    while mudou:
        mudou = False
        for b in page.get_text("blocks"):
            txt = b[4].strip()
            if not txt or LEGENDA.match(txt):
                continue
            tb = fitz.Rect(b[:4])
            if tb.width > page.rect.width * 0.7:
                continue
            if tb in r:
                continue
            if (r + (-folga, -folga, folga, folga)).intersects(tb):
                r |= tb
                mudou = True
    return r


def legenda_proxima(page, rect):
    melhor, dist = "", 1e9
    for b in page.get_text("blocks"):
        txt = b[4].strip().replace("\n", " ")
        if LEGENDA.match(txt):
            r = fitz.Rect(b[:4])
            d = abs(r.y0 - rect.y1) if r.y0 > rect.y0 else abs(rect.y0 - r.y1)
            if d < dist:
                melhor, dist = txt[:70], d
    return melhor


def cmd_listar(args):
    n = int(args[0])
    doc = abrir()
    page = doc[n - 1]
    print(f"PDF p.{n} (livro p.{pdf2livro(n)})  mediabox={page.rect}")
    for i, r in enumerate(caixas(page)):
        e = expandir(page, r)
        print(f"  [{i}] x0={e.x0:.0f} y0={e.y0:.0f} x1={e.x1:.0f} y1={e.y1:.0f}"
              f"  ({e.width:.0f}x{e.height:.0f})  <- {legenda_proxima(page, e)}")


def cmd_salvar(args):
    n, saida = int(args[0]), args[1]
    idx = int(args[2]) if len(args) > 2 else 0
    doc = abrir()
    page = doc[n - 1]
    cs = caixas(page)
    if not cs:
        raise SystemExit("nenhuma figura encontrada")
    r = expandir(page, cs[idx]) + (-8, -8, 8, 8)
    pix = page.get_pixmap(dpi=300, clip=r)
    pix.save(saida)
    print(f"salvo: {saida}  ({pix.width}x{pix.height})  de {r}")


if __name__ == "__main__":
    cmds = {"listar": cmd_listar, "salvar": cmd_salvar}
    if len(sys.argv) < 2 or sys.argv[1] not in cmds:
        print(__doc__)
        sys.exit(1)
    cmds[sys.argv[1]](sys.argv[2:])
