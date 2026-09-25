# Dependência urgente de usabilidade — 25/09/2026

| Dependência | Estado e próximo passo |
|---|---|
| D11 — aparelho real e interação | **Bloqueante.** Sol relata que nenhum botão funciona no iPhone e que a LÚCIDA não responde. O navegador remoto executou os cliques testados, então a causa permanece aberta. Reproduzir em Safari/iOS e no navegador interno do ChatGPT; registrar console/rede/assets/hidratação/cache/overlay/navegação. Só considerar resolvido depois de reteste no aparelho afetado. |
| D01 — sessão privada | Pós-login no aparelho de Sol ainda não homologado. Dois 401 de /api/biblioteca ocorreram durante diagnóstico sem sessão autenticada comprovada; não atribuir esses eventos à conta de Sol nem concluir a causa por inferência. |
| Documentação/revisão | Entregar [o relatório geral para Manus](RELATORIO-GERAL-RELACIONE-SE-PARA-MANUS-2026-09-25.md) junto com a matriz integral. Site e documentação estão no GitHub; código do app permanece no Git interno do Sites. |

Nenhum código ou deployment foi alterado por esta atualização. D11 permanece aberto e C2 continua parcial.

---

## Dependências de publicação anteriores, preservadas

# Dependências vigentes após publicação — 25/09/2026

A autorização de publicação foi recebida e executada: app v9 privado e site em produção. Não pedir novamente autorização para esta publicação já concluída. Os registros abaixo que ainda pedem publicação são históricos.

| Dependência | Estado e próximo passo |
|---|---|
| D09 — publicação deste recorte | Concluída: app `appgdep_6ab5be97ee208191b39f9480473cf3a9` succeeded; site `dpl_75Lpf3Laav5qiqGw3hbi8kTNgEta` READY production. Não amplia audiência do app. |
| D06 — LÚCIDA | Implementação canônica localizada no Magnetus3. Adaptar identidade e persistência entre Node/PostgreSQL/Better Auth e Sites/Workers/D1; configurar provedor/modelo por mecanismo seguro autorizado, validar custo/consentimentos/fontes/isolamento. Guia público e reflexão editorial disponíveis; IA conversacional indisponível. |
| D01/D02 | Autenticação externa, vínculo legado, identidade administrativa e isolamento real permanecem pendentes. Sites está na revisão de ambiente 0, sem variáveis. Não inferir identidade por e-mail ou pelo proprietário do projeto. |
| D11 | Sol deve testar os cliques no aparelho em que falharam e a persistência do Dia Zero após fechar/reabrir o app. Segunda conta real exige autorização própria. Dois 401 de /api/biblioteca não demonstram falha de execução nem sessão autenticada. |
| D07 | PR #2 Magnetus3 continua draft, head `673a96f0d6da004237560a940d149101ea6b59e3`. Jarvis/SOL-IA e MM01–MM17 preservados; nenhuma integração operacional nova declarada. |

D03–D05, D08, D10 e D12 mantêm seus gates. A rota /produtos/magnetus/lucida no domínio legado da Vercel respondeu 404; não oferecê-la como conversa disponível. Deploy READY sozinho não prova funcionalidade.

Ação simples de Sol: abrir /programas e /lucida no site publicado; no app privado, conferir LÚCIDA e salvar/reabrir o Dia Zero. Para configuração administrativa posterior, usar apenas o identificador autenticado mostrado em Meu espaço → Identificação desta conta para suporte; não enviar senha ou chave de API em conversa. Não é preciso fornecer esse dado para visitar os testes gratuitos.

[Relatório desta publicação](RELATORIO-PUBLICACAO-LUCIDA-2026-09-25.md).

---

## Dependências históricas preservadas

# Atualização de dependências — 25/09/2026

Dois testes gratuitos integrados ao app e ao site; catálogo com Script do Silêncio, Minutos Magnetus · Mulheres, Mapa da Suspeita e Dor-de-Cotovelo. Produtos incompletos abrem “Em breve”. LÚCIDA mantém reflexão editorial e IA “Em breve”.

A candidata resolve a dependência dos testes em relação aos deploys antigos: o feminino teve erro de lockfile e uma página masculina publicada tinha botões sem lógica. Os originais não foram sobrescritos; perguntas foram preservadas e o resultado contraditório do teste masculino foi corrigido na integração.

- Publicação: app v9 salvo e site PR #3 draft; faltam revisão/autorização de publicação e ensaio da versão no aparelho afetado. A instrução anterior de salvar sem publicar foi mantida. Não alterar audiência por inferência.
- Links: Mapa responde na Vercel; isso não valida checkout/resultado pago. Canva e convite Telegram estão configurados, sem comprovação completa de seu conteúdo externo. Canal não equivale ao pack pago.
- Dor-de-Cotovelo: documentação localizada; programa executável/deploy correspondente não localizado pelo nome. Apresentação “Em breve” pronta.
- D01/D02/D11 continuam abertos nos limites anteriores: autenticação, administração e dispositivos reais. C3–C8, corpus, ofertas e IA não são concluídos por este catálogo.

