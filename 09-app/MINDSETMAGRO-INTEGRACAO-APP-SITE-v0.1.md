# MINDSETmagro™ — Integração App/Site v0.1

**Data:** 2026-09-30.  
**Status:** especificação; sem publicação automática.

## 1. Topologia verificada

### Repositório canônico de integração
`Sollimastudio/universo-relacione-se`

Função: mapa-mestre, governança, fontes, produto, pesquisa, arquitetura e especificações do app/site.

### Site público
`Sollimastudio/relacionese-website`

Estado verificado:
- existe rota `/mindset-magro`;
- a página atual apresenta MINDSETmagro como conceito transversal em desenvolvimento;
- ainda não descreve o novo protocolo de 30 dias completo;
- `programs.ts` ainda não lista MINDSETmagro entre programas/ferramentas.

### App privado
Fonte operacional atual está no projeto Sites interno e **não é este repositório GitHub**.

Logo:
- universo-relacione-se = fonte canônica documental;
- relacionese-website = código do site;
- Sites interno = código do app privado;
- Magnetus3 = referência operacional madura para motor de conteúdo.

## 2. Decisão técnica

MINDSETmagro deve **reutilizar a infraestrutura conceitual do Magnetus3**, mas não copiar sua jornada.

### Reutilizar
- ContentBlocks;
- Caderno Vivo;
- fonte única;
- progression gate;
- entitlement;
- source-lock;
- LÚCIDA bridge;
- privacidade/memória separadas;
- analytics sem respostas brutas;
- renderer App + PDF + workbook.

### Criar
- product_id `mindsetmagro_30d`;
- 30 dias;
- seis travessias;
- tipos de bloco específicos de Sala de Controle/MMI/saúde/ritual;
- manutenção 30/60/90;
- biblioteca visual própria.

## 3. Arquitetura de entrega

```text
UNIVERSO RELACIONE-SE (cânone)
│
├─ MINDSETmagro source package
│  ├─ manifest
│  ├─ day-01 ... day-30
│  ├─ source-lock
│  ├─ evidence-map
│  └─ visual-assets
│
├─ APP PRIVADO
│  ├─ vitrine
│  ├─ jornada interativa
│  ├─ Caderno Vivo
│  ├─ LÚCIDA
│  └─ progresso/gating
│
├─ SITE PÚBLICO
│  ├─ página do produto
│  └─ entrada na vitrine/programas
│
└─ RENDERERS
   ├─ eBook PDF
   └─ Workbook PDF
```

## 4. Vitrine

Enquanto a engenharia não estiver congelada:
- status: **Em construção**;
- não exibir promessa de resultado garantido;
- não exibir checkout inexistente;
- CTA: conhecer o projeto / acompanhar desenvolvimento.

Quando houver produto mínimo aprovado:
- CTA público aponta para acesso/checkout real;
- app mostra entitlement;
- não misturar página de venda com conteúdo pago.

## 5. Gating

Candidato: um Dia por intervalo de 24 h, usando relógio do servidor e primeira abertura significativa, reaproveitando a lógica Magnetus.

Isso é **decisão de produto**, não mecanismo científico obrigatório. Deve ser testado com usuárias/os.

## 6. PDF + interativo + workbook

Não manter três versões editoriais independentes.

A fonte estruturada deve renderizar:
- leitura contínua premium para PDF;
- blocos interativos para app;
- campos e tabelas para workbook;
- exportação futura do Caderno.

## 7. Próxima implementação

1. revisar/aprovar esta planta;
2. congelar mapa Dia 1–30;
3. criar manifest/source-lock;
4. estruturar Dias 1–3 como piloto;
5. testar no app em mobile;
6. atualizar site público;
7. somente depois expandir Dias 4–30;
8. gerar PDF/workbook da mesma fonte.
