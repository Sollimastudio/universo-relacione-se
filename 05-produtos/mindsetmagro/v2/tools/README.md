# Renderizadores MINDSETmagro 2.0

A fonte editorial é `../days/*.json`, `../prebook.json` e `../postbook.json`. Referências completas vêm de `../research/claims-evidence.json`. Não editar PDFs/HTML para corrigir conteúdo: editar a fonte e gerar novamente.

## Gerar

Dependências Python: reportlab, svglib. Fontes DejaVu Sans e Serif em `/usr/share/fonts/truetype/dejavu`.

```sh
python tools/build_assets.py
python tools/render.py --output /caminho/absoluto/output
```

O comando recusa conjuntos sem os dias 1–30 completos ou IDs de campo duplicados. Gera livro, Caderno imprimível, referência HTML e snapshot/hash da fonte. O Caderno usa as mesmas perguntas e IDs do livro/app. Referências são anexadas sem reescrever as alegações.

## Direção de arte

Verde profundo `#25483e`, papel claro `#faf8f1`, texto escuro, linhas de apoio discretas. Serif nos títulos editoriais; sans nos controles e leitura digital. Diagramas vetoriais têm função explicativa; dias de exercícios predominantemente verbais podem dispensar imagem. Sem balança como emblema, sem corpo ideal imposto, sem anatomia cerebral decorativa. Todos os arquivos SVG são editáveis e exportáveis. `visual-assets.json` decide a colocação por dia; `v-dNN` aponta para o diagrama correspondente.

MMI enfatiza função/cuidado, aparência opcional. Árvore tem cajus e explicita que resultados não medem valor pessoal. Açúcar usa rótulo fictício identificado, com cálculo de massa exato; não atribui a um refrigerante real nem usa copo cheio como equivalência. Sala de Controle declara ser metáfora.

## Referência HTML local

Abrir `MINDSETmagro-2.0-Interativo.html`. A primeira escolha é salvar apenas no navegador ou usar sem salvar. localStorage não é cofre nem sincronização de conta. Respostas podem ser exportadas/importadas como JSON; importação confere esquema, versão da fonte, IDs, tipos e limite de tamanho, e pede confirmação antes de substituir registros. Exportações contêm dados pessoais, sem criptografia.

O gate de 24 horas usa relógio/estado local e exige registro de conclusão. Ele demonstra pedagogia, **não protege conteúdo pago**: todo conteúdo está no HTML. Proteção comercial precisa entitlement, API autenticada e relógio do servidor no app real. Não publicar o HTML completo como vitrine de conteúdo pago.

Imprimir Caderno gera uma visualização das respostas já existentes; o PDF imprimível independente contém espaços para escrita. Desativar opt-in oculta os campos mas não apaga respostas anteriores; exclusão total é explícita. A referência não faz chamadas de IA, analytics ou nuvem.

## QA

Rodar compilação Python, geração, extração de texto, renderização de páginas PDF e revisão visual. Validar em navegador: 320px, 390px, teclado, persistência, gate, export/import, opt-ins e exclusão. Usar `node tools/qa-reference.cjs /caminho/output` para harness lógico de DOM em Node; ele não requer navegador e não comprova layout visual. Emulação Chromium não comprova Safari ou iPhone real. Acessibilidade automática também não substitui leitor de tela.
