# LÚCIDA — prompt profissional de conclusão e tarefas de Sol

Versão 2 de orientação executiva · 25/09/2026 · Universo Relacione\-se

Este arquivo é uma instrução para a próxima execução\. Sua criação não instala funcionalidades, não altera a hospedagem e não declara a LÚCIDA pronta\. Reúne o comando atualizado e, nos anexos, os dois documentos originais completos\. Não é preciso reescrever o escopo em uma nova conversa\.

## Como usar

Anexe este arquivo ao ambiente de desenvolvimento com acesso aos projetos e envie:

> Execute o prompt deste arquivo a partir do estado atual. Leia os anexos, confira as versões remotas e os registros de continuidade, preserve trabalhos posteriores e comece pelo login e pela estabilidade da conversa. Prossiga nos demais lotes autorizados. Entregue funções utilizáveis com evidências e registre cada dependência externa, sem me transferir decisões técnicas rotineiras.

O trabalho deve ocorrer no projeto existente\. Não crie uma nova LÚCIDA do zero nem um novo banco apenas por receber este arquivo em outra conversa\.

## A parte de Sol, em linguagem simples

### Já feito

- A chave Gemini foi cadastrada e aceita em teste real registrado no lote 5\. Não é necessário cadastrá\-la novamente\.
- Gemini é o provedor escolhido; OpenAI fica como opção futura\.
- A aparência, a navegação e o conteúdo existentes devem ser preservados\.
- Os testes e seus resultados são gratuitos; Telegram fica fora desta fase\.

### Decisões suas que ainda serão necessárias

|Momento                                                       |O que você precisa fazer                                                                                                                                                                       |O que a equipe deve preparar antes                                                                                                                                                             |
|--------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|Preparação editorial                                          |Confirmar quais versões dos materiais estão aprovadas e quais trechos podem ser oferecidos gratuitamente. Enviar somente arquivos que a equipe realmente não encontrar.                        |Inventariar os repositórios e arquivos acessíveis; apresentar uma lista curta das lacunas e uma proposta de amostras.                                                                          |
|Preparação comercial                                          |Confirmar produtos da primeira abertura, preços, prazo de acesso e o que cada compra inclui. Se houver assinatura, confirmar seus benefícios e limites; para mentoria, formato, valor e agenda.|Recuperar as ofertas existentes e apresentar uma tabela pronta para conferir. Não obrigar você a inventar uma assinatura para o chat funcionar.                                                |
|Antes de ampliar o uso                                        |Definir um teto mensal em reais para IA e serviços novos. Esse teto é uma decisão de gasto, não uma promessa de que o fornecedor nunca cobrará além dele.                                      |Estimar custos com tarifas atuais, separar custos fixos e variáveis e implementar limites, alertas e suspensão compatíveis. Não contratar planos automaticamente.                              |
|Somente se faltar acesso                                      |Entrar na sua própria conta do serviço indicado e concluir eventual confirmação de identidade ou conexão.                                                                                      |Usar primeiro os acessos já disponíveis; informar o endereço exato, a ação e o motivo. Não pedir senha, código de acesso ou chave no chat.                                                     |
|Se o envio de códigos por e-mail ainda não estiver configurado|Confirmar o remetente e, se necessário, autorizar o serviço de envio e o acesso ao domínio.                                                                                                    |Conferir a configuração existente, escolher a solução compatível e entregar a configuração pronta ou os registros exatos a inserir. Não pedir que você escolha arquitetura, banco ou protocolo.|
|Na homologação                                                |Testar no iPhone: entrar com um e-mail seu, conversar, fazer um teste, abrir uma indicação, voltar e reencontrar um registro salvo. Digitar o código de acesso somente na tela do app.         |Entregar um link restrito realmente utilizável e um roteiro curto; realizar antes os testes técnicos e as verificações que não dependem do seu aparelho.                                       |
|Antes de abrir ao público                                     |Aprovar a versão, o endereço público, os termos apresentados e a abertura correspondente.                                                                                                      |Demonstrar o fluxo completo e confirmar que a área privada e os dados dos clientes continuam protegidos. A restrição atual está registrada em LUC-259.                                         |
|Na fase de WhatsApp e lives                                   |Indicar o número comercial e as contas que serão usadas; informar se transmite por um ou dois celulares ou computador; realizar o ensaio de áudio.                                             |Conferir as integrações oficiais, acessos disponíveis, custos e ferramentas necessárias. Esses itens não devem interromper a correção do chat do app.                                          |

Você não precisa programar, montar o banco, configurar modelos manualmente nem “treinar” a LÚCIDA conversando com ela\. A equipe deve organizar os materiais e preparar o fluxo pelo Jarvis\. Sua revisão de conteúdo e decisões comerciais continuam importantes\.

### Chaves e configuração: o que fazer agora

**Agora: nenhuma nova chave foi identificada como necessária\.** Revalidar tecnicamente a configuração antes de solicitar qualquer ação a Sol\.

|Item                                  |Local/ação                                                                                                                                                                                                                  |
|--------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|Gemini já configurado                 |Segredo `LUCIDA_GEMINI_API_KEY` no projeto Supabase ACESSORA-SOL.IA. Não apagar ou substituir os segredos do Jarvis.                                                                                                        |
|Painel para eventual troca futura     |https://supabase.com/dashboard/project/rkkpbmzrucaghrojujvb/functions/secrets                                                                                                                                               |
|OpenAI no futuro                      |Somente quando Sol tiver uma chave e quiser ativar: `LUCIDA_OPENAI_API_KEY` no mesmo painel. A equipe configura e testa o provedor/modelo; a opção permanece desativada até então.                                          |
|Conexão entre app e serviço de IA     |`LUCIDA_GATEWAY_TOKEN`, gerenciado pela equipe no servidor. Sol não precisa copiar esse token.                                                                                                                              |
|Login por e-mail, pagamento e WhatsApp|Configurações a inventariar. Se faltar algo, a equipe entrega nome exato do campo, painel correto e valor não secreto ou modo seguro de inserir o segredo. Não solicitar variáveis genéricas que o código ainda não utiliza.|

Para login por e\-mail via Supabase Auth, o envio padrão é restrito e não é um serviço de produção para clientes\. Conferir um serviço de envio próprio já existente antes de contratar outro\. Códigos e links de acesso são opções suportadas; a integração ainda precisa ser implementada e testada\. Referências oficiais consultadas em 25/09/2026:

- https://supabase\.com/docs/guides/auth/auth\-smtp
- https://supabase\.com/docs/guides/auth/auth\-email\-passwordless

## PROMPT DE EXECUÇÃO — INÍCIO

Assuma a direção técnica da conclusão da LÚCIDA no Universo Relacione\-se de Sol Lima\. Atue como responsável por engenharia, arquitetura de IA, experiência de uso, integração, operação e verificação\. Execute o trabalho autorizado, resolva as decisões técnicas rotineiras e conduza a implementação até entregas comprovadamente utilizáveis\.

Sol é leiga\. Comunique o que ela consegue fazer, o que está falhando, o que depende dela e o que você está resolvendo\. Não use o número de testes, um deploy bem\-sucedido ou a presença de um botão como substituto de uma experiência funcional\.

### 1\. Escopo, fontes e precedência

Leia o checklist mestre completo e o método original nos anexos deste arquivo\. Consulte também suas versões canônicas no projeto\. Esta instrução complementa o método, atualiza a prioridade após o problema de login e preserva todas as tarefas LUC\-001 a LUC\-259\. Não reduz o escopo a um chatbot simples\.

Instruções explícitas posteriores de Sol e alterações posteriores verificadas devem ser conciliadas com o histórico\. Preserve a origem das decisões\. Se um requisito mudar, registre sua substituição; não apague a versão anterior\. A ordem operacional deste prompt dá prioridade ao acesso e à estabilidade, sem cancelar as fases restantes\.

Leia os documentos existentes antes de criar equivalentes:

- `docs/lucida/CONTINUIDADE_LUCIDA.md`
- `docs/lucida/EXECUCAO_LUCIDA.json`
- `docs/lucida/DECISOES_LUCIDA.md`
- `docs/lucida/FUNCOES_APROVADAS_LUCIDA.md`
- `docs/lucida/MANUAL_LUCIDA.md`
- `docs/lucida/CHAVE_E_CONHECIMENTO.md`
- `docs/lucida/LOTE_5_2026-09-25.md` e lotes posteriores existentes
- contratos, instruções locais e recibos canônicos de entrega\.

Referências para localizar e revalidar, não para presumir estado atual:

- App Sites: `appgprj_6ab11d2e84188191a90910ec6b06c64d`\.
- Endereço registrado: https://relacione\-se\-universo\.sollimalovecoach\.chatgpt\.site
- Especificação transversal: `Sollimastudio/universo-relacione-se`, diretório `04-lucida`\.
- Site institucional: `Sollimastudio/relacionese-website`; https://relacionese\-website\.vercel\.app/
- Jarvis: `Sollimastudio/SOL-IA`\.
- Produtos e acervo: `Sollimastudio/Magnetus3`, `Sollimastudio/biblia-magnetus` e `Sollimastudio/trilogia-sol-lima`\.
- Supabase reaproveitado para o provedor: `rkkpbmzrucaghrojujvb`, ACESSORA\-SOL\.IA\.

### 2\. Situação conhecida — revalidar antes de agir

Esta base foi conferida nos documentos e no checkout local ao elaborar este prompt; não constitui uma nova auditoria da produção\.

- Checkout consultado: `e756a64b07573ca4d2b64bf2b36ac237c5b55af4`, sem alterações locais indicadas pelo Git\. Última entrega registrada: v20, lote 5, homologação privada, somente proprietária\.
- Registro de execução: 259 tarefas; 14 concluídas no escopo registrado, 46 em homologação, 51 em execução, 115 pendentes e 33 bloqueadas\. Os números não medem percentual de produto pronto\. Não reclassifique uma tarefa sem cumprir seu critério completo\.
- O app usa Sites/Workers/D1, com estrutura de armazenamento R2\. O Supabase executa o gateway exclusivo `lucida-provider` e guarda segredos\. Não foi feita uma migração geral do app para Supabase ou Vercel\.
- Gemini foi aceito e gerou respostas reais em parte dos cenários\. O modelo registrado é `gemini-3.1-flash-lite`; confirmar disponibilidade, escolha vigente e comportamento real antes de alterá\-lo\. OpenAI permanece opcional\.
- O chat usa manual e fichas públicas; não está conectado ao acervo integral, à memória persistente ou às conversas privadas do Jarvis\. Existe busca autorizada de livros a reaproveitar, mas isso não prova sua integração ao chat\.
- O acesso atual depende da sessão ChatGPT da hospedagem\. Na gravação de Sol, o envio exibiu “Entre na sua conta para continuar”\. Não foi concluído o cadastro próprio dos clientes do Relacione\-se\.
- Há falhas reais de reflexão com 502/504 e demora\. Há também respostas bem\-sucedidas\. A causa não foi comprovada; não atribuir automaticamente o problema à chave, ao celular ou ao modelo\.
- Os 145 cenários determinísticos registrados e os testes com identidade sintética não equivalem a uma conversa autenticada de Sol nem à jornada de um cliente em produção\.

### 3\. Conferência inicial e preservação obrigatória

Antes da primeira edição, confira fontes oficiais do projeto, branch, HEAD, versão publicada, ambiente, público, banco, arquivos e mudanças posteriores\. Compare código local, remoto e publicado\. Preserve alterações em andamento e PRs de Jarvis/Magnetus; seus números e commits históricos não são prova de estado atual\.

Use branch ou worktree quando adequado e mantenha um ponto rastreável de recuperação\. Não use reset destrutivo, force\-push, remoção ampla de arquivos, troca de árvore ou restauração de banco para facilitar a tarefa\. Não reescreva o app, altere o estilo global ou atualize todas as dependências como efeito colateral\.

Identifique e proteja: navegação e retorno, guia contextual, ícone de olho com raio, consentimento de métricas, links institucionais, vitrine, “Em breve”, testes, resultados/cartões, rascunhos, Caderno, leitura, progresso, áudio, direitos, administração e gates de 24 horas existentes\.

Diferencie defeitos anteriores de regressões introduzidas\. Corrija uma regressão sua antes de concluir o lote ou reverta apenas seu delta, preservando mudanças alheias\. Não prometa risco zero; produza evidência e recuperação proporcionais\.

### 4\. Primeiro lote: entrada compreensível e conversa estável

Faça uma entrega coerente que permita a Sol testar o chat e confirme o desenho de acesso dos clientes\. Não a declare lançamento público\.

**Investigue a autenticação:** reproduza o erro pelo caminho autorizado, confira a identidade entregue ao app e verifique navegador normal, navegação no ChatGPT e sessão expirada\. Diferencie a proteção externa da hospedagem da conta interna do Relacione\-se\. Um token de inspeção da hospedagem não é uma sessão de cliente\.

Não falsifique cabeçalhos de identidade, desative proteções, dê privilégios administrativos a visitantes nem exponha dados para fazer o teste passar\. Se a plataforma impedir cadastro independente dentro da audiência privada, documente a limitação comprovada e prepare a menor superfície de homologação compatível, mantendo a área privada restrita\. Não remova a barreira externa silenciosamente\.

**Investigue a demora:** meça separadamente carregamento da interface, sessão, consulta ao catálogo, gateway e modelo\. Use identificadores de correlação, duração e códigos de erro sem registrar relatos íntimos ou segredos\. Compare um conjunto pequeno e representativo de perguntas\. Após falhas repetidas, mude a hipótese com base em evidências; não faça chamadas indefinidas\.

Corrija a causa identificada e trate cancelamento, indisponibilidade, limite e repetição segura\. Mostre estado de envio imediatamente, preserve o rascunho e permita recuperação\. Não atribua uma resposta fixa ao Gemini para esconder falha\. Não corte regras de acesso ou o manual para obter velocidade\.

Defina metas mensuráveis após uma medição inicial: tempo até interface utilizável, tempo de resposta da IA, erros e condições de rede\. Registre amostra e resultados observados\. Não prometa resposta instantânea nem apresente uma única resposta rápida como comprovação de estabilidade\.

### 5\. Segundo lote: visitante e conta própria do Relacione\-se

Implemente o fluxo com os seguintes comportamentos:

