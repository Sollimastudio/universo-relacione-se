# Matriz integral da planta — C1

Referência: `09-app/PLANTA-ECOSSISTEMA-RELACIONE-SE-REFERENCIA.html`, blob `44e19d5cbbf88bd4b94f186a086a8b198d75f9a7`. Inventário: **9 áreas e 260 itens**, incluindo pais e folhas. IDs seguem a ordem congelada da planta, não devem ser renumerados; acrescentar novos IDs ao expandir. Mapeamento completo não significa implementação completa.

Cada item separa implementação, conteúdo, configuração, verificação e publicação. As notas da planta são históricas. `Verificado` refere-se somente ao ambiente e escopo do relatório C1; nenhuma linha certifica produção. Dependências D01–D12 estão em DEPENDENCIAS.md. Arquivos referem-se ao código do Site, não a este repositório documental.

## 01 · Entrada pública e descoberta

A calçada, a recepção e os caminhos de volta ao app.

### entrada.1 · Recepção do Relacione-se

Vínculo técnico: `app/page.tsx`. Rota/serviço: `/`. Dados: catálogo. Permissão: público.

| ID / ramificação | Camada | Implementação | Conteúdo | Configuração | Verificação | Publicação |
|---|---|---|---|---|---|---|
| entrada.1 · Recepção do Relacione-se | C1 | implementado em revisão | UI/estrutura; sem conteúdo novo inventado | ver dependências D10 | UI e inspeção | C1 não publicada; live permanece v1 |

### entrada.2 · Explorar o universo

Vínculo técnico: `components/site/catalog.tsx; components/site/product-preview.tsx; components/site/library.tsx`. Rota/serviço: `/explorar`. Dados: catálogo/favoritos. Permissão: público; favoritos por titular.

| ID / ramificação | Camada | Implementação | Conteúdo | Configuração | Verificação | Publicação |
|---|---|---|---|---|---|---|
| entrada.2 · Explorar o universo | C1/C2 | implementado em revisão | UI/estrutura; sem conteúdo novo inventado | ver dependências D01 | UI; testes de catálogo/acesso | C1 não publicada; live permanece v1 |
| entrada.2.1 · Busca por nome, tema e formato | C1/C2 | implementado em revisão | UI/estrutura; sem conteúdo novo inventado | ver dependências D01 | UI; testes de catálogo/acesso | C1 não publicada; live permanece v1 |
| entrada.2.2 · Conhecer um produto sem perder o atual | C1/C2 | implementado em revisão | UI/estrutura; sem conteúdo novo inventado | ver dependências D01 | UI; testes de catálogo/acesso | C1 não publicada; live permanece v1 |
| entrada.2.3 · Salvar para depois | C1/C2 | implementado em revisão | UI/estrutura; sem conteúdo novo inventado | ver dependências D01 | UI; testes de catálogo/acesso | C1 não publicada; live permanece v1 |
| entrada.2.4 · Gratuito, adquirido, incluído e em preparação | C1/C2 | parcial | UI/estrutura; sem conteúdo novo inventado | ver dependências D01 | UI; testes de catálogo/acesso | C1 não publicada; live permanece v1 |

### entrada.3 · Comece por aqui

Vínculo técnico: `app/comece/page.tsx`. Rota/serviço: `/comece`. Dados: catálogo/curadoria. Permissão: amostras somente autorizadas.

| ID / ramificação | Camada | Implementação | Conteúdo | Configuração | Verificação | Publicação |
|---|---|---|---|---|---|---|
| entrada.3 · Comece por aqui | C1/C4 | implementado em revisão; operação real pendente | UI/estrutura; sem conteúdo novo inventado | ver dependências D04 | UI; curadoria pendente | C1 não publicada; live permanece v1 |
| entrada.3.1 · Experiências gratuitas autorizadas | C1/C4 | depende de definição | UI/estrutura; sem conteúdo novo inventado | ver dependências D04 | UI; curadoria pendente | C1 não publicada; live permanece v1 |
| entrada.3.2 · Quem já sabe o que quer → produto | C1/C4 | implementado em revisão | UI/estrutura; sem conteúdo novo inventado | ver dependências D04 | UI; curadoria pendente | C1 não publicada; live permanece v1 |

### entrada.4 · Canais de descoberta

Vínculo técnico: `lib/traffic.ts; components/site/operations.tsx`. Rota/serviço: `/admin/operacao`. Dados: campanhas/agregados. Permissão: admin; consentimento de métricas.

| ID / ramificação | Camada | Implementação | Conteúdo | Configuração | Verificação | Publicação |
|---|---|---|---|---|---|---|
| entrada.4 · Canais de descoberta | C7 | pendente | UI/estrutura; sem conteúdo novo inventado | ver dependências D08,D10 | núcleo testado; canais não conectados | C1 não publicada; live permanece v1 |
| entrada.4.1 · Instagram, TikTok e YouTube | C7 | pendente | UI/estrutura; sem conteúdo novo inventado | ver dependências D08,D10 | núcleo testado; canais não conectados | C1 não publicada; live permanece v1 |
| entrada.4.2 · WhatsApp | C7 | pendente | UI/estrutura; sem conteúdo novo inventado | ver dependências D08,D10 | núcleo testado; canais não conectados | C1 não publicada; live permanece v1 |
| entrada.4.3 · Telegram · Minutos Magnetus | C7 | depende de definição | UI/estrutura; sem conteúdo novo inventado | ver dependências D08,D10 | núcleo testado; canais não conectados | C1 não publicada; live permanece v1 |
| entrada.4.4 · Links de retorno por conteúdo | C7 | pendente | UI/estrutura; sem conteúdo novo inventado | ver dependências D08,D10 | núcleo testado; canais não conectados | C1 não publicada; live permanece v1 |

### entrada.5 · Saída e retorno

Vínculo técnico: `components/site/context-link.tsx; components/site/use-exit-checkpoint.ts; app/sair/[destination]/page.tsx`. Rota/serviço: `/sair/pack; /sair/script`. Dados: contexto de rota/checkpoint. Permissão: mesma origem; compra verificada separadamente.

| ID / ramificação | Camada | Implementação | Conteúdo | Configuração | Verificação | Publicação |
|---|---|---|---|---|---|---|
| entrada.5 · Saída e retorno | C1/C3 | parcial | UI/estrutura; sem conteúdo novo inventado | ver dependências D01,D03,D11 | UI e continuity.cjs; checkout/login real pendente | C1 não publicada; live permanece v1 |
| entrada.5.1 · Destino externo explicado | C1/C3 | implementado em revisão | UI/estrutura; sem conteúdo novo inventado | ver dependências D01,D03,D11 | UI e continuity.cjs; checkout/login real pendente | C1 não publicada; live permanece v1 |
| entrada.5.2 · Salvar a atividade antes de seguir links | C1/C3 | implementado em revisão | UI/estrutura; sem conteúdo novo inventado | ver dependências D01,D03,D11 | UI e continuity.cjs; checkout/login real pendente | C1 não publicada; live permanece v1 |
| entrada.5.3 · Voltar após checkout, login e troca de aplicativo | C1/C3 | parcial | UI/estrutura; sem conteúdo novo inventado | ver dependências D01,D03,D11 | UI e continuity.cjs; checkout/login real pendente | C1 não publicada; live permanece v1 |

## 02 · Biblioteca e espaço do cliente

Uma conta; vários produtos; uma história de uso.

### biblioteca.1 · Conta única

Vínculo técnico: `app/chatgpt-auth.ts; components/site/library.tsx; components/site/help.tsx`. Rota/serviço: `/perfil; /biblioteca; /ajuda`. Dados: identidade/solicitações. Permissão: titular; vínculo legado comprovado.

| ID / ramificação | Camada | Implementação | Conteúdo | Configuração | Verificação | Publicação |
|---|---|---|---|---|---|---|
| biblioteca.1 · Conta única | C2 | parcial | UI/estrutura; sem conteúdo novo inventado | ver dependências D01,D02 | handlers testados; login real pendente | C1 não publicada; live permanece v1 |
| biblioteca.1.1 · Entrada e sessão | C2 | implementado em revisão | UI/estrutura; sem conteúdo novo inventado | ver dependências D01,D02 | handlers testados; login real pendente | C1 não publicada; live permanece v1 |
| biblioteca.1.2 · Unificação dos clientes antigos | C2 | pendente | UI/estrutura; sem conteúdo novo inventado | ver dependências D01,D02 | handlers testados; login real pendente | C1 não publicada; live permanece v1 |
| biblioteca.1.3 · Recuperação de conta e compra | C2 | parcial | UI/estrutura; sem conteúdo novo inventado | ver dependências D01,D02 | handlers testados; login real pendente | C1 não publicada; live permanece v1 |

### biblioteca.2 · Minha biblioteca

Vínculo técnico: `components/site/library.tsx; app/api/biblioteca/route.ts`. Rota/serviço: `/biblioteca`. Dados: direitos/progresso/favoritos. Permissão: titular autenticado; união dos direitos.

| ID / ramificação | Camada | Implementação | Conteúdo | Configuração | Verificação | Publicação |
|---|---|---|---|---|---|---|
| biblioteca.2 · Minha biblioteca | C2 | implementado em revisão | UI/estrutura; sem conteúdo novo inventado | ver dependências D01,D03 | testes de biblioteca, expiração e sobreposição | C1 não publicada; live permanece v1 |
| biblioteca.2.1 · Continuar de onde parei | C2 | implementado em revisão | UI/estrutura; sem conteúdo novo inventado | ver dependências D01,D03 | testes de biblioteca, expiração e sobreposição | C1 não publicada; live permanece v1 |
| biblioteca.2.2 · Meus conteúdos e componentes | C2 | implementado em revisão | UI/estrutura; sem conteúdo novo inventado | ver dependências D01,D03 | testes de biblioteca, expiração e sobreposição | C1 não publicada; live permanece v1 |
| biblioteca.2.3 · Salvos para depois | C2 | implementado em revisão | UI/estrutura; sem conteúdo novo inventado | ver dependências D01,D03 | testes de biblioteca, expiração e sobreposição | C1 não publicada; live permanece v1 |
| biblioteca.2.4 · Prazos e histórico de acesso | C2 | implementado em revisão | UI/estrutura; sem conteúdo novo inventado | ver dependências D01,D03 | testes de biblioteca, expiração e sobreposição | C1 não publicada; live permanece v1 |
| biblioteca.2.5 · Conteúdo comprado por mais de uma oferta | C2 | implementado em revisão | UI/estrutura; sem conteúdo novo inventado | ver dependências D01,D03 | testes de biblioteca, expiração e sobreposição | C1 não publicada; live permanece v1 |

### biblioteca.3 · Meu Caderno Vivo

Vínculo técnico: `components/site/notebook.tsx; components/site/workbook-notes.tsx; app/api/registros/route.ts`. Rota/serviço: `/caderno`. Dados: notebook_entries/learning_progress. Permissão: proprietário; enunciados pagos protegidos.

