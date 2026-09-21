# Prompt mestre — evolução do app Relacione-se

Versão 1 · 21/09/2026. Preparado a pedido de Sol Lima. Esta entrega cria o prompt; não executa as alterações descritas.

Atue como arquiteto de software e responsável sênior por produto, UX, acessibilidade, integrações e qualidade. Assuma a evolução profissional do app/site RELACIONE-SE, de Sol Lima, seguindo as orientações abaixo.

OBJETIVO

Consolidar o Relacione-se como a casa de todo o ecossistema: vitrine pública, experiências gratuitas selecionadas, produtos avulsos, combos, biblioteca pessoal, jornadas interativas e assistência contextual da LÚCIDA. O usuário deve entender por onde começar, encontrar o que adquiriu e continuar de onde parou. Sol deve conseguir administrar a operação pelo Jarvis.

Execute o trabalho autorizado em etapas verificáveis. Aproveite conteúdo e código existentes, preserve a autoria e mantenha a experiência elegante, legível e simples.

1. AUDITORIA INICIAL E FONTES

Leia as instruções aplicáveis dos projetos e examine o estado atual antes de editar. As referências centrais são:
- https://github.com/Sollimastudio/universo-relacione-se
- https://github.com/Sollimastudio/Magnetus3
- https://github.com/Sollimastudio/biblia-magnetus
- https://github.com/Sollimastudio/trilogia-sol-lima

Em universo-relacione-se, leia os documentos de 09-app:
- DIRETRIZES-APROVADAS-ACESSOS-E-NAVEGACAO-2026-09-21.md
- PARECER-PROFISSIONAL-NAVEGACAO-TELEGRAM-2026-09-21.md
- LINKS-E-PAPEIS-JARVIS-LUCIDA-2026-09-21.md
- ENTREGA-VITRINE-SITES-2026-09-21.md
- RELATORIO-MESTRE-APP-UNIVERSO-RELACIONE-SE-PROTOTIPO-MANUS-v1.md

Localize a fonte da vitrine Sites pelo relatório de entrega. Referência de publicação: https://relacione-se-universo.sollimalovecoach.chatgpt.site

O estado documentado em 21/09/2026 era: vitrine privada, catálogo, Caderno e analytics básicos em Sites; runtime especializado Magnetus3 com parte de login, permissões, progresso, gate e LÚCIDA, ainda com homologações pendentes. As bases estavam separadas. Revalide esse estado; documentação e código existente não provam operação em produção.

Inspecione os pequenos aplicativos relevantes e classifique cada recurso como produto, componente, brinde, ferramenta interna ou legado. Há testes de presença, Teste da Árvore, Mapa da Suspeita, Dor de Cotovelo, Script do Silêncio e páginas de MINDSETmagro. Verifique funcionamento, conteúdo, versão, links e possibilidade de reaproveitamento. Não publique um protótipo como produto pronto.

2. ARQUITETURA E IDENTIDADE

Defina uma autoridade única para conta, compras, permissões e progresso. Compare a vitrine Sites e o runtime Magnetus3 e registre a escolha técnica com suas consequências.

Entregue uma experiência de conta e biblioteca unificadas, ainda que existam serviços especializados. Preserve dados, versões e contratos existentes. Planeje migração com backup e reversão quando necessária. Não apresente um iframe de outro site como integração de identidade ou progresso.

Separe conteúdo, produto, oferta e direito de acesso. Use identificadores estáveis e um catálogo administrável. O mesmo conteúdo pode aparecer em várias ofertas sem ser duplicado.

3. PRODUTOS E REGRAS COMERCIAIS

O Magnetus3 contempla homens e mulheres e reúne ebook interativo com workbook, Antídoto do Antivalor e acesso à LÚCIDA. Preserve esse combo e permita ofertas avulsas de seus componentes. A orientação mais recente permite venda separada; textos antigos que afirmam exclusividade do combo precisam ser conciliados com essa decisão.

A trilogia deve admitir coleção e livros individuais: Morte em Vida, Reposicione-se e Fuga Identitária. Preserve os títulos/subtítulos editoriais vigentes nas fontes autorizadas.

MINDSETmagro deve entrar no mesmo modelo, com protocolo e bônus próprios. Script do Silêncio, áudios, testes e ferramentas também devem admitir relações claras com produtos.

Suporte gratuito, avulso, combo, bônus, acesso por dias/meses e assinatura com catálogo definido. Bônus é uma condição da oferta: o mesmo conteúdo pode ter oferta individual.

Versione a composição das ofertas. Preserve o que cada cliente contratou. Não invente preços, duração, desconto, acesso vitalício ou conteúdo ainda inexistente. Pré-requisitos precisam ser explícitos; a compra individual deve entregar o que promete.