[Relatório e evidências](RELATORIO-PROGRAMAS-2026-09-25.md). Demais dependências preservadas integralmente abaixo.

---

# Dependências atuais — 24/09/2026

O acesso ao código original foi restabelecido; a revisão 8 está salva sem publicar e a v7 permanece privada. Esta atualização prevalece sobre referências históricas a ambiente perdido, v1 publicada, revisão 5 como última ou apenas 107 testes.

| ID | Estado atual e próximo trabalho |
|---|---|
| D01 | C2 parcial. Login/callback/logout/expiração e isolamento entre contas reais continuam sem homologação. Receptor/helper de vínculo legado existem; integrar emissor autenticado e consentimento entre domínios, preservando titularidade. Não unir por e-mail. |
| D02 | C2-B com busca/paginação de suporte recuperada e 30 testes de conta aprovados. Ambiente Sites revisão 0, sem variáveis. Obter o userId autenticado de Sol em Meu espaço → Identificação desta conta para suporte. Não usar IDs de proprietário/GitHub. Configurar administração apenas com escopo autorizado. |
| D09 | V7 já publicada privadamente antes desta sessão; v8 salva, fonte `2c2b75550903c798c1e859f087b9c9281c241f0b`, sem deployment. Site PR #3 draft sobre PR #2; branch candidata não dispara deploy Git. Publicação nova ainda depende de autorização aplicável. |
| D11 | 129 testes locais e builds aprovados; navegação verificada em telas menores. Login real, segunda conta autorizada, iPhone/Safari, perda de sessão, persistência e restauração real pendentes. |
| D06 | Uma LÚCIDA, modos APP/SITE. Nova navegação entrega apenas parte da diretriz; provider, corpus ativo, IA e memória consentida continuam pendentes. Chave de API isolada não conclui a integração. |
| D07 | SOL-IA PR #11 e Magnetus3 PR #2 confirmados como drafts abertos. Contexto MM01–MM17 preservado. Conexão operacional do Jarvis não demonstrada. |

D03–D05, D08, D10 e D12 mantêm seus gates; não ativar C3 antes do aceite C2. Conteúdos já existentes devem ser localizados nos repositórios, sem pedir novamente a Sol ou recriar manuscritos. Site e app mantêm dados e responsabilidades separados.

Ação mínima de Sol agora: enviar o identificador autenticado exibido no Perfil, testar salvamento/reabertura do Dia Zero no seu iPhone e decidir a publicação privada da candidata. Para teste entre contas será necessária uma segunda conta explicitamente autorizada; nenhum convite ou acesso foi criado nesta entrega.

[Estado e recibos](ESTADO.md) · [Relatório](RELATORIO-DIRECAO-GERAL-2026-09-24.md).

---

## Histórico integral de dependências — ler em conjunto com a atualização acima

# Dependências da conclusão — Relacione-se

Atualizado na C2-A, 21/09/2026; C2 permanece parcial. Ausência de configuração homologada não significa ausência de conteúdo ou de código. Investigar fontes/autorização existentes antes de pedir algo a Sol. Não enviar mensagens, gastar, publicar ou ampliar permissões por inferência técnica.