| ID / ramificação | Camada | Implementação | Conteúdo | Configuração | Verificação | Publicação |
|---|---|---|---|---|---|---|
| biblioteca.3 · Meu Caderno Vivo | C1/C2 | implementado em revisão | UI/estrutura; sem conteúdo novo inventado | ver dependências D01,D11 | 15 handlers; workbook/expiração; rascunho UI sintético | C1 não publicada; live permanece v1 |
| biblioteca.3.1 · Respostas do workbook e do Antídoto | C1/C2 | implementado em revisão | UI/estrutura; sem conteúdo novo inventado | ver dependências D01,D11 | 15 handlers; workbook/expiração; rascunho UI sintético | C1 não publicada; live permanece v1 |
| biblioteca.3.2 · Anotações e consulta aos próprios registros | C1/C2 | implementado em revisão | UI/estrutura; sem conteúdo novo inventado | ver dependências D01,D11 | 15 handlers; workbook/expiração; rascunho UI sintético | C1 não publicada; live permanece v1 |
| biblioteca.3.3 · Depois da expiração | C1/C2 | implementado em revisão | UI/estrutura; sem conteúdo novo inventado | ver dependências D01,D11 | 15 handlers; workbook/expiração; rascunho UI sintético | C1 não publicada; live permanece v1 |
| biblioteca.3.4 · Continuidade entre dispositivos | C1/C2 | parcial | UI/estrutura; sem conteúdo novo inventado | ver dependências D01,D11 | 15 handlers; workbook/expiração; rascunho UI sintético | C1 não publicada; live permanece v1 |

### biblioteca.4 · Preferências pessoais

Vínculo técnico: `app/api/preferencias/route.ts; components/site/preferences.tsx`. Rota/serviço: `/perfil`. Dados: personal_preferences. Permissão: titular; acessibilidade local.

| ID / ramificação | Camada | Implementação | Conteúdo | Configuração | Verificação | Publicação |
|---|---|---|---|---|---|---|
| biblioteca.4 · Preferências pessoais | C2 | implementado em revisão | UI/estrutura; sem conteúdo novo inventado | ver dependências D01 | inspeção; produção não homologada | C1 não publicada; live permanece v1 |

### biblioteca.5 · Memória e consentimentos da LÚCIDA

Vínculo técnico: `docs/CONTRATOS-INTEGRACAO.md`. Rota/serviço: `/lucida`. Dados: memória futura separada. Permissão: consentimento granular.

| ID / ramificação | Camada | Implementação | Conteúdo | Configuração | Verificação | Publicação |
|---|---|---|---|---|---|---|
| biblioteca.5 · Memória e consentimentos da LÚCIDA | C5 | especificado; memória não implementada | UI/estrutura; sem conteúdo novo inventado | ver dependências D06 | especificação; não implementado | C1 não publicada; live permanece v1 |

### biblioteca.6 · Ajuda

Vínculo técnico: `components/site/help.tsx; app/api/ajuda/route.ts`. Rota/serviço: `/ajuda`. Dados: solicitações de ajuda. Permissão: titular/admin.

| ID / ramificação | Camada | Implementação | Conteúdo | Configuração | Verificação | Publicação |
|---|---|---|---|---|---|---|
| biblioteca.6 · Ajuda | C2 | parcial | UI/estrutura; sem conteúdo novo inventado | ver dependências D02 | protocolo interno; resolução externa pendente | C1 não publicada; live permanece v1 |

## 03 · Produtos e expansão

Alas independentes, conectadas pela mesma biblioteca.

### produtos.1 · Magnetus III

Vínculo técnico: `lib/ecosystem.ts; components/site/lesson.tsx; content/magnetus-mulher/manifest.json`. Rota/serviço: `/produtos/mulher; /produtos/homem; /jornada`. Dados: catálogo/D0–D3/versões. Permissão: direito do componente e gate canônico.

| ID / ramificação | Camada | Implementação | Conteúdo | Configuração | Verificação | Publicação |
|---|---|---|---|---|---|---|
| produtos.1 · Magnetus III | C4 | parcial | fontes existentes a selecionar/aprovar | ver dependências D01,D03,D04,D06 | hashes D0–D3; gate/acesso; demais Dias não integrados | C1 não publicada; live permanece v1 |
| produtos.1.1 · Magnetus III · Mulher | C4 | parcial | fontes existentes a selecionar/aprovar | ver dependências D01,D03,D04,D06 | hashes D0–D3; gate/acesso; demais Dias não integrados | C1 não publicada; live permanece v1 |
| produtos.1.1.1 · Dia 0 · Reset Magnétus | C4 | implementado em revisão | D0–D3 importados, hashes preservados | ver dependências D01,D03,D04,D06 | hashes D0–D3; gate/acesso; demais Dias não integrados | C1 não publicada; live permanece v1 |
| produtos.1.1.2 · Dias 1–3 | C4 | implementado em revisão | D0–D3 importados, hashes preservados | ver dependências D01,D03,D04,D06 | hashes D0–D3; gate/acesso; demais Dias não integrados | C1 não publicada; live permanece v1 |
| produtos.1.1.3 · Dias 4–7 · Magnetus Interior | C4 | pendente | fontes existentes a selecionar/aprovar | ver dependências D01,D03,D04,D06 | hashes D0–D3; gate/acesso; demais Dias não integrados | C1 não publicada; live permanece v1 |
| produtos.1.1.4 · Dia 8 · Perdão e autoperdão | C4 | pendente | fontes existentes a selecionar/aprovar | ver dependências D01,D03,D04,D06 | hashes D0–D3; gate/acesso; demais Dias não integrados | C1 não publicada; live permanece v1 |
| produtos.1.1.5 · Dias 9–15 · Magnetus Físico | C4 | pendente | fontes existentes a selecionar/aprovar | ver dependências D01,D03,D04,D06 | hashes D0–D3; gate/acesso; demais Dias não integrados | C1 não publicada; live permanece v1 |
| produtos.1.1.6 · Tarefas de campo e experimentos do M1 | C4 | parcial | fontes existentes a selecionar/aprovar | ver dependências D01,D03,D04,D06 | hashes D0–D3; gate/acesso; demais Dias não integrados | C1 não publicada; live permanece v1 |
| produtos.1.2 · Magnetus III · Homem | C4 | pendente | fontes existentes a selecionar/aprovar | ver dependências D01,D03,D04,D06 | hashes D0–D3; gate/acesso; demais Dias não integrados | C1 não publicada; live permanece v1 |
| produtos.1.3 · Ebook interativo + workbook | C4 | parcial | fontes existentes a selecionar/aprovar | ver dependências D01,D03,D04,D06 | hashes D0–D3; gate/acesso; demais Dias não integrados | C1 não publicada; live permanece v1 |
| produtos.1.4 · Antídoto do Antivalor | C4 | implementado em revisão | fontes existentes a selecionar/aprovar | ver dependências D01,D03,D04,D06 | hashes D0–D3; gate/acesso; demais Dias não integrados | C1 não publicada; live permanece v1 |
| produtos.1.5 · Acesso à LÚCIDA | C4 | parcial | fontes existentes a selecionar/aprovar | ver dependências D01,D03,D04,D06 | hashes D0–D3; gate/acesso; demais Dias não integrados | C1 não publicada; live permanece v1 |
| produtos.1.6 · PDF, cartilhas e cards compartilháveis | C4 | pendente | fontes existentes a selecionar/aprovar | ver dependências D01,D03,D04,D06 | hashes D0–D3; gate/acesso; demais Dias não integrados | C1 não publicada; live permanece v1 |

### produtos.2 · Trilogia Sol Lima

Vínculo técnico: `lib/ecosystem.ts; components/site/book-reader.tsx`. Rota/serviço: `/produtos/trilogia; /ler/:recurso`. Dados: catálogo/versões editoriais. Permissão: avulso ou coleção contratada.

| ID / ramificação | Camada | Implementação | Conteúdo | Configuração | Verificação | Publicação |
|---|---|---|---|---|---|---|
| produtos.2 · Trilogia Sol Lima | C4 | apresentação/estado sinalizado; experiência pendente | fontes existentes a selecionar/aprovar | ver dependências D03,D04 | rotas e leitor testados; livros autorais não publicados | C1 não publicada; live permanece v1 |
| produtos.2.1 · Morte em Vida | C4 | apresentação/estado sinalizado; experiência pendente | fontes existentes a selecionar/aprovar | ver dependências D03,D04 | rotas e leitor testados; livros autorais não publicados | C1 não publicada; live permanece v1 |
| produtos.2.2 · Reposicione-se | C4 | apresentação/estado sinalizado; experiência pendente | fontes existentes a selecionar/aprovar | ver dependências D03,D04 | rotas e leitor testados; livros autorais não publicados | C1 não publicada; live permanece v1 |
| produtos.2.3 · Fuga Identitária | C4 | apresentação/estado sinalizado; experiência pendente | fontes existentes a selecionar/aprovar | ver dependências D03,D04 | rotas e leitor testados; livros autorais não publicados | C1 não publicada; live permanece v1 |
| produtos.2.4 · Coleção completa ou cada livro separado | C4 | apresentação/estado sinalizado; experiência pendente | fontes existentes a selecionar/aprovar | ver dependências D03,D04 | rotas e leitor testados; livros autorais não publicados | C1 não publicada; live permanece v1 |
| produtos.2.5 · Exercícios e ferramentas vinculados aos livros | C4 | apresentação/estado sinalizado; experiência pendente | fontes existentes a selecionar/aprovar | ver dependências D03,D04 | rotas e leitor testados; livros autorais não publicados | C1 não publicada; live permanece v1 |

### produtos.3 · MINDSETmagro

Vínculo técnico: `lib/catalog.ts; lib/ecosystem.ts`. Rota/serviço: `/produtos/mindsetmagro`. Dados: catálogo; protocolo/bônus a integrar. Permissão: composição comercial aprovada.

| ID / ramificação | Camada | Implementação | Conteúdo | Configuração | Verificação | Publicação |
|---|---|---|---|---|---|---|
| produtos.3 · MINDSETmagro | C4 | apresentação/estado sinalizado; experiência pendente | fontes existentes a selecionar/aprovar | ver dependências D03,D04,D06 | página de preparação; entrega não homologada | C1 não publicada; live permanece v1 |
| produtos.3.1 · Protocolo principal | C4 | apresentação/estado sinalizado; experiência pendente | fontes existentes a selecionar/aprovar | ver dependências D03,D04,D06 | página de preparação; entrega não homologada | C1 não publicada; live permanece v1 |
| produtos.3.2 · Bônus próprios | C4 | apresentação/estado sinalizado; experiência pendente | fontes existentes a selecionar/aprovar | ver dependências D03,D04,D06 | página de preparação; entrega não homologada | C1 não publicada; live permanece v1 |
| produtos.3.3 · Bônus também como produto avulso | C4 | apresentação/estado sinalizado; experiência pendente | fontes existentes a selecionar/aprovar | ver dependências D03,D04,D06 | página de preparação; entrega não homologada | C1 não publicada; live permanece v1 |
| produtos.3.4 · Acompanhamento pela LÚCIDA | C4 | apresentação/estado sinalizado; experiência pendente | fontes existentes a selecionar/aprovar | ver dependências D03,D04,D06 | página de preparação; entrega não homologada | C1 não publicada; live permanece v1 |

### produtos.4 · Minuto Magnetus · pack de áudios

Vínculo técnico: `components/site/audio-experience.tsx; lib/platform/audio.ts; lib/platform/links.ts`. Rota/serviço: `/produtos/minuto-magnetus; /ouvir/:recurso`. Dados: mídia/transcrição/progresso. Permissão: gratuito/pago explícito.

