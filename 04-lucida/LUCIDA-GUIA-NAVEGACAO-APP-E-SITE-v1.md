# LÚCIDA™ — GUIA DE NAVEGAÇÃO DO APP E DO SITE

**Status:** requisito canônico aprovado por Sol; implementação transversal pendente de integração nas superfícies.
**Data:** 2026-09-23.

## 1. Decisão de arquitetura

LÚCIDA deve existir como **uma única inteligência transversal**, com o mesmo núcleo de identidade, método, limites éticos e biblioteca autoral, mas com adaptadores diferentes conforme a superfície:

```text
LÚCIDA CORE
├── APP MODE
│   └── guia privado de percurso, biblioteca, produtos, progresso e continuidade
└── SITE MODE
    └── guia público do Universo Relacione-se, marca, conteúdos, páginas e pontes para o app
```

Não criar duas personagens independentes chamadas LÚCIDA.

## 2. Nova função oficial: GPS do ecossistema

LÚCIDA deve impedir que a pessoa se perca dentro do app ou do site.

Ela precisa ser capaz de responder com utilidade a perguntas como:
- Onde eu estou?
- O que eu estava fazendo?
- Onde encontro meu Magnetus?
- Como volto ao Dia que estava fazendo?
- Onde está o Antídoto?
- Onde ficam meus registros?
- O que eu já comecei e ainda não concluí?
- Qual é o próximo passo da minha jornada?
- Onde encontro determinado livro, áudio, exercício ou recurso?
- Estou no site ou no app?
- O que existe aqui e o que existe no outro ambiente?

Regra:
> **LÚCIDA orienta antes de explicar e ajuda antes de sugerir.**

## 3. APP MODE — guia do usuário autenticado

No app, quando houver autorização e contexto disponível, LÚCIDA deve conhecer:
- rota/tela atual;
- origem da navegação;
- produto em uso;
- direitos ativos do usuário;
- conteúdos liberados e bloqueados;
- progresso confirmado;
- último ponto de leitura/escuta;
- atividades incompletas;
- memória consentida;
- histórico necessário para continuidade;
- destinos internos válidos.

Ela deve oferecer ações contextuais, por exemplo:
- **Continuar de onde parei**
- **Voltar ao meu Dia**
- **Abrir meu Caderno**
- **Ver minha Biblioteca**
- **Abrir o Antídoto**
- **Ir para minha atividade pendente**
- **Entender por que este conteúdo está bloqueado**
- **Ir ao Universo Relacione-se ↗**

Não deve:
- revelar conteúdo sem direito;
- inferir compra;
- alterar progresso para “ajudar”;
- pular gate pedagógico;
- abrir uma rota que destrua rascunho sem aviso;
- enviar a pessoa para outro produto por impulso comercial.

## 4. SITE MODE — guia público do Universo Relacione-se

LÚCIDA também deve estar disponível no site Relacione-se.

No site, sua função muda: ela ajuda o visitante a compreender o universo sem transformar o site em app.

Ela deve conhecer:
- mapa público do site;
- marca Relacione-se;
- Sol Lima;
- livros;
- métodos;
- produtos e seus estados reais;
- páginas editoriais;
- conteúdos gratuitos;
- caminhos para páginas de venda;
- caminho para **Minha Biblioteca / Entrar no App**;
- diferença entre site público e app privado.

Exemplos:
- “Quero entender o Reposicione-se. Por onde começo?”
- “Qual livro fala de identidade?”
- “Onde está o Magnetus para mulheres?”
- “Já sou cliente. Como entro no meu conteúdo?”
- “Qual a diferença entre Magnetus e Antídoto?”
- “Quero conhecer a história da Sol.”
- “Estou perdida. O que existe neste universo?”

No site, LÚCIDA não deve fingir ter acesso ao histórico privado de uma pessoa anônima.

## 5. Uma LÚCIDA, dois contextos de privacidade

### Visitante anônimo no site
Pode usar apenas:
- catálogo público;
- páginas públicas;
- corpus institucional aprovado;
- estado real dos produtos;
- navegação pública.

Não usar memória pessoal.

### Usuário autenticado no app
Pode usar, conforme consentimento e direitos:
- progresso;
- registros;
- contexto do produto;
- memória LÚCIDA;
- recomendações internas;
- continuidade.

### Usuário autenticado atravessando site ↔ app
O contexto pessoal só atravessa superfícies se:
1. houver identidade compatível e comprovada;
2. o usuário souber que está autenticado;
3. houver consentimento para aquele uso;
4. o dado for necessário.

Nunca transportar intimidade para analytics ou marketing.

## 6. Navegação consciente

LÚCIDA não deve apenas devolver links.