- Visitante acessa a vitrine, testes/resultados gratuitos e degustação limitada da LÚCIDA sem precisar de conta do ChatGPT\.
- “Entrar ou criar conta” identifica claramente uma conta do Relacione\-se\. Preferir e\-mail verificado com código, se compatível com a infraestrutura e a operação; avaliar link de acesso conforme testes nos aparelhos\.
- A conta é solicitada quando necessária para salvar, continuar em outro aparelho ou acessar direitos pessoais\. Cadastro não concede acesso pago\.
- Implementar estados de envio de código, código incorreto/expirado, reenvio limitado, entrada, saída, retorno à atividade e continuidade de sessão\. Não expor se um e\-mail pertence a outra pessoa por mensagens desnecessárias\.
- Visitantes têm sessões independentes e limites de abuso\. A vinculação posterior ao cadastro exige sessão válida, confirmação de titularidade e escolha de salvar; nunca aceitar um identificador de visitante arbitrário enviado pelo cliente\.
- Identidades ChatGPT existentes e novas identidades de cliente precisam de uma transição compatível\. Não alterar o dono de Cadernos, compras ou progressos por igualdade de nome/e\-mail não verificado\. Preserve os registros anteriores e teste a migração em cópia de homologação quando necessária\.
- A administração mantém autorização própria\. Estar autenticado não transforma um cliente em administrador\.

Avalie o uso do Supabase Auth existente sem presumir que já está configurado\. Antes de mudar autenticação no projeto compartilhado com Jarvis, inventarie URLs, provedores, modelos de e\-mail, sessões e usuários afetados\. Preserve as configurações e os fluxos do Jarvis; um projeto compartilhado não cria isolamento administrativo automático\.

Confira serviço de envio, remetente, limites e entrega real\. Não desative verificação de e\-mail para contornar falta de envio\. Novas contratações ou acesso manual a uma conta devem ser pedidos somente com configuração e motivo concretos\. A criação de tabelas e variáveis é responsabilidade técnica\.

### 6\. Conhecimento, memória e personalidade

Reaproveite manual, catálogo, permissões e recuperação existentes\. Inventarie primeiro as fontes acessíveis; solicite apenas materiais ausentes ou uma decisão editorial que não possa ser inferida com segurança\.

Organize três conjuntos separados:

1. **Conhecimento editorial:** biografia pública, produtos, livros, métodos, testes, amostras, disponibilidade e ofertas aprovadas; cada fonte com versão, autoria e classificação\.
2. **Memória do cliente:** preferências, resumo de continuidade, progresso e informações que a pessoa autorizou salvar, isolados por titular e revisáveis\.
3. **Memória privada de Sol/Jarvis:** permanece privada; não é incorporada ao atendimento público por estar no mesmo projeto\.

Implemente importação com original preservado, hash, extração/OCR quando necessário, capítulo/página reais, revisão, classificação antes da indexação, publicação e retirada de versões\. RAG significa consultar trechos pertinentes; não alegar que o PDF foi absorvido para sempre nem exigir retreinamento a cada atualização\.

Escolha busca textual, vetorial ou híbrida por qualidade medida\. Preserve D1 e dados existentes enquanto forem adequados; não crie um segundo acervo concorrente ou migre tudo para Supabase sem necessidade e plano\.

Busque texto pago somente após conferir direitos no servidor, incluindo etapas de 24 horas, e revalide antes de responder\. Separe os caches por permissão e versão; retirada de fonte ou revogação também deve atingir cache, links e arquivos\. Documentos recuperados são dados, não comandos administrativos\.

A LÚCIDA deve responder diretamente quando pedirem uma informação e usar maiêutica quando ela ajudar\. Adaptar o tom, ritmo e nível de detalhe por preferências e observações contextualizadas; não gerar laudo clínico nem pontuação DISC válida a partir de conversa informal\. Respeitar recusas comerciais, evitar bajulação e não explorar sofrimento para vender\.

Memória persistente requer identidade e escolha informada, separada de métricas e marketing\. Implementar visualização, correção, exclusão, retenção e comportamento quando o banco estiver indisponível\. Não gravar histórias privadas no Git nem em telemetria\.

### 7\. Ofertas, produtos pagos e mentoria

Prepare uma matriz de oferta para Sol revisar usando informações atuais já aprovadas\. Não invente preço, assinatura, benefício, prazo ou agenda\. Produto indisponível mostra “Em breve”, sem cobrança por algo apresentado como entregue\.

Integre o checkout vigente, previsto como Kiwify, por contrato oficial atualizado\. Receber um clique ou uma frase “já paguei” não libera conteúdo\. Verifique eventos/autenticidade, duplicação, ordem, falhas e reconciliação de compra, renovação, reembolso e cancelamento\. Testes de pagamento devem usar o mecanismo de teste disponível; não cobrar pessoas para verificar código sem autorização específica\.

Assinatura vencida não cancela uma compra avulsa válida\. Permissões são aplicadas a todos os caminhos: chat, busca, leitor, download, API e cache\. A LÚCIDA considera o que a pessoa já possui ao recomendar\.

Mentoria exige oferta e agenda reais\. Prepare briefing privado somente com autorização específica, permitindo revisão pelo cliente\. Separe fatos, relatos e hipóteses; a proposta de sessão precisa da revisão de Sol\. Não enviar o resumo a terceiros automaticamente\.

### 8\. Testes gratuitos, compartilhamento, Jarvis e canais

Conclua os itens do checklist sem perder o que já existe:

- Testes: fórmula determinística e versão, casos conhecidos, interpretação aprovada e resultado gratuito\. Nenhum cadastro de marketing, compra ou compartilhamento como condição para ver o resultado\.
- Cartões: visual da marca, números reais, prévia editável nos campos permitidos, legenda, download e compartilhamento quando suportado\. Link abre o teste para outra pessoa; não expõe o resultado privado original\. Não prometer que uma imagem é um link clicável em qualquer rede\.
- Jarvis: transformar orientações explícitas de Sol em propostas, avaliações, versões e alterações reversíveis dentro da autonomia autorizada\. Ideias e desabafos ficam em rascunho/privado\. Conector de leitura não equivale a um operador de atualização\.
- WhatsApp e redes: conferir contas e APIs oficiais, consentimento de vínculo, transferência humana, condições e custos atuais\. Preparar código e contratos enquanto faltarem acessos; não anunciar canal operacional por ter apenas um webhook\.
- Voz e live: separar bastidor de transmissão pública, acionar explicitamente, interromper/silenciar, testar eco e queda de conexão\. Responder em voz, transmitir áudio e ler comentários são três integrações distintas\. Não expor memória privada durante live\.
- Telegram permanece excluído desta fase da LÚCIDA; preservar trabalhos autorizados em outros projetos\.

### 9\. Provedores, segredos, custos e infraestrutura

Preserve a escolha Gemini e a opção futura OpenAI, permitindo trocar modelo/chave por configuração no servidor com validação e reversão\. Não pedir uma chave OpenAI para desbloquear esta entrega\. Não usar rodízio de chaves para superar cotas\.

Chaves permanentes, tokens de serviço e credenciais privilegiadas não podem ir para componentes públicos, URLs, logs ou documentos\. Reutilize os mecanismos existentes; não crie variáveis sem ligação comprovada com o código\. Quando Sol tiver de inserir um segredo, explique painel, projeto e nome exato, sem solicitar seu valor no chat\.

No Supabase, consulte documentação vigente antes de implementar\. Se tocar dados expostos, verifique políticas de acesso por titular e papel; não enfraqueça RLS ou autenticação para resolver um erro\. No D1, mantenha a autorização no servidor\. Teste isolamento real entre duas contas\.

Registre modelo, política, fontes e consumo sem conteúdo íntimo\. Preserve limites existentes até substituí\-los por limites justificados; 30 mensagens por conta e 100 por app/dia registrados no lote 5 não equivalem a um teto financeiro mensal garantido\. Antes de expandir tráfego, estime custo, defina controles e obtenha a decisão comercial de gasto necessária\.

Não migre para Vercel só porque o site institucional está lá\. Se houver limitação comprovada da infraestrutura atual, apresente solução compatível e impacto, preserve os dados e prepare a migração como trabalho separado\. Publicação de código e ampliação de audiência são ações distintas\.

### 10\. Método de trabalho e continuidade sem dependência do chat

Use lotes pequenos, com objetivo funcional, IDs LUC, critérios observáveis e regressões a conferir\. Para cada lote: conferir base; implementar; validar; revisar diff; integrar pelo fluxo autorizado; verificar a versão no destino; registrar e prosseguir\.

Mantenha uma única fonte de acompanhamento com todos os 259 IDs estáveis\. Registre implementação, evidência, versão, ambiente, estado, dependências e próxima ação\. Novos requisitos recebem identificação adicional sem renumerar os antigos\.

Ao trocar de contexto, salve: objetivo atual, último commit, alterações não publicadas, resultados, falhas conhecidas, configuração não secreta, bloqueios e próximo passo exato\. Na retomada, compare com o remoto; não restaure uma versão antiga por ser a que está neste prompt\.

Um bloqueio externo deve indicar: o que falta, evidência, tarefas afetadas, ação mínima de Sol e trabalho independente que continua\. Não termine pedindo “posso continuar?” para programação já autorizada\. Não transforme uma sugestão de arquitetura em dependência artificial de contratação\.

Não execute trabalho em segundo plano sem processo real\. Não declare ausência de falhas, porcentagem de conclusão ou prazo fechado sem base\. Este método reduz perda de contexto; não existe garantia absoluta de “sem fadiga” ou “sem regressões”\.

### 11\. Critérios obrigatórios de entrega

Registre separadamente local, homologação e produção\. Use dados sintéticos quando apropriado, deixando explícito o limite dessa prova\. Compile e rode os gates do projeto; acrescente verificações proporcionais para autenticação, direitos, memória, compra e mudanças de esquema\. Não apague testes para obter aprovação\.

Antes de declarar **a experiência do app pronta para lançamento**, comprove:

1. Visitante fora da conta de Sol abre a entrada destinada ao público, usa teste gratuito e inicia degustação dentro dos limites\. O ensaio deve ocorrer em ambiente autorizado, sem ampliar silenciosamente a audiência atual\.
2. Cadastro/entrada funciona com e\-mail verificado, sessão continua e logout/troca de conta não expõem dados\. Não há exigência de conta ChatGPT no percurso público final\.
3. Conversa responde com fonte e tom adequados, lida com perguntas diretas/reflexivas, recusa comercial e falhas; tempos medidos são informados\.
4. Duas pessoas não acessam histórico, Caderno, resultados ou direitos uma da outra\. Administração permanece separada\.
5. Conteúdo público, amostra, pago e etapas respeitam a matriz de acesso, inclusive após expiração/revogação\.
6. Compra e assinatura efetivamente oferecidas foram homologadas; ofertas sem definição não são anunciadas como ativas\.
7. Navegação, retorno, testes, rascunhos, cartões, leitura, progresso, consentimento e aparência afetados foram conferidos, incluindo o celular de Sol quando necessário\.
8. Conhecimento utilizado está inventariado; lacunas são reconhecidas\. Memória funciona com os controles prometidos\.
9. Configuração, orçamento, monitoramento, suporte, recuperação e implantação têm responsáveis e evidências\.
10. O endereço entregue corresponde ao commit testado e ao público autorizado\. Deploy bem\-sucedido é apenas uma dessas provas\.

“App pronto para lançamento” e “escopo integral concluído” são estados diferentes\. Para declarar a LÚCIDA integralmente pronta, todos os requisitos aplicáveis do checklist, inclusive Jarvis, mentoria, compartilhamento e canais/voz, precisam de seu aceite\. Uma fase pronta não encerra as demais\. Integração inviável ou bloqueada permanece registrada; só uma decisão explícita de Sol pode retirar escopo\. Não fingir conclusão nem impedir a entrega útil de um lote por dependência de outra fase\.

Em cada entrega informe, em português simples: o que ficou utilizável, link e modo de acesso, versão efetiva, como foi verificado, quais funções anteriores foram conferidas, falhas/limites restantes, próxima ação e somente as providências realmente necessárias de Sol\.

**Comece pela conferência das fontes e da base atual\. Em seguida, implemente o lote de acesso e estabilidade e avance pelos demais trabalhos viáveis, mantendo o progresso salvo\.**

## PROMPT DE EXECUÇÃO — FIM

## Anexos de preservação

Os documentos abaixo foram copiados integralmente do checkout consultado\. Seus estados históricos não substituem a conferência atual\. Quando houver uma versão canônica posterior, preserve e concilie essa atualização\. Os anexos não autorizam exposição da área privada nem convertem este pedido de prompt em execução imediata do app\.

SHA\-256 do checklist mestre copiado: `1234d7f443a3d447fb31425221d296238c5e97698b341463fc01c2c51952f86f`\.

---

## Anexo A — checklist mestre original integral

<!-- INICIO_CHECKLIST_ORIGINAL -->

# Checklist mestre e ficha técnica da LÚCIDA

**Projeto:** Universo Relacione\-se · Sol Lima
**Versão:** 2 · 25 de setembro de 2026 · atualização e ampliação do registro anterior
**Finalidade:** preservar os pedidos e as diretrizes discutidas para orientar a implementação futura, sem depender da memória de uma conversa\.

Este documento registra requisitos, propostas e pendências\. Uma caixa vazia significa trabalho a executar ou validar; não comprova que a funcionalidade existe\. As sugestões de arquitetura e de oferta comercial continuam sujeitas à definição de Sol\. Salvar este documento não instala regras na LÚCIDA nem conecta o Jarvis automaticamente\.

**Conclusão operacional:** existe uma base de app, navegação e controles para aproveitar\. A LÚCIDA conversacional, a base de conhecimento em uso pelo modelo, a memória personalizada, o pagamento automático, a atualização pelo Jarvis e os novos recursos de compartilhamento e voz ainda exigem implantação e homologação\. A abertura pública deve preservar a área privada\.

**Como acompanhar:** tarefas usam caixas vazias e identificadores LUC\. Marcar uma tarefa somente quando houver evidência do seu critério de aceite; registrar responsável, data, versão e prova\. “Existe no código”, “testado localmente” e “funciona em produção” são estados diferentes\. O inventário de evidências está na seção 23\. A ficha técnica, os cadastros e o plano de validação estão nas seções 15 a 22\.

## 1\. Norte do projeto

A LÚCIDA deve trazer lucidez, discernimento e clareza\. Ela recebe visitantes, ajuda cada pessoa a navegar pelo ecossistema, oferece testes gratuitos, contextualiza conteúdos, orienta próximos passos e recomenda produtos ou mentoria quando houver pertinência\. Sua comunicação deve ser acolhedora, inteligente, adaptável e capaz de questionar respeitosamente, com maiêutica, sem frases repetidas ou concordância automática\.

O Jarvis será o interlocutor cotidiano de Sol e o operador interno da evolução da LÚCIDA\. Sol quer conversar com o Jarvis sobre suas ideias e orientações; o Jarvis deve transformá\-las em atualizações organizadas, verificáveis e reversíveis\. Os visitantes conversam com a LÚCIDA\.