| ID / ramificação | Camada | Implementação | Conteúdo | Configuração | Verificação | Publicação |
|---|---|---|---|---|---|---|
| produtos.4 · Minuto Magnetus · pack de áudios | C4/C7 | parcial | fontes existentes a selecionar/aprovar | ver dependências D03,D05,D08 | áudio/ranges sintéticos; pack real pendente | C1 não publicada; live permanece v1 |
| produtos.4.1 · Acervo, transcrições e player | C4/C7 | pendente | fontes existentes a selecionar/aprovar | ver dependências D03,D05,D08 | áudio/ranges sintéticos; pack real pendente | C1 não publicada; live permanece v1 |
| produtos.4.2 · Acesso ao canal ou dentro do app | C4/C7 | depende de definição | fontes existentes a selecionar/aprovar | ver dependências D03,D05,D08 | áudio/ranges sintéticos; pack real pendente | C1 não publicada; live permanece v1 |
| produtos.4.3 · Conteúdo gratuito de descoberta | C4/C7 | depende de definição | fontes existentes a selecionar/aprovar | ver dependências D03,D05,D08 | áudio/ranges sintéticos; pack real pendente | C1 não publicada; live permanece v1 |

### produtos.5 · Script do Silêncio

Vínculo técnico: `lib/ecosystem.ts; lib/platform/links.ts`. Rota/serviço: `/produtos/script-do-silencio; /sair/script`. Dados: catálogo/link oficial. Permissão: entrega contratada; timer não homologado.

| ID / ramificação | Camada | Implementação | Conteúdo | Configuração | Verificação | Publicação |
|---|---|---|---|---|---|---|
| produtos.5 · Script do Silêncio | C4 | apresentação/estado sinalizado; experiência pendente | fontes existentes a selecionar/aprovar | ver dependências D03,D04,D08 | rotas de oferta/preparação; conteúdo real pendente | C1 não publicada; live permanece v1 |
| produtos.5.1 · Conteúdo do produto | C4 | apresentação/estado sinalizado; experiência pendente | fontes existentes a selecionar/aprovar | ver dependências D03,D04,D08 | rotas de oferta/preparação; conteúdo real pendente | C1 não publicada; live permanece v1 |
| produtos.5.2 · Cronômetro Canva | C4 | apresentação/estado sinalizado; experiência pendente | fontes existentes a selecionar/aprovar | ver dependências D03,D04,D08 | rotas de oferta/preparação; conteúdo real pendente | C1 não publicada; live permanece v1 |
| produtos.5.3 · Prática e retomada | C4 | apresentação/estado sinalizado; experiência pendente | fontes existentes a selecionar/aprovar | ver dependências D03,D04,D08 | rotas de oferta/preparação; conteúdo real pendente | C1 não publicada; live permanece v1 |

### produtos.6 · Testes, ferramentas e outros apps conhecidos

Vínculo técnico: `lib/ecosystem.ts; docs/DECISAO-INTEGRACAO-2026-09-21.md`. Rota/serviço: `/produtos/labs; /recursos/:slug`. Dados: inventário de legados. Permissão: classificar por recurso; Oráculo interno.

| ID / ramificação | Camada | Implementação | Conteúdo | Configuração | Verificação | Publicação |
|---|---|---|---|---|---|---|
| produtos.6 · Testes, ferramentas e outros apps conhecidos | C4/C6 | apresentação/estado sinalizado; experiência pendente | fontes existentes a selecionar/aprovar | ver dependências D04,D07 | inventário documentado; não executados todos os legados | C1 não publicada; live permanece v1 |
| produtos.6.1 · Testes de presença feminino e masculino | C4/C6 | apresentação/estado sinalizado; experiência pendente | fontes existentes a selecionar/aprovar | ver dependências D04,D07 | inventário documentado; não executados todos os legados | C1 não publicada; live permanece v1 |
| produtos.6.2 · Teste da Árvore | C4/C6 | apresentação/estado sinalizado; experiência pendente | fontes existentes a selecionar/aprovar | ver dependências D04,D07 | inventário documentado; não executados todos os legados | C1 não publicada; live permanece v1 |
| produtos.6.3 · Mapa da Suspeita | C4/C6 | apresentação/estado sinalizado; experiência pendente | fontes existentes a selecionar/aprovar | ver dependências D04,D07 | inventário documentado; não executados todos os legados | C1 não publicada; live permanece v1 |
| produtos.6.4 · Dor de Cotovelo | C4/C6 | apresentação/estado sinalizado; experiência pendente | fontes existentes a selecionar/aprovar | ver dependências D04,D07 | inventário documentado; não executados todos os legados | C1 não publicada; live permanece v1 |
| produtos.6.5 · Matemática do Perdão 490 | C4/C6 | apresentação/estado sinalizado; experiência pendente | fontes existentes a selecionar/aprovar | ver dependências D04,D07 | inventário documentado; não executados todos os legados | C1 não publicada; live permanece v1 |
| produtos.6.6 · Oráculo Magnético | C4/C6 | apresentação/estado sinalizado; experiência pendente | fontes existentes a selecionar/aprovar | ver dependências D04,D07 | inventário documentado; não executados todos os legados | C1 não publicada; live permanece v1 |
| produtos.6.7 · Outros repositórios e páginas antigas | C4/C6 | apresentação/estado sinalizado; experiência pendente | fontes existentes a selecionar/aprovar | ver dependências D04,D07 | inventário documentado; não executados todos os legados | C1 não publicada; live permanece v1 |

### produtos.7 · Novas alas do ecossistema

Vínculo técnico: `lib/platform/editorial.ts; lib/platform/commerce.ts`. Rota/serviço: `/admin`. Dados: versões/conteúdos/ofertas. Permissão: admin; contratação por recurso.

| ID / ramificação | Camada | Implementação | Conteúdo | Configuração | Verificação | Publicação |
|---|---|---|---|---|---|---|
| produtos.7 · Novas alas do ecossistema | C4 | pendente | fontes existentes a selecionar/aprovar | ver dependências D02,D03,D04 | novo livro/áudio em testes; outros formatos parciais | C1 não publicada; live permanece v1 |
| produtos.7.1 · Novo livro, protocolo, áudio ou ferramenta | C4 | pendente | fontes existentes a selecionar/aprovar | ver dependências D02,D03,D04 | novo livro/áudio em testes; outros formatos parciais | C1 não publicada; live permanece v1 |
| produtos.7.2 · Mesmo conteúdo em diferentes ofertas | C4 | parcial | fontes existentes a selecionar/aprovar | ver dependências D02,D03,D04 | novo livro/áudio em testes; outros formatos parciais | C1 não publicada; live permanece v1 |
| produtos.7.3 · Relações: complemento, pré-requisito e próximo passo | C4 | depende de definição | fontes existentes a selecionar/aprovar | ver dependências D02,D03,D04 | novo livro/áudio em testes; outros formatos parciais | C1 não publicada; live permanece v1 |
| produtos.7.4 · Novos produtos ainda sem nome | C4 | pendente | fontes existentes a selecionar/aprovar | ver dependências D02,D03,D04 | novo livro/áudio em testes; outros formatos parciais | C1 não publicada; live permanece v1 |

## 04 · Compras, ofertas e chaves de acesso

Cada contratação abre somente as portas que inclui.

### chaves.1 · Quatro peças diferentes

Vínculo técnico: `lib/platform/types.ts; lib/platform/access.ts; lib/platform/editorial.ts`. Rota/serviço: `/api/biblioteca`. Dados: conteúdo/produto/oferta/direito. Permissão: autorização no servidor.

| ID / ramificação | Camada | Implementação | Conteúdo | Configuração | Verificação | Publicação |
|---|---|---|---|---|---|---|
| chaves.1 · Quatro peças diferentes | C3 | parcial | UI/estrutura; sem conteúdo novo inventado | ver dependências D03 | cenários de catálogo e direitos sintéticos | C1 não publicada; live permanece v1 |
| chaves.1.1 · Conteúdo | C3 | implementado em revisão | UI/estrutura; sem conteúdo novo inventado | ver dependências D03 | cenários de catálogo e direitos sintéticos | C1 não publicada; live permanece v1 |
| chaves.1.2 · Produto | C3 | implementado em revisão | UI/estrutura; sem conteúdo novo inventado | ver dependências D03 | cenários de catálogo e direitos sintéticos | C1 não publicada; live permanece v1 |
| chaves.1.3 · Oferta | C3 | implementado em revisão | UI/estrutura; sem conteúdo novo inventado | ver dependências D03 | cenários de catálogo e direitos sintéticos | C1 não publicada; live permanece v1 |
| chaves.1.4 · Direito de acesso | C3 | implementado em revisão | UI/estrutura; sem conteúdo novo inventado | ver dependências D03 | cenários de catálogo e direitos sintéticos | C1 não publicada; live permanece v1 |

### chaves.2 · Modalidades de contratação

Vínculo técnico: `lib/platform/commerce.ts; components/site/offer-details.tsx`. Rota/serviço: `/produtos/:slug`. Dados: ofertas/versionamento/vigência. Permissão: contrato imutável.

| ID / ramificação | Camada | Implementação | Conteúdo | Configuração | Verificação | Publicação |
|---|---|---|---|---|---|---|
| chaves.2 · Modalidades de contratação | C3 | parcial | UI/estrutura; sem conteúdo novo inventado | ver dependências D03 | núcleo de datas testado; cálculo/termos reais pendentes | C1 não publicada; live permanece v1 |
| chaves.2.1 · Gratuito e avulso | C3 | parcial | UI/estrutura; sem conteúdo novo inventado | ver dependências D03 | núcleo de datas testado; cálculo/termos reais pendentes | C1 não publicada; live permanece v1 |
| chaves.2.2 · Combo e bônus | C3 | parcial | UI/estrutura; sem conteúdo novo inventado | ver dependências D03 | núcleo de datas testado; cálculo/termos reais pendentes | C1 não publicada; live permanece v1 |
| chaves.2.3 · Dias ou meses | C3 | parcial | UI/estrutura; sem conteúdo novo inventado | ver dependências D03 | núcleo de datas testado; cálculo/termos reais pendentes | C1 não publicada; live permanece v1 |
| chaves.2.4 · Assinatura com catálogo definido | C3 | parcial | UI/estrutura; sem conteúdo novo inventado | ver dependências D03 | núcleo de datas testado; cálculo/termos reais pendentes | C1 não publicada; live permanece v1 |
| chaves.2.5 · Pré-requisitos e atualizações | C3 | depende de definição | UI/estrutura; sem conteúdo novo inventado | ver dependências D03 | núcleo de datas testado; cálculo/termos reais pendentes | C1 não publicada; live permanece v1 |

### chaves.3 · Caminho de uma compra

Vínculo técnico: `app/api/integracoes/kiwify/route.ts; lib/platform/commerce.ts`. Rota/serviço: `/sair/:destino; /api/integracoes/kiwify`. Dados: evento verificado/vínculo/oferta. Permissão: webhook fechado; compra não inferida.

