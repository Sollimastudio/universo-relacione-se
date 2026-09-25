# Próximos lotes da LÚCIDA — configuração vigente em 25/09/2026

Este documento atualiza a orientação operacional anterior. Método integral: docs/lucida/PROMPT_EXECUCAO_LUCIDA_V1.md. Escopo integral: docs/lucida/LUCIDA_CHECKLIST_MESTRE_2026-09-25.md, 259 IDs. Não reduz requisitos. O histórico Git e os recibos dos lotes 1–4 preservam instruções/estados anteriores.

## Estado confirmado após lote 5

- App Sites appgprj_6ab11d2e84188191a90910ec6b06c64d, https://relacione-se-universo.sollimalovecoach.chatgpt.site .
- v20, commit e756a64b07573ca4d2b64bf2b36ac237c5b55af4, deployment appgdep_6ab6b34239c08191b9fe302e7792b9a0 succeeded, ambiente revisão4.
- Somente proprietária; não abrir público automaticamente.
- Gemini cadastrado por Sol, aceito pelo Google e geração real verificada. **Não pedir novamente API key ou cadastro.**
- Modelo gemini-3.1-flash-lite, transporte Supabase, saída768, timeout30s no app. OpenAI opcional futura.
- /api/lucida conectado ao manual e fichas públicas, histórico curto, fontes validadas, cotas30/conta e100/app por dia UTC. Nenhum texto de conversa gravado em banco.
- D1 continua dados editoriais/direitos/Caderno. Nova tabela operacional lucida_usage, sem texto pessoal. Supabase ACESSORA-SOL.IA mantém cofre e função exclusiva lucida-provider v8, sem ler memórias privadas do Jarvis.
- Navegação e proteção de acesso responderam em avaliação real. Reflexão apresentou instabilidade502/504 no teste integrado; respondeu no teste direto. Não considerar qualidade/estabilidade integral homologada.
- 145 cenários sintéticos, TypeScript/lint/build e publicação aprovados. Isto não equivale a todos os produtos/canais ou a uma compra real. Recibo: 04-lucida/EXECUCAO-LOTE-5-2026-09-25.md.

## Parte de Sol

O cadastro da chave já está feito. Para troca futura, o local é https://supabase.com/dashboard/project/rkkpbmzrucaghrojujvb/functions/secrets — projeto ACESSORA-SOL.IA → Edge Functions → Secrets → LUCIDA_GEMINI_API_KEY. Não substituir GEMINI_API_KEY/GOOGLE_API_KEY do Jarvis; nunca enviar valor no chat. A chave Google pode ser administrada em https://aistudio.google.com/apikey .

Sol pode experimentar o chat no app privado e revisar se o tom representa a LÚCIDA. As próximas decisões que dependem dela são editoriais/comerciais: versões aprovadas, amostras gratuitas, benefícios/limites/preços/ofertas e orçamento mensal. Engenharia deve primeiro apresentar inventário e opções concretas, sem pedir reenvio do que já está acessível. Contas/número/permissões de WhatsApp entram apenas na etapa própria.

Sol não precisa migrar banco, programar, editar prompts ou fazer redeploy manual.

## Configuração técnica vigente

| Configuração | Local / valor |
|---|---|
| LUCIDA_GEMINI_API_KEY | Supabase Secrets, já cadastrada |
| LUCIDA_GATEWAY_TOKEN | Segredo Sites, conexão exclusiva sem acesso a banco |
| LUCIDA_PROVIDER / LUCIDA_TRANSPORT | Sites: gemini / supabase |
| GEMINI_MODEL | Sites: gemini-3.1-flash-lite |
| LUCIDA_CHAT_ENABLED | Sites: true; false + deploy interrompe somente conversa IA |
| LUCIDA_DAILY_ACCOUNT_LIMIT / LUCIDA_DAILY_TOTAL_LIMIT | Sites:30 /100, limites operacionais privados, não oferta comercial |
| LUCIDA_MAX_OUTPUT_TOKENS / LUCIDA_TIMEOUT_MS | Sites:768 /30000 |
| LUCIDA_DIAGNOSTICS_ENABLED | Não ativado; diagnóstico administrativo exige identidade autorizada |
| LUCIDA_OPENAI_API_KEY / OPENAI_MODEL | Opcionais, Supabase e Sites respectivamente, quando houver chave |
| Chaves secundárias e slots | LUCIDA_GEMINI_API_KEY_SECONDARY / LUCIDA_OPENAI_API_KEY_SECONDARY; seletores GEMINI_API_KEY_SLOT / OPENAI_API_KEY_SLOT primary ou secondary |