| ID | Camada / dependência | O que já existe | Como destravar / trabalho independente |
|---|---|---|---|
| D01 | C2: identidade pública/legada — parcial | Contrato Better Auth localizado; entrada/saída intermediárias; receptor assinado/desafio por titular; helper emissor; testes sintéticos. Ver integrations/magnetus/README.md | Falta endpoint emissor autenticado, consentimento/transação entre domínios, chaves e contas autorizadas. Não unir por nome/email, migrar ou conceder direitos. Homologar callback/login/logout/cancelamento/expiração reais. |
| D02 | C2: administração de Sol/suporte — parcial | /admin/suporte/API restrita; histórico próprio, protocolo idempotente, estados, revisão e auditoria. Ambiente sem variáveis, revisão 0. | ID autenticado Site de Sol não disponível; propriedade GitHub/Sites não equivale a userId. Allowlist inalterada. Localizar prova pelo acesso autorizado e configurar somente sob autorização aplicável. Ampliar consulta além dos 100 recentes, sem mensagens externas. |
| D03 | C3: Kiwify e contratação real | Dois checkouts oficiais; esquema de ofertas/direitos; eventos internos e testes; webhook fecha com 503 sem configuração | Verificar documentação atual, credenciais, assinatura/token, eventos reais disponíveis, SKU/oferta versionada, vínculo comprador→titular e vigências confirmadas. Implementar adaptador, idempotência, reordenação, reembolso, renovação e conciliação. Não inferir compra do retorno, inventar duração/preço nem cobrar para testar. |
| D04 | C4: versões autorais e legados | D0–D3 Mulher importados e bloqueados por hashes; fontes em Magnetus3/biblia/trilogia; catálogo e páginas contextuais | Selecionar fonte canônica aprovada por obra/componente, com proveniência. Integrar demais conteúdos encontrados e autorizados; não recriar manuscritos. Inventariar homens, trilogia e livros individuais, MINDSETmagro/bônus, Script/ferramentas/apps. Complementaridade não cria dependência obrigatória de compra. |
| D05 | C4: mídia/transcrições e armazenamento | Leitor/áudio, progresso, R2 autorizado e streaming com ranges em código/testes | Conferir bucket/binding, limites/custos e arquivos finais autorizados; publicar versões editoriais só no ambiente autorizado. Homologar áudio real, codecs, seek, expiração e transcrição protegida. Fixture não é acervo entregue. |
| D06 | C5: Lúcida real, corpus e governança | Reflexão fixa declarada, guia determinístico, contrato/contexto por direito, fontes/corpus existentes | Confirmar provedor, configuração, orçamento, corpus aprovado e avaliações. Separar memória consentida, correção/exclusão/exportação e dados operacionais. Não ativar provider pago sem autorização nem expor respostas a Jarvis/marketing. |
| D07 | C6: Jarvis canônico e conexão | API com token de leitura, eventos/cursor, consumidor em integrations/jarvis e testes | Fonte recente aponta SOL-IA PR #8 commit 1355a9bc5c7d420b7c15139c609a2d051a50258f; verificar estado real antes de conectar. Magnetus3 PR #1 commit 7bff435d8f451db7053c9850eb2099b4b9b76498 complementa Lúcida. JARVIS-SOL é referência anterior, não assumir runtime definitivo; app.Sol.ia é outro elemento. Resolver gateway/URL/token/escopos e auditar execução. Nenhuma exportação íntima implícita. |
| D08 | C4/C7: finalidade Telegram e cronômetro | Convite e Canva registrados; páginas contextualizadas com retorno | Confirmar se canal é gratuito, pago, bônus ou misto nas fontes. Verificar destino sem ingressar/enviar mensagem. Não publicar convite como brinde antes da classificação. Falha de acesso de ferramenta não prova link quebrado. |
| D09 | C8: publicação e permissões de audiência | Versão 1 publicada; revisões posteriores salvas; histórico recuperável | Preparar migrações, smoke tests e plano de reversão; promover somente sob autorização válida. Não transformar o link antigo em prova da revisão atual nem mudar público/privado nesta obra de revisão. |
| D10 | C7: SEO, domínio, tráfego e resultados reais | Metadados/sitemap condicionados; eventos consentidos/GPC; campanhas, agregados e registro de links | Conferir domínio, indexação deliberada e páginas privadas; atribuir compras a eventos verificados. Receita não é lucro; cliques não são vendas. Identificar custos reais quando disponíveis, sem estimativas apresentadas como dados. |
| D11 | C2/C8: homologação — parcial | 107 testes locais, TypeScript/build; cancelamento/Voltar e rascunho; suporte/preferências sintéticos; Ajuda 320/390/768 e fonte 200%; foco da entrada. | Login externo e duas contas reais não homologados; Perfil ampliado teve timeout. Conferir Safari/iPhone/Android, leitor de tela, backup/restauração e perda de processo. Rascunhos só na memória da aba; não há offline durável. |
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

## Evidência C2-A

Revisão 5, commit `5fb0375ba3170985bca3d7a768dbb9d6e81c714a`. Relatório `docs/REVISAO-C2-2026-09-21.md`. Migração 0004 somente gerada/testada localmente. Preparação criptográfica não equivale a legado conectado. Resolução de suporte não libera conteúdo. Nenhuma chave, allowlist, pagamento, mensagem ou publicação ativada.

## Recuperação C2-B — 22/09/2026

**Bloqueio de recuperação de ambiente (ativo nesta retomada):**
- GitHub documental disponível.
- Sites/fonte privada executável não disponíveis neste runtime; não é o mesmo HTTP 400 histórico.
- Não há base técnica atual para homologar D01, D02 ou D11, emitir revisão Sites, aplicar migração ou integrar o vínculo legado.
- Não usar o texto projetado da vitrine, arquivos editoriais ou o repositório documental como substitutos do código-fonte.
- Antes de qualquer nova implementação, recuperar Sites/fonte e comparar a versão mais recente com os checkpoints C2-B conhecidos.

**D01:** segue pendente para login/logout/cancelamento/expiração/duas contas reais e troca de sessão em ambiente autorizado.

**D02:** segue pendente; o userId administrativo real de Sol não foi obtido por mecanismo autorizado nesta retomada. Propriedade GitHub/Sites não é prova de identidade do app.

**D11:** verificações 320/390/768 e fonte 200% permanecem evidência histórica local. iPhone/Safari, Android, leitor de tela, persistência/restauração e conflitos reais seguem não homologados.

A paginação/busca de suporte C2-B não deve ser reimplementada; deve ser confirmada na fonte recuperada.