| ID / ramificação | Camada | Implementação | Conteúdo | Configuração | Verificação | Publicação |
|---|---|---|---|---|---|---|
| chaves.3 · Caminho de uma compra | C3 | parcial | UI/estrutura; sem conteúdo novo inventado | ver dependências D01,D03 | 503 sem configuração; processador interno sintético | C1 não publicada; live permanece v1 |
| chaves.3.1 · Oferta clara → checkout Kiwify | C3 | parcial | UI/estrutura; sem conteúdo novo inventado | ver dependências D01,D03 | 503 sem configuração; processador interno sintético | C1 não publicada; live permanece v1 |
| chaves.3.2 · Confirmação verificada no servidor | C3 | pendente | UI/estrutura; sem conteúdo novo inventado | ver dependências D01,D03 | 503 sem configuração; processador interno sintético | C1 não publicada; live permanece v1 |
| chaves.3.3 · Vincular compra ao titular | C3 | pendente | UI/estrutura; sem conteúdo novo inventado | ver dependências D01,D03 | 503 sem configuração; processador interno sintético | C1 não publicada; live permanece v1 |
| chaves.3.4 · Gerar direitos dos componentes contratados | C3 | implementado em revisão | UI/estrutura; sem conteúdo novo inventado | ver dependências D01,D03 | 503 sem configuração; processador interno sintético | C1 não publicada; live permanece v1 |
| chaves.3.5 · Retornar à biblioteca → abrir o produto | C3 | parcial | UI/estrutura; sem conteúdo novo inventado | ver dependências D01,D03 | 503 sem configuração; processador interno sintético | C1 não publicada; live permanece v1 |

### chaves.4 · Contratos e proteção do acesso

Vínculo técnico: `lib/platform/commerce.ts; lib/platform/access.ts`. Rota/serviço: `/api/biblioteca`. Dados: origens/direitos/versionamento. Permissão: titular; eventos verificados.

| ID / ramificação | Camada | Implementação | Conteúdo | Configuração | Verificação | Publicação |
|---|---|---|---|---|---|---|
| chaves.4 · Contratos e proteção do acesso | C3 | implementado em revisão | UI/estrutura; sem conteúdo novo inventado | ver dependências D03 | sobreposição/ordem/cancelamento/reembolso sintéticos | C1 não publicada; live permanece v1 |
| chaves.4.1 · Somar direitos válidos | C3 | implementado em revisão | UI/estrutura; sem conteúdo novo inventado | ver dependências D03 | sobreposição/ordem/cancelamento/reembolso sintéticos | C1 não publicada; live permanece v1 |
| chaves.4.2 · Eventos repetidos ou fora de ordem | C3 | implementado em revisão | UI/estrutura; sem conteúdo novo inventado | ver dependências D03 | sobreposição/ordem/cancelamento/reembolso sintéticos | C1 não publicada; live permanece v1 |
| chaves.4.3 · Renovação e cancelamento | C3 | implementado em revisão | UI/estrutura; sem conteúdo novo inventado | ver dependências D03 | sobreposição/ordem/cancelamento/reembolso sintéticos | C1 não publicada; live permanece v1 |
| chaves.4.4 · Reembolso e chargeback | C3 | implementado em revisão | UI/estrutura; sem conteúdo novo inventado | ver dependências D03 | sobreposição/ordem/cancelamento/reembolso sintéticos | C1 não publicada; live permanece v1 |
| chaves.4.5 · Reembolso parcial e reconciliação externa | C3 | parcial; adaptação comercial pendente | UI/estrutura; sem conteúdo novo inventado | ver dependências D03 | sobreposição/ordem/cancelamento/reembolso sintéticos | C1 não publicada; live permanece v1 |
| chaves.4.6 · Versão editorial antes do primeiro uso | C3 | parcial; adaptação comercial pendente | UI/estrutura; sem conteúdo novo inventado | ver dependências D03 | sobreposição/ordem/cancelamento/reembolso sintéticos | C1 não publicada; live permanece v1 |

### chaves.5 · Duas fechaduras independentes

Vínculo técnico: `lib/platform/learning.ts; lib/protocol/gate.mjs`. Rota/serviço: `/jornada/:dia`. Dados: direitos/abertura/conclusão. Permissão: vigência comercial + conclusão + 24h.

| ID / ramificação | Camada | Implementação | Conteúdo | Configuração | Verificação | Publicação |
|---|---|---|---|---|---|---|
| chaves.5 · Duas fechaduras independentes | C3/C4 | implementado em revisão | UI/estrutura; sem conteúdo novo inventado | ver dependências D03 | gate e acesso real do módulo, com identidades sintéticas | C1 não publicada; live permanece v1 |
| chaves.5.1 · Posso acessar? | C3/C4 | implementado em revisão | UI/estrutura; sem conteúdo novo inventado | ver dependências D03 | gate e acesso real do módulo, com identidades sintéticas | C1 não publicada; live permanece v1 |
| chaves.5.2 · Posso abrir o próximo Dia? | C3/C4 | implementado em revisão | UI/estrutura; sem conteúdo novo inventado | ver dependências D03 | gate e acesso real do módulo, com identidades sintéticas | C1 não publicada; live permanece v1 |

## 05 · LÚCIDA, assistente dos clientes

Atendimento transversal com contexto e limites de acesso.

### lucida.1 · Onde a cliente está

Vínculo técnico: `lib/platform/lucida-context.ts; components/site/continuity-guide.tsx`. Rota/serviço: `/api/lucida/contexto; /lucida`. Dados: contexto mínimo/direitos. Permissão: recurso + assistência autorizados.

| ID / ramificação | Camada | Implementação | Conteúdo | Configuração | Verificação | Publicação |
|---|---|---|---|---|---|---|
| lucida.1 · Onde a cliente está | C5 | parcial | UI/estrutura; sem conteúdo novo inventado | ver dependências D06 | filtro/contexto testados; IA ausente | C1 não publicada; live permanece v1 |
| lucida.1.1 · Produto e capítulo ou Dia atual | C5 | implementado em revisão | UI/estrutura; sem conteúdo novo inventado | ver dependências D06 | filtro/contexto testados; IA ausente | C1 não publicada; live permanece v1 |
| lucida.1.2 · Objetivo da prática e próximo passo | C5 | pendente | UI/estrutura; sem conteúdo novo inventado | ver dependências D06 | filtro/contexto testados; IA ausente | C1 não publicada; live permanece v1 |
| lucida.1.3 · Biblioteca e recursos já adquiridos | C5 | parcial | UI/estrutura; sem conteúdo novo inventado | ver dependências D06 | filtro/contexto testados; IA ausente | C1 não publicada; live permanece v1 |

### lucida.2 · Conhecimento autoral

Vínculo técnico: `lib/platform/lucida-context.ts; docs/CONTRATOS-INTEGRACAO.md`. Rota/serviço: `/api/lucida`. Dados: fontes aprovadas/versões. Permissão: fontes permitidas por acesso.

| ID / ramificação | Camada | Implementação | Conteúdo | Configuração | Verificação | Publicação |
|---|---|---|---|---|---|---|
| lucida.2 · Conhecimento autoral | C5 | parcial | fontes existentes a selecionar/aprovar | ver dependências D04,D06 | filtro sintético; recuperação/modelo não homologados | C1 não publicada; live permanece v1 |
| lucida.2.1 · Trilogia autorizada | C5 | pendente | fontes existentes a selecionar/aprovar | ver dependências D04,D06 | filtro sintético; recuperação/modelo não homologados | C1 não publicada; live permanece v1 |
| lucida.2.2 · Bíblia Magnetus e conteúdo dos produtos | C5 | parcial | fontes existentes a selecionar/aprovar | ver dependências D04,D06 | filtro sintético; recuperação/modelo não homologados | C1 não publicada; live permanece v1 |
| lucida.2.3 · Universo Relacione-se e orientações oficiais | C5 | pendente | fontes existentes a selecionar/aprovar | ver dependências D04,D06 | filtro sintético; recuperação/modelo não homologados | C1 não publicada; live permanece v1 |
| lucida.2.4 · Proveniência, aprovação e versão da fonte | C5 | parcial | fontes existentes a selecionar/aprovar | ver dependências D04,D06 | filtro sintético; recuperação/modelo não homologados | C1 não publicada; live permanece v1 |
| lucida.2.5 · Não revelar obra paga sem direito | C5 | parcial | fontes existentes a selecionar/aprovar | ver dependências D04,D06 | filtro sintético; recuperação/modelo não homologados | C1 não publicada; live permanece v1 |

### lucida.3 · Acompanhamento pessoal

Vínculo técnico: `docs/CONTRATOS-INTEGRACAO.md`. Rota/serviço: `/lucida`. Dados: memória futura. Permissão: consentir/revisar/corrigir/apagar.

| ID / ramificação | Camada | Implementação | Conteúdo | Configuração | Verificação | Publicação |
|---|---|---|---|---|---|---|
| lucida.3 · Acompanhamento pessoal | C5 | especificado; memória não implementada | UI/estrutura; sem conteúdo novo inventado | ver dependências D06 | somente especificação | C1 não publicada; live permanece v1 |
| lucida.3.1 · Consentir uso do contexto pessoal | C5 | especificado; memória não implementada | UI/estrutura; sem conteúdo novo inventado | ver dependências D06 | somente especificação | C1 não publicada; live permanece v1 |
| lucida.3.2 · Escolher o que pode atravessar produtos | C5 | especificado; memória não implementada | UI/estrutura; sem conteúdo novo inventado | ver dependências D06 | somente especificação | C1 não publicada; live permanece v1 |
| lucida.3.3 · Consultar, corrigir e apagar memória | C5 | especificado; memória não implementada | UI/estrutura; sem conteúdo novo inventado | ver dependências D06 | somente especificação | C1 não publicada; live permanece v1 |
| lucida.3.4 · Caderno não vira memória automaticamente | C5 | especificado; memória não implementada | UI/estrutura; sem conteúdo novo inventado | ver dependências D06 | somente especificação | C1 não publicada; live permanece v1 |

### lucida.4 · Orientação dentro do universo

Vínculo técnico: `components/site/continuity-guide.tsx; components/site/lucida.tsx`. Rota/serviço: `/lucida`. Dados: direitos/progresso/rascunho temporário. Permissão: prioridade ao já adquirido; sem IA ativa.

| ID / ramificação | Camada | Implementação | Conteúdo | Configuração | Verificação | Publicação |
|---|---|---|---|---|---|---|
| lucida.4 · Orientação dentro do universo | C5 | pendente | UI/estrutura; sem conteúdo novo inventado | ver dependências D06 | guia determinístico; recomendação IA pendente | C1 não publicada; live permanece v1 |
| lucida.4.1 · Priorizar gratuito ou já adquirido | C5 | guia determinístico implementado; IA pendente | UI/estrutura; sem conteúdo novo inventado | ver dependências D06 | guia determinístico; recomendação IA pendente | C1 não publicada; live permanece v1 |
| lucida.4.2 · Voltar à atividade atual | C5 | guia determinístico implementado; IA pendente | UI/estrutura; sem conteúdo novo inventado | ver dependências D06 | guia determinístico; recomendação IA pendente | C1 não publicada; live permanece v1 |
| lucida.4.3 · Sugerir complemento quando pertinente | C5 | pendente | UI/estrutura; sem conteúdo novo inventado | ver dependências D06 | guia determinístico; recomendação IA pendente | C1 não publicada; live permanece v1 |
| lucida.4.4 · Respeitar recusa e vulnerabilidade | C5 | pendente | UI/estrutura; sem conteúdo novo inventado | ver dependências D06 | guia determinístico; recomendação IA pendente | C1 não publicada; live permanece v1 |
| lucida.4.5 · Encaminhar para suporte quando necessário | C5 | pendente | UI/estrutura; sem conteúdo novo inventado | ver dependências D06 | guia determinístico; recomendação IA pendente | C1 não publicada; live permanece v1 |

### lucida.5 · Operação da IA