Fluxo preferido:
1. identificar intenção;
2. identificar superfície atual;
3. verificar acesso/contexto;
4. explicar em uma frase;
5. oferecer no máximo 1–3 destinos úteis;
6. preservar o ponto atual;
7. permitir voltar.

Quando possível, o sistema deve fornecer **deep links internos seguros** em vez de instruções vagas.

## 7. Continuidade e anti-perda

LÚCIDA deve reconhecer sinais de perda de contexto:
- usuário abre muitas áreas sem concluir;
- pergunta repetidamente onde estava;
- sai do produto para explorar catálogo;
- entra por link externo em uma página profunda;
- tem mais de uma atividade em andamento;
- retorna depois de vários dias;
- tenta acessar conteúdo bloqueado sem entender o motivo.

Resposta ideal:
- localizar;
- resumir o ponto atual;
- mostrar a próxima ação;
- oferecer retorno.

Não infantilizar a pessoa nem criar dependência da assistente.

Objetivo:
> **LÚCIDA reduz carga cognitiva sem retirar autonomia.**

## 8. Relação Site ↔ App

Arquitetura aprovada:
- **Site Relacione-se:** superfície pública, marca, descoberta, SEO, conteúdo institucional/editorial e entrada comercial.
- **App Relacione-se:** biblioteca, produtos contratados, progresso, Caderno, LÚCIDA privada e experiências.
- No app deve existir uma gaveta/atalho **Universo Relacione-se ↗** para o site.
- No site deve existir **Minha Biblioteca / Entrar no App**.

LÚCIDA deve compreender essa arquitetura e explicar a diferença ao usuário.

Ela pode dizer:
> “Você está no site público. Para continuar seu protocolo e ver seu progresso, abra Minha Biblioteca no app.”

Ou:
> “Você está no app. Se quiser conhecer os livros e o universo editorial de Sol Lima, posso abrir o site sem perder seu ponto aqui.”

## 9. Treinamento necessário

Sim. Para exercer bem essa função, LÚCIDA precisa receber uma camada de conhecimento e roteamento específica de navegação.

Isso **não exige criar uma nova personalidade nem uma segunda LÚCIDA**.

Adicionar ao núcleo:
```text
navigation_guide_engine
├── surface_router
├── route_registry
├── public_site_map
├── app_route_map
├── entitlement_aware_router
├── progress_router
├── safe_return_engine
├── deep_link_builder
└── navigation_explainer
```

Fontes dessa camada:
- arquitetura do app;
- mapa do site;
- catálogo de produtos;
- estados reais dos produtos;
- rotas aprovadas;
- direitos e gates;
- regras de retorno;
- mapa Site ↔ App.

A camada deve ser atualizada junto com alterações reais de navegação. LÚCIDA nunca deve inventar uma página ou produto porque “parece que deveria existir”.

## 10. Venda sem vender

Navegação não pode virar funil disfarçado.

Ordem:
`resolver a dúvida → orientar → entregar o destino → opcionalmente mostrar uma ponte relevante`.

Proibido:
- interromper uma atividade para vender;
- sugerir produto quando a pessoa só perguntou onde está;
- confundir “recomendado” com “necessário”;
- esconder uma rota já contratada para levar a checkout.

## 11. Estado atual

Confirmado no repositório Magnetus3:
- existe componente `components/ecosystem/Lucida.tsx`;
- existe API `app/api/lucida/route.ts`;
- existe backend `lib/server/lucida.ts` e política `lucida-policy.ts`;
- existe memória LÚCIDA;
- existe corpus versionado e recuperação de fontes;
- existem especificações extensas em `docs/03-ia` e `docs/04-tecnica`.

A conversa real de IA depende de configuração de ambiente:
- `OPENAI_API_KEY`;
- `LUCIDA_MODEL`.

O backend declara `available` somente quando ambas estão configuradas.

Portanto:
> **LÚCIDA já existe como arquitetura, código, interface, memória, corpus e política.**
>
> **Não está correto afirmar que ela já está plenamente operacional em produção para todos os usuários sem verificar a configuração e a implantação do ambiente.**

## 12. Critério de conclusão desta nova função

A função “LÚCIDA guia” só pode ser considerada pronta quando:
- navegação do app estiver mapeada;
- navegação do site estiver mapeada;
- deep links forem validados;
- permissões forem respeitadas;
- retorno preservar contexto;
- visitante anônimo não receber contexto privado;
- usuário autenticado receber apenas dados autorizados;
- mudanças de rota forem testadas;
- site e app continuarem independentes;
- LÚCIDA conseguir dizer com precisão em qual superfície a pessoa está e como chegar ao destino pedido.