Diretrizes solicitadas que devem ser preservadas:

- Preservar o que já funciona, a identidade visual e o conteúdo existente do app\.
- Manter a vitrine gratuita, com livros, trilogia, linhas para homens e mulheres, testes, ferramentas, outros produtos e futuras ofertas\.
- Manter os testes e seus resultados gratuitos\. Usá\-los como portas de entrada úteis para o ecossistema\.
- Exibir “Em breve” para produtos ainda indisponíveis, sem links mortos ou promessa de entrega já existente\.
- Manter acesso claro ao site institucional Relacione\-se, com informações sobre Sol, e aos recursos públicos do YouTube\.
- Oferecer degustações autorizadas de conteúdos pagos e proteger o restante conforme os direitos de cada pessoa\.
- Adaptar a conversa para favorecer compreensão, autonomia, vínculo e recomendações pertinentes\.
- Preparar encaminhamento para mentoria com Sol, com resumo autorizado pelo cliente\.
- Conectar os canais planejados a uma base de conhecimento governada em comum\.
- Manter Telegram fora do escopo desta fase, conforme a decisão mais recente de Sol\.
- Trocar o símbolo de estrelinhas por um único ícone de olho com um raio integrado, quando a execução visual for iniciada\.

## 2\. Situação registrada e limites de prontidão

|Item                       |Situação / consequência                                                                                                                                                                                                 |
|---------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|App Universo Relacione-se  |Consulta atual de 25/09/2026: ativo, versão publicada 14, acesso restrito a um usuário, sem visitantes externos. Preservar layout, dados e controles. É necessária uma entrada pública planejada para receber o público.|
|Site institucional         |Endereço registrado: https://relacionese-website.vercel.app/ . Repositório identificado no histórico de trabalho: Sollimastudio/relacionese-website. Revalidar domínio e destino ao integrar novos caminhos.            |
|Interface da LÚCIDA        |Guia contextual, voltar, início, mapa, biblioteca e link institucional presentes no código. Há reflexão de perguntas fixas, explicitamente identificada como não sendo IA. O ícone flutuante ainda usa estrelinhas.     |
|Conversa com IA            |O código local consultado em 25/09/2026 retorna HTTP 503 em `app/api/lucida/route.ts`, informando que a IA ainda não está ativa.                                                                                        |
|Conhecimento e memória     |`lib/platform/lucida-context.ts` registra provedor/corpus pendentes de homologação e memória desativada. Há controles de acesso existentes a preservar.                                                                 |
|Conexão com Jarvis         |O conector consultado oferece leitura de catálogo/eventos; não permite publicar, enviar mensagens ou ler notas pessoais. Não equivale a um atualizador automático da LÚCIDA.                                            |
|Jarvis por voz em produção |Sol informa que o Jarvis terá voz. O funcionamento completo de captura, resposta e transmissão ao vivo não foi verificado nesta etapa.                                                                                  |
|Cobrança e direitos        |A integração de cobrança completa e seus cenários devem ser homologados antes de prometer desbloqueio automático.                                                                                                       |
|Novos cartões e voz em live|Requisitos novos para desenvolvimento. Não implementados nesta etapa de planejamento.                                                                                                                                   |

Os estados acima se baseiam no histórico disponível e na inspeção local indicada\. Antes de executar, comparar a versão do código com a produção\. Publicar ou fazer redeploy na Vercel não cria, por si só, provedor de IA, conhecimento, memória, pagamentos ou integrações\.

## 3\. Identidade, conversa e navegação

- [ ] **LUC\-001** Criar um manual versionado com propósito, tom, limites, exemplos e fontes autorizadas\.
- [ ] **LUC\-002** Incorporar as instruções essenciais a cada atendimento, junto apenas do contexto necessário\.
- [ ] **LUC\-003** Usar perguntas maiêuticas quando ajudarem: distinguir fato, interpretação, consequência e escolha; responder diretamente quando a pessoa pedir um link ou informação objetiva\.
- [ ] **LUC\-004** Evitar frases feitas, bajulação, interrogatórios e confrontos humilhantes\. Acolher sentimentos sem confirmar automaticamente interpretações\.
- [ ] **LUC\-005** Oferecer caminhos concretos: continuar, voltar, início da vitrine, explorar, biblioteca e ajuda na página atual\.
- [ ] **LUC\-006** Mostrar onde o visitante está e preservar respostas de testes ou outras atividades ao abrir e fechar a ajuda\.
- [ ] **LUC\-007** Manter ajuda disponível durante a navegação, com convites discretos e dispensáveis; evitar interrupções contínuas\.
- [ ] **LUC\-008** Ajustar o ícone do olho com raio, nome acessível e estados de foco, mantendo a linguagem visual aprovada\.
- [ ] **LUC\-009** Verificar que o botão e o convite não cobrem consentimento de métricas, menus ou controles, inclusive no celular\.
- [ ] **LUC\-010** Revisar destinos da vitrine, retorno ao app e comportamento dos links externos\.

## 4\. Conteúdo, PDFs e proteção do material pago

- [ ] **LUC\-011** Inventariar materiais existentes e confirmar nomes, versões e estado de cada produto, incluindo a trilogia, linhas para homens/mulheres e Magnetus/Magnetos conforme o nome oficial\.
- [ ] **LUC\-012** Reaproveitar os repositórios e as fontes canônicas existentes; decidir depois se um módulo separado basta ou se há motivo para um repositório próprio da LÚCIDA\.
- [ ] **LUC\-013** Extrair PDFs e documentos, aplicar OCR quando necessário e conferir títulos, capítulos, páginas e qualidade da extração\.
- [ ] **LUC\-014** Catalogar fonte, autoria, versão, produto, público, tema, permissões e situação editorial de cada trecho\.
- [ ] **LUC\-015** Distinguir rascunho, revisão, aprovado, publicado e arquivado\. Ideias de Sol e pesquisas externas não se tornam conteúdo oficial automaticamente\.
- [ ] **LUC\-016** Criar fichas públicas: para quem é, o que inclui, temas, formato, disponibilidade, links válidos e amostras autorizadas\.
- [ ] **LUC\-017** Manter capítulos integrais, exercícios e protocolos pagos separados das fichas e degustações públicas\.
- [ ] **LUC\-018** Buscar apenas trechos relevantes de fontes autorizadas para responder, com referência correta à obra, capítulo ou página\. Não inventar referências\.
- [ ] **LUC\-019** Aplicar permissões no servidor antes de consultar conteúdo ou executar ferramentas\. Não depender apenas de uma instrução dizendo “não revele”\.
- [ ] **LUC\-020** Para visitantes, permitir apenas fontes públicas e amostras aprovadas; para compradores e assinantes, liberar somente o que o direito adquirido inclui\.
- [ ] **LUC\-021** Preservar eventuais liberações por dia/etapa existentes em produtos\.
- [ ] **LUC\-022** Testar pedidos para extrair material pago por partes, trocar de usuário, contornar regras ou usar uma fala do chat como suposta autorização\.
- [ ] **LUC\-023** Prever resposta útil quando uma fonte faltar, estiver desatualizada ou conflitar com outra; encaminhar a correção ao processo editorial\.

Um PDF passa a integrar uma base consultável após processamento e validação\. Isso não significa que o modelo o “absorveu para sempre”\. A atualização habitual pode ocorrer por documentos, busca, instruções, exemplos e ferramentas; não exige retreinar o modelo inteiro a cada mudança\.

## 5\. Ofertas, assinatura e recomendações

Proposta comercial discutida, ainda sem definição final de preços, limites e composição:

|Modalidade         |Benefício proposto                                                                             |Definição pendente                                           |
|-------------------|-----------------------------------------------------------------------------------------------|-------------------------------------------------------------|
|Gratuito           |Vitrine, testes/resultados, orientação inicial, YouTube e amostras autorizadas                 |Limites operacionais da conversa gratuita                    |
|Compra avulsa      |Produto comprado e suporte contextual previsto na oferta                                       |Prazo de acesso e recursos incluídos                         |
|Assinatura Universo|Catálogo digital incluído, aplicação contínua com a LÚCIDA e novidades previstas enquanto ativa|Produtos incluídos, limites, preço e política de cancelamento|
|Mentoria com Sol   |Encontro ou programa com agenda, escopo e acompanhamento definidos                             |Formatos, preço, disponibilidade e eventual inclusão em plano|

- [ ] **LUC\-024** Definir o significado de “todos os acessos” para cada oferta\. A compra de um livro não deve liberar implicitamente todo o ecossistema\.
- [ ] **LUC\-025** Diferenciar direitos permanentes ou por prazo de compras avulsas e direitos vinculados a uma assinatura ativa\.
- [ ] **LUC\-026** Preservar compras avulsas válidas após o cancelamento de uma assinatura\.
- [ ] **LUC\-027** Justificar a assinatura por benefícios contínuos concretos, sem vender produtos ainda não entregáveis como se estivessem prontos\.
- [ ] **LUC\-028** Integrar o checkout escolhido, previsto como Kiwify, com identificação de produto/oferta e confirmação de pagamento confiável\.
- [ ] **LUC\-029** Tratar renovação, cancelamento, expiração, reembolso, eventos repetidos e falhas de entrega; reconciliar o estado com o provedor\.
- [ ] **LUC\-030** Não conceder acesso com base apenas em “eu comprei” ou em um endereço de e\-mail informado no chat\.
- [ ] **LUC\-031** Recomendar conforme necessidade, acesso já adquirido e preferências: recurso gratuito, teste, amostra, produto, capítulo já disponível ou mentoria\.
- [ ] **LUC\-032** Explicar por que a indicação faz sentido; reconhecer recusas e compras existentes, sem repetir ofertas inadequadas\.
- [ ] **LUC\-033** Evitar urgência inventada, exploração de sofrimento ou promessa de transformação garantida\.
- [ ] **LUC\-034** Calcular custos de IA antes de definir limites e preços\. Não prometer uso ilimitado sem viabilidade operacional\.

## 6\. Identificação, memória e privacidade

- [ ] **LUC\-035** Permitir exploração pública e testes sem exigir cadastro apenas para ver o resultado gratuito\.
- [ ] **LUC\-036** Definir conta por e\-mail verificado, código ou link de acesso quando houver necessidade de salvar histórico, comprar ou continuar em outro aparelho\. Essa é uma proposta; não está implementada por este documento\.
- [ ] **LUC\-037** Usar um identificador interno por cliente, com vínculos verificados para cada canal\.
- [ ] **LUC\-038** Vincular WhatsApp, app e redes sociais mediante confirmação apropriada; nunca unir pessoas só por nome parecido ou e\-mail não verificado\.
- [ ] **LUC\-039** Manter visitantes anônimos em sessões separadas e explicar quando o histórico não acompanha outro aparelho\.
- [ ] **LUC\-040** Permitir que a pessoa escolha salvar preferências e continuidade, veja o que foi registrado, corrija ou peça exclusão\.
- [ ] **LUC\-041** Guardar resumos, progresso e direitos em banco com acesso por usuário; não colocar conversas privadas, segredos ou dados de pagamento no Git\.
- [ ] **LUC\-042** Manter conhecimento editorial compartilhado e histórias pessoais rigorosamente separados\.
- [ ] **LUC\-043** Definir retenção, recuperação, cópias de segurança, monitoramento e comportamento quando a memória não estiver disponível\.
- [ ] **LUC\-044** Não prometer memória perfeita\. Este checklist deve ser consultado e versionado no processo de trabalho; não depende de a IA lembrar espontaneamente de tudo\.

## 7\. Comunicação adaptativa e análise comportamental

Objetivo solicitado: compreender como conversar melhor com cada pessoa, favorecer entendimento e permanência por utilidade, e indicar caminhos comerciais coerentes\. A proposta é um perfil contextual e revisável de comunicação, apoiado em evidências e preferências, sem diagnóstico disfarçado\.

- [ ] **LUC\-045** Separar preferência confirmada, tendência recorrente, estado emocional momentâneo, hipótese e informação desconhecida\.
- [ ] **LUC\-046** Registrar evidências relevantes e contexto, sem percentuais de certeza inventados ou rótulos definitivos como “pessoa muito emocional”\.
- [ ] **LUC\-047** Adaptar ritmo, extensão, estrutura e exemplos: resumo direto; exemplos concretos; passos previsíveis; detalhes, critérios e fontes\.
- [ ] **LUC\-048** Permitir comandos simples, como “seja mais direta”, “explique melhor”, “prefiro áudio” ou “mostre um exemplo”\.
- [ ] **LUC\-049** Usar DISC apenas com escopo claro\. Conversa informal não deve gerar um laudo ou pontuação DISC supostamente validada; um instrumento formal exigiria avaliação específica de método e uso\.
- [ ] **LUC\-050** Tratar preferências por áudio, texto e visual como preferências flexíveis; não como tipos fixos de aprendizagem ou diagnósticos inferidos automaticamente\.
- [ ] **LUC\-051** Adaptar a forma de explicar mantendo os fatos, a honestidade, os direitos de acesso e a identidade da LÚCIDA\.
- [ ] **LUC\-052** Explicar a personalização e permitir controle sobre o perfil persistente\.
- [ ] **LUC\-053** Avaliar compreensão, resolução, satisfação, uso dos materiais e pertinência das recomendações, além de conversão; não premiar apenas conversas longas\.

## 8\. Encaminhamento e preparação para mentoria

- [ ] **LUC\-054** Oferecer mentoria quando corresponder ao objetivo da pessoa e houver oferta/agenda reais\.
- [ ] **LUC\-055** Solicitar autorização específica para compartilhar o resumo com Sol e permitir revisão pelo cliente\.
- [ ] **LUC\-056** Preparar um briefing privado com objetivos declarados, dúvidas, recursos usados, testes realizados, compras e preferências confirmadas\.
- [ ] **LUC\-057** Distinguir relatos do usuário sobre terceiros de fatos verificados; registrar hipóteses como hipóteses\.
- [ ] **LUC\-058** Propor uma estrutura inicial de mentoria: objetivos, perguntas, atividades pertinentes e acompanhamento, para revisão de Sol\.
- [ ] **LUC\-059** Não produzir diagnóstico clínico ou plano definitivo como se a conversa automatizada substituísse avaliação profissional\.
- [ ] **LUC\-060** Restringir o briefing a pessoas autorizadas\. Nunca reutilizar esses dados em outro atendimento, em cartão público ou em live\.

## 9\. Jarvis como operador da evolução da LÚCIDA

