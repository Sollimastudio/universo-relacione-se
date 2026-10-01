# Relatório de Alterações — 2.0.0-rc.2

## Implementado nesta revisão
- subtítulo público claro para reduzir ambiguidade da marca;
- retirada de estado “review” da edição pública;
- página “MINDSETmagro em 60 segundos”;
- três rotas por Dia: Mínima, Completa e Aprofundada;
- guia não prescritivo de preparação para consulta;
- página operacional de parada/apoio;
- termo de compromisso não coercitivo;
- travessias com símbolo + numeral + nome;
- salvaguardas repetidas nos pontos de risco;
- mapa problema → ferramenta principal → opcional → sinal de parada;
- taxonomia simples de ferramentas;
- tabela “evidência × autoria × não testado”;
- revisão do ritmo editorial dos Dias 16–30;
- C30 sobre clareza do autoconceito (2026), com limite causal explícito;
- visualizações vetoriais acessíveis;
- HTML acessível com rotas, consentimento, exportação/importação, exclusão e migração v1→v2;
- Caderno PDF como versão imprimível e HTML como equivalente digital acessível;
- fonte canônica JSON para Livro/Workbook/HTML;
- mapa de sincronização e manifesto.

## Não executável neste ambiente
- revisão clínica independente por profissional habilitado;
- piloto com leitores reais;
- homologação em aparelho iPhone/Android real;
- leitor de tela real;
- teste de provedor LÚCIDA e entitlement do app privado, pois a fonte/runtime integrado não está disponível no container desta execução.


## Upgrade 2.1 — integração editorial completa

- Edição Dia a Dia aplicada aos 30 Dias: contraexemplo, critério observável, fecho do método e Fruto a observar.
- Fonte canônica estruturada criada em `source/content-source.json`, com fichas individuais `source/days/d01.json`–`d30.json`.
- Método Posicione-se™ integrado explicitamente ao Livro, Workbook e HTML.
- Sistema vetorial de 16 assets criado, com descrição SVG e inventário atualizado.
- Livro e pré-livro reexportados em A5 com capa frontal; Workbook reexportado em A4.
- QA de headings, links, SVG, HTML, texto extraído, páginas e layout executado.
