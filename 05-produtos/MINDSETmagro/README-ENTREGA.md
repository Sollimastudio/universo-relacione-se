# MINDSETmagro™ 2.1 — pacote editorial integrado

**Build:** `2.1.0-editorial-upgrade`  
**Uso:** candidato a piloto editorial fechado.  
**Autoria conceitual/metodológica:** Sol Lima.

## O que esta entrega contém

- `MINDSETmagro-2.1-Livro-Editorial-Final.pdf` — ebook editorial final, A5, 176 páginas.
- `MINDSETmagro-2.1-Workbook-Editorial-Final.pdf` — Workbook/Caderno Vivo para impressão, A4, 55 páginas.
- `MINDSETmagro-2.1-PreLivro-Editorial-Final.pdf` — pré-livro, A5, 15 páginas.
- `MINDSETmagro-2.0-Interativo.html` — versão digital interativa, com fonte embutida e schema v2.
- `source/content-source.json` — fonte canônica estruturada dos 30 Dias.
- `source/days/d01.json` a `d30.json` — fichas editoriais por Dia.
- `source/manifest.json` — manifesto de sincronização e inventário visual.
- `visual/` — sistema vetorial acessível de travessias, mapas, ciclo e ferramentas.
- `capas/` — artes de capa e frente usada nesta exportação.

## O que foi editado

1. **Dia a Dia:** cada um dos 30 Dias recebeu mapa metodológico, contraexemplo, critério observável de progresso, fecho de integração e orientação para observar o Fruto.
2. **Método Posicione-se™ visível:** os quatro pilares, a Árvore do Discernimento™ e o ciclo Perceber → Nomear → Distanciar → Discernir → Escolher → Praticar → Observar → Revisar foram integrados ao Livro e ao Workbook.
3. **Sistema visual:** seis travessias, mapa do método, ciclo, três rotas, Sala de Controle, MMI 2.0, Tradutor do Prato, Árvore e Frutos, Ritual da Nova Semente e capa/planta em vetor acessível.
4. **Fonte única:** metadados dos 30 Dias incorporados a `content-source.json` e ao HTML.
5. **Produção:** Livro em A5 com capa frontal; Workbook em A4; pré-livro regenerado; links e fontes validados.
6. **Limites preservados:** sem promessa de emagrecimento, diagnóstico, prescrição, meta corporal universal, jejum obrigatório ou suplemento universal.

## QA executado

- 30/30 Dias presentes no Livro e no Workbook.
- 30/30 blocos de mapa metodológico presentes em cada arquivo.
- 30/30 fichas JSON válidas e completas.
- 16 SVGs parseados sem erro XML.
- Links de imagens Markdown verificados.
- Fonte embutida do HTML validada com 30 Dias e build `2.1.0-editorial-upgrade`.
- PDF extraído com `pdftotext`; Livro e Workbook terminam no Dia 30.
- Page sizes verificados: Livro/Pré-livro A5; Workbook A4.
- Capa, abertura metodológica e Workbook renderizados para inspeção visual.

## Gates ainda obrigatórios

A edição está **pronta para piloto editorial fechado**, não para declarar validação clínica ou publicação irrestrita. Ainda são necessários:

- revisão humana final de claims e referências;
- leitura de prova externa, incluindo tecnologia assistiva;
- homologação em iPhone/Safari/leitor de tela;
- teste real de consentimento, persistência e erro do app/LÚCIDA;
- piloto cego para verificar se “magro” é compreendido como metáfora de excesso, e não como dieta ou corpo ideal;
- revisão profissional independente das trilhas de corpo, alimentação, movimento e saúde.

**Nota:** “10/10” nesta execução significa que os gates verificáveis foram tratados e documentados. Não substitui teste com leitores, validação clínica ou aprovação jurídica/regulatória.
