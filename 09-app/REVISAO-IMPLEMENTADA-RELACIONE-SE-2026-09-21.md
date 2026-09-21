# Relacione-se · entrega de revisão

Solicitação de 21/09/2026; validação final em 22/09/2026 UTC. Mudanças concretas para revisão, sem publicar em produção, migrar clientes, contratar serviços ou enviar mensagens.

## Implementado e seus limites

| Área | Implementação | Limite atual |
|---|---|---|
| Vitrine | 12 entradas; busca e filtros; Trilogia como coleção e livros separados; MINDSETmagro; painéis relacionados com fechamento e retorno | Obras não aprovadas permanecem em preparação |
| Biblioteca | Retomada, acessos, favoritos, histórico e soma de contratações sem duplicar produtos | Clientes reais dependem de identidade e direitos verificados |
| Magnetus Mulher | D0–D3 canônicos, campos progressivos, gravação, retomada, marcador, fontes e temas | Jornada parcial; exportação de tarefas de campo e registro de experimentos do M1 não portados |
| Ritmo pedagógico | Primeira abertura significativa inicia relógio; próximo Dia exige conclusão e 24 horas no servidor | Histórico legado precisa de reconciliação |
| Caderno | Mesma fonte de respostas do workbook/Antídoto; registros próprios após expiração | Sem enunciados pagos quando o direito expira |
| Antídoto | Recurso independente com prática canônica, persistência, gravação ao seguir links e controle de conflitos | Oferta avulsa depende da integração comercial |
| Leitor | Capítulos, índice, marcador, preferências, posição por capítulo e versão preservada após início | Manuscritos não publicados; sem retomada de rolagem por parágrafo |
| Áudios | Componente com transcrição, velocidade e callback de posição | Não conectado; falta mídia, armazenamento e transcrições; publicação bloqueada |
| Administração | Rascunho/revisão/publicação/arquivo, histórico, editor de capítulos e ofertas | Allowlist ainda não configurada; publicação de oferta não concede direitos |
| Comércio | Núcleo de direitos cumulativos, períodos, renovação, cancelamento, reembolso, chargeback e deduplicação | Webhook Kiwify fechado; cálculo de dias/meses depende do adaptador contratual |
| LÚCIDA | Contexto autorizado por recurso e Dia iniciado; filtro de fontes aprovadas | Sem provedor, corpus completo ou memória; prática editorial preservada |
| Jarvis | Exportação administrativa sem respostas íntimas | Contrato preparado; sem conexão, fila ou automações |
| Ajuda e analytics | Solicitação privada com protocolo; contagens agregadas sob consentimento | Sem envio externo; sem lucro ou conversão comercial real |

## Fontes e preservação

Prompt mestre e fontes de 09-app consultados integralmente antes das edições. Estado do Site e do Magnetus3 conferidos. Decisão e inventário em `DECISAO-INTEGRACAO-2026-09-21.md`; hashes e revisões importadas em `SOURCE-LOCK-REVISAO.json`. Os testes comparam blobs Git com bytes locais. Nenhum manuscrito da Trilogia foi reescrito ou divulgado. Identidade visual e recursos existentes reaproveitados.

## Evidências

