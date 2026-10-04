# MINDSETmagro — integração no app vigente

Status: implementação em branch de revisão, sem publicação e sem emissão de entitlement. Recurso de acesso independente `mindsetmagro_30d`; nenhuma URL concede acesso.

## Fonte
`content/mindsetmagro/manifest.json`, `prebook.json`, `days/d01.json`…`d30.json` devem ser derivados do cânone. O adapter é server-only e importa os JSON somente no servidor. Componentes clientes importam apenas tipos. Pré-livro deve ter `day:0`, `blocks`, `title`, `objective` e os campos do contrato comum. Alterar versão do manifest provoca conflito preservando respostas antigas, até migração explícita.

## API
Todas as rotas `/api/mindsetmagro/[resource]` exigem identidade e entitlement. GET: `overview`, `day?day=N`, `notebook`. POST: `start`, `save`, `complete`. Dia 0 = pré-livro; unidade técnica 31 = pós-livro/manutenção, acessível depois de concluir D30. A manutenção permanece editável e não pede conclusão pela interface. Mutações reutilizam verificação de origem e proprietário da aba. Respostas usam `private, no-store`.

`overview` só entrega metadados dos dias e estados. Primeira abertura explícita cria timestamp no servidor. Dia N>1 exige conclusão anterior e 24h desde primeira abertura anterior. Cliente não fornece relógio nem duração. Read e write revalidam entitlement. Registros concluídos são somente leitura.

Persistência em `learning_progress` existente, sem nova tabela. UPDATE exige revision atual; conflito não sobrescreve. Limites: 6.000 caracteres/campo e 100.000 caracteres/dia. Campos desconhecidos, selects inválidos e números não finitos são rejeitados. Corpo e alimentação exigem opt-in independente; não são condições de conclusão sem opt-in.

Conclusão: campo Fruto canônico (reutilizado sem digitação duplicada) ou evidência + required_field_ids canônicos, OU obstáculo + próxima ação segura. Evidência negativa é válida. Campos técnicos: completionEvidence, completionObstacle, completionNextAction, optBody, optFood. Nenhum escore de saúde ou diagnóstico.

## Cliente
Um bloco por tela, cursor e `learning_progress.location={field_id}` salvos junto com respostas. O servidor aceita somente IDs do bloco atual (ou campos de fechamento); a UI retoma foco no campo salvo. Salvamento manual explícito, alerta ao sair com texto não salvo, rascunho exportável. Em 401/409 o texto permanece na tela; comparação consulta servidor sem apagar rascunho. Escolha explícita entre substituir após comparar ou descartar rascunho. Nenhum texto sensível gravado em localStorage. Queda de processo antes de salvar pode perder rascunho: não há promessa de autosave.

Caderno agregado usa os mesmos campos; impressão do navegador permite PDF pessoal. Bridge contextual reutiliza `sendChatMessage` do chat existente. O texto preparado contém somente título/objetivo do dia, é editável e exige checkbox de consentimento + botão de envio. Respostas do Caderno não são recebidas pelo componente nem copiadas. O backend vigente continua `public_catalog`; é reflexão geral, sem tutor source-locked do protocolo. A integração profunda exigirá novo contrato de contexto autorizado, política de retrieval e homologação do provedor. O link `/lucida` também permite abrir conversa livre sem transferência automática. Nenhuma chamada real ao provedor foi feita na QA. Sem analytics de respostas.

## Verificação
`node --test scripts/qa/mindsetmagro.test.mjs`: 6 testes passaram. Cobrem lógica de conclusão, opt-in, campos inválidos, gate 24h e ausência de import de conteúdo no cliente. Não equivalem a teste end-to-end de identidade/D1.

TypeScript completo, lint focado e build Vinext passaram após sincronização. Harness de API real passou 17 cenários usando SQLite em memória, migrações reais e identidades sintéticas. Browser real bloqueado: Chromium indisponível após falha de download CDN (ZIP vazio); não afirmar homologação 320px/Safari. Executar após instalação/sincronização: typecheck, lint focado, build, browser 320px/teclado/iOS Safari, cenário duas abas 409, expiração 401/403, boundary de bundle, API com identidade/grants sintéticos. Não emitir grants comerciais para testar.

## Limites conhecidos
Sem migração automática de versões. Sem serviço de exportação PDF no servidor; impressão local do Caderno disponível. Não se validou leitor de tela nem aparelho iPhone real. Rota não é adicionada automaticamente a ofertas antigas. Conferir cadastro do recurso comercial antes de lançamento. Dez SVGs pedagógicos em public/mindsetmagro; o mapa visual-assets.json resolve o visual_ref no servidor e envia alt/src apenas com o dia autorizado.