Vínculo técnico: `app/api/lucida/route.ts; components/site/lucida.tsx`. Rota/serviço: `/lucida`. Dados: disponibilidade/limites futuros. Permissão: sem provedor nem memória automática.

| ID / ramificação | Camada | Implementação | Conteúdo | Configuração | Verificação | Publicação |
|---|---|---|---|---|---|---|
| lucida.5 · Operação da IA | C5 | pendente | UI/estrutura; sem conteúdo novo inventado | ver dependências D06 | 503 honesto e reflexão fixa existentes | C1 não publicada; live permanece v1 |
| lucida.5.1 · Orçamento e uso conforme contratação | C5 | depende de definição | UI/estrutura; sem conteúdo novo inventado | ver dependências D06 | 503 honesto e reflexão fixa existentes | C1 não publicada; live permanece v1 |
| lucida.5.2 · Avaliar respostas, segurança e custo | C5 | pendente | UI/estrutura; sem conteúdo novo inventado | ver dependências D06 | 503 honesto e reflexão fixa existentes | C1 não publicada; live permanece v1 |
| lucida.5.3 · Indisponibilidade explícita | C5 | implementado em revisão | UI/estrutura; sem conteúdo novo inventado | ver dependências D06 | 503 honesto e reflexão fixa existentes | C1 não publicada; live permanece v1 |
| lucida.5.4 · Reflexão editorial existente | C5 | implementado em revisão | UI/estrutura; sem conteúdo novo inventado | ver dependências D06 | 503 honesto e reflexão fixa existentes | C1 não publicada; live permanece v1 |

## 06 · Salas de leitura, prática e áudio

Experiências compartilhadas pelos produtos do ecossistema.

### experiencias.1 · Leitor de livros

Vínculo técnico: `components/site/book-reader.tsx; lib/platform/reader.ts`. Rota/serviço: `/ler/:recurso`. Dados: capítulo/parágrafo/marcador/versão. Permissão: titular ou obra gratuita aprovada.

| ID / ramificação | Camada | Implementação | Conteúdo | Configuração | Verificação | Publicação |
|---|---|---|---|---|---|---|
| experiencias.1 · Leitor de livros | C1/C4 | implementado em revisão | fontes existentes a selecionar/aprovar | ver dependências D04,D11 | persistência e versões testadas; UI sintética | C1 não publicada; live permanece v1 |
| experiencias.1.1 · Capítulos e índice | C1/C4 | implementado em revisão | fontes existentes a selecionar/aprovar | ver dependências D04,D11 | persistência e versões testadas; UI sintética | C1 não publicada; live permanece v1 |
| experiencias.1.2 · Marcadores e posição por capítulo | C1/C4 | implementado em revisão | fontes existentes a selecionar/aprovar | ver dependências D04,D11 | persistência e versões testadas; UI sintética | C1 não publicada; live permanece v1 |
| experiencias.1.3 · Tema confortável e tamanho da fonte | C1/C4 | implementado em revisão | fontes existentes a selecionar/aprovar | ver dependências D04,D11 | persistência e versões testadas; UI sintética | C1 não publicada; live permanece v1 |
| experiencias.1.4 · Retomar no parágrafo exato | C1/C4 | implementado em revisão; operação real pendente | fontes existentes a selecionar/aprovar | ver dependências D04,D11 | persistência e versões testadas; UI sintética | C1 não publicada; live permanece v1 |
| experiencias.1.5 · Versão da leitura iniciada | C1/C4 | implementado em revisão | fontes existentes a selecionar/aprovar | ver dependências D04,D11 | persistência e versões testadas; UI sintética | C1 não publicada; live permanece v1 |

### experiencias.2 · Ebook interativo e workbook

Vínculo técnico: `components/site/lesson.tsx; lib/platform/learning.ts`. Rota/serviço: `/jornada/:dia`. Dados: answers/cursor/revision. Permissão: titular, gate e conflitos.

| ID / ramificação | Camada | Implementação | Conteúdo | Configuração | Verificação | Publicação |
|---|---|---|---|---|---|---|
| experiencias.2 · Ebook interativo e workbook | C1/C4 | parcial | UI/estrutura; sem conteúdo novo inventado | ver dependências D04,D11 | conteúdo preservado; persistência/gates testados | C1 não publicada; live permanece v1 |
| experiencias.2.1 · Conteúdo + exercício progressivo | C1/C4 | implementado em revisão | UI/estrutura; sem conteúdo novo inventado | ver dependências D04,D11 | conteúdo preservado; persistência/gates testados | C1 não publicada; live permanece v1 |
| experiencias.2.2 · Salvamento automático e manual | C1/C4 | implementado em revisão | UI/estrutura; sem conteúdo novo inventado | ver dependências D04,D11 | conteúdo preservado; persistência/gates testados | C1 não publicada; live permanece v1 |
| experiencias.2.3 · Uma fonte de respostas para o Caderno | C1/C4 | implementado em revisão | UI/estrutura; sem conteúdo novo inventado | ver dependências D04,D11 | conteúdo preservado; persistência/gates testados | C1 não publicada; live permanece v1 |
| experiencias.2.4 · Conflito entre dispositivos sinalizado | C1/C4 | implementado em revisão | UI/estrutura; sem conteúdo novo inventado | ver dependências D04,D11 | conteúdo preservado; persistência/gates testados | C1 não publicada; live permanece v1 |
| experiencias.2.5 · Gate por conclusão e tempo | C1/C4 | implementado em revisão | UI/estrutura; sem conteúdo novo inventado | ver dependências D04,D11 | conteúdo preservado; persistência/gates testados | C1 não publicada; live permanece v1 |
| experiencias.2.6 · Experimentos, tarefas externas e cards | C1/C4 | parcial | UI/estrutura; sem conteúdo novo inventado | ver dependências D04,D11 | conteúdo preservado; persistência/gates testados | C1 não publicada; live permanece v1 |

### experiencias.3 · Antídoto e ferramentas de prática

Vínculo técnico: `components/site/antidote.tsx; app/api/antidoto/route.ts`. Rota/serviço: `/praticar/antidoto`. Dados: notas/revision. Permissão: direito independente e titular.

| ID / ramificação | Camada | Implementação | Conteúdo | Configuração | Verificação | Publicação |
|---|---|---|---|---|---|---|
| experiencias.3 · Antídoto e ferramentas de prática | C1/C4 | parcial | UI/estrutura; sem conteúdo novo inventado | ver dependências D03,D04 | Antídoto e falha/retry UI; outras ferramentas pendentes | C1 não publicada; live permanece v1 |
| experiencias.3.1 · Semáforo e prática P.A.R.A. | C1/C4 | implementado em revisão | UI/estrutura; sem conteúdo novo inventado | ver dependências D03,D04 | Antídoto e falha/retry UI; outras ferramentas pendentes | C1 não publicada; live permanece v1 |
| experiencias.3.2 · Reflexões privadas | C1/C4 | implementado em revisão | UI/estrutura; sem conteúdo novo inventado | ver dependências D03,D04 | Antídoto e falha/retry UI; outras ferramentas pendentes | C1 não publicada; live permanece v1 |
| experiencias.3.3 · Acesso independente do workbook | C1/C4 | implementado em revisão | UI/estrutura; sem conteúdo novo inventado | ver dependências D03,D04 | Antídoto e falha/retry UI; outras ferramentas pendentes | C1 não publicada; live permanece v1 |
| experiencias.3.4 · Cronômetros e testes aproveitáveis | C1/C4 | pendente | UI/estrutura; sem conteúdo novo inventado | ver dependências D03,D04 | Antídoto e falha/retry UI; outras ferramentas pendentes | C1 não publicada; live permanece v1 |

### experiencias.4 · Sala de áudio

Vínculo técnico: `components/site/audio-player.tsx; lib/platform/audio.ts; lib/platform/media.ts`. Rota/serviço: `/ouvir/:recurso; /api/midia/:recurso`. Dados: segundos/velocidade/R2/transcrição. Permissão: cada request autorizado.

| ID / ramificação | Camada | Implementação | Conteúdo | Configuração | Verificação | Publicação |
|---|---|---|---|---|---|---|
| experiencias.4 · Sala de áudio | C4 | parcial | fontes existentes a selecionar/aprovar | ver dependências D05,D11 | núcleo e stream sintéticos; codecs reais pendentes | C1 não publicada; live permanece v1 |
| experiencias.4.1 · Reprodução e velocidade | C4 | implementado em revisão; operação real pendente | fontes existentes a selecionar/aprovar | ver dependências D05,D11 | núcleo e stream sintéticos; codecs reais pendentes | C1 não publicada; live permanece v1 |
| experiencias.4.2 · Transcrição acessível | C4 | implementado em revisão; operação real pendente | fontes existentes a selecionar/aprovar | ver dependências D05,D11 | núcleo e stream sintéticos; codecs reais pendentes | C1 não publicada; live permanece v1 |
| experiencias.4.3 · Favorito e posição na conta | C4 | pendente | fontes existentes a selecionar/aprovar | ver dependências D05,D11 | núcleo e stream sintéticos; codecs reais pendentes | C1 não publicada; live permanece v1 |
| experiencias.4.4 · Separar acervo gratuito e pago | C4 | implementado em revisão; operação real pendente | fontes existentes a selecionar/aprovar | ver dependências D05,D11 | núcleo e stream sintéticos; codecs reais pendentes | C1 não publicada; live permanece v1 |

### experiencias.5 · Materiais para compartilhar

Vínculo técnico: `docs/CONTRATOS-INTEGRACAO.md; lib/platform/access.ts`. Rota/serviço: `/recursos/:slug`. Dados: assets exportáveis a integrar. Permissão: exportação intencional; pago protegido.

| ID / ramificação | Camada | Implementação | Conteúdo | Configuração | Verificação | Publicação |
|---|---|---|---|---|---|---|
| experiencias.5 · Materiais para compartilhar | C4 | pendente | fontes existentes a selecionar/aprovar | ver dependências D04 | política e proteção; cards não entregues | C1 não publicada; live permanece v1 |
| experiencias.5.1 · Cards autorizados, identidade e marca d’água | C4 | pendente | fontes existentes a selecionar/aprovar | ver dependências D04 | política e proteção; cards não entregues | C1 não publicada; live permanece v1 |
| experiencias.5.2 · Download ou compartilhamento intencional | C4 | pendente | fontes existentes a selecionar/aprovar | ver dependências D04 | política e proteção; cards não entregues | C1 não publicada; live permanece v1 |
| experiencias.5.3 · Conteúdo privado protegido por acesso | C4 | implementado em revisão | fontes existentes a selecionar/aprovar | ver dependências D04 | política e proteção; cards não entregues | C1 não publicada; live permanece v1 |

### experiencias.6 · Continuidade da experiência

Vínculo técnico: `components/site/product-preview.tsx; lib/exit-checkpoints.ts; lib/transient-drafts.ts`. Rota/serviço: `rotas contextuais`. Dados: contexto/checkpoints/rascunhos na aba. Permissão: sem texto pessoal em URL/analytics.