- `scripts/qa/ecosystem.cjs`: 36 verificações, zero falhas. Módulos e handlers reais com SQLite isolado: titularidade, acesso por URL, soma de direitos, expiração, preservação de avulso, deduplicação, eventos fora de ordem, cancelamento, renovação, migração aditiva, retomada, concorrência, conclusão e limite exato de 24 horas, Caderno, Antídoto, versões, leitor, catálogo sem texto pago, Jarvis e contexto LÚCIDA.
- `scripts/qa/data-handlers.cjs`: 15 verificações, zero falhas. CRUD real do Caderno, isolamento por proprietário e whitelist de analytics.
- TypeScript sem erros e build oficial Sites concluído. Identidades sintéticas somente no harness isolado: nenhuma permissão de teste adicionada ao app.
- Chromium supervisionado: catálogo, busca por silêncio, produto Script, navegação, painel contextual, Escape e retorno do foco ao acionador observados.
- Produto e biblioteca em frames de 320, 390 e 768 px, sem overflow horizontal. Larguras úteis descontadas as barras: produto 305/375/753 px; biblioteca 305/375/768 px. Produto com fonte raiz a 200%, frame de 480 px e largura útil 465 px: sem overflow. Harness temporário removido antes do build final.
- `revisao-produto.jpg`: captura da página de produto. Um parágrafo integral protegido de D0 foi buscado no bundle cliente sem ocorrência; conteúdo completo importado por módulos de servidor. Isso não substitui os testes de autorização.
- Migração 0001 aplicada apenas no SQLite local. Preservação do Caderno anterior testada em isolamento. Nenhum dado real ou contrato importado/alterado.

Não é certificação WCAG, auditoria integral de segurança nem homologação comercial. Sem teste em Safari, dispositivo físico, leitor de tela, conta real de cliente ou provedor de IA. Sem Core Web Vitals de campo. Salvamento ao seguir links implementado; botão Voltar nativo durante edição pendente e recuperação de conexão exigem teste E2E autenticado.

## Pendências para produção

1. Definir identidade pública, vincular contas legadas com prova de titularidade, fazer backups e testar restauração. A revisão conserva a identidade do Site; não mescla por e-mail.
2. Configurar IDs administrativos; selecionar obras finais e conteúdos gratuitos aprovados.
3. Homologar Kiwify: autenticidade, credenciais, SKUs, composição/versionamento, titular, prazo, ativação, reconciliação, reembolso parcial e compra real de ponta a ponta. Fixar também a versão editorial contratada antes do primeiro uso.
4. Configurar LÚCIDA com provedor/orçamento autorizados, corpus por produto, consentimentos e avaliações reais; conectar Jarvis com escopo operacional mínimo.
5. Disponibilizar mídia/transcrições, conteúdo Homem e próximos Dias, MINDSETmagro e bônus aprovados; completar atividades de campo do M1.
6. Definir Telegram gratuito ou entrega paga. Convite não oferecido como brinde. Kiwify e timer Canva responderam 403 na última tentativa; funcionamento transacional não homologado. Sem ingresso ou mensagens no canal.
7. QA autenticado entre dispositivos, retorno durante gravação, conexão interrompida, teclado, leitor de tela e Safari/Android; medir desempenho real. Publicação depende de autorização vigente.

## Roteiro de revisão e reversão

Público: Início → Explorar → produto → painel relacionado → fechar → retornar ao catálogo com filtro preservado. Biblioteca sem sessão orienta a entrar. Autenticado, com direito verificado: Biblioteca → Dia → resposta → Antídoto → retorno → Caderno. Administração exige allowlist.

Revisão salva sem deploy. A versão publicada anterior permanece como referência de reversão. Migração aditiva: não apagar novas tabelas num rollback, pois podem conter registros legítimos após ativação. Contratos e detalhes: `CONTRATOS-INTEGRACAO.md`.


## Registro da entrega salva

- Revisão salva em Sites: versão 2, sem deployment associado.
- Fonte exata: `dc72dcdb5820af66b6525f0e9d2cf7f7c1036439`, enviada à branch configurada do repositório de código do Site.
- Site: `appgprj_6ab11d2e84188191a90910ec6b06c64d`.
- Versão salva: `appgprj_6ab11d2e84188191a90910ec6b06c64d~appgver_c2d6a56d20208191aeb3bab4ba721184`.
- Integridade do artefato: `sha256:31af403e23aa92d1dd873a8665c6242b373ade5adbb495145c9d2c8fd513da1f`.
- A publicação anterior permanece preservada; o endereço publicado não representa esta revisão. Não há link público de homologação criado nesta entrega.
- Os arquivos de código, captura e documentos técnicos citados acima estão versionados no repositório do Site; este documento registra a entrega no repositório canônico Universo Relacione-se.
