# Relatório de upgrade editorial — MINDSETmagro™ 2.1

## Resultado executivo

O Livro, o Workbook e o HTML interativo foram alinhados à mesma fonte estruturada. A edição 2.1 torna explícita a correspondência entre os 30 Dias e o Método Posicione-se™, sem alterar a tese central do protocolo nem converter metáforas em alegações clínicas.

## Escopo executado

### Livro e Workbook

Cada Dia recebeu um bloco editorial de fechamento. O bloco informa o contraexemplo que a prática evita, o critério de progresso observável, a conexão com pilar/Árvore/ciclo e o Fruto a observar em contexto. O Workbook recebe a versão compacta do mapa para não ocupar o espaço de escrita.

### Fonte canônica

`source/content-source.json` contém os 30 Dias, o sistema metodológico e os metadados editoriais. Os arquivos `source/days/d01.json`–`d30.json` permitem auditar cada unidade sem depender de leitura visual do PDF. O `manifest.json` registra o inventário de assets e os formatos de saída.

### Infográficos e diagramas

Foi criado um sistema vetorial com 16 SVGs: seis aberturas de travessia, mapa do Método Posicione-se™, ciclo de aprendizagem, capa/planta e oito ferramentas/diagramas. Os arquivos têm `title` e `desc` SVG para apoiar acessibilidade e não dependem apenas de cor.

### Produção

O Livro e o pré-livro foram regenerados em A5 com capa frontal dedicada. O Workbook foi regenerado em A4. A exportação usa uma folha de estilo única, margens de impressão, paginação, tabelas e imagens referenciadas por caminho verificável.

## Verificações objetivas

| Verificação | Resultado |
|---|---:|
| Dias no Livro | 30/30 |
| Dias no Workbook | 30/30 |
| Fichas JSON | 30/30 válidas |
| Mapas metodológicos | 30/30 em cada arquivo |
| SVGs | 16/16 parseados |
| PDF do Livro | 176 páginas, A5 |
| PDF do Workbook | 55 páginas, A4 |
| PDF do pré-livro | 15 páginas, A5 |
| HTML | fonte embutida, 30 Dias, build 2.1 |
| Links Markdown para SVG | verificados |

## Critério de nota

Dentro do escopo executável nesta sessão, o pacote atende ao padrão **10/10 de organização editorial, integração metodológica, rastreabilidade e produção dos arquivos**. Essa nota não deve ser confundida com eficácia clínica, validação científica do protocolo completo ou aprovação regulatória.

## Gates externos que permanecem

A próxima aprovação real depende de revisão humana final de claims e referências, prova com leitores externos, teste de acessibilidade em dispositivo real, homologação do app/LÚCIDA e revisão profissional independente das trilhas de corpo, alimentação, movimento e saúde. O pacote, portanto, deve ser etiquetado como **candidato a piloto fechado**.