| ID / ramificação | Camada | Implementação | Conteúdo | Configuração | Verificação | Publicação |
|---|---|---|---|---|---|---|
| experiencias.6 · Continuidade da experiência | C1/C8 | parcial | UI/estrutura; sem conteúdo novo inventado | ver dependências D11 | UI; falha/retry; offline durável não implementado | C1 não publicada; live permanece v1 |
| experiencias.6.1 · Referência curta em painel contextual | C1/C8 | implementado em revisão | UI/estrutura; sem conteúdo novo inventado | ver dependências D11 | UI; falha/retry; offline durável não implementado | C1 não publicada; live permanece v1 |
| experiencias.6.2 · Ir a outro produto sem perder a atividade | C1/C8 | parcial | UI/estrutura; sem conteúdo novo inventado | ver dependências D11 | UI; falha/retry; offline durável não implementado | C1 não publicada; live permanece v1 |
| experiencias.6.3 · Rede lenta, offline e troca de aplicativo | C1/C8 | recuperação durante a aba parcial; offline durável ausente | UI/estrutura; sem conteúdo novo inventado | ver dependências D11 | UI; falha/retry; offline durável não implementado | C1 não publicada; live permanece v1 |

## 07 · Jarvis, central de comando de Sol

Bastidores privados: coordenação do ecossistema existente.

### jarvis.1 · Conexão com o app

Vínculo técnico: `lib/platform/jarvis.ts; lib/platform/events.ts; integrations/jarvis/relacione-client.mjs`. Rota/serviço: `/api/integracoes/jarvis`. Dados: catálogo/eventos/cursor. Permissão: Bearer leitura + gateway privado.

| ID / ramificação | Camada | Implementação | Conteúdo | Configuração | Verificação | Publicação |
|---|---|---|---|---|---|---|
| jarvis.1 · Conexão com o app | C6 | parcial | UI/estrutura; sem conteúdo novo inventado | ver dependências D07 | API e consumidor testados; conexão real pendente | C1 não publicada; live permanece v1 |
| jarvis.1.1 · Catálogo, versões e estados | C6 | implementado em revisão | UI/estrutura; sem conteúdo novo inventado | ver dependências D07 | API e consumidor testados; conexão real pendente | C1 não publicada; live permanece v1 |
| jarvis.1.2 · Links e dependências operacionais | C6 | implementado em revisão | UI/estrutura; sem conteúdo novo inventado | ver dependências D07 | API e consumidor testados; conexão real pendente | C1 não publicada; live permanece v1 |
| jarvis.1.3 · Autenticação e escopo mínimo | C6 | implementado em revisão; operação real pendente | UI/estrutura; sem conteúdo novo inventado | ver dependências D07 | API e consumidor testados; conexão real pendente | C1 não publicada; live permanece v1 |
| jarvis.1.4 · Eventos de conteúdo, oferta e acesso | C6 | parcial | UI/estrutura; sem conteúdo novo inventado | ver dependências D07 | API e consumidor testados; conexão real pendente | C1 não publicada; live permanece v1 |

### jarvis.2 · Inteligência operacional

Vínculo técnico: `lib/platform/link-registry.ts; components/site/operations.tsx`. Rota/serviço: `/admin/operacao`. Dados: links/dependências/campanhas. Permissão: admin; nenhuma ação externa implícita.

| ID / ramificação | Camada | Implementação | Conteúdo | Configuração | Verificação | Publicação |
|---|---|---|---|---|---|---|
| jarvis.2 · Inteligência operacional | C6 | módulo interno parcial; Jarvis real não conectado | UI/estrutura; sem conteúdo novo inventado | ver dependências D07 | verificador interno; coordenação externa pendente | C1 não publicada; live permanece v1 |
| jarvis.2.1 · Verificar links e detectar inconsistências | C6 | módulo interno parcial; Jarvis real não conectado | UI/estrutura; sem conteúdo novo inventado | ver dependências D07 | verificador interno; coordenação externa pendente | C1 não publicada; live permanece v1 |
| jarvis.2.2 · Conferir produtos, ofertas e conteúdos | C6 | módulo interno parcial; Jarvis real não conectado | UI/estrutura; sem conteúdo novo inventado | ver dependências D07 | verificador interno; coordenação externa pendente | C1 não publicada; live permanece v1 |
| jarvis.2.3 · Identificar lacunas e priorizar trabalho | C6 | módulo interno parcial; Jarvis real não conectado | UI/estrutura; sem conteúdo novo inventado | ver dependências D07 | verificador interno; coordenação externa pendente | C1 não publicada; live permanece v1 |
| jarvis.2.4 · Coordenar tarefas autorizadas | C6 | módulo interno parcial; Jarvis real não conectado | UI/estrutura; sem conteúdo novo inventado | ver dependências D07 | verificador interno; coordenação externa pendente | C1 não publicada; live permanece v1 |
| jarvis.2.5 · Preparar distribuição por canal | C6 | módulo interno parcial; Jarvis real não conectado | UI/estrutura; sem conteúdo novo inventado | ver dependências D07 | verificador interno; coordenação externa pendente | C1 não publicada; live permanece v1 |

### jarvis.3 · Estúdio e distribuição

Vínculo técnico: `integrations/jarvis/README.md`. Rota/serviço: `Jarvis externo a conectar`. Dados: brief/séries/canais/voz. Permissão: Sol; publicação autorizada.

| ID / ramificação | Camada | Implementação | Conteúdo | Configuração | Verificação | Publicação |
|---|---|---|---|---|---|---|
| jarvis.3 · Estúdio e distribuição | C6/C7 | módulo interno parcial; Jarvis real não conectado | UI/estrutura; sem conteúdo novo inventado | ver dependências D07,D08 | especificado, não operacional | C1 não publicada; live permanece v1 |
| jarvis.3.1 · Conteúdo editorial e campanhas | C6/C7 | módulo interno parcial; Jarvis real não conectado | UI/estrutura; sem conteúdo novo inventado | ver dependências D07,D08 | especificado, não operacional | C1 não publicada; live permanece v1 |
| jarvis.3.2 · Redes sociais e WhatsApp | C6/C7 | módulo interno parcial; Jarvis real não conectado | UI/estrutura; sem conteúdo novo inventado | ver dependências D07,D08 | especificado, não operacional | C1 não publicada; live permanece v1 |
| jarvis.3.3 · Telegram com retorno ao app | C6/C7 | módulo interno parcial; Jarvis real não conectado | UI/estrutura; sem conteúdo novo inventado | ver dependências D07,D08 | especificado, não operacional | C1 não publicada; live permanece v1 |
| jarvis.3.4 · Jarvis Live · apoio à Sol | C6/C7 | módulo interno parcial; Jarvis real não conectado | UI/estrutura; sem conteúdo novo inventado | ver dependências D07,D08 | especificado, não operacional | C1 não publicada; live permanece v1 |
| jarvis.3.5 · Voz e contexto de Sol | C6/C7 | módulo interno parcial; Jarvis real não conectado | UI/estrutura; sem conteúdo novo inventado | ver dependências D07,D08 | especificado, não operacional | C1 não publicada; live permanece v1 |

### jarvis.4 · Acompanhamento comercial

Vínculo técnico: `lib/platform/traffic.ts; lib/platform/commerce.ts`. Rota/serviço: `/admin/operacao`. Dados: agregados/eventos/custos futuros. Permissão: sem intimidade; métricas reais.

| ID / ramificação | Camada | Implementação | Conteúdo | Configuração | Verificação | Publicação |
|---|---|---|---|---|---|---|
| jarvis.4 · Acompanhamento comercial | C6/C7 | módulo interno parcial; Jarvis real não conectado | UI/estrutura; sem conteúdo novo inventado | ver dependências D03,D07,D10 | contagens; receita/custos/margem não conectados | C1 não publicada; live permanece v1 |
| jarvis.4.1 · Conversão, renovação e reembolso | C6/C7 | módulo interno parcial; Jarvis real não conectado | UI/estrutura; sem conteúdo novo inventado | ver dependências D03,D07,D10 | contagens; receita/custos/margem não conectados | C1 não publicada; live permanece v1 |
| jarvis.4.2 · Custo de mídia, IA, taxas e suporte | C6/C7 | módulo interno parcial; Jarvis real não conectado | UI/estrutura; sem conteúdo novo inventado | ver dependências D03,D07,D10 | contagens; receita/custos/margem não conectados | C1 não publicada; live permanece v1 |
| jarvis.4.3 · Margem por produto e canal | C6/C7 | módulo interno parcial; Jarvis real não conectado | UI/estrutura; sem conteúdo novo inventado | ver dependências D03,D07,D10 | contagens; receita/custos/margem não conectados | C1 não publicada; live permanece v1 |
| jarvis.4.4 · Avaliar retorno do Telegram | C6/C7 | módulo interno parcial; Jarvis real não conectado | UI/estrutura; sem conteúdo novo inventado | ver dependências D03,D07,D10 | contagens; receita/custos/margem não conectados | C1 não publicada; live permanece v1 |

### jarvis.5 · Limites do comando

Vínculo técnico: `lib/platform/jarvis.ts; lib/platform/http.ts`. Rota/serviço: `/api/integracoes/jarvis`. Dados: exportação/eventos. Permissão: allowlist/token e escopo mínimo.

| ID / ramificação | Camada | Implementação | Conteúdo | Configuração | Verificação | Publicação |
|---|---|---|---|---|---|---|
| jarvis.5 · Limites do comando | C6 | parcial | UI/estrutura; sem conteúdo novo inventado | ver dependências D02,D07 | nega clientes/token inválido; ações externas pendentes | C1 não publicada; live permanece v1 |
| jarvis.5.1 · Somente Sol e administradores autorizados | C6 | implementado em revisão | UI/estrutura; sem conteúdo novo inventado | ver dependências D02,D07 | nega clientes/token inválido; ações externas pendentes | C1 não publicada; live permanece v1 |
| jarvis.5.2 · Sem respostas íntimas na exportação | C6 | implementado em revisão | UI/estrutura; sem conteúdo novo inventado | ver dependências D02,D07 | nega clientes/token inválido; ações externas pendentes | C1 não publicada; live permanece v1 |
| jarvis.5.3 · Mensagens, gastos e publicação autorizados | C6 | pendente | UI/estrutura; sem conteúdo novo inventado | ver dependências D02,D07 | nega clientes/token inválido; ações externas pendentes | C1 não publicada; live permanece v1 |
| jarvis.5.4 · Revisão humana e registro de ações | C6 | pendente | UI/estrutura; sem conteúdo novo inventado | ver dependências D02,D07 | nega clientes/token inválido; ações externas pendentes | C1 não publicada; live permanece v1 |

## 08 · Administração editorial e operação

A área de serviço que mantém o universo organizado.

### operacao.1 · Mesa editorial

Vínculo técnico: `components/site/admin.tsx; lib/platform/editorial.ts; lib/platform/media.ts`. Rota/serviço: `/admin`. Dados: conteúdo/histórico/assets. Permissão: admin; versão publicada imutável.

| ID / ramificação | Camada | Implementação | Conteúdo | Configuração | Verificação | Publicação |
|---|---|---|---|---|---|---|
| operacao.1 · Mesa editorial | C4 | implementado em revisão | UI/estrutura; sem conteúdo novo inventado | ver dependências D02,D04,D05 | workflow/editorial/rollback/hashes testados | C1 não publicada; live permanece v1 |
| operacao.1.1 · Rascunho → revisão → publicado → arquivado | C4 | implementado em revisão | UI/estrutura; sem conteúdo novo inventado | ver dependências D02,D04,D05 | workflow/editorial/rollback/hashes testados | C1 não publicada; live permanece v1 |
| operacao.1.2 · Conteúdo, capítulos e histórico | C4 | implementado em revisão | UI/estrutura; sem conteúdo novo inventado | ver dependências D02,D04,D05 | workflow/editorial/rollback/hashes testados | C1 não publicada; live permanece v1 |
| operacao.1.3 · Nova versão sem apagar a anterior | C4 | implementado em revisão | UI/estrutura; sem conteúdo novo inventado | ver dependências D02,D04,D05 | workflow/editorial/rollback/hashes testados | C1 não publicada; live permanece v1 |
| operacao.1.4 · Proveniência e autoria | C4 | implementado em revisão | UI/estrutura; sem conteúdo novo inventado | ver dependências D02,D04,D05 | workflow/editorial/rollback/hashes testados | C1 não publicada; live permanece v1 |
| operacao.1.5 · Arquivos finais e mídia protegida | C4 | implementado em revisão; operação real pendente | UI/estrutura; sem conteúdo novo inventado | ver dependências D02,D04,D05 | workflow/editorial/rollback/hashes testados | C1 não publicada; live permanece v1 |