Some os direitos válidos: a expiração de uma assinatura não remove uma compra independente. Mostre prazo, componentes incluídos e conteúdo já adquirido. Separe validade comercial de liberação pedagógica; preserve os gates aprovados do Magnetus, inclusive a regra de 24 horas.

Valide pagamentos e acessos no servidor. Trate eventos duplicados, atrasados e fora de ordem, renovação, reembolso e cancelamento conforme o contrato. Um link de checkout ou página de agradecimento não comprova pagamento.

4. NAVEGAÇÃO E CONTINUIDADE

Organize três experiências:
- Visitante: apresentação clara, “Comece por aqui”, seleção gratuita e catálogo público.
- Comprador: oferta compreensível, checkout e retorno ao acesso adquirido.
- Cliente: “Continuar de onde parei”, atividade atual, biblioteca, favoritos e validade.

Mantenha menu enxuto e catálogo pesquisável por objetivo, tema, formato e nome. Mostre detalhes progressivamente. Identifique gratuito, adquirido, incluído, disponível para compra e em preparação.

Referências curtas devem abrir em painel contextual acessível, preservando foco e posição. Mudanças de capítulo ou atividade devem manter respostas e permitir retorno ao ponto exato. Outro produto pode oferecer prévia e “Salvar para depois”.

Identifique destinos externos, salve a atividade antes da saída e recupere a rota após retorno ou login. Respeite o botão Voltar. Não use novas abas indiscriminadamente como estratégia de retenção.

Não interrompa leitura, exercício ou checkout com convites para redes sociais e ofertas. Quem sabe o que quer comprar não precisa passar por um quiz.

5. LEITURA, PRÁTICA E ÁUDIO

Implemente leitor com capítulos, marcadores, posição salva, fonte ajustável e tema confortável. Preserve a experiência literária dos livros.

Workbook e Caderno Vivo devem compartilhar respostas persistidas, com estado de salvamento claro, isolamento entre contas e recuperação entre dispositivos. Não dependa apenas de armazenamento local. Defina o tratamento das anotações pessoais após expiração de acesso, sem apagamento silencioso.

Player: áudio, transcrição, velocidade, favoritos e retomada. Use arquivos autorizados e diferencie acervo gratuito de pago.

Integre o cronômetro do Script do Silêncio apenas após verificar comportamento, autoria, permissão de acesso e retorno. Preserve a proposta pedagógica aprovada.

Não prometa bloqueio absoluto de screenshots. Proteja conteúdo por autenticação e autorização; diferencie cards destinados ao compartilhamento de materiais privados.

6. LÚCIDA E JARVIS

LÚCIDA é a assistente dos clientes em todo o ecossistema. Deve conhecer produto, capítulo/dia, objetivo e contexto permitido, ajudar a compreender e aplicar, localizar recursos e orientar a continuidade.

Priorize material gratuito ou já adquirido quando adequado. Sugestões comerciais devem ser opcionais, pertinentes e explicadas. Respeite recusa e situações de vulnerabilidade; a recomendação pode ser apenas continuar a prática atual.

Use fontes autorais aprovadas, controle de acesso e memória consentida, revisável e removível. Não exponha conteúdo protegido de outros produtos. Identifique indisponibilidade da IA com honestidade. Valide respostas, custo e limites de uso antes de prometer assistência ilimitada.

Jarvis é a central interna usada por Sol. Deve consultar o mesmo catálogo, verificar links e estados, identificar inconsistências, preparar distribuição por canais, coordenar tarefas autorizadas e acompanhar desempenho.

Prepare contratos de integração e eventos para o Jarvis existente. Evite criar outro Jarvis ou exigir um segundo assistente/cadastro do cliente. Separe catálogo compartilhado de memória pessoal: indicadores comerciais não devem carregar conversas ou respostas íntimas.

7. LINKS E TELEGRAM

Preserve estes endereços e revalide antes de usar:
- Pack de áudios: https://pay.kiwify.com.br/ZecEQ9d
- Script do Silêncio: https://pay.kiwify.com.br/YVJ3Lke
- Cronômetro Canva: https://variedadesuteis.my.canva.site/script-silencio
- Convite Telegram: https://t.me/+C-ZEhFeueW40ZWFh
- Endereço equivalente consultado: https://telegram.me/+C-ZEhFeueW40ZWFh

Na checagem registrada, os dois checkouts responderam com os títulos dos respectivos produtos. Isso não homologou pagamento nem entrega. O Canva respondeu com “Untitled App”; seu cronômetro não foi testado. O atalho https://canva.link/convite-canal-link retornou 404: não o use como destino validado.

A prévia do convite identifica “Minutos Magnetus.” e descreve o pack de áudios. Falta definir se o canal é gratuito, entrega paga ou mistura de ambos. Não divulgue esse convite como brinde enquanto essa classificação não estiver resolvida. Prepare a configuração e prossiga com as partes independentes.

