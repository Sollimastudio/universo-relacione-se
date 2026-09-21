# Relacione-se — evolução por camadas, 21/09/2026

Versão de revisão preparada a partir da planta e da revisão anterior. Esta entrega amplia o app existente; não reconstrói nem substitui o Magnetus3 canônico. Produção, permissões, contratos e dados reais permanecem preservados. A revisão não equivale a operação comercial integral homologada.

## O que mudou

| Camada | Implementação concreta | Estado |
|---|---|---|
| Circulação | “Comece por aqui”, mapa do universo, famílias, componentes dos produtos e 17 destinos sinalizados | Implementada; links locais verificados |
| Crescimento | Novas publicações do catálogo aparecem na exploração e no mapa; livros/áudio publicados substituem seus destinos de preparação | Implementado para os formatos livro e áudio |
| Continuidade | Biblioteca, favoritos, versão de leitura, capítulo/marcador e agora parágrafo; salvamento complementar na saída do workbook/Antídoto | Implementado; persistência confirmada no servidor é a referência |
| Áudio | Envio administrativo, armazenamento protegido, transcrição, velocidade, retomada e streaming com byte range | Implementado e testado com arquivos sintéticos isolados; acervo real pendente |
| Descoberta | Canonical, metadados sociais, dados estruturados de obras, breadcrumbs, robots e sitemap condicionais | Implementado; indexação continua desabilitada para o Site privado |
| Medição | Origem por canal, campanhas cadastradas, deduplicação por evento, contagens consentidas e totais reais | Implementado; nenhuma venda/receita inferida de cliques |
| Operação | Painel de tráfego/campanhas/links/áudios, verificações por destino cadastrado e estados honestos | Implementado; conta administrativa precisa estar autorizada em configuração |
| Jarvis | API autenticada de leitura, eventos persistidos e consumidor Node separado para o Jarvis existente | Código pronto para homologação; conexão de produção não ativada |
| LÚCIDA | Guia de continuidade prioriza recursos disponíveis da conta; reflexão editorial preservada | Guia funcional; IA, corpus e memória continuam dependências explícitas |

## Preservação

Base recuperável: `dc72dcdb5820af66b6525f0e9d2cf7f7c1036439` (revisão 2). Checkpoints das primeiras camadas: `1eb8c93` e `cde7c0c`; os commits subsequentes conservam a mesma linhagem. A planta original foi copiada para `docs/planta-relacione-se.html`. Os arquivos canônicos importados mantêm os hashes de `docs/SOURCE-LOCK-REVISAO.json`. Nenhum preço, aula, livro, bônus, depoimento ou resultado foi inventado. Nenhuma tabela anterior foi removida.

Mantidos: combo Magnetus III com ebook/workbook, Antídoto e LÚCIDA conforme contratação; componentes avulsos; trilogia e livros individuais; biblioteca sem duplicação; união dos direitos válidos; versões de ofertas; gate de 24 horas; Caderno próprio mesmo após expiração; distinção Jarvis interno/LÚCIDA dos clientes. O acesso legado de outro sistema não é inferido por e-mail.

## Sublinks e pendências visíveis

Os dois checkouts oficiais continuam acessíveis pelas páginas de saída `/sair/pack` e `/sair/script`, com retorno ao produto e aviso da integração pendente. O destino não é um comprovante de pagamento. O cronômetro Canva mantém uma página de verificação. O Telegram tem sua página contextual, mas o convite não é entregue ao cliente enquanto gratuito/pago não estiver decidido. O atalho Canva antes identificado como 404 não foi usado. A nova tentativa de consulta pública em 21/09 não conseguiu acessar os quatro endereços pela ferramenta disponível; não se concluiu que estejam quebrados e não se declarou nova homologação.