- [ ] **LUC\-061** Confirmar o projeto/runtime canônico do Jarvis e suas interfaces atuais antes de ligar o conector existente\. Há referências históricas que podem estar desatualizadas\.
- [ ] **LUC\-062** Criar fluxo para o Jarvis reconhecer orientação explícita de Sol, ideia em elaboração, correção editorial e conversa privada\.
- [ ] **LUC\-063** Transformar orientações em regras concretas, exemplos e mudanças rastreáveis, com referência à origem\.
- [ ] **LUC\-064** Detectar conflitos com regras anteriores, direitos de acesso e materiais publicados\.
- [ ] **LUC\-065** Manter ideias ambíguas em rascunho\. Não transformar desabafos e informações confidenciais de Sol em conhecimento público\.
- [ ] **LUC\-066** Permitir mudanças rotineiras dentro da autonomia autorizada, sem obrigar Sol a entrar em outro painel nem pedir a mesma aprovação novamente\.
- [ ] **LUC\-067** Avaliar mudanças com conversas simuladas sobre tom, fontes, navegação, recusas comerciais, acesso pago e isolamento entre pessoas\.
- [ ] **LUC\-068** Versionar, registrar alterações, publicar pelo processo autorizado e possibilitar retorno à versão anterior\.
- [ ] **LUC\-069** Manter permissões técnicas fora do alcance de mudanças de personalidade ou de uma instrução recebida no chat\.
- [ ] **LUC\-070** Validar fontes externas antes de incorporá\-las\. Pesquisas diárias não devem substituir automaticamente o método de Sol\.
- [ ] **LUC\-071** Usar feedback mínimo e autorizado para melhorar o atendimento, sem copiar indiscriminadamente conversas íntimas de clientes\.

## 10\. Canais e automação

- [ ] **LUC\-072** Priorizar uma base central de regras, conhecimento e catálogo, com adaptações por canal\.
- [ ] **LUC\-073** Implementar a entrada pública do app e a conversa funcional antes de anunciar atendimento automatizado nas redes\.
- [ ] **LUC\-074** Planejar WhatsApp pela integração oficial apropriada, verificando conta, recebimento, envio, janelas e condições vigentes antes da implantação\.
- [ ] **LUC\-075** Planejar Instagram/Facebook por recursos oficiais compatíveis com a conta e o tipo de atendimento\. Não pressupor que personagens nativos dessas plataformas importem toda a LÚCIDA\.
- [ ] **LUC\-076** Prever atendimento humano e contatos claros quando a automação não resolver\.
- [ ] **LUC\-077** Medir falhas, latência, custo e qualidade; limitar abusos e preservar uma saída útil quando serviços externos estiverem indisponíveis\.
- [ ] **LUC\-078** Não ativar Telegram nesta fase\. Referências antigas a Telegram em código não substituem a decisão atual de Sol\.

## 11\. Novo requisito: resultados bonitos e compartilháveis

**Avaliação:** tecnicamente viável\. É um mecanismo coerente de aquisição por indicação, mas o efeito comercial precisa ser medido; não existe garantia de viralização ou compra\.

Fluxo proposto:

1. A LÚCIDA identifica uma oportunidade e sugere um teste gratuito pertinente\.
2. A pessoa faz o teste e recebe seu resultado completo, com explicação útil\.
3. Pode escolher “Criar meu cartão”, revisar a imagem e a legenda e decidir o que compartilhar\.
4. O cartão convida outras pessoas a fazer o mesmo teste por uma entrada pública\.
5. Cada novo visitante inicia sua própria sessão, recebe seu resultado e pode continuar com a LÚCIDA\.
6. A LÚCIDA indica o próximo passo adequado, inclusive opções gratuitas, amostra, compra ou mentoria\.

- [ ] **LUC\-079** Interpretar a “planilhazinha bonita” como um relatório/cartão visual de resultado; decidir depois se também haverá planilha ou PDF para download\.
- [ ] **LUC\-080** Separar o relatório detalhado privado do cartão público resumido\.
- [ ] **LUC\-081** Criar modelos visuais com a marca Relacione\-se/LÚCIDA, título do teste, uma descoberta compreensível e convite para fazer o teste\.
- [ ] **LUC\-082** Oferecer versões adequadas para publicação e Stories; sugestão inicial: 1080 × 1350 e 1080 × 1920, a validar nos canais de lançamento\.
- [ ] **LUC\-083** Gerar números e gráficos a partir do cálculo real do teste\. A IA pode redigir uma explicação autorizada, sem alterar pontuações ou inventar avaliação\.
- [ ] **LUC\-084** Renderizar texto, pontuação e marca com modelos controlados para assegurar legibilidade e consistência\.
- [ ] **LUC\-085** Usar linguagem não estigmatizante\. Não apresentar um teste de autoconhecimento como diagnóstico ou certificado comportamental\.
- [ ] **LUC\-086** Oferecer prévia e escolha da pessoa antes de compartilhar; não publicar em contas sociais silenciosamente\.
- [ ] **LUC\-087** Não incluir respostas íntimas, histórico, e\-mail, perfil comportamental detalhado ou conteúdo pago por padrão\. Nome de exibição somente se a pessoa escolher\.
- [ ] **LUC\-088** Usar “Perguntei à LÚCIDA…” apenas quando corresponder ao que aconteceu; não fabricar depoimento, fala literal ou experiência\.
- [ ] **LUC\-089** Disponibilizar baixar imagem, copiar legenda, copiar link e compartilhamento nativo quando o dispositivo permitir\.
- [ ] **LUC\-090** Tratar cancelamento e indisponibilidade do compartilhamento sem perda do resultado\. Abrir o menu de compartilhar não prova que o post foi publicado\.
- [ ] **LUC\-091** Apontar o link para o teste público, sem abrir a conta ou o resultado privado de quem compartilhou\.
- [ ] **LUC\-092** Não colocar dados pessoais em códigos de campanha, URLs ou eventos de métricas\.
- [ ] **LUC\-093** Se futuramente houver página pública individual de resultado, exigir escolha explícita e oferecer revogação\. Não torná\-la pública por padrão\.
- [ ] **LUC\-094** Não exigir compartilhamento ou compra para liberar o resultado gratuito\.
- [ ] **LUC\-095** Medir, conforme as escolhas de consentimento aplicáveis, chegadas, início/conclusão do teste, cliques em próximos passos e compras, sem enviar respostas íntimas para métricas\.

Limites de plataforma para orientar o desenho:

- Uma imagem de post não se torna clicável simplesmente por conter um botão desenhado ou URL\. Preparar o caminho adequado a cada plataforma\.
- Para Instagram, prever imagem \+ legenda e convite por link do perfil, QR ou figurinha de link nos Stories quando disponível\. Não prometer links clicáveis universais em qualquer legenda\.
- Para Facebook, preparar uma página pública compartilhável com título, imagem de prévia e destino correto; conferir o fluxo na conta/dispositivo real\.
- O compartilhamento nativo da web depende do navegador, aparelho e apps disponíveis, e deve partir de uma ação da pessoa\. Manter alternativas de download e cópia\.
- APIs nativas de compartilhamento do Instagram não equivalem automaticamente a uma função disponível em qualquer site\. Publicação direta via API é outra integração, sujeita às contas e permissões elegíveis\.

## 12\. Novo requisito: TikTok, voz e participação em lives

**Avaliação:** viável, com mais integração e operação que o cartão de resultado\. Responder em voz, transmitir essa voz à live e receber automaticamente comentários são três capacidades diferentes\.

Arquitetura recomendada:

|Papel        |Responsabilidade proposta                                                                     |
|-------------|----------------------------------------------------------------------------------------------|
|Sol          |Conduzir a live, escolher perguntas e controlar o que vai ao ar                               |
|Jarvis       |Apoiar Sol, organizar perguntas e acionar o atendimento/voz no modo autorizado                |
|LÚCIDA       |Fornecer as respostas públicas com sua identidade e a base aprovada; receber visitantes no app|
|Camada de voz|Captar a fala, gerar áudio, permitir interrupção e encaminhar o som ao destino escolhido      |

O Jarvis pode chamar a mesma LÚCIDA que atende o público\. Isso evita manter duas cópias divergentes de conteúdo\. A memória privada de Sol permanece separada do contexto público usado em live\.

- [ ] **LUC\-096** Escolher entre modo de bastidor, ouvido apenas por Sol, e modo público, ouvido pela audiência; manter destinos de áudio separados e identificados\.
- [ ] **LUC\-097** Criar um contexto de live que consulte apenas material autorizado para divulgação pública, mesmo que Sol possua acesso administrativo a tudo\.
- [ ] **LUC\-098** Ativar a participação explicitamente, com comando/botão de falar, parar, interromper e silenciar; começar com acionamento manual\.
- [ ] **LUC\-099** Planejar respostas curtas, naturais e úteis, compatíveis com o ritmo de uma live\.
- [ ] **LUC\-100** Selecionar serviço de voz de baixa latência, avaliar português, pronúncia dos produtos, custo por uso e qualidade em condições reais\.
- [ ] **LUC\-101** Identificar se Sol usa um celular, dois aparelhos ou computador e testar microfone, saída de áudio, retorno, eco e captura no software de transmissão\.
- [ ] **LUC\-102** Não pressupor que dois apps no mesmo celular consigam usar o microfone e encaminhar áudio simultaneamente do modo necessário\.
- [ ] **LUC\-103** Preparar alternativa em texto, controle de volume e recuperação se houver atraso, queda de rede ou resposta interrompida\.
- [ ] **LUC\-104** Identificar a participação da LÚCIDA como IA\. Não simular uma profissional humana que esteja atendendo em tempo real\.
- [ ] **LUC\-105** Nunca enviar à live conversas privadas de Sol, histórico de clientes ou briefings de mentoria\.
- [ ] **LUC\-106** Confirmar que a conta TikTok pode adicionar link externo à bio\. A ajuda consultada informa 1\.000 seguidores ou conta empresarial registrada, com disponibilidade dependente da conta/região\.
- [ ] **LUC\-107** Direcionar a bio para página pública simples, com “Converse com a LÚCIDA” e testes ligados ao tema da live\.
- [ ] **LUC\-108** Preparar entradas específicas por teste/campanha para reduzir a chance de o visitante se perder na vitrine\.
- [ ] **LUC\-109** Permitir que o novo visitante comece sem acesso à área privada de Sol ou a materiais pagos não adquiridos\.
- [ ] **LUC\-110** Validar tráfego simultâneo, tempo de resposta, limites por sessão, orçamento e comportamento quando houver excesso de demanda\.
- [ ] **LUC\-111** Se for desejada leitura automática do chat da live, verificar integração oficial suportada antes de prometer esse recurso\. Na primeira versão, Sol pode selecionar ou repetir a pergunta\.

## 13\. Sequência recomendada de execução e critérios de aceite

|Etapa              |Entrega                                           |Critério para considerar pronta                                                                 |
|-------------------|--------------------------------------------------|------------------------------------------------------------------------------------------------|
|1. Base            |Manual, catálogo, corpus autorizado e IA por texto|Responde com fontes corretas, reconhece lacunas e não vaza conteúdo/usuários                    |
|2. Acessos         |Identidade, direitos e cobrança definidos         |Compra/assinatura liberam somente a oferta correta; cancelamento não remove compra avulsa válida|
|3. Entrada pública |Vitrine, testes e navegação para visitantes       |Pessoa fora da conta de Sol entra, faz teste, vê resultado e encontra o retorno                 |
|4. Compartilhamento|Cartões, prévia, legenda e link                   |Outra pessoa chega ao teste certo sem receber dados privados; download funciona como alternativa|
|5. Jarvis          |Fluxo versionado de atualização                   |Orientação autorizada vira mudança avaliada e reversível, sem publicar conversa privada         |
|6. Voz controlada  |Ensaio com Sol e modo público/bastidor            |Áudio chega apenas ao destino escolhido; interrupção, mute e falhas são testados                |
|7. Ampliação       |WhatsApp, canais elegíveis e campanhas            |Continuidade de identidade autorizada, canais homologados e custo acompanhado                   |

As etapas podem compartilhar preparação\. Começar com um teste representativo e um cartão permite validar o fluxo antes de multiplicar produtos e formatos\.

Pendências que ainda precisam de definição, sem bloquear o registro do plano:

- Qual teste inaugura o compartilhamento e qual material público fundamenta seu resultado?
- Quais conteúdos entram em cada oferta e quais amostras Sol autoriza?
- Qual limite de conversa gratuita e qual benefício recorrente da assinatura?
- Quais contas de rede social serão usadas e quais recursos estão habilitados nelas?
- Qual é o ambiente atual do Jarvis e como Sol faz suas lives?
- Qual orçamento mensal e quais limites de consumo serão adotados para texto, voz e geração de cartões?
- Quem revisa materiais, ofertas e versões; quais mudanças o Jarvis pode publicar sob autorização permanente?

## 14\. Fontes técnicas consultadas para esta ampliação

Consulta em 25/09/2026\. Revalidar requisitos de plataformas antes de implementar, porque podem mudar\.

- MDN, Navigator\.share: compatibilidade limitada, compartilhamento de texto/URLs/arquivos, destinos dependentes do dispositivo e acionamento pelo usuário\. https://developer\.mozilla\.org/en\-US/docs/Web/API/Navigator/share
- TikTok, links no perfil: critérios de conta para adicionar site\. https://support\.tiktok\.com/en/getting\-started/setting\-up\-your\-profile/linking\-another\-social\-media\-account
- Meta, anúncio oficial de links em Stories: https://about\.fb\.com/ja/news/2021/10/linkaccessstickers/amp/
- Meta, Sharing to Stories: integração específica de plataforma nativa, a verificar para o canal escolhido\. https://developers\.facebook\.com/documentation/instagram\-platform/sharing\-to\-stories
- Google, Live API: demonstra viabilidade de áudio em tempo real com interrupção e transcrição\. É referência técnica, não escolha definitiva de fornecedor\. https://ai\.google\.dev/gemini\-api/docs/live\-api

**Próxima manutenção do documento:** preservar decisões anteriores, registrar alterações de escopo e só marcar tarefas concluídas com implementação e verificação correspondentes\.

## 15 Ficha técnica da LÚCIDA

Esta ficha especifica o sistema desejado\. Campos marcados como proposta ainda precisam ser escolhidos; nomes lógicos de ferramentas e dados não significam APIs já implementadas\.

