# Dossiê MINDSETmagro™ 30 Dias — Mobile v2.6

**Autoria conceitual e metodológica:** Sol Lima  
**Ecossistema:** Relacione-se®  
**Status:** revisão mobile-first pós-QA visual  
**Formato-fonte:** HTML vertical responsivo / exportável para PDF 9:16

## O que esta revisão corrige

Esta versão substitui o primeiro dossiê mobile que apresentava texto pequeno, números cortados nos badges e hierarquia insuficiente entre os Dias.

### Mobile-first real
- 1 coluna;
- tipografia ampliada para leitura sem zoom no telefone;
- cards empilhados;
- badges numerados reconstruídos, com número centralizado;
- nenhuma linha essencial depende de layout horizontal;
- página-base para PDF: **432 × 768 pt (9:16)**;
- navegação interna preservada.

### Cada Dia agora é reconhecível
Cada Dia ganhou **cinco telas/páginas próprias**:
1. abertura forte do Dia, com número XX/30, travessia, objetivo e ferramentas;
2. Caderno Vivo;
3. experiência real + SE → ENTÃO + ação mínima;
4. Fruto + atalho a evitar;
5. **LÚCIDA + saída**, com prompt pronto e checklist.

As seis travessias possuem famílias cromáticas próprias:
**Descongestionar · Discernir · Voltar a Si · Reposicionar · Habitar · Sustentar**.

## LÚCIDA integrada ao leitor

A LÚCIDA não foi colocada como rodapé promocional. Ela funciona como apoio de investigação e redução de carga cognitiva.

Diretrizes preservadas:
- **LÚCIDA não sentencia. Investiga.**
- a pessoa compartilha apenas o que escolher;
- a IA diferencia fato, interpretação, hipótese e incógnita;
- não decide pelo leitor;
- termina buscando um próximo teste pequeno e um Fruto observável;
- em risco, crise, violência ou necessidade clínica, o fluxo prioriza apoio adequado.

O dossiê contém:
- guia inicial de uso da LÚCIDA;
- modos **Espelho / Maiêutica / Experimento**;
- regra de parada;
- **30 prompts diferentes**, um para cada Dia.

## Estrutura desta edição

- capa e modo de usar;
- rotas Mínima / Completa / Aprofundada;
- ética, saúde e segurança;
- Marco Zero;
- mapa das seis travessias;
- mapa dos 30 Dias;
- guia LÚCIDA;
- Manual de Emergência;
- engrenagem central;
- Atlas com **18 ferramentas, uma por tela/página**;
- Sala de Controle;
- MMI 2.0;
- Tradutor do Prato;
- Poda · Nova Semente · Fruto;
- 30 Dias integrais;
- biblioteca de práticas;
- visualização como ensaio;
- manutenção D+30/D+60/D+90;
- Ritual da Nova Semente;
- navegação final.

## QA desta revisão

- **210 páginas/telas intencionais** na exportação PDF;
- 210/210 rodapés identificados;
- page size 432 × 768 pt;
- nenhuma linha textual com largura anômala no extrator;
- inspeção visual das páginas de uso, LÚCIDA, Atlas, abertura dos Dias e das seis travessias;
- removidos gradientes dependentes de `color-mix` que apresentavam renderização inadequada em PDF;
- badges 1–5 verificados visualmente sem corte;
- PDF aberto com PyMuPDF; sem criptografia, XFA ou dependência de JavaScript.

## Arquivo

`DOSSIE-MINDSETmagro-30-DIAS-Mobile-v2.6.html`

Esse HTML é a fonte mobile da edição e pode ser aberto diretamente no navegador. A exportação de revisão usa WeasyPrint em 432 × 768 pt.

## Nota editorial

PDF é um formato de página fixa; portanto, “responsivo” no PDF significa **mobile-first, legível sem zoom no viewport de telefone**. O HTML desta pasta é a versão que realmente se adapta à largura de tela.
