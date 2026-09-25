# Correção do chat: resposta HTML no lugar de JSON

## Base preservada

Fonte oficial reaberta limpa em `98df76144321f546b9e59f6571a584c8315ab53d`, versão 23. Público somente Sol, ambiente revisão 5. A geração Gemini e a correção Workers do lote 6 permanecem. Nenhuma mudança em dependências, banco, segredos, acervo, direitos, Jarvis, conteúdo Magnetus ou audiência.

## Diagnóstico e limites

Sol relatou `Unexpected token '<', "<!DOCTYPE ..." is not valid JSON`. O cliente chamava `.json()` indiscriminadamente e aceitava uma sessão HTTP 200 sem verificar seu corpo.

Em produção, requisições sem acesso à camada privada para GET `/api/lucida` e POST `/api/lucida/sessao` retornaram **401 text/html** com título do app. As mesmas rotas, usando a credencial técnica nativa autorizada de inspeção, retornaram **200 application/json**, `available:true` e `access:visitor`. Nenhum token foi salvo no código ou entregue ao navegador. Esse ensaio não representa a sessão pessoal de Sol.

Logs próximos ao relato (~22:03 UTC): página inicial 200; biblioteca 401; nenhum POST de conversa nos eventos retornados. Amostra não demonstra completude dos logs. Evidências são compatíveis com bloqueio antes da rota do chat; não foi observado o pedido exato do aparelho de Sol. Não afirmar que a causa é certamente cookie de terceiro, iframe ou expiração de conta.

## Mudanças

- Cliente confere tipo de conteúdo, JSON e contrato da sessão antes de enviar a pergunta.
- Não segue redirecionamentos da API; reconhece resposta opaca/HTML, erros de sessão e respostas incompletas.
- Erros técnicos de parser e de rede não aparecem como resposta da IA; mensagens legítimas de limite/serviço são preservadas.
- Não reenvia automaticamente nem limpa a pergunta quando ocorre falha.
- Oferece cópia por ação explícita e abertura da LÚCIDA em outra aba no endereço canônico. Texto não é transportado na URL nem persistido; a pessoa cola se quiser. Falha de clipboard recebe alternativa manual.
- Referências recebidas são validadas antes de renderizar, mantendo os destinos aprovados.
- Nenhum acesso privado foi desativado. Abertura direta pode pedir a conta ChatGPT autorizada; cadastro de clientes é trabalho distinto.

## Verificação

- `scripts/qa/lucida-chat-client.mjs`: 10 cenários aprovados, incluindo HTML 401/200, redirects, JSON inválido, sessão inválida, erro no segundo pedido, sucesso e referências, 429, conta expirada/conflito, contrato de status e falha de rede.
- Regressões existentes: guia 9; continuidade/rascunhos 9. TypeScript e lint do delta aprovados.
- Browser local: erro normal 503 legível; fixture temporária 401 HTML reproduziu recuperação sem SyntaxError; pergunta conservada e copiada; destino da nova aba conferido sem levar mensagem no link. Fixture removida e rota original restaurada integralmente antes do build.
- Evidência visual: `docs/evidencias/lucida-html-20260925/recuperacao.jpg`. É simulação local de acesso recusado, não resposta real da IA nem sessão do celular.
- Build/commit/publicação final: conferir recibo canônico `04-lucida/CORRECAO_CHAT_HTML_2026-09-25.md` no Universo, gravado após implantação.

## Continuidade

LUC-077, 119, 120 e 225 recebem evidência, sem promover seus estados. Todos os 259 IDs conservados. Próxima ação: confirmar o caminho direto no aparelho de Sol; se ainda houver falha, correlacionar horário e rota com registros da plataforma. A identidade pessoal e o navegador embutido não podem ser homologados por uma inspeção de serviço. Manter a expansão de conta própria e a classificação editorial no plano; não pedir novamente a chave Gemini.

Reversão: reverter somente este delta de cliente se houver regressão, preservando alterações posteriores e todos os dados/configurações. Não restaurar banco ou versões antigas do runtime para remover apenas esta correção.

## Recibo de publicação confirmado

- Commit de fonte e build: `24563932f69c4f87fcd93da2ec45a42ae86936ae`.
- Versão: `appgprj_6ab11d2e84188191a90910ec6b06c64d~appgver_32a139b9e0f08191b6f0df5511d465d8`.
- Implantação: `appgdep_6ab6f2b2febc81919afa0aa381ff0583`, **succeeded** em 2026-09-25T22:16:44.376472+00:00.
- URL: https://relacione-se-universo.sollimalovecoach.chatgpt.site/lucida#conversa .
- Ambiente revisão 5, audiência privada preservada.
- Build Workers aprovado, arquivo de implantação lido integralmente e validado antes do upload. Nenhuma migração nova.
- Rascunhos de página e painel também conferidos no navegador: textos independentes; fechar/reabrir o painel preservou o seu rascunho. Clipboard conferido com texto sintético.
- Cobertura do ledger: 259 IDs, hash original mantido; 14 concluídos, 46 em homologação, 55 em execução, 111 pendentes, 33 bloqueados. Não houve promoção de estado nesta correção.
- Registro completo atualizado em `docs/lucida/EXECUCAO_LUCIDA.json` na fonte do app. D28 em `DECISOES_LUCIDA.md`.

### Ação de Sol

Copiar a mensagem da aba antiga antes de atualizar/fechar. Abrir a URL acima diretamente; se solicitado, entrar com a conta ChatGPT já autorizada para o app e colar a mensagem. Não cadastrar nem alterar a chave Gemini. A validação no aparelho real permanece aberta; não foi prometida solução do login por teste técnico.