|Campo                    |Especificação                                                                                                                 |
|-------------------------|------------------------------------------------------------------------------------------------------------------------------|
|Nome e proprietária      |LÚCIDA, do Universo Relacione-se de Sol Lima                                                                                  |
|Missão                   |Orientar, promover reflexão e clareza, ajudar na navegação e na aplicação de conteúdos autorizados                            |
|Público                  |Visitantes, pessoas com conta gratuita, compradores avulsos, assinantes e clientes de mentoria                                |
|Idioma inicial           |Português brasileiro; linguagem simples, natural e ajustável                                                                  |
|Personalidade            |Acolhedora, lúcida, curiosa, direta e respeitosa; sem concordância automática; humor contextual sem ridicularizar sofrimento  |
|Método de conversa       |Entender intenção, responder ou perguntar conforme necessário, esclarecer e oferecer próximo passo pertinente                 |
|Identidade visual        |Olho com raio integrado; cores e estilo já estabelecidos; variações acessíveis de tamanho e contraste                         |
|Administradora           |Sol, operando preferencialmente pelo Jarvis                                                                                   |
|Canais desejados         |App e site; WhatsApp; Instagram/Facebook quando a integração permitir; participação em lives por voz                          |
|Canal excluído nesta fase|Telegram para a LÚCIDA; isso não altera automaticamente o escopo de outros projetos de Sol                                    |
|Conhecimento permanente  |Manual, catálogo, materiais e regras aprovados, versionados e consultáveis                                                    |
|Memória pessoal          |Preferências e continuidade autorizadas, isoladas por pessoa e sujeitas a correção/exclusão                                   |
|Modelo e fornecedor      |A selecionar/homologar. Gemini e a alternativa OpenAI são referências do ecossistema, não uma ativação comprovada nesta LÚCIDA|
|Voz                      |Provedor, voz e pronúncia a homologar; português natural, resposta interrompível e modo de live controlado                    |
|Atualização              |Jarvis transforma orientações autorizadas em mudanças avaliadas, versionadas e reversíveis                                    |
|Limites de atuação       |Não inventar conteúdo, disponibilidade, compras, diagnósticos, pontuações, promessas ou credenciais profissionais             |
|Intervenção humana       |Suporte e encaminhamento a Sol/mentoria conforme disponibilidade, necessidade e autorização                                   |

### 15 1 Arquitetura recomendada

Cada canal chama um serviço de atendimento comum\. Esse serviço identifica a sessão, verifica os direitos, seleciona o contexto autorizado, consulta fontes e ferramentas, gera a resposta e salva somente a memória permitida\. Catálogo e método podem ser compartilhados entre canais; dados pessoais permanecem isolados\.

- [ ] **LUC\-112** Mapear os projetos existentes antes de escolher infraestrutura nova\. O app local usa React/Next com adaptação Vinext, Cloudflare Workers, D1 e referência a R2; não tratá\-lo como um site estático que basta copiar para Vercel\.
- [ ] **LUC\-113** Confirmar serviços realmente provisionados, migrações, variáveis e ambientes\. Binding declarado não comprova armazenamento operacional em produção\.
- [ ] **LUC\-114** Definir onde reside o serviço central da LÚCIDA e como site, app, Jarvis e canais o acessam com autenticação apropriada\.
- [ ] **LUC\-115** Definir responsabilidades de hospedagem, domínio, banco, objetos, busca, filas e tarefas recorrentes; reaproveitar serviços existentes quando adequados\.
- [ ] **LUC\-116** Escolher busca textual, vetorial ou híbrida conforme volume, custo e qualidade medida\. Não obrigar uma migração para outro banco sem necessidade comprovada\.
- [ ] **LUC\-117** Fixar versões de modelo, regras, catálogo e índices por atendimento para rastrear problemas\.
- [ ] **LUC\-118** Manter segredos no servidor, com permissões mínimas e rotação\. Nunca embutir chaves permanentes no navegador ou em documentos públicos\.
- [ ] **LUC\-119** Implementar limites, cancelamento, timeout, repetição segura e mensagem de recuperação; uma falha do modelo não deve bloquear a vitrine e os testes independentes\.
- [ ] **LUC\-120** Definir autenticação própria para visitante/cliente e para Jarvis; a sessão privada de Sol no ChatGPT não serve como login universal dos clientes\.
- [ ] **LUC\-121** Se for escolhida migração para Vercel, incluir substituição/compatibilização de bindings, dados, autenticação, arquivos e publicação\. Tratar migração como projeto específico\.

### 15 2 Documentação permanente necessária

Nomes abaixo são sugestões de artefatos a manter em um módulo privado canônico\. Não foram criados como arquivos operacionais nesta entrega\.

|Documento             |Conteúdo obrigatório                                                      |
|----------------------|--------------------------------------------------------------------------|
|MANUAL_LUCIDA         |Missão, tom, maiêutica, exemplos bons/ruins, limites e encaminhamentos    |
|CATALOGO_PRODUTOS     |Fichas oficiais, versões, disponibilidade, links e recursos incluídos     |
|POLITICA_ACESSOS      |Gratuito, amostras, avulsos, assinatura, etapas e expirações              |
|MAPA_CONHECIMENTO     |Fontes, capítulos, versões, permissões, responsável e índice de busca     |
|CATALOGO_TESTES       |Instrumentos, fórmulas, interpretação, limitações, resultados e indicações|
|MEMORIA_E_IDENTIDADE  |Dados salvos, vinculação entre canais, revisão, exclusão e retenção       |
|CONTRATOS_INTEGRACOES |Ferramentas, eventos, autenticação, erros, limites e ambientes            |
|EXEMPLOS_E_AVALIACOES |Conversas de referência e cenários usados para liberar versões            |
|OPERACAO_E_RECUPERACAO|Monitoramento, custos, incidentes, cópias, retorno de versão e suporte    |
|CONTINUIDADE_LUCIDA   |Estado atual, decisões, tarefas, bloqueios, versões e próxima ação        |

## 16 Inventário do conhecimento a incorporar

A presença de um nome nesta lista significa que deve entrar no inventário\. A versão editorial vigente precisa ser lida e conferida antes de alimentar o atendimento; nomes citados em conversas não substituem os originais aprovados\.

- [ ] **LUC\-122** Identidade profissional pública de Sol: biografia autorizada, posicionamento, método, canais e limites do atendimento\. Não importar automaticamente a memória privada do Jarvis\.
- [ ] **LUC\-123** Trilogia: Morte em Vida, Reposicione\-se e Fuga Identitária, com títulos/subtítulos finais confirmados na versão canônica\.
- [ ] **LUC\-124** Método Reposicione\-se: Árvore do Discernimento, Jaula Aberta, tipos de posicionamento e comandos reflexivos aprovados\.
- [ ] **LUC\-125** Testes de Reposicione\-se: localizar o conjunto central vigente, confirmar os quatro instrumentos e evitar duplicações com versões antigas\. O conjunto inclui referências à Árvore, Posicionamento e Influência Indevida/Autonomia de Pensamento; confirmar a relação completa no material atual\.
- [ ] **LUC\-126** Workbook de Reposicione\-se: localizar a versão integrada ao livro e distinguir exercícios pagos de testes/degustações gratuitos\.
- [ ] **LUC\-127** Magnetus: confirmar a Bíblia e os materiais atuais, Dia 0, Dias 1 a 7, Dia 8, Dias 9 a 15, práticas acumulativas e continuidade\.
- [ ] **LUC\-128** Preservar os gates previstos no produto Magnetus e a classificação específica de cada conteúdo\. Teste gratuito não é liberação automática de toda a jornada\.
- [ ] **LUC\-129** Caderno Vivo, Antídoto Antivalor, Script do Silêncio, cartilhas, Matemática do Perdão e áudios existentes: mapear disponibilidade, autorizações e vínculo com ofertas\.
- [ ] **LUC\-130** Linhas Relacione\-se para homens e para mulheres, testes de presença e outros programas da vitrine: confirmar diferenças reais, sem duplicar conteúdo por suposição\.
- [ ] **LUC\-131** Acervo de estratégias autorais: incorporar apenas fichas revisadas e classificadas como públicas, amostra ou pagas\.
- [ ] **LUC\-132** Conteúdos públicos do YouTube: cadastrar links válidos, tema, resumo aprovado e transcrição quando houver autorização e necessidade\.
- [ ] **LUC\-133** Mentorias: escopo, formatos, duração, preço vigente, agendamento, preparação, entrega e encaminhamento humano\.
- [ ] **LUC\-134** Produtos em desenvolvimento: registrar somente o que pode ser anunciado e a mensagem “Em breve”; não fabricar datas\.
- [ ] **LUC\-135** Perguntas frequentes comerciais e de uso: acesso, pagamento, continuação de leitura, suporte, cancelamento e recuperação de conta\.
- [ ] **LUC\-136** Usar como referências de localização os repositórios indicados: Sollimastudio/universo\-relacione\-se, Magnetus3, trilogia\-sol\-lima, biblia\-magnetus, relacionese\-website e SOL\-IA\. Revalidar origem, branch e versão ao executar\.

### 16 1 Fluxo de entrada e atualização de conteúdos

- [ ] **LUC\-137** Receber arquivo ou referência e gerar um identificador de importação, preservando o original\.
- [ ] **LUC\-138** Calcular hash para reconhecer duplicatas e distinguir uma revisão real de um arquivo renomeado\.
- [ ] **LUC\-139** Extrair texto e estrutura; comparar uma amostra com o original, principalmente tabelas, exercícios, imagens e fórmulas\.
- [ ] **LUC\-140** Separar trechos por unidades de sentido, preservando produto, capítulo, seção e página quando disponíveis\.
- [ ] **LUC\-141** Aplicar a classificação de acesso antes de indexar\. Um documento misto exige separação explícita de trechos públicos e pagos\.
- [ ] **LUC\-142** Revisar amostras e respostas de referência, incluindo perguntas cuja resposta não consta no material\.
- [ ] **LUC\-143** Publicar o índice da versão aprovada de modo controlado e invalidar a busca/cache de material retirado\.
- [ ] **LUC\-144** Guardar histórico de alterações e permitir retorno de versão\. Uma retirada de acesso deve valer também para caches e ferramentas\.
- [ ] **LUC\-145** Registrar materiais ainda ausentes, ilegíveis ou não aprovados; tornar a lacuna visível ao operador e não preenchê\-la com invenção\.

## 17 Fichas de cadastro e dados necessários

Estas são fichas técnicas mínimas propostas\. Campos de identidade, observações e autorizações não devem aparecer em URLs públicas nem em registros de métricas\.

### 17 1 Ficha de cada produto

- [ ] **LUC\-146** Identificador estável, nome oficial, nomes antigos, categoria, público e responsável editorial\.
- [ ] **LUC\-147** Objetivo, temas, resultado esperado sem garantia, indicação e situações em que outro recurso é mais adequado\.
- [ ] **LUC\-148** Formato, duração, módulos/capítulos/dias, idioma, pré\-requisitos e sequência sugerida\.
- [ ] **LUC\-149** Conteúdos incluídos, bônus, dependências e o que não integra a oferta\.
- [ ] **LUC\-150** Estado: rascunho, em preparação, disponível, suspenso ou arquivado; data de revisão\.
- [ ] **LUC\-151** Ficha pública, amostras aprovadas, acervo integral e respectiva versão/fonte\.
- [ ] **LUC\-152** Oferta, SKU, moeda, preço confirmado, parcelamento e validade; consultar o cadastro vigente ao recomendar, sem congelar preços no prompt\.
- [ ] **LUC\-153** Tipo e prazo de acesso, gates, assinatura que inclui o item e regras de manutenção de compras avulsas\.
- [ ] **LUC\-154** URL da apresentação, checkout, acesso, suporte e retorno ao app, com última verificação e alternativa em caso de falha\.
- [ ] **LUC\-155** Perguntas frequentes, objeções respondidas com honestidade, produtos relacionados e próximo passo gratuito\.

### 17 2 Ficha de cada teste

- [ ] **LUC\-156** Identificador, título, autoria, versão, propósito, público, tempo estimado e natureza de autoconhecimento ou instrumento formal\.
- [ ] **LUC\-157** Base metodológica, limitações e direitos de uso/licenciamento quando aplicáveis\.
- [ ] **LUC\-158** Perguntas, respostas possíveis, regras de preenchimento, pesos e eventuais itens invertidos\.
- [ ] **LUC\-159** Fórmula determinística, tratamento de empates, respostas faltantes e casos de borda, com exemplos calculados e revisados\.
- [ ] **LUC\-160** Faixas e textos de interpretação aprovados, evitando diagnóstico e falsas certezas\.
- [ ] **LUC\-161** Recomendações por resultado, com justificativa e opções gratuitas; pontuação não deve ser ajustada para favorecer uma venda\.
- [ ] **LUC\-162** Dados necessários para responder, dados opcionais para salvar e informações excluídas do compartilhamento\.
- [ ] **LUC\-163** Relatório privado, modelo de cartão público, legenda, link para o teste e texto alternativo\.
- [ ] **LUC\-164** Política para refazer o teste e comparação entre versões; não comparar pontuações incompatíveis como se fossem iguais\.
- [ ] **LUC\-165** Evidência de revisão por Sol e validação técnica antes da oferta pública\.

### 17 3 Ficha de cada fonte e trecho

- [ ] **LUC\-166** Identificadores de fonte/trecho, título, autoria, origem autorizada, hash e versão\.
- [ ] **LUC\-167** Produto, capítulo, seção, página ou marca temporal; limites de recorte e texto integral do trecho\.
- [ ] **LUC\-168** Temas e relações úteis, preservando o significado original e a atribuição\.
- [ ] **LUC\-169** Classificação público/amostra/pago/interno, recurso exigido e eventual gate\.
- [ ] **LUC\-170** Estado editorial, aprovador, datas de aprovação/revisão e trecho que esta versão substitui\.
- [ ] **LUC\-171** Limite de citação/uso da amostra, política de retirada e referências de teste de resposta\.

### 17 4 Ficha de pessoa e perfil de comunicação

- [ ] **LUC\-172** Identificador interno, canais vinculados de forma verificada e preferências de contato\.
- [ ] **LUC\-173** Objetivo declarado, produtos com acesso, testes feitos, progresso e dúvida em aberto\.
- [ ] **LUC\-174** Preferências confirmadas de formato, ritmo, nível de detalhe e exemplos\.
- [ ] **LUC\-175** Observações com fonte, contexto e data; distinguir preferência, tendência, emoção momentânea e hipótese\.
- [ ] **LUC\-176** Permissões para memória, continuidade entre canais e compartilhamento com Sol, separadas das métricas e do marketing\.
- [ ] **LUC\-177** Resumo de continuidade mínimo, última revisão, prazo de retenção e correções solicitadas\.
- [ ] **LUC\-178** Campos que a pessoa pode visualizar, corrigir e excluir; explicar eventual retenção necessária de registros comerciais conforme a política validada\.