Se houver canal gratuito aprovado, use-o como acompanhamento opcional, com conteúdo útil e retornos específicos ao app. Preserve a distinção do pack pago. Comprar ou utilizar o app não deve exigir adesão ao canal.

O código Canva-domain-verify registrado é infraestrutura de domínio, não conteúdo de navegação. Não o exiba aos clientes.

8. IDENTIDADE VISUAL, ACESSIBILIDADE E DESEMPENHO

Preserve a direção de autoridade, elegância e luxo discreto: grafite/preto, creme, dourado contido e acentos coerentes com cada produto. Aproveite referências autorais e assets aprovados. O Cajueiro de Pirangi é a referência quando se representar a origem do método.

Priorize hierarquia, tipografia confortável, imagens otimizadas e movimentos discretos. Evite excesso de blocos, efeitos e texto pequeno.

Meta de acessibilidade: WCAG 2.2 AA, com avaliação automatizada e manual. Inclua teclado, foco, semântica, contraste, ampliação/refluxo, leitores de tela, transcrições, redução de movimento, ajuda consistente e autenticação acessível.

Teste celular, tablet e desktop; especialmente Safari/iPhone, Android, rede lenta, troca de aplicativo e texto ampliado. Não chame teste de largura de tela de homologação completa em aparelho real.

Meça carregamento, resposta e estabilidade com ferramentas atuais. Use as metas documentadas de Web Vitals, revalidando a referência vigente. Diferencie resultado de laboratório de dados reais de uso.

9. OPERAÇÃO E ANALYTICS

Crie administração protegida para conteúdos, versões, capítulos, arquivos, ofertas, combos, bônus e prazos. Inclua rascunho, revisão, publicação e histórico. Sol deve conseguir expandir o catálogo sem reconstruir o app.

Centralize nomes oficiais e links, com destino esperado, última verificação e estado. Ofereça suporte e recuperação de conta/compra.

Meça descoberta, consumo, primeira atividade, retomada, conversão confirmada, renovação, reembolso e custos. Defina eventos, origem e deduplicação. Exclua cadernos, conversas, respostas íntimas e dados pessoais de URLs e eventos de marketing.

Avalie Telegram por retorno e margem, considerando taxas, mídia, IA e suporte. Não confunda clique, visualização, inscrito e compra. Reconheça limites de atribuição entre aplicativos. Não invente indicadores ou conclusões de rentabilidade.

Considere instalação na tela inicial, notificações opcionais e automações editoriais após a base funcionar. Mini Apps do Telegram exigem avaliação própria; não os transforme em dependência inicial.

10. EXECUÇÃO, TESTES E ENTREGA

Quando autorizado a executar este prompt, trabalhe autonomamente nas mudanças reversíveis e prepare uma versão de revisão. Não solicite confirmação para cada detalhe técnico. Respeite autorizações vigentes para publicação, gastos, cobrança, alteração de DNS e envio de mensagens; este documento, sozinho, não autoriza essas ações.

Sequência:
A. Inventário e decisão de integração.
B. Conta, catálogo, ofertas e direitos de acesso.
C. Fluxo completo de um produto existente: entrada, acesso, prática, Caderno e retomada.
D. Biblioteca, leitor, áudio, LÚCIDA e administração.
E. Brindes, canais e analytics.
F. Expansão de produtos e integração operacional com Jarvis.

Não preencha lacunas com aulas, depoimentos, preços ou resultados inventados. Mantenha conteúdo em preparação claramente identificado. Se faltar credencial ou decisão comercial, descreva a dependência e conclua o restante autorizado.

Verifique pelo menos:
- visitante encontra e entende uma oferta;
- pagamento confirmado concede somente os acessos corretos;
- combo e avulso coexistem sem duplicação;
- expiração não remove outro direito válido;
- alteração de URL não permite acesso indevido;
- respostas de um cliente não aparecem para outro;
- referência, saída externa e novo login preservam retomada;
- LÚCIDA respeita fontes, acesso e consentimento;
- cancelamento, renovação e reembolso refletem as regras;
- controles e fluxos principais funcionam com teclado e no celular;
- novo conteúdo e nova oferta podem ser administrados sem alteração de código.

Entregue alterações concretas, testes relevantes, documentação atualizada e link de revisão quando disponível. Informe o que funciona, o que foi efetivamente testado, o que depende de integração e o que falta para produção. Registre repositório, versão, migrações e reversão quando aplicáveis.

Comece verificando o estado real, escolha a integração com base nas evidências e avance nas etapas autorizadas. A entrega deve permitir conhecer, comprar, acessar, usar e retornar com clareza, preservando a autoria de Sol Lima.
