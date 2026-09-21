Execute a retomada C2-B do app/site Relacione-se: concluir identidade, conta, biblioteca e recuperação de acessos, preservando C1 e C2-A. Assuma a direção técnica e resolva detalhes reversíveis sem pedir que Sol gerencie arquivos ou reconstrua o histórico.

Leia integralmente os quatro registros canônicos em:
https://github.com/Sollimastudio/universo-relacione-se/tree/main/09-app/OBRA-RELACIONE-SE
Leia ESTADO.md, MATRIZ-PLANTA.md, DEPENDENCIAS.md e PROXIMO-PROMPT.md, depois o protocolo C1, prompt mestre com todas as fontes, planta completa e registros posteriores em 09-app. No código, leia docs/REVISAO-C2-2026-09-21.md, docs/REVISAO-C1-2026-09-21.md, contratos, decisão de integração, SOURCE-LOCK-REVISAO.json e integrations/magnetus/README.md. Consulte Magnetus3, biblia-magnetus e trilogia-sol-lima conforme as dependências. Não refaça funcionalidades legadas sem localizar suas fontes.

Referências de recuperação, a revalidar antes de editar:
- Sites: appgprj_6ab11d2e84188191a90910ec6b06c64d.
- Fonte: https://git.chatgpt-team.site/56efd1eb-ab0f-4d8a-a764-f07b91b55c32/appgprj_6ab11d2e84188191a90910ec6b06c64d.git
- Checkout anterior: /workspace/sites/relacione-se-universo.
- C2-A: commit 5fb0375ba3170985bca3d7a768dbb9d6e81c714a; revisão 5, ID appgprj_6ab11d2e84188191a90910ec6b06c64d~appgver_4ac37f2041fc8191a444949b896aa8dd.
- Base C1: b69c1116c1aa91938fa6da002640b3662f8b8603, revisão 4.
- Produção permaneceu v1. Não apresente a URL antiga como revisão 5.
- C2-A aprovou 107 testes, TypeScript e build, mas C2 permanece parcial.

Confira Git, alterações de outras sessões e versões posteriores; recupere pelo acesso autorizado se necessário. Não faça reset para essas referências, não troque de plataforma e não recrie o site.

Estado implementado: entrada intermediária com retorno validado e cancelamento local; confirmação de saída; proteção de escrita quando a conta muda em outra aba; biblioteca com direitos sobrepostos e histórico por origem; preferências persistidas por titular; ajuda com protocolo idempotente, estados e orientações; administração restrita com revisão/auditoria; receptor de vínculo assinado e helper legado preparados. Preserve lib/navigation.ts, exit-checkpoints.ts, transient-drafts.ts, ContextLink/ReturnLink, continuidade, rascunhos separados por titular, D0–D3, gate, Caderno, versões, contratos e autorização no servidor.

Execute em subetapas recuperáveis:

1. D01 — Homologue login/logout, cancelamento no provedor, expiração, retorno à intenção e entrada direta em atividade no ambiente autorizado disponível. Teste duas contas, troca em outra aba e tentativa de acesso cruzado. A prévia local anterior não tinha o dispatcher de autenticação externa. Não simule sessão como entrega nem crie rotas que aceitem identidade do navegador. Rascunhos ficam só na memória da aba; explique cópia/reabertura, sem prometer persistência ao fechar ou transferência entre contas.

2. Vínculo legado — O contrato localizado em Magnetus3 main 8e737a65f9b47bf2d8f621d101283129c61b028d usa Better Auth/PostgreSQL: lib/server/auth.ts, lib/server/http.ts e db/migrations/000_auth.sql. Revalide a fonte. Reutilize requireUser/requireOrigin. Complete, onde houver acesso autorizado, o emissor HTTP, estado da transação e consentimento inequívoco entre as duas sessões, com destinos fixos e confirmação da conta correta. Reutilize lib/platform/identity-link.ts e integrations/magnetus/issue-identity-proof.mjs. Chave privada fica apenas no emissor; não exponha prova/chave em URL, analytics ou logs. Valide assinatura, desafio, expiração, replay, concorrência e conflito. Não una por nome/email; não migre clientes reais nem conceda acesso por vínculo.

3. D02 — Localize o userId autenticado real de Sol pelo mecanismo autorizado. A propriedade GitHub/Sites não prova esse ID. A última leitura do ambiente estava vazia, revisão 0; não invente ID nem amplie allowlist para testar. Homologue a administração somente com configuração autorizada. Preserve auditoria e negação por padrão. Resolver suporte não altera compra ou direito; não envie mensagens externas.

4. Parte independente executável — Amplie a consulta de suporte além dos 100 protocolos recentes com paginação e busca segura por protocolo, sempre restrita ao titular ou administrador autorizado. Acrescente estados de busca vazia/erro e retorno, sem expor protocolos de terceiros. Preserve rascunhos e conflito de revisão. Verifique cancelamento de saída, sessão alterada, preferências e histórico da biblioteca com contratos sobrepostos/expirados. Conteúdo expirado não apaga registros nem invalida outra compra.

5. D11 — Complete verificações possíveis de teclado/foco, telas pequenas e texto ampliado em Perfil/Biblioteca/Ajuda; a medição ampliada de Perfil teve timeout na C2-A. Verifique persistência e conflitos com contas autorizadas quando disponíveis; documente exatamente aparelhos, leitor de tela e recuperação que não puder homologar. Nenhuma fixture conta como autenticação externa.

Reexecute scripts/qa/ecosystem.cjs, data-handlers.cjs, account.cjs, continuity.cjs e jarvis-client.test.mjs; TypeScript e build. Acrescente testes somente para riscos corrigidos. Remova rotas de QA antes de salvar. Preserve migrações antigas e não aplique migrações reais nesta revisão sem autorização válida.

Se faltar ambiente, identidade ou configuração, registre evidência exata e continue a parte independente, sem repetir indefinidamente C1/C2-A. C2 só recebe aceite integral com revisão recuperável, isolamento verificado, nenhuma regressão conhecida e prova dos percursos reais; código preparado, chave vazia e mock continuam pendências.

Salve fonte, versão de revisão, relatório técnico e os quatro arquivos canônicos atualizados. Publicação, gastos, migrações reais, permissões e mensagens respeitam as autorizações da sessão. Ao terminar, gere e salve o próximo prompt integral já preenchido: C3 se C2 cumprir seu aceite; caso contrário, retomada exata da pendência ou parte independente identificada, mantendo C2 parcial. Entregue situação real, testes, limites e referência da revisão, com esse único prompt pronto para copiar e colar; não encerre perguntando se pode continuar nem afirme execução em segundo plano.

Mantenha C3 contratação/Kiwify; C4 conteúdos/experiências; C5 Lúcida dos clientes; C6 Jarvis interno de Sol; C7 distribuição/SEO/analytics; C8 homologação final. Preserve as 260 ramificações e MM01–MM17, SOL-IA PR #8 e Magnetus3 PR #1, Magnetus homens/mulheres com ebook/workbook, Antídoto e Lúcida conforme contratação; trilogia/avulsos, MINDSETmagro/bônus, áudios, Script, ferramentas e expansões opcionais. Não invente preços, conteúdo, dependências de compra ou resultados.