### 17 5 Ficha de atendimento e encaminhamento

- [ ] **LUC\-179** Identificador da sessão, canal, intenção, contexto autorizado, versões de regras/modelo/fontes e estado do atendimento\.
- [ ] **LUC\-180** Ações realmente executadas, status de ferramenta, falhas e alternativa oferecida; intenção de executar não é execução concluída\.
- [ ] **LUC\-181** Resumo aprovado para mentoria, destinatário, autorização, objetivos e proposta de pauta para revisão de Sol\.
- [ ] **LUC\-182** Agendamento e pagamento com estado verificado, sem inventar horário disponível\.
- [ ] **LUC\-183** Motivo de encerramento ou transferência e próximo passo visível ao usuário\.

### 17 6 Ficha de mudança feita pelo Jarvis

- [ ] **LUC\-184** Identificador da mudança, origem da instrução, escopo autorizado e materiais afetados\.
- [ ] **LUC\-185** Diferença entre versão anterior e proposta, justificativa e conflitos identificados\.
- [ ] **LUC\-186** Avaliações executadas, resultado, responsável, ambiente e critérios de publicação\.
- [ ] **LUC\-187** Versão publicada, horário, registro de auditoria e procedimento para desfazer\.
- [ ] **LUC\-188** Pendências e falhas reportadas a Sol em linguagem simples, sem afirmar que uma atualização ocorreu antes da confirmação\.

## 18 Ferramentas e contratos de integração

Capacidades lógicas propostas para o serviço central\. A implementação pode reaproveitar rotas existentes, desde que preserve esses limites\.

|Ferramenta              |Entrada essencial             |Resultado e limite                                                         |
|------------------------|------------------------------|---------------------------------------------------------------------------|
|Consultar catálogo      |Intenção e filtros            |Fichas oficiais com estado e links atuais                                  |
|Consultar direitos      |Identidade verificada         |Recursos autorizados no servidor; nunca aceitar direitos enviados pelo chat|
|Buscar conhecimento     |Pergunta e escopo autorizado  |Trechos aprovados com fonte e versão                                       |
|Orientar navegação      |Rota e tarefa atual           |Destinos válidos e retorno; URLs validadas                                 |
|Iniciar e concluir teste|Teste, versão e respostas     |Resultado calculado pelas regras do teste                                  |
|Gerar cartão            |Resultado e campos escolhidos |Imagem/legenda e link público para o teste                                 |
|Ler ou atualizar memória|Titular e autorização         |Preferências/resumo permitidos, com revisão                                |
|Abrir oferta            |Produto e oferta vigente      |Destino real do checkout; não confirma compra                              |
|Consultar compra        |Identidade e evento confirmado|Situação comercial e direitos correspondentes                              |
|Preparar mentoria       |Objetivo e resumo autorizado  |Briefing para revisão e opções de agenda verificadas                       |
|Transferir atendimento  |Motivo e canal                |Encaminhamento rastreável a pessoa responsável                             |
|Atualizar LÚCIDA        |Instrução autorizada do Jarvis|Mudança testada, versionada e publicada no escopo permitido                |

- [ ] **LUC\-189** Padronizar entrada, saída, validação, erros e autorização de cada ferramenta\.
- [ ] **LUC\-190** Usar identificadores de requisição/evento e deduplicação para não duplicar cobrança, cadastro, postagem ou publicação em tentativas repetidas\.
- [ ] **LUC\-191** Validar assinatura/autenticidade e prazo de eventos externos conforme cada provedor\.
- [ ] **LUC\-192** Tratar eventos fora de ordem, filas pendentes, falhas permanentes e reprocessamento seguro\.
- [ ] **LUC\-193** Validar destinos permitidos para navegação, arquivos e integrações; conteúdo recuperado não pode ordenar execução de ferramentas privilegiadas\.
- [ ] **LUC\-194** Registrar falhas e versões com o mínimo de dados pessoais; não copiar relatos íntimos em logs de infraestrutura\.
- [ ] **LUC\-195** Separar ambientes de desenvolvimento, homologação e produção, com dados de teste e credenciais próprios\.
- [ ] **LUC\-196** Verificar permissões em cada chamada, inclusive quando a resposta veio de cache e após revogação de acesso\.
- [ ] **LUC\-197** Habilitar revisão e interrupção operacional por Sol/Jarvis autorizado; não depender de alterar código para silenciar a voz ou suspender uma oferta incorreta\.

## 19 Matriz de acesso e exemplos de comportamento

|Recurso                    |Visitante             |Conta gratuita             |Comprador                  |Assinante                  |
|---------------------------|----------------------|---------------------------|---------------------------|---------------------------|
|Vitrine e páginas públicas |Sim                   |Sim                        |Sim                        |Sim                        |
|Testes e resultado gratuito|Sim                   |Sim                        |Sim                        |Sim                        |
|Amostras aprovadas         |Sim                   |Sim                        |Sim                        |Sim                        |
|Histórico entre aparelhos  |Não por padrão        |Com identificação e escolha|Com identificação e escolha|Com identificação e escolha|
|Conteúdo pago integral     |Não                   |Não                        |Itens adquiridos           |Itens incluídos e ativos   |
|Ajuda no material pago     |Apenas amostra pública|Apenas amostra pública     |Conforme produto           |Conforme plano             |
|Voz para todos             |A definir             |A definir                  |Conforme oferta            |Conforme oferta            |
|Mentoria pessoal com Sol   |Oferta separada       |Oferta separada            |Conforme compra            |Inclusão ainda a definir   |

Os limites de uso da IA ainda precisam de definição comercial\. Eles não tornam o resultado do teste pago\. Um administrador em modo de transmissão pública também deve receber apenas o contexto autorizado para divulgação\.

Exemplos a incorporar às avaliações:

- Visitante pede um capítulo pago: a LÚCIDA explica o tema com a ficha pública, oferece a amostra autorizada e indica o caminho de acesso, sem reconstruir o capítulo\.
- Comprador pede ajuda: o sistema verifica a compra e a etapa liberada antes de recuperar o exercício e orientar sua aplicação\.
- Assinatura expira: acessos do plano são revistos; compras avulsas válidas continuam disponíveis\.
- Pessoa quer resposta direta: a LÚCIDA responde e oferece aprofundamento, sem impor uma sequência de perguntas reflexivas\.
- Pessoa muda a preferência: “Hoje quero algo curto” prevalece sobre uma hipótese antiga de que ela gosta de explicações longas\.
- Pessoa pede Sol: a LÚCIDA mostra a oferta/encaminhamento existente e prepara resumo apenas com autorização\.
- Pergunta sem fonte: a LÚCIDA reconhece a lacuna e oferece um caminho de esclarecimento, sem citar um capítulo inexistente\.

## 20 Estudo de viabilidade consolidado

As classificações de complexidade são avaliações de engenharia para planejamento, não orçamentos fechados ou prazos\. O esforço depende do estado real dos repositórios, do conteúdo aprovado, dos acessos às contas e do tráfego\.

|Capacidade                                 |Viabilidade e complexidade              |Dependência principal                         |
|-------------------------------------------|----------------------------------------|----------------------------------------------|
|Guia contextual e retorno                  |Viável, menor; base já existe           |Preservar navegação e validar dispositivos    |
|Ícone de olho com raio                     |Viável, menor                           |Desenho, acessibilidade e revisão visual      |
|Testes gratuitos                           |Viável, média                           |Instrumentos, cálculo e textos revisados      |
|Cartão e legenda de resultado              |Viável, média                           |Resultado confiável e modelos de imagem       |
|Atendimento com acervo                     |Viável, média a alta                    |Fontes aprovadas, recuperação e avaliação     |
|Proteção do material pago                  |Viável, alta                            |Direitos verificados antes da recuperação     |
|Memória e perfil revisável                 |Viável, alta                            |Identidade, autorizações e isolamento         |
|Assinatura                                 |Viável tecnicamente; oferta em definição|Benefício recorrente, custo e cobrança        |
|Jarvis atualiza a LÚCIDA                   |Viável, alta                            |Interface interna, testes e versionamento     |
|Preparação para mentoria                   |Viável, média                           |Resumo autorizado e revisão de Sol            |
|WhatsApp                                   |Viável sob condições da plataforma, alta|Conta/API, regras atuais e atendimento humano |
|Instagram e Facebook                       |Condicional, alta                       |Conta elegível, permissões e APIs disponíveis |
|Personagem nativo no AI Studio             |Não usar como base deste plano          |Alteração oficial de disponibilidade em 2026  |
|Voz para Sol em live                       |Viável, alta                            |Áudio em tempo real e transmissão testada     |
|Leitura automática do chat TikTok          |Ainda não demonstrada                   |Integração suportada para a conta e ferramenta|
|Viralização ou conversão garantida         |Não pode ser garantida                  |Experimentos com público e dados reais        |
|Diagnóstico certo de personalidade por chat|Não sustenta promessa de certeza        |Preferências observáveis e revisão humana     |

### 20 1 Personalização com fundamento

É razoável adaptar explicações ao pedido e ao comportamento observado, perguntando se o formato ajudou\. Isso não valida inferir um tipo psicológico fixo com poucas mensagens\. Uma meta\-análise de 2024 encontrou benefícios pequenos e inconsistentes de combinar ensino a estilos de aprendizagem e não recomendou adoção ampla; por isso, áudio/visual entram como preferências flexíveis &#91;F6&#93;\. DISC deve ter instrumento, escopo e limitações próprios, sem transformar a conversa em certificação automática\.

### 20 2 Plataformas e canais

O compartilhamento web permite enviar arquivos, texto e URLs quando suportado; destinos e combinações aceitas variam\. É necessário acionamento da pessoa e alternativa de download/cópia &#91;F1&#93;\. No Instagram, planejar o caminho de acesso de acordo com o formato: Stories com link quando disponível, perfil ou QR; imagem não garante clique &#91;F3&#93;\.

A ajuda do TikTok consultada informa critérios para adicionar site ao perfil, incluindo mil seguidores ou conta empresarial registrada\. A conta real deve ser conferida antes da campanha &#91;F2&#93;\. Serviço de áudio em tempo real é tecnicamente disponível; isso não comprova roteamento de som no equipamento de Sol, leitura de comentários ou resposta sem atraso &#91;F5&#93;\.

No WhatsApp, homologar atendimento e vendas conforme a conta e os termos vigentes\. A política prevê janela de atendimento e modelos aprovados em situações específicas &#91;F7&#93;\. Os termos consultados incluem condições para provedores de IA, exceções territoriais e limites sobre uso dos dados de conversas para treinamento; o enquadramento do serviço deve ser validado antes de ativar o canal &#91;F8&#93;\. Não presumir que ter uma API permite qualquer automação\.

O anúncio oficial do AI Studio foi atualizado em 10/08/2026 para informar que novas personagens e a edição de existentes deixariam de estar disponíveis, mantendo conversas/personagens existentes ativas\. Por isso, a LÚCIDA própria deve ter seu serviço central e integrações elegíveis, sem depender da criação de um personagem nessa interface &#91;F9&#93;\.

### 20 3 Viabilidade econômica e capacidade

Separar investimento inicial de manutenção recorrente\. Sem medir uso e consultar as tarifas do fornecedor escolhido, não há base para prometer um preço mensal fechado\.

- [ ] **LUC\-198** Estimar visitantes, testes concluídos, conversas, mensagens por conversa, assinantes ativos e picos provocados por live\.
- [ ] **LUC\-199** Medir consumo real por atendimento: texto de entrada/saída, busca, armazenamento, duração de voz e geração de cartão\.
- [ ] **LUC\-200** Levantar custos fixos: hospedagem, domínio, banco, objetos, monitoramento, manutenção e suporte\.
- [ ] **LUC\-201** Levantar custos variáveis: IA de texto, voz, mensageria, pagamentos e imagens, usando tarifas atuais na data da decisão\.
- [ ] **LUC\-202** Simular cenário inicial, usual e de pico, com limites e alertas de orçamento\.
- [ ] **LUC\-203** Definir quotas transparentes por modalidade e alternativa ao atingir limite; manter vitrine e resultados gratuitos úteis\.
- [ ] **LUC\-204** Preferir modelos visuais reutilizáveis para cartões quando bastarem, evitando gerar uma ilustração nova e cara para cada resultado\.
- [ ] **LUC\-205** Definir separadamente voz usada por Sol em lives e eventual voz para todos os visitantes\.
- [ ] **LUC\-206** Apurar margem com receitas confirmadas menos taxas, custos de atendimento e operação; clique em checkout não é venda\.
- [ ] **LUC\-207** Revisar os limites após uso real, sem alterar retroativamente o que foi prometido nas ofertas\.

Modelo de cálculo: custo mensal estimado = custos fixos \+ conversas × custo médio por conversa \+ minutos de voz × tarifa aplicável \+ mensagens cobradas pelos canais \+ cartões/arquivos \+ suporte/manutenção\. Receitas, taxas e impostos entram na avaliação comercial correspondente; os valores permanecem por definir\.

## 21 Checklist de homologação e provas de funcionamento

Cada item abaixo deve gerar um registro com data, ambiente, versão, cenário, resultado esperado, resultado obtido e evidência\. Reutilizar provas válidas e repetir verificações quando a mudança afetar o comportamento correspondente\.

### 21 1 Conteúdo e atendimento

- [ ] **LUC\-208** Responder perguntas de referência sobre cada produto disponível, citando a fonte correta\.
- [ ] **LUC\-209** Reconhecer perguntas sem resposta no acervo e conflitos de versão\.
- [ ] **LUC\-210** Distinguir conteúdo público, amostra e integral pago em perguntas diretas e indiretas\.
- [ ] **LUC\-211** Testar extração de capítulos por partes e instruções maliciosas embutidas em documentos, links ou mensagens\.
- [ ] **LUC\-212** Variar a conversa de acordo com preferências explícitas, sem alterar fatos, regras ou pontuações\.
- [ ] **LUC\-213** Testar ajuda direta, reflexão maiêutica, recusa de compra, pedido de humano e situação delicada que exija acolhimento e encaminhamento apropriado\.
- [ ] **LUC\-214** Confirmar que a LÚCIDA não oferece repetidamente produtos já comprados nem uma mentoria sem agenda/oferta real\.

### 21 2 Identidade e acesso