Homem, próximos Dias, MINDSETmagro e bônus, testes, Árvore, Suspeita, Dor de Cotovelo, Perdão, livros e agenda têm lugares próprios. O inventário continua extensível; “todo o ecossistema” significa estrutura para os itens conhecidos e expansão, não conteúdo futuro fictício. Os protótipos não foram promovidos a produtos homologados. A inspeção dos legados permanece documentada em `DECISAO-INTEGRACAO-2026-09-21.md`.

## Testes concluídos

- **57 cenários do ecossistema** com módulos reais e SQLite isolado: permissões, privacidade, origem, contratos sobrepostos, expiração, cancelamento, reembolso, ordem/idempotência, gates, Caderno único, versões, leitura, eventos atômicos, campanhas, GPC, SEO fechado, token Jarvis, links restritos, áudio/ranges e hashes canônicos.
- **15 verificações anteriores do Caderno e analytics**, mantidas e passando.
- **4 testes do consumidor Jarvis**: domínio fixado, somente GET, contrato/cursor, bloqueio de resposta do gateway e credenciais inválidas.
- **76 verificações automatizadas** ao todo; dados e identidades sintéticos, sem compra real nem IA real. Falha de evento foi injetada em SQLite para demonstrar rollback de publicação/campanha.
- TypeScript e build Worker de revisão concluídos. Novas migrações geradas e inspecionadas; nenhuma aplicada a produção.
- Navegador de revisão: entrada → mapa com teclado, retorno nativo, canonical/noindex; frames de 320, 390 e 768 px e desktop de 1363 px. Entrada com texto de 125%; mapa, Telegram pendente, Magnetus e LÚCIDA sem overflow nas larguras verificadas. A largura útil em frames inclui a redução da barra de rolagem.
- Corrigida na QA uma falha de compatibilidade de `crypto.randomUUID` na prévia HTTP. As métricas não podem derrubar o fluxo principal. Hierarquia tipográfica das páginas novas ajustada.
- Screenshot: `docs/revisao-camadas.jpg`. Harness temporário removido antes do build final.

Limites: teste de largura não é teste em aparelho real. Não há certificação WCAG 2.2 AA, teste com VoiceOver/TalkBack/Safari real, medição de Web Vitals de campo, comprovação de persistência após encerramento abrupto/offline ou compra real ponta a ponta. O player foi verificado na camada de dados/streaming com bucket simulado; ainda precisa tocar os arquivos reais e seus codecs nos aparelhos-alvo. A posição de leitura é guardada por ação explícita; o áudio salva periodicamente e ao pausar. A origem do tráfego é limitada por consentimento e pela troca de aplicativos.

## Antes da produção comercial

| Dependência | Por que permanece | Próxima ação concreta |
|---|---|---|
| Identidade pública e contas antigas | Revisão usa a autenticação Sites já existente; não há migração legada homologada | Backup e vínculo autenticado entre IDs; reconciliar contratos e testar reversão |
| Administração de Sol | Não havia variáveis de runtime cadastradas na partida | Configurar `RELACIONE_ADMIN_IDS` com ID autenticado comprovado de Sol; testar isolamento |
| Kiwify | Checkouts não validam pedidos; webhook segue fechado | Credenciais, autenticidade/consulta autoritativa, SKUs, vínculo do comprador e testes de compra/renovação/reembolso |
| Obras e jornadas | Versões integrais e autorizações finais não foram entregues para publicação | Aprovar obras, Homem, próximos Dias e MINDSETmagro/bônus sem alterar autoria |
| Acervo de áudio | Arquivos/transcrições finais ausentes | Autorizar ativação do R2, enviar áudios de até 8 MB nesta versão, transcrever, ouvir e publicar pelo fluxo editorial |
| LÚCIDA com IA | Provedor, orçamento, corpus por direito, memória/consentimento e avaliações ausentes | Homologar fontes, acesso, segurança, limites de uso e custo antes da ativação |
| Jarvis | Mais de um projeto candidato; gateway privado e autenticação do runtime precisam ser resolvidos | Seguir `integrations/jarvis/README.md`; proteger acesso de Sol, configurar segredo de leitura e persistir cursor |
| Telegram e Canva | Classificação comercial do canal e cronômetro não homologados | Definir gratuito/pago e testar ferramenta, permissão e retorno; então liberar destino real |
| SEO/lançamento | Site permanece privado | Autorizar público/domínio definitivo; só então ativar indexação e cadastrar Search Console |
| Qualidade final | Não houve aparelhos reais, leitores de tela ou transação externa | Homologar Safari/iPhone, Android, teclado, leitor de tela, rede instável e contrato real |