### operacao.2 · Mesa comercial

Vínculo técnico: `components/site/admin.tsx; lib/platform/commerce.ts`. Rota/serviço: `/admin`. Dados: oferta/contrato/mapeamento. Permissão: admin; sem concessão pelo browser.

| ID / ramificação | Camada | Implementação | Conteúdo | Configuração | Verificação | Publicação |
|---|---|---|---|---|---|---|
| operacao.2 · Mesa comercial | C3 | parcial | UI/estrutura; sem conteúdo novo inventado | ver dependências D02,D03 | estrutura testada; conciliação real pendente | C1 não publicada; live permanece v1 |
| operacao.2.1 · Produtos, ofertas e componentes | C3 | implementado em revisão | UI/estrutura; sem conteúdo novo inventado | ver dependências D02,D03 | estrutura testada; conciliação real pendente | C1 não publicada; live permanece v1 |
| operacao.2.2 · Combos, bônus e prazos informados | C3 | implementado em revisão | UI/estrutura; sem conteúdo novo inventado | ver dependências D02,D03 | estrutura testada; conciliação real pendente | C1 não publicada; live permanece v1 |
| operacao.2.3 · Mapeamento de ofertas Kiwify | C3 | pendente | UI/estrutura; sem conteúdo novo inventado | ver dependências D02,D03 | estrutura testada; conciliação real pendente | C1 não publicada; live permanece v1 |
| operacao.2.4 · Suporte a compra e conciliação | C3 | pendente | UI/estrutura; sem conteúdo novo inventado | ver dependências D02,D03 | estrutura testada; conciliação real pendente | C1 não publicada; live permanece v1 |

### operacao.3 · Mapa de links oficiais

Vínculo técnico: `lib/platform/link-registry.ts; components/site/operations.tsx`. Rota/serviço: `/admin/operacao`. Dados: destino/checagem. Permissão: allowlist de destinos; sem SSRF livre.

| ID / ramificação | Camada | Implementação | Conteúdo | Configuração | Verificação | Publicação |
|---|---|---|---|---|---|---|
| operacao.3 · Mapa de links oficiais | C6/C7 | parcial | UI/estrutura; sem conteúdo novo inventado | ver dependências D07,D08 | verificador testado; recorrência não ativada | C1 não publicada; live permanece v1 |
| operacao.3.1 · Destino e estado esperado | C6/C7 | parcial | UI/estrutura; sem conteúdo novo inventado | ver dependências D07,D08 | verificador testado; recorrência não ativada | C1 não publicada; live permanece v1 |
| operacao.3.2 · Última checagem e falhas | C6/C7 | parcial | UI/estrutura; sem conteúdo novo inventado | ver dependências D07,D08 | verificador testado; recorrência não ativada | C1 não publicada; live permanece v1 |
| operacao.3.3 · Monitoramento recorrente pelo Jarvis | C6/C7 | pendente | UI/estrutura; sem conteúdo novo inventado | ver dependências D07,D08 | verificador testado; recorrência não ativada | C1 não publicada; live permanece v1 |
| operacao.3.4 · Canva e Telegram | C6/C7 | depende de definição | UI/estrutura; sem conteúdo novo inventado | ver dependências D07,D08 | verificador testado; recorrência não ativada | C1 não publicada; live permanece v1 |

### operacao.4 · Analytics

Vínculo técnico: `lib/platform/traffic.ts; components/site/traffic-runtime.ts`. Rota/serviço: `/api/trafego; /admin/operacao`. Dados: agregados/recibos. Permissão: opt-in/GPC; sem texto íntimo.

| ID / ramificação | Camada | Implementação | Conteúdo | Configuração | Verificação | Publicação |
|---|---|---|---|---|---|---|
| operacao.4 · Analytics | C7 | parcial | UI/estrutura; sem conteúdo novo inventado | ver dependências D03,D10 | deduplicação/origem/GPC; comércio real pendente | C1 não publicada; live permanece v1 |
| operacao.4.1 · Descoberta e ações agregadas | C7 | implementado em revisão | UI/estrutura; sem conteúdo novo inventado | ver dependências D03,D10 | deduplicação/origem/GPC; comércio real pendente | C1 não publicada; live permanece v1 |
| operacao.4.2 · Conclusão de Dia sem respostas pessoais | C7 | implementado em revisão | UI/estrutura; sem conteúdo novo inventado | ver dependências D03,D10 | deduplicação/origem/GPC; comércio real pendente | C1 não publicada; live permanece v1 |
| operacao.4.3 · Consumo, retomada e primeira atividade | C7 | parcial | UI/estrutura; sem conteúdo novo inventado | ver dependências D03,D10 | deduplicação/origem/GPC; comércio real pendente | C1 não publicada; live permanece v1 |
| operacao.4.4 · Venda confirmada e atribuição | C7 | pendente | UI/estrutura; sem conteúdo novo inventado | ver dependências D03,D10 | deduplicação/origem/GPC; comércio real pendente | C1 não publicada; live permanece v1 |
| operacao.4.5 · Renovação, reembolso e custo | C7 | pendente | UI/estrutura; sem conteúdo novo inventado | ver dependências D03,D10 | deduplicação/origem/GPC; comércio real pendente | C1 não publicada; live permanece v1 |
| operacao.4.6 · Sem Caderno, conversas ou termos íntimos | C7 | implementado em revisão | UI/estrutura; sem conteúdo novo inventado | ver dependências D03,D10 | deduplicação/origem/GPC; comércio real pendente | C1 não publicada; live permanece v1 |

### operacao.5 · Suporte e qualidade

Vínculo técnico: `components/site/help.tsx; docs/CONTRATOS-INTEGRACAO.md`. Rota/serviço: `/ajuda`. Dados: solicitações/recuperação. Permissão: titular/admin.

| ID / ramificação | Camada | Implementação | Conteúdo | Configuração | Verificação | Publicação |
|---|---|---|---|---|---|---|
| operacao.5 · Suporte e qualidade | C2/C8 | parcial | UI/estrutura; sem conteúdo novo inventado | ver dependências D01,D02,D11 | ajuda interna; homologação operacional pendente | C1 não publicada; live permanece v1 |
| operacao.5.1 · Ajuda consistente e protocolo | C2/C8 | implementado em revisão | UI/estrutura; sem conteúdo novo inventado | ver dependências D01,D02,D11 | ajuda interna; homologação operacional pendente | C1 não publicada; live permanece v1 |
| operacao.5.2 · Tratamento de falhas e recuperação | C2/C8 | pendente | UI/estrutura; sem conteúdo novo inventado | ver dependências D01,D02,D11 | ajuda interna; homologação operacional pendente | C1 não publicada; live permanece v1 |
| operacao.5.3 · Acessibilidade e testes de uso | C2/C8 | parcial | UI/estrutura; sem conteúdo novo inventado | ver dependências D01,D02,D11 | ajuda interna; homologação operacional pendente | C1 não publicada; live permanece v1 |
| operacao.5.4 · Backup, restauração e reversão | C2/C8 | parcial | UI/estrutura; sem conteúdo novo inventado | ver dependências D01,D02,D11 | ajuda interna; homologação operacional pendente | C1 não publicada; live permanece v1 |

## 09 · Fundações e engenharia

A estrutura que sustenta todas as alas sem duplicar clientes e conteúdo.

### fundacao.1 · Camada de apresentação

Vínculo técnico: `app/layout.tsx; components/site/chrome.tsx`. Rota/serviço: `rotas do app`. Dados: apresentação/estado. Permissão: UI não substitui servidor.

| ID / ramificação | Camada | Implementação | Conteúdo | Configuração | Verificação | Publicação |
|---|---|---|---|---|---|---|
| fundacao.1 · Camada de apresentação | C1/C8 | implementado em revisão | UI/estrutura; sem conteúdo novo inventado | ver dependências D11 | build e UI parcial; serviços externos pendentes | C1 não publicada; live permanece v1 |
| fundacao.1.1 · Início, Explorar e páginas de produto | C1/C8 | implementado em revisão | UI/estrutura; sem conteúdo novo inventado | ver dependências D11 | build e UI parcial; serviços externos pendentes | C1 não publicada; live permanece v1 |
| fundacao.1.2 · Biblioteca, Caderno, Jornada e leitor | C1/C8 | implementado em revisão | UI/estrutura; sem conteúdo novo inventado | ver dependências D11 | build e UI parcial; serviços externos pendentes | C1 não publicada; live permanece v1 |
| fundacao.1.3 · LÚCIDA e administração | C1/C8 | parcial | UI/estrutura; sem conteúdo novo inventado | ver dependências D11 | build e UI parcial; serviços externos pendentes | C1 não publicada; live permanece v1 |

### fundacao.2 · Camada de serviços

Vínculo técnico: `lib/platform/http.ts; lib/platform/access.ts; lib/platform/learning.ts`. Rota/serviço: `/api/*`. Dados: identidade/versões/direitos/progresso. Permissão: validação no servidor.

| ID / ramificação | Camada | Implementação | Conteúdo | Configuração | Verificação | Publicação |
|---|---|---|---|---|---|---|
| fundacao.2 · Camada de serviços | C2/C3/C5/C6 | parcial | UI/estrutura; sem conteúdo novo inventado | ver dependências D01,D03,D06,D07 | núcleo testado; integrações externas parciais | C1 não publicada; live permanece v1 |
| fundacao.2.1 · Identidade e permissões por titular | C2/C3/C5/C6 | implementado em revisão | UI/estrutura; sem conteúdo novo inventado | ver dependências D01,D03,D06,D07 | núcleo testado; integrações externas parciais | C1 não publicada; live permanece v1 |
| fundacao.2.2 · Catálogo editorial e versões | C2/C3/C5/C6 | implementado em revisão | UI/estrutura; sem conteúdo novo inventado | ver dependências D01,D03,D06,D07 | núcleo testado; integrações externas parciais | C1 não publicada; live permanece v1 |
| fundacao.2.3 · Direitos comerciais e ritmo pedagógico | C2/C3/C5/C6 | implementado em revisão | UI/estrutura; sem conteúdo novo inventado | ver dependências D01,D03,D06,D07 | núcleo testado; integrações externas parciais | C1 não publicada; live permanece v1 |
| fundacao.2.4 · Progresso e registros pessoais | C2/C3/C5/C6 | implementado em revisão | UI/estrutura; sem conteúdo novo inventado | ver dependências D01,D03,D06,D07 | núcleo testado; integrações externas parciais | C1 não publicada; live permanece v1 |
| fundacao.2.5 · Conectores de Kiwify, LÚCIDA e Jarvis | C2/C3/C5/C6 | parcial | UI/estrutura; sem conteúdo novo inventado | ver dependências D01,D03,D06,D07 | núcleo testado; integrações externas parciais | C1 não publicada; live permanece v1 |