- [ ] **LUC\-215** Verificar separadamente visitante, conta gratuita, comprador, assinante, assinatura expirada, acesso revogado e administrador\.
- [ ] **LUC\-216** Comprovar isolamento entre duas pessoas, incluindo memória, histórico, resultado, arquivos, links e caches\.
- [ ] **LUC\-217** Testar troca de conta em abas abertas e impedir salvamento no titular errado\.
- [ ] **LUC\-218** Confirmar que dados enviados pelo navegador não conseguem inventar um direito de acesso\.
- [ ] **LUC\-219** Testar vinculação entre canais, recuperação de conta e desvinculação\.
- [ ] **LUC\-220** Verificar visualização/correção/exclusão de memória conforme a política definida\.

### 21 3 Comércio e operação

- [ ] **LUC\-221** Homologar pagamento confirmado, pendente, recusado, cancelado, renovado, expirado e reembolsado\.
- [ ] **LUC\-222** Repetir e reordenar eventos para comprovar deduplicação e consistência de direitos\.
- [ ] **LUC\-223** Verificar que cancelamento de assinatura preserva compras avulsas válidas\.
- [ ] **LUC\-224** Confirmar funcionamento do suporte quando a compra não se vincular automaticamente à conta\.
- [ ] **LUC\-225** Testar falha de IA, busca, banco, canal e rede, com mensagem correta e possibilidade de retomar\.
- [ ] **LUC\-226** Verificar restauração de backup e retorno de versão com dados de homologação\.

### 21 4 Interface e compartilhamento

- [ ] **LUC\-227** Verificar botões, estados “Em breve”, retorno, mapa, biblioteca, site institucional e atalhos de contexto\.
- [ ] **LUC\-228** Abrir/fechar a ajuda durante teste e leitura, preservando a atividade correspondente\.
- [ ] **LUC\-229** Conferir ícone/convite com consentimento de métricas, teclado do celular, menus e diferentes tamanhos de tela\.
- [ ] **LUC\-230** Testar teclado, foco, leitor de tela, contraste, tamanho do texto, movimento reduzido e rótulos dos controles\.
- [ ] **LUC\-231** Validar os cálculos de cada teste com casos conhecidos, inclusive empates e respostas faltantes\.
- [ ] **LUC\-232** Conferir cada cartão: números, texto, corte de imagem, nome opcional e ausência de informação privada\.
- [ ] **LUC\-233** Testar compartilhamento, cancelamento, download e cópia nos aparelhos usados pelo público\.
- [ ] **LUC\-234** Abrir o link compartilhado em outro aparelho/conta e confirmar que começa o teste certo sem mostrar o resultado privado original\.
- [ ] **LUC\-235** Verificar que recusar métricas não impede navegação ou resultado e que eventos não carregam respostas pessoais\.

### 21 5 Jarvis e voz

- [ ] **LUC\-236** Comprovar que uma ordem autorizada a Jarvis gera mudança rastreável e testada na LÚCIDA\.
- [ ] **LUC\-237** Comprovar que ideia ambígua ou conversa privada não vira regra pública automaticamente\.
- [ ] **LUC\-238** Executar mudança de teste, conferir a versão ativa e reverter com sucesso\.
- [ ] **LUC\-239** Ensaiar uma live com microfone, interrupção, mute, eco, atraso e queda de conexão\.
- [ ] **LUC\-240** Comprovar separação entre áudio de bastidor e áudio transmitido\.
- [ ] **LUC\-241** Confirmar que modo público não recupera conteúdo administrativo, memória privada ou briefing de cliente\.
- [ ] **LUC\-242** Medir pico simultâneo e custos antes de campanha maior; fila ou limite devem ter explicação útil\.

## 22 Prioridades e responsabilidades propostas

Papéis representam responsabilidades necessárias, não contratação de equipe\. O Jarvis pode assumir operações autorizadas quando suas ferramentas estiverem funcionando; não substitui a validação editorial do método de Sol\.

|Prioridade  |Entrega                                    |Responsável proposto       |Dependências                         |
|------------|-------------------------------------------|---------------------------|-------------------------------------|
|P0          |Estado canônico dos projetos e continuidade|Engenharia com Jarvis      |Acesso e versão remota conferidos    |
|P0          |Manual, fichas e amostras aprovadas        |Sol/editorial com Jarvis   |Materiais oficiais                   |
|P0          |IA por texto com permissões                |Engenharia                 |Provedor, fontes e avaliações        |
|P0          |Entrada pública controlada                 |Engenharia/design          |Identidade e isolamento              |
|P0 comercial|Oferta, pagamento e direitos               |Sol/comercial e engenharia |Oferta definida e provedor habilitado|
|P1          |Perfil revisável e memória                 |Engenharia/editorial       |Identidade e autorizações            |
|P1          |Teste completo e cartão                    |Editorial/design/engenharia|Cálculo e textos aprovados           |
|P1          |Jarvis como operador de atualizações       |Engenharia                 |Serviço interno e testes             |
|P1          |Mentoria com resumo autorizado             |Sol/engenharia             |Oferta, agenda e autorizações        |
|P2          |Ensaio de voz em live                      |Engenharia e Sol           |Serviço de voz e equipamentos        |
|P2          |WhatsApp e redes elegíveis                 |Engenharia/operação        |Conta, termos e permissões           |
|Contínua    |Qualidade, custos, suporte e atualização   |Sol/Jarvis/operação        |Métricas e revisões                  |

Complementos de lançamento:

- [ ] **LUC\-243** Definir a primeira experiência pública completa e quais produtos podem ser vendidos na primeira abertura\.
- [ ] **LUC\-244** Definir domínio público, caminhos de entrada e links institucionais\. Conferir domínio/registro/DNS/SSL sem confundir hospedagem HostGator desativada com expiração do domínio\.
- [ ] **LUC\-245** Decidir se o app permanece na infraestrutura atual, usa entrada pública separada ou migra, com plano explícito de dados e continuidade\.
- [ ] **LUC\-246** Confirmar termos da oferta, privacidade, uso dos dados e contatos de suporte com revisão adequada antes de divulgação ampla\.
- [ ] **LUC\-247** Definir público etário atendido e tratamento de situações fora do escopo; não coletar mais dados só para personalizar uma venda\.
- [ ] **LUC\-248** Definir métricas de sucesso: conclusão de teste, resolução, utilidade, retorno voluntário e compras confirmadas, com limitações de atribuição claras\.
- [ ] **LUC\-249** Confirmar materiais pendentes, responsável por cada um e critério de aceite, sem anunciar data que não foi definida\.
- [ ] **LUC\-250** Registrar separadamente tema e momento dos lembretes desejados por Sol\. As falas anteriores “me lembre” não definiram aqui um agendamento executável\.
- [ ] **LUC\-251** Fazer homologação privada do fluxo completo antes de abrir os recursos correspondentes ao público\.

## 23 Evidências e limites do que já existe

Inspeção de 25/09/2026\. Este inventário distingue estado da hospedagem, presença no código e provas históricas de execução\. Não corresponde a uma nova compra real ou a um teste completo de produção\.

|Evidência                          |O que confirma                                                                               |O que ainda não confirma                                       |
|-----------------------------------|---------------------------------------------------------------------------------------------|---------------------------------------------------------------|
|Sites consultado nesta revisão     |App ativo, publicação 14, acesso customizado para um usuário, nenhum visitante externo       |Atendimento por IA ou jornada comercial pública                |
|Checkout local Git                 |Commit 7fa1819c93945d3e5354553598af1526cd642583, sem alterações de código antes desta revisão|Igualdade com qualquer alteração remota posterior não comparada|
|components/site/lucida-float.tsx   |Ajuda contextual, continuar na página, voltar, início, mapa, biblioteca e link institucional |Resposta inteligente do modelo                                 |
|lib/lucida-navigation.ts           |Textos e destinos de orientação conforme a rota                                              |Compreensão livre da pergunta do visitante                     |
|lucida-float.css e consentimento   |Espaçamento para o aviso e ocultação do convite enquanto o aviso aparece                     |Ausência de sobreposição em todo aparelho possível             |
|lib/surfaces.ts                    |Link institucional para https://relacionese-website.vercel.app                               |Disponibilidade contínua de todos os destinos externos         |
|components/site/lucida.tsx         |Reflexão de perguntas fixas e interface de salvamento no Caderno                             |Análise personalizada por IA                                   |
|app/api/lucida/route.ts            |Rota retorna 503 de IA ainda não ativa                                                       |Provedor conversacional operacional                            |
|lib/platform/lucida-context.ts     |Filtro de fontes aprovadas/autorizadas; memória desativada; runtime não pronto               |Busca semântica e memória em uso pelo modelo                   |
|app/api/integracoes/kiwify/route.ts|Rota retorna 503 e não concede acesso                                                        |Compra, renovação e reembolso homologados                      |
|app/api/integracoes/jarvis/route.ts|Leitura de catálogo/eventos; publish, sendMessages e readPersonalNotes desabilitados         |Treinamento, publicação ou mensagens automáticas pelo Jarvis   |
|Prova local Magnetus de 24/09      |17 verificações registradas como aprovadas, sem erros, em conta sintética e Chromium         |Produção, Safari real, cobrança ou IA                          |

A prova local Magnetus inclui vitrine, painéis, teclado, ausência de overflow, salvamento/reabertura, retenção de rascunho em falha, navegação nas etapas, conclusão, Caderno e leitura\. Ela se refere ao escopo implementado daquela homologação; não declara todos os dias/produtos prontos\.

Arquivo da prova: `docs/evidencias/magnetus-20260924/browser-results.json`\. Contratos existentes: `docs/CONTRATOS-INTEGRACAO.md`\. As referências antigas a Telegram e a projetos Jarvis precisam ser reconciliadas com as decisões atuais, não adotadas automaticamente\.

Endereços registrados:

- App restrito: https://relacione\-se\-universo\.sollimalovecoach\.chatgpt\.site
- Site institucional: https://relacionese\-website\.vercel\.app/
- Referência indicada para Jarvis: repositório Sollimastudio/SOL\-IA, a revalidar na execução\.

## 24 Continuidade e registro de execução

- [ ] **LUC\-252** Incorporar a versão aprovada deste checklist ao módulo canônico de documentação, preservando seu histórico\.
- [ ] **LUC\-253** Manter tarefas com ID, estado, responsável, dependências, evidência, data e versão entregue\.
- [ ] **LUC\-254** Ao retomar, ler continuidade, mudanças posteriores e instruções do repositório antes de editar\.
- [ ] **LUC\-255** Atualizar o registro após cada entrega; não remover requisito apenas porque não cabe na etapa atual\.
- [ ] **LUC\-256** Separar correção de defeito, mudança editorial, novo requisito e decisão comercial\.
- [ ] **LUC\-257** Preservar versões anteriores e registrar o motivo de substituição de uma regra ou material\.
- [ ] **LUC\-258** Confirmar sucesso de publicação, evento e gravação antes de informar conclusão a Sol\.
- [ ] **LUC\-259** Manter os materiais privados e preservar o público atual enquanto se prepara a entrada pública correspondente\.

Estado sugerido por tarefa: a definir, pendente, em execução, bloqueada, em homologação ou concluída com evidência\. A decisão de implementar esta ficha não significa que todos os recursos devam ser lançados ao mesmo tempo\.

Modelo de registro de execução:

|Campo              |Preenchimento                                    |
|-------------------|-------------------------------------------------|
|ID                 |Identificador LUC da tarefa                      |
|Responsável        |Pessoa ou processo autorizado                    |
|Estado             |Um dos estados definidos acima                   |
|Dependências       |Tarefas, conteúdo e conta necessários            |
|Critério de aceite |Comportamento observável que deve funcionar      |
|Evidência          |Teste, captura, log reduzido ou evento confirmado|
|Versão e ambiente  |Commit/versão e local, homologação ou produção   |
|Data e próxima ação|Última alteração e passo restante                |

## 25 Referências complementares de viabilidade

Fontes primárias consultadas em 25/09/2026\. Requisitos de plataformas devem ser revalidados na implantação\. As escolhas de arquitetura e os níveis de complexidade são propostas de engenharia deste documento\.

- F1 — MDN, Navigator\.share\. https://developer\.mozilla\.org/en\-US/docs/Web/API/Navigator/share
- F2 — TikTok, Linking another social media account\. https://support\.tiktok\.com/en/getting\-started/setting\-up\-your\-profile/linking\-another\-social\-media\-account
- F3 — Meta, link stickers em Stories\. https://about\.fb\.com/ja/news/2021/10/linkaccessstickers/amp/
- F4 — Meta, Sharing to Stories\. https://developers\.facebook\.com/documentation/instagram\-platform/sharing\-to\-stories
- F5 — Google, Gemini Live API overview\. https://ai\.google\.dev/gemini\-api/docs/live\-api
- F6 — Clinton\-Lisell e Litzinger, 2024, Is it really a neuromyth A meta\-analysis of the learning styles matching hypothesis\. https://pubmed\.ncbi\.nlm\.nih\.gov/39055994/
- F7 — WhatsApp Business Messaging Policy\. https://whatsappbusiness\.com/policy/
- F8 — WhatsApp Business Solution Terms, versão indicada de 06/03/2026\. https://www\.whatsapp\.com/legal/business\-solution\-terms
- F9 — Meta, Create Your Own Custom AI With AI Studio, atualização de 10/08/2026\. https://about\.fb\.com/news/2024/07/create\-your\-own\-custom\-ai\-with\-ai\-studio/amp/

**Histórico desta versão:** preservação do registro inicial; ampliação da ficha técnica; inventário de conhecimentos; fichas de produto, teste, fonte, pessoa, atendimento e mudança; contratos de ferramentas; matriz de acesso; viabilidade técnica, econômica e de canais; homologação, prioridades e evidências\. Nenhuma funcionalidade foi ativada por esta atualização documental\.

<!-- FIM_CHECKLIST_ORIGINAL -->

---

## Anexo B — método original integral

<!-- INICIO_METODO_ORIGINAL -->

# Direção e execução do desenvolvimento da LÚCIDA

Você assume a direção técnica do desenvolvimento da LÚCIDA, assistente do Universo Relacione\-se de Sol Lima\. Atue com responsabilidade de engenharia de software, arquitetura de IA, experiência do usuário e qualidade\. Sol é leiga: resolva escolhas técnicas com justificativas objetivas e conduza o trabalho até entregas funcionais verificadas\.

Execute o projeto existente a partir do estado atual\. Preserve conteúdo, identidade visual, dados, direitos e funções aprovadas\. Uma nova função deve se integrar ao que existe\. Não substitua o sistema por uma demonstração simplificada\.

## 1 Fonte de verdade e escopo completo

Leia integralmente o arquivo **LUCIDA\_CHECKLIST\_MESTRE\_2026\-09\-25\.md**, versão 2 ou atualização posterior confirmada\. A versão 2 contém **259 tarefas, LUC\-001 a LUC\-259, em 25 blocos**\. O arquivo **LUCIDA\_CHECKLIST\_COMPLETO\_V2\.docx** é a apresentação editável da mesma especificação\.

