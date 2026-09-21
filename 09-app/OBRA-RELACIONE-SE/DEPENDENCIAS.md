# Dependências da conclusão — Relacione-se

Atualizado na C1, 21/09/2026. Ausência de configuração homologada não significa ausência de conteúdo ou de código. Investigar fontes/autorização existentes antes de pedir algo a Sol. Não enviar mensagens, gastar, publicar ou ampliar permissões por inferência técnica.

| ID | Camada / dependência | O que já existe | Como destravar / trabalho independente |
|---|---|---|---|
| D01 | C2: identidade pública, conta legada e login/retorno reais | Auth Sites/ChatGPT, retornos validados, APIs por titular, biblioteca e fontes Magnetus3 | Localizar contrato de identidade do legado e identificadores comprovados. Não mesclar por nome/email não verificado. Implementar fluxo de reivindicação, conflitos e recuperação auditável sem migrar clientes. Homologar login/logout/expiração/cancelamento com ambiente e conta autorizados. |
| D02 | C2: administração de Sol e resolução de suporte | Allowlist administrativa e solicitações de ajuda internas | Resolver o identificador real pelo mecanismo autenticado; nome/email do GitHub não é userId do app. Configurar só sob autorização aplicável, preservar negação por padrão; construir triagem/consulta/resolução com auditoria e sem acesso indiscriminado ao Caderno. |
| D03 | C3: Kiwify e contratação real | Dois checkouts oficiais; esquema de ofertas/direitos; eventos internos e testes; webhook fecha com 503 sem configuração | Verificar documentação atual, credenciais, assinatura/token, eventos reais disponíveis, SKU/oferta versionada, vínculo comprador→titular e vigências confirmadas. Implementar adaptador, idempotência, reordenação, reembolso, renovação e conciliação. Não inferir compra do retorno, inventar duração/preço nem cobrar para testar. |
| D04 | C4: versões autorais e legados | D0–D3 Mulher importados e bloqueados por hashes; fontes em Magnetus3/biblia/trilogia; catálogo e páginas contextuais | Selecionar fonte canônica aprovada por obra/componente, com proveniência. Integrar demais conteúdos encontrados e autorizados; não recriar manuscritos. Inventariar homens, trilogia e livros individuais, MINDSETmagro/bônus, Script/ferramentas/apps. Complementaridade não cria dependência obrigatória de compra. |
| D05 | C4: mídia/transcrições e armazenamento | Leitor/áudio, progresso, R2 autorizado e streaming com ranges em código/testes | Conferir bucket/binding, limites/custos e arquivos finais autorizados; publicar versões editoriais só no ambiente autorizado. Homologar áudio real, codecs, seek, expiração e transcrição protegida. Fixture não é acervo entregue. |
| D06 | C5: Lúcida real, corpus e governança | Reflexão fixa declarada, guia determinístico, contrato/contexto por direito, fontes/corpus existentes | Confirmar provedor, configuração, orçamento, corpus aprovado e avaliações. Separar memória consentida, correção/exclusão/exportação e dados operacionais. Não ativar provider pago sem autorização nem expor respostas a Jarvis/marketing. |
| D07 | C6: Jarvis canônico e conexão | API com token de leitura, eventos/cursor, consumidor em integrations/jarvis e testes | Fonte recente aponta SOL-IA PR #8 commit 1355a9bc5c7d420b7c15139c609a2d051a50258f; verificar estado real antes de conectar. Magnetus3 PR #1 commit 7bff435d8f451db7053c9850eb2099b4b9b76498 complementa Lúcida. JARVIS-SOL é referência anterior, não assumir runtime definitivo; app.Sol.ia é outro elemento. Resolver gateway/URL/token/escopos e auditar execução. Nenhuma exportação íntima implícita. |
| D08 | C4/C7: finalidade Telegram e cronômetro | Convite e Canva registrados; páginas contextualizadas com retorno | Confirmar se canal é gratuito, pago, bônus ou misto nas fontes. Verificar destino sem ingressar/enviar mensagem. Não publicar convite como brinde antes da classificação. Falha de acesso de ferramenta não prova link quebrado. |
| D09 | C8: publicação e permissões de audiência | Versão 1 publicada; revisões posteriores salvas; histórico recuperável | Preparar migrações, smoke tests e plano de reversão; promover somente sob autorização válida. Não transformar o link antigo em prova da revisão atual nem mudar público/privado nesta obra de revisão. |
| D10 | C7: SEO, domínio, tráfego e resultados reais | Metadados/sitemap condicionados; eventos consentidos/GPC; campanhas, agregados e registro de links | Conferir domínio, indexação deliberada e páginas privadas; atribuir compras a eventos verificados. Receita não é lucro; cliques não são vendas. Identificar custos reais quando disponíveis, sem estimativas apresentadas como dados. |
| D11 | C2/C8: homologação de sessão, dispositivos e recuperação | 85 testes locais; percursos em Chromium; rascunhos/checkpoints na mesma aba; evidência visual | Homologar login real, contas distintas, Safari/iPhone/Android e leitor de tela disponíveis. Verificar fechamento abrupto, rede real, backup/restauração e conflitos. Persistência offline sensível não implementada: projetar proteção antes de armazenar novos dados. |
| D12 | Opcional após C8: PWA, notificações, Telegram Mini App etc. | Ramificações da planta mantidas no inventário | Avaliar benefício, orçamento e permissões depois do núcleo; não ativar agendamentos, assinaturas ou mensagens nesta camada. |

## Sublinks oficiais

| Finalidade | Destino registrado | Estado atual no app |
|---|---|---|
| Pack Minuto Magnetus | https://pay.kiwify.com.br/ZecEQ9d | `/sair/pack` identifica Kiwify e retorna ao produto/origem. Compra não libera biblioteca automaticamente. |
| Script do Silêncio | https://pay.kiwify.com.br/YVJ3Lke | `/sair/script`, mesmas salvaguardas de continuidade. |
| Cronômetro | https://variedadesuteis.my.canva.site/script-silencio | Em verificação; referência operacional preservada. |
| Canal | https://t.me/+C-ZEhFeueW40ZWFh | Finalidade comercial a confirmar; `/recursos/canal-minutos-magnetus` explica e permite retornar. |

`canva.link/convite-canal-link` é atalho histórico; não é canônico. O token Canva de verificação de domínio não é convite nem conteúdo para exibir ao cliente.

## Limitações verificadas nesta C1

- Não houve homologação de autenticação externa completa, cliente legado real, webhook Kiwify, acervo de áudio real, provedor Lúcida ou Jarvis conectado.
- A tentativa de abertura externa da Kiwify no navegador de QA terminou em `about:blank`. Href oficial e tela de saída foram conferidos; disponibilidade e retorno do serviço permanecem não homologados neste ambiente. Não se concluiu que o link está quebrado.
- Rascunhos não enviados ficam só na memória da aba. O aviso beforeunload não garante persistência se o sistema fechar o processo. Retentativa e cópia de registros pendentes funcionam durante a sessão; não são modo offline durável.
- Fonte ampliada nos quadros passou após correções; isso não certifica WCAG AA nem substitui aparelhos físicos. Acessibilidade e contraste integrais entram em C8.

## Complemento MM01–MM17

Preservar `09-app/JARVIS-LUCIDA-MINUTOS-MAGNETUS-2026-09-21.md`: referências multimodais, Visionário, brief, séries/episódios/perguntas, distribuição autorizada, Lúcida contextual, respostas consentidas, mapa pré-mentoria e agregados. Distribuir execução em C5–C7. Esse escopo está inventariado, não conectado nesta C1.