Os bloqueios não foram mascarados com demonstrações. Não foram enviados dados ao provedor de IA, mensagens a canais ou credenciais ao cliente.

## Migrações e reversão

`0002_safe_captain_stacy.sql`: campanhas, conferência de links, eventos operacionais, agregados de tráfego e recibos de deduplicação. `0003_futuristic_scarlet_spider.sql`: metadados de mídia e coluna `learning_progress.location` com default constante `{}`. Deltas aditivos; `0000` e `0001` não foram reescritos. Aplicação somente no banco local de QA e em SQLite de testes.

Manifesto solicita o binding R2 `BUCKET` necessário ao fluxo de áudio; salvar esta revisão não provisiona a produção. Antes de publicar, exportar D1 e testar restauração. Para reverter código, recuperar a revisão anterior sem remover tabelas/coluna novas ou objetos: podem conter registros válidos. Não reconstruir o banco nem sobrescrever contratos. Nenhuma migração de banco Magnetus3 ocorreu.

## Referências técnicas consultadas

- [Prompt mestre autorizado](https://github.com/Sollimastudio/universo-relacione-se/blob/main/09-app/PROMPT-MESTRE-EVOLUCAO-APP-RELACIONE-SE-2026-09-21.md) e fontes registradas no documento de decisão.
- [Google — diretivas robots](https://developers.google.com/search/docs/crawling-indexing/robots-meta-tag), [canonical](https://developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls) e [sitemaps](https://developers.google.com/search/docs/crawling-indexing/sitemaps/overview).
- [Kiwify — API](https://docs.kiwify.com.br/api-reference/general), [OAuth](https://docs.kiwify.com.br/api-reference/auth/oauth), [consulta de venda](https://docs.kiwify.com.br/api-reference/sales/single) e [webhooks](https://docs.kiwify.com.br/api-reference/webhooks/list). Consulta documental não significa integração ativada.
- [JARVIS-SOL — API consultada](https://github.com/Sollimastudio/JARVIS-SOL/blob/main/src/api.ts), blob `6a928f3c35c589e392c2657668ad3b6e8666e37c`. Repositório homônimo `Jarvis-Sol.IA` e módulo separado `app.Sol.ia` também foram examinados para evitar ligação ao destino errado.


## Registro confirmado no Sites

- Revisão salva: **3**, com pacote de execução; **não implantada em produção**.
- Fonte: `be301b3e9b99341e3e71796639d8b06662bb851f`.
- Projeto: `appgprj_6ab11d2e84188191a90910ec6b06c64d`.
- Versão: `appgprj_6ab11d2e84188191a90910ec6b06c64d~appgver_94653464d9948191bf3a223bdac648b6`.
- SHA-256 do pacote registrado: `3acdb3f8683b30291ac61c0a2834fad8b0e082ca053421bc9f40927b3c85ce17`.
- Repositório-fonte do Site: `https://git.chatgpt-team.site/56efd1eb-ab0f-4d8a-a764-f07b91b55c32/appgprj_6ab11d2e84188191a90910ec6b06c64d.git`, branch `main`. O Universo mantém esta documentação canônica; o app executável continua no repositório do Site existente.
- A versão 1 permanece a publicação existente; versões 2 e 3 estão preservadas para revisão. O endereço de produção ainda não representa as melhorias desta revisão.