Use o checklist completo como fonte de requisitos, incluindo decisões, fichas técnicas, estudo de viabilidade, dependências, evidências e critérios de aceite\. Este prompt define o método de execução; ele não reduz o escopo do checklist\. Quando houver uma instrução posterior explícita de Sol, registre a mudança e sua origem, preservando o histórico da decisão anterior\.

Se o checklist não estiver anexado, procure\-o nas fontes autorizadas disponíveis\. Se não conseguir acessá\-lo, peça somente esse arquivo\. Não reconstrua as 259 tarefas por suposição\. Enquanto isso, pode inspecionar o estado existente sem alterar o escopo\.

Leia também as instruções aplicáveis dos repositórios e os documentos de continuidade e integração existentes\. Reutilize seus registros antes de criar documentos concorrentes\. Se as versões das fontes divergirem, identifique a versão vigente; não escolha silenciosamente um documento antigo\.

Referências para localizar o trabalho, a revalidar:

- App Sites: `appgprj_6ab11d2e84188191a90910ec6b06c64d`, em `https://relacione-se-universo.sollimalovecoach.chatgpt.site`\. Use o repositório associado a esse projeto; não presuma que seja o mesmo do site institucional\.
- Site institucional: `https://relacionese-website.vercel.app/`, referência de repositório `Sollimastudio/relacionese-website`\.
- Jarvis: referência atual indicada `Sollimastudio/SOL-IA`\. Referências antigas a outros projetos precisam ser reconciliadas\.
- Conteúdo e integrações: `Sollimastudio/universo-relacione-se`, `Sollimastudio/Magnetus3`, `Sollimastudio/trilogia-sol-lima` e `Sollimastudio/biblia-magnetus`\.

Em 25/09/2026, a inspeção registrada encontrou o app ativo e restrito, guia contextual existente, conversa por IA e pagamento automático desativados no código e conector Jarvis de leitura\. Esses são registros históricos para conferência, não prova do estado atual\. O checklist também contém evidências locais que não devem ser apresentadas como testes atuais de produção\.

## 2 Primeiro trabalho obrigatório

Comece pelas ferramentas disponíveis: leia o checklist, localize os projetos, confira o código atual e reconcilie o que existe com as tarefas\. Não encerre a primeira etapa entregando apenas outro plano\.

Antes da primeira edição:

1. Confirme projeto, repositório, branch, commit, publicação vigente, ambiente, público e alterações posteriores à documentação\.
2. Identifique alterações locais, branches e PRs de outros trabalhos\. Preserve\-as\. Não execute reset destrutivo, descarte, limpeza abrangente, force\-push ou substituição de árvore para facilitar sua tarefa\.
3. Use branch ou worktree isolada quando apropriado, partindo da base correta\. Registre diferenças entre a base publicada e alterações ainda não publicadas\.
4. Levante rotas, componentes, contratos de API, autenticação, dados, armazenamento, direitos de acesso, integrações e verificações existentes\.
5. Identifique quais funções estão comprovadamente operacionais, quais existem apenas no código, quais falham e quais não foram verificadas\. Registre defeitos preexistentes separadamente\.
6. Selecione a primeira entrega funcional possível com as dependências disponíveis e inicie sua implementação após essa conferência\.

Não recrie contas, repositórios, bancos ou serviços que já existem\. Não migre o app para Vercel só porque o site institucional está lá\. Confirme a infraestrutura real e preserve\-a, salvo necessidade técnica demonstrada ou decisão autorizada\.

## 3 Memória de trabalho que não depende do chat

Estabeleça um conjunto enxuto de registros no repositório canônico\. Reutilize os equivalentes existentes ou crie:

- **CONTINUIDADE\_LUCIDA\.md:** estado atual, versões, decisões, bloqueios e próxima ação exata\.
- **EXECUCAO\_LUCIDA:** tabela ou arquivo estruturado contendo todos os IDs LUC, estado, prioridade, dependências, responsável, implementação, evidência e versão entregue\.
- **FUNCOES\_APROVADAS\_LUCIDA\.md:** comportamentos e contratos que devem continuar funcionando, com referências de código e provas\.
- **DECISOES\_LUCIDA\.md:** escolhas técnicas/comerciais, origem, justificativa e eventuais substituições\.

Conserve o checklist integral como referência\. Não troque requisitos detalhados por um resumo\. Cada uma das 259 tarefas iniciais deve ter destino rastreável: pendente, em execução, bloqueada, em homologação ou concluída com evidência\. Uma decisão ainda aberta deve estar identificada\. Não exclua itens por dificuldade; registre qualquer alteração explícita de escopo com justificativa\.

Mantenha os IDs existentes estáveis\. Acrescente novos requisitos sem renumerar os antigos\. Verifique a cobertura do registro para que nenhuma tarefa desapareça durante reorganizações\.

Leia a especificação completa na primeira preparação\. Depois, trabalhe com um contexto focado: continuidade, funções protegidas, tarefas do lote, código afetado e fontes relevantes\. Consulte o restante quando necessário; não releia todos os livros e repositórios a cada pequeno ajuste\.

Ao concluir um lote ou antes de trocar de contexto, registre o que mudou, o que foi testado, arquivos/commits, estado de publicação, pendências e a próxima ação\. Na retomada, confira os arquivos e o estado remoto antes de continuar\. Não afirme trabalho em segundo plano se nenhum processo estiver realmente ativo\.

## 4 Proteção contra regressões

Trate como patrimônio do projeto os comportamentos aprovados: navegação, retorno, ajuda contextual, links, testes, respostas em andamento, Caderno, leitura, progresso, autenticação, permissões, gates, consentimento de métricas e identidade visual, conforme a evidência disponível\.

- Faça alterações localizadas e revise o diff completo antes de integrar\. Preserve mudanças concorrentes\.
- Evite reescritas amplas, refatorações oportunistas, atualizações gerais de dependências, renomeações e mudanças de estilos globais fora da necessidade da tarefa\.
- Se precisar alterar uma função existente, documente seu comportamento esperado e os impactos antes da mudança; valide os consumidores afetados depois\.
- Preserve contratos de rotas, APIs e dados ou faça uma transição compatível\. Migrações devem proteger registros existentes e ter estratégia de recuperação adequada\.
- Compare as telas afetadas com referências aprovadas\. Melhorar a LÚCIDA não autoriza redesenhar toda a vitrine\.
- Use controles de ativação quando ajudarem a manter uma função incompleta fora do fluxo normal\. Não desative funcionalidades aprovadas para fazer uma nova passar\.
- Não apague testes, enfraqueça verificações ou exponha dados/acessos para contornar falhas\. Diferencie um teste obsoleto de uma regressão demonstrável\.
- Se introduzir uma regressão, corrija\-a ou reverta somente a sua alteração de maneira segura\. Preserve trabalhos de outras pessoas e não considere esse lote concluído\.

## 5 Ciclo obrigatório de cada lote

Um lote deve ter **um objetivo funcional coerente**, pequeno o suficiente para revisão e recuperação\. Pode atender vários IDs relacionados\. Não abra várias frentes dependentes sem concluir seus pontos de integração\.

Para cada lote:

1. **Defina:** IDs atendidos, resultado esperado, dependências, áreas afetadas e funções que precisam permanecer intactas\.
2. **Prepare:** confirme a versão de partida, registre o estado necessário e escolha uma estratégia proporcional de recuperação\.
3. **Implemente:** faça a menor mudança completa que atenda ao objetivo e aos cenários de erro relevantes\.
4. **Verifique:** execute as verificações exigidas pelo projeto e os testes proporcionais ao risco\. Cubra a função nova, os fluxos antigos afetados e as permissões envolvidas\. Registre comandos, ambiente e resultados\.
5. **Revise:** confira o diff, a experiência do usuário, fontes, acesso, mensagens de erro e ausência de alterações alheias ao objetivo\.
6. **Integre:** salve uma versão rastreável pelo fluxo autorizado do projeto\. Ao publicar, confira o commit efetivamente publicado, o resultado do deploy e o comportamento no ambiente de destino\.
7. **Registre e prossiga:** atualize continuidade e tarefas; avance ao próximo lote disponível sem pedir “posso continuar?” a cada etapa\.

Verificação deve comprovar comportamento real\. Build concluído não prova compra; botão não prova integração; retorno HTTP não prova conteúdo correto; simulação não prova produção\. Use dados sintéticos nas verificações apropriadas e declare seus limites\. Não repita toda a suíte sem necessidade, mas cumpra os gates obrigatórios e amplie testes quando houver risco concreto não resolvido\.

## 6 Ordem de execução orientada por dependências

Transforme as fases abaixo em lotes associados aos IDs do checklist\. Aproveite o que já estiver pronto e verificado\. Antecipe fundações necessárias a outras fases sem antecipar sua ativação pública\.

**Marco 0 — Continuidade e base protegida:** conferir projetos, registrar funcionalidades aprovadas, cobrir o checklist e estabelecer recuperação e ambiente de homologação\.

**Marco 1 — LÚCIDA por texto:** manual de personalidade e maiêutica, catálogo aprovado, processamento de fontes, busca autorizada, provedor conectado, respostas com referências e tratamento de falhas\. Entregar um atendimento completo com conteúdo real autorizado, inicialmente no escopo que possa ser validado\.

**Marco 2 — Identidade e comércio:** sessões de visitante/cliente, vinculação verificada, direitos de compras e planos, amostras, gates, pagamento e seus eventos\. Preservar compras avulsas quando a assinatura terminar\. Não inventar ofertas ou benefícios ainda não decididos\.

**Marco 3 — Experiência e aquisição:** entrada para visitantes, navegação contextual, olho com raio, “Em breve”, teste gratuito com cálculo correto, relatório privado, cartão compartilhável e link para outra pessoa fazer o teste\. Preparar a abertura pública preservando áreas privadas e respeitando a autorização aplicável\.

**Marco 4 — Continuidade pessoal e mentoria:** memória autorizada, preferências revisáveis, recomendações pertinentes, encaminhamento humano e resumo para Sol com autorização da pessoa\.

**Marco 5 — Jarvis operador:** transformar orientações de Sol em mudanças avaliadas, versionadas e reversíveis na LÚCIDA\. Integrar com o Jarvis atual, preservando sua memória privada\. Não confundir conector de leitura com capacidade de atualizar o sistema\.

**Marco 6 — Canais e voz:** homologar WhatsApp e redes elegíveis; voz natural com interrupção; ensaio com Sol; separação de bastidor e transmissão pública; avaliação de picos e custos\. Validar integrações suportadas antes de prometer leitura automática de comentários\.

**Marco 7 — Operação:** fluxo completo, monitoramento, suporte, orçamento, recuperação, documentação e manutenção\. Considerar concluído somente o escopo efetivamente validado; manter bloqueios visíveis\.

## 7 Regras do produto que devem sobreviver a toda alteração

- A LÚCIDA promove clareza, adapta a conversa e pode confrontar respeitosamente\. Não inventa conteúdo nem concorda automaticamente para agradar\.
- Testes e resultados são gratuitos\. Compartilhar, comprar ou fornecer contato de marketing não é condição para ver o resultado gratuito\.
- Visitantes recebem fichas públicas e degustações aprovadas\. A autorização do conteúdo pago é aplicada no servidor antes da busca e das ferramentas, inclusive em caches\.
- Preferências de comunicação são revisáveis\. Não produza diagnóstico clínico ou pontuação DISC supostamente validada a partir de conversa informal\.
- Recomendações devem considerar necessidade, acesso já adquirido e recusas, sem explorar sofrimento nem fabricar urgência\.
- Um cartão público só contém o que a pessoa escolheu compartilhar\. O link leva ao teste, preservando sua conta e seu resultado privado\.
- Conhecimento editorial pode ser comum; memórias pessoais, briefings de clientes e conversas privadas de Sol permanecem separados\.
- Jarvis é a central de Sol; LÚCIDA atende o público\. Ideia, desabafo ou pesquisa externa não vira regra publicada automaticamente\.
- Preserve todos os produtos e fontes previstos no checklist, inclusive itens futuros como “Em breve”\. Telegram permanece fora desta fase da LÚCIDA\.
- Não presuma que regras antigas das plataformas continuam válidas\. Consulte documentação oficial quando uma integração depender delas\.

## 8 Autonomia e bloqueios reais

Resolva decisões técnicas reversíveis dentro do escopo autorizado\. Use contas, conectores e configurações existentes quando disponíveis; não peça a Sol que repita informações já acessíveis\. Não exponha segredos nem peça chaves em mensagens públicas\.

Respeite aprovações e controles do ambiente\. Não altere instruções, permissões ou autenticação para contorná\-los\. Preserve o público atual; tornar uma área privada acessível a outras pessoas exige autorização correspondente\. Contratações, cobranças, publicação de mensagens em redes e alterações comerciais não decorrem automaticamente de uma tarefa de programação\.

Quando faltar credencial, material aprovado, decisão comercial, acesso ou permissão, registre: dependência exata, tarefas afetadas, tentativas realizadas e menor ação necessária de Sol\. Continue o trabalho independente que estiver autorizado\. Não substitua uma integração bloqueada por respostas fictícias apresentadas como reais\.

Prepare uma solução concreta e revisável antes de pedir uma decisão\. Não transfira a Sol escolhas técnicas rotineiras\. Se uma ação exigir nova aprovação, explique qual ação e por quê; não peça novamente o que já está autorizado\.

## 9 Comunicação e conclusão verificável

Fale em português simples\. Durante o trabalho, comunique brevemente o que está sendo resolvido, o que foi descoberto e o próximo passo\. Evite promessas de perfeição, percentuais sem base e conclusões antecipadas\.

Ao entregar um marco ou atingir um bloqueio real, informe:

- O que Sol já pode usar e onde acessar\.
- IDs concluídos, evidência, versão e ambiente de validação\.
- Comportamentos anteriores afetados que foram conferidos\.
- O que continua pendente/bloqueado e a razão concreta\.
- Onde a continuidade foi salva e qual é a próxima ação\.

Não declare o projeto inteiro pronto porque um marco terminou\. Não encerre com oferta de executar depois o trabalho já autorizado\. Se o limite da sessão impedir avanço, deixe o estado salvo de forma retomável, sem prometer atividade futura inexistente\.

**Comece agora pela conferência das fontes e da base atual\. Em seguida, implemente o primeiro lote viável\. Conduza os lotes seguintes conforme as dependências, preservando todas as tarefas e o que já funciona\.kk**

<!-- FIM_METODO_ORIGINAL -->