Não há fallback automático ou rodízio para ultrapassar cotas. Não expor segredos no navegador/Git/logs. O modelo listado nem sempre gera:2.5 retornou404; validar uma troca com teste limitado. Atualização de variável Sites exige aplicar nova revisão em deploy; segredo Supabase é independente.

## Prompt de execução da próxima etapa

Assuma a direção técnica e prossiga do estado real, seguindo integralmente o prompt mestre e o checklist de259 IDs em docs/lucida. Antes de editar, reabra a fonte Sites autenticada, confira produção, HEAD, ambiente e público. Preserve alterações posteriores, trabalhos locais/PRs, dados e identidade visual. Leia continuidade, funções protegidas, decisões e recibo do lote5. Não restaure uma árvore histórica, não refaça o chat e não migre para Vercel por conveniência.

1. **Homologação privada do atendimento:** conferir a v20 ou sucessora e as falhas registradas. Separar timeout do ambiente de teste, erro HTTP do provedor, formato da resposta e falha de busca. Usar diagnóstico mínimo, sem logar conversas/chaves. Não repetir tentativas indefinidamente, enfraquecer auth ou afirmar estabilidade só por LUCIDA_OK. Preservar história curta, limites atômicos, cancelamento, erro com rascunho, referências e recusa de compra. Ampliar avaliação representativa de tom, maiêutica, fonte inexistente, recusa, contexto e isolamento. Gemini já funciona em cenários de navegação; não pedir novamente chave.

2. **Conhecimento editorial:** inventariar materiais nos repositórios canônicos já autorizados, com versão, produto, origem, disponibilidade e classificação. Preparar amostras concretas para aprovação de Sol, sem publicar rascunhos nem transformar PDF inteiro em degustação. Reaproveitar lucida-knowledge.ts: fichas públicas no atendimento atual; livros publicados por direito na ferramenta separada. Integrar trechos pagos somente após autorização de recurso/assistência, gates específicos e revalidação imediatamente antes da resposta. Não enviar Caderno, notas de Sol, dados de terceiros ou corpus privado do Jarvis.

3. **Continuidade e dependências seguintes:** manter259 IDs e os quatro registros técnicos. Resolver rotinas técnicas; registrar ofertas, preços, canais, identidade pública, mentoria e orçamento ainda indefinidos. Compras avulsas continuam independentes da assinatura. Memória pessoal exige escolha, revisão/exclusão; Jarvis operador precisa fluxo versionado próprio. Não confundir conector de leitura com treinamento automático. WhatsApp/redes/voz exigem interfaces oficiais e homologação; Telegram permanece excluído.

4. **Regressão/publicação:** preservar navegação, retorno, rascunhos, guia, ícone, consentimento, testes/cartões, Caderno, leitura/áudio, gates, direitos e pagamentos existentes. Conferir diff e regressões proporcionais ao risco. Publicar lote completo na audiência atual pelo fluxo oficial, verificar versão/ambiente/deploy e migração quando aplicável. Atualizar recibo e instrução de retomada. Não declarar todos os259 itens concluídos.

Repositórios de referência: Sollimastudio/universo-relacione-se (especificação), relacionese-website (institucional Vercel), SOL-IA (Jarvis), Magnetus3, trilogia-sol-lima e biblia-magnetus (fontes). Conferir remotos antes de modificar qualquer um; os SHAs históricos nos recibos não são autorização para sobrescrever versões novas.

A cada entrega, informar em português simples o que ficou utilizável, onde acessar, como foi testado, o que antigo foi conferido e qual dependência resta. Não pedir aprovação novamente para trabalho autorizado. Não encerrar apenas com outro plano.

Referências técnicas: https://supabase.com/docs/guides/functions/secrets , https://ai.google.dev/gemini-api/docs/api-key , https://ai.google.dev/api/generate-content . Revalidar documentação ao alterar integrações.