### fundacao.3 · Camada de dados

Vínculo técnico: `db/schema.ts; drizzle/0003_futuristic_scarlet_spider.sql`. Rota/serviço: `D1/R2`. Dados: tabelas existentes/aditivas. Permissão: por proprietário; mídia protegida.

| ID / ramificação | Camada | Implementação | Conteúdo | Configuração | Verificação | Publicação |
|---|---|---|---|---|---|---|
| fundacao.3 · Camada de dados | C2/C4 | implementado em revisão | UI/estrutura; sem conteúdo novo inventado | ver dependências D05,D11 | SQLite isolado; não migrado em produção | C1 não publicada; live permanece v1 |
| fundacao.3.1 · Caderno e analytics existentes | C2/C4 | implementado em revisão | UI/estrutura; sem conteúdo novo inventado | ver dependências D05,D11 | SQLite isolado; não migrado em produção | C1 não publicada; live permanece v1 |
| fundacao.3.2 · Versões editoriais e histórico | C2/C4 | implementado em revisão | UI/estrutura; sem conteúdo novo inventado | ver dependências D05,D11 | SQLite isolado; não migrado em produção | C1 não publicada; live permanece v1 |
| fundacao.3.3 · Origens de contratação e direitos | C2/C4 | implementado em revisão | UI/estrutura; sem conteúdo novo inventado | ver dependências D05,D11 | SQLite isolado; não migrado em produção | C1 não publicada; live permanece v1 |
| fundacao.3.4 · Progresso, favoritos e preferências | C2/C4 | implementado em revisão | UI/estrutura; sem conteúdo novo inventado | ver dependências D05,D11 | SQLite isolado; não migrado em produção | C1 não publicada; live permanece v1 |
| fundacao.3.5 · Pedidos de ajuda | C2/C4 | implementado em revisão | UI/estrutura; sem conteúdo novo inventado | ver dependências D05,D11 | SQLite isolado; não migrado em produção | C1 não publicada; live permanece v1 |
| fundacao.3.6 · Mídia autorizada e armazenamento privado | C2/C4 | implementado em revisão; operação real pendente | UI/estrutura; sem conteúdo novo inventado | ver dependências D05,D11 | SQLite isolado; não migrado em produção | C1 não publicada; live permanece v1 |

### fundacao.4 · Ponte com o Magnetus3 canônico

Vínculo técnico: `docs/SOURCE-LOCK-REVISAO.json; docs/DECISAO-INTEGRACAO-2026-09-21.md`. Rota/serviço: `Magnetus3 canônico`. Dados: fontes/contas/contratos legados. Permissão: vínculo com prova; sem mescla por email.

| ID / ramificação | Camada | Implementação | Conteúdo | Configuração | Verificação | Publicação |
|---|---|---|---|---|---|---|
| fundacao.4 · Ponte com o Magnetus3 canônico | C2/C4 | parcial | UI/estrutura; sem conteúdo novo inventado | ver dependências D01,D04 | hashes preservados; legado não migrado | C1 não publicada; live permanece v1 |
| fundacao.4.1 · Regras e conteúdo D0–D3 reaproveitados | C2/C4 | implementado em revisão | D0–D3 importados, hashes preservados | ver dependências D01,D04 | hashes preservados; legado não migrado | C1 não publicada; live permanece v1 |
| fundacao.4.2 · Runtime Better Auth + PostgreSQL | C2/C4 | pendente | UI/estrutura; sem conteúdo novo inventado | ver dependências D01,D04 | hashes preservados; legado não migrado | C1 não publicada; live permanece v1 |
| fundacao.4.3 · Migração e vínculo de contas | C2/C4 | pendente | UI/estrutura; sem conteúdo novo inventado | ver dependências D01,D04 | hashes preservados; legado não migrado | C1 não publicada; live permanece v1 |
| fundacao.4.4 · Preservação de contratos e progresso antigo | C2/C4 | pendente | UI/estrutura; sem conteúdo novo inventado | ver dependências D01,D04 | hashes preservados; legado não migrado | C1 não publicada; live permanece v1 |

### fundacao.5 · Cofres separados

Vínculo técnico: `lib/platform/access.ts; app/api/caderno/route.ts; lib/platform/jarvis.ts`. Rota/serviço: `catálogo; /caderno; /lucida`. Dados: domínios separados. Permissão: público/pago/pessoal/operacional.

| ID / ramificação | Camada | Implementação | Conteúdo | Configuração | Verificação | Publicação |
|---|---|---|---|---|---|---|
| fundacao.5 · Cofres separados | C2/C5/C6 | parcial | UI/estrutura; sem conteúdo novo inventado | ver dependências D01,D06,D07 | isolamento testado; memória/conexão futuras | C1 não publicada; live permanece v1 |
| fundacao.5.1 · Catálogo público | C2/C5/C6 | implementado em revisão | UI/estrutura; sem conteúdo novo inventado | ver dependências D01,D06,D07 | isolamento testado; memória/conexão futuras | C1 não publicada; live permanece v1 |
| fundacao.5.2 · Conteúdo pago autorizado | C2/C5/C6 | implementado em revisão | UI/estrutura; sem conteúdo novo inventado | ver dependências D01,D06,D07 | isolamento testado; memória/conexão futuras | C1 não publicada; live permanece v1 |
| fundacao.5.3 · Caderno particular por conta | C2/C5/C6 | implementado em revisão | UI/estrutura; sem conteúdo novo inventado | ver dependências D01,D06,D07 | isolamento testado; memória/conexão futuras | C1 não publicada; live permanece v1 |
| fundacao.5.4 · Memória pessoal da LÚCIDA | C2/C5/C6 | pendente | UI/estrutura; sem conteúdo novo inventado | ver dependências D01,D06,D07 | isolamento testado; memória/conexão futuras | C1 não publicada; live permanece v1 |
| fundacao.5.5 · Indicadores operacionais do Jarvis | C2/C5/C6 | parcial | UI/estrutura; sem conteúdo novo inventado | ver dependências D01,D06,D07 | isolamento testado; memória/conexão futuras | C1 não publicada; live permanece v1 |

### fundacao.6 · Qualidade antes de abrir a casa

Vínculo técnico: `scripts/qa/ecosystem.cjs; scripts/qa/data-handlers.cjs; scripts/qa/continuity.cjs`. Rota/serviço: `QA`. Dados: dados sintéticos/relatórios. Permissão: produção preservada.

| ID / ramificação | Camada | Implementação | Conteúdo | Configuração | Verificação | Publicação |
|---|---|---|---|---|---|---|
| fundacao.6 · Qualidade antes de abrir a casa | C8 | parcial | UI/estrutura; sem conteúdo novo inventado | ver dependências D01,D03,D11 | 85 automatizados + UI descrita; sem certificação integral | C1 não publicada; live permanece v1 |
| fundacao.6.1 · Isolamento, conflitos e regras comerciais | C8 | implementado em revisão | UI/estrutura; sem conteúdo novo inventado | ver dependências D01,D03,D11 | 85 automatizados + UI descrita; sem certificação integral | C1 não publicada; live permanece v1 |
| fundacao.6.2 · Responsividade e teclado | C8 | parcial | UI/estrutura; sem conteúdo novo inventado | ver dependências D01,D03,D11 | 85 automatizados + UI descrita; sem certificação integral | C1 não publicada; live permanece v1 |
| fundacao.6.3 · WCAG 2.2 AA e leitor de tela | C8 | pendente | UI/estrutura; sem conteúdo novo inventado | ver dependências D01,D03,D11 | 85 automatizados + UI descrita; sem certificação integral | C1 não publicada; live permanece v1 |
| fundacao.6.4 · Safari/iPhone, Android e rede instável | C8 | pendente | UI/estrutura; sem conteúdo novo inventado | ver dependências D01,D03,D11 | 85 automatizados + UI descrita; sem certificação integral | C1 não publicada; live permanece v1 |
| fundacao.6.5 · Desempenho e Core Web Vitals | C8 | pendente | UI/estrutura; sem conteúdo novo inventado | ver dependências D01,D03,D11 | 85 automatizados + UI descrita; sem certificação integral | C1 não publicada; live permanece v1 |
| fundacao.6.6 · Compra → acesso → uso → retorno | C8 | pendente | UI/estrutura; sem conteúdo novo inventado | ver dependências D01,D03,D11 | 85 automatizados + UI descrita; sem certificação integral | C1 não publicada; live permanece v1 |

### fundacao.7 · Expansões de plataforma

Vínculo técnico: `docs/planta-relacione-se.html`. Rota/serviço: `não ativado`. Dados: a definir por expansão. Permissão: consentimento/permissões específicos.

| ID / ramificação | Camada | Implementação | Conteúdo | Configuração | Verificação | Publicação |
|---|---|---|---|---|---|---|
| fundacao.7 · Expansões de plataforma | opcional após C8 | expansão opcional não ativada | UI/estrutura; sem conteúdo novo inventado | ver dependências D12 | não implementado; não bloqueia núcleo | C1 não publicada; live permanece v1 |
| fundacao.7.1 · Instalação na tela inicial | opcional após C8 | expansão opcional não ativada | UI/estrutura; sem conteúdo novo inventado | ver dependências D12 | não implementado; não bloqueia núcleo | C1 não publicada; live permanece v1 |
| fundacao.7.2 · Notificações opcionais | opcional após C8 | expansão opcional não ativada | UI/estrutura; sem conteúdo novo inventado | ver dependências D12 | não implementado; não bloqueia núcleo | C1 não publicada; live permanece v1 |
| fundacao.7.3 · Automações editoriais | opcional após C8 | expansão opcional não ativada | UI/estrutura; sem conteúdo novo inventado | ver dependências D12 | não implementado; não bloqueia núcleo | C1 não publicada; live permanece v1 |
| fundacao.7.4 · Telegram Mini App | opcional após C8 | expansão opcional não ativada | UI/estrutura; sem conteúdo novo inventado | ver dependências D12 | não implementado; não bloqueia núcleo | C1 não publicada; live permanece v1 |

## Complementos que não podem desaparecer nas próximas camadas

- **MM01–MM17** de `09-app/JARVIS-LUCIDA-MINUTOS-MAGNETUS-2026-09-21.md`: referências multimodais → Visionário → séries/episódios/perguntas → LÚCIDA → respostas autorizadas → mapa pré-mentoria → agregados. Associados às áreas Jarvis, LÚCIDA, produtos e operação; execução em C5–C7, com orçamento/permissões próprios.
- A atualização documental aponta **Sollimastudio/SOL-IA, PR #8**, e **Magnetus3, PR #1**, como fontes adicionais a verificar em C5/C6. Não afirmar que JARVIS-SOL seja o runtime definitivo. app.Sol.ia não deve ser confundido com o Jarvis por semelhança de nome.
- Telas/funções do handoff Manus não detalhadas na planta (onboarding, mapas, experimentos, mentoria e notificações) ficam rastreadas na fonte de 09-app e nas camadas C2/C4/C5/C8; não foram declaradas prontas por existir uma rota genérica.
- Estados editoriais das obras devem ser conferidos nas fontes atuais antes de integração. Manuscritos e corpus existem; falta selecionar e homologar a versão publicável para cada destino, não pedir que Sol reconstrua material já disponível.
