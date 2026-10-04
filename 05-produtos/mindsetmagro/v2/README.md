# MINDSETmagro™ 2.0 — edição integral para revisão

Autoria conceitual e metodológica: Sol Lima. RELACIONE-SE® / Método Posicione-se™.

Esta fonte reúne pré-livro, 30 dias integrais, pós-livro, campos do Caderno Vivo, referências, ativos e contratos. O pacote não é validação clínica. A integração de app foi implementada sobre o código real do Sites versão 24, em branch isolada; não foi publicada.

## Uma fonte, três saídas

- `days/d01.json` a `d30.json`, `prebook.json`, `postbook.json`: conteúdo e campos canônicos.
- `manifest.json`, `source-lock.json`: versão, mapa e hashes.
- `research/`: 29 alegações com limites, fontes e textos permitidos; mercado/diferenciação.
- `governance/`: constituição, taxonomia, fontes e matriz de migração.
- `contracts/`: progressão, privacidade, analytics desativados, renderização e LÚCIDA.
- `assets/`, `visual-assets.json`: diagramas exatos e função por dia.
- `tools/`: validar, sincronizar e renderizar.
- `qa/`: verificações executadas e suas limitações.

Não edite cópias em `app/content/mindsetmagro` ou PDFs. Edite a fonte, revise os claims, regenere o lock, sincronize e renderize novamente.

## Compilar e verificar

Python 3 com reportlab, svglib, pypdf/PyMuPDF; fontes DejaVu e Poppler para inspeção. Node e pnpm do lockfile do app; nenhuma troca de framework.

```bash
python tools/validate_sync.py --write-lock --app /caminho/do/app-relacionese
python tools/render.py --output /caminho/da/entrega
# Sem --write-lock, o validador denuncia deriva.
python tools/validate_sync.py
```

No runtime Sites (Vinext/React/Cloudflare D1):

```bash
pnpm install --frozen-lockfile
node --test scripts/qa/mindsetmagro.test.mjs
node scripts/qa/mindsetmagro-api.cjs
pnpm exec tsc --noEmit
pnpm build
```

A aplicação usa `learning_progress` já existente e exige `requireResource(userId, 'mindsetmagro_30d')` a cada operação. Nenhum grant real é criado pelo build. O cadastro comercial e concessão de acesso exigem decisão de lançamento. Sem entitlement, o código falha fechado.

## Gates e dados

A abertura significativa é POST explícito. Próximo dia exige 24h de relógio do servidor e conclusão do anterior. O Fruto existente é reaproveitado; obstáculo mais próxima ação segura é alternativa. Campos corporais/alimentares são opcionais. Conflitos usam revisão otimista. Navegação retoma bloco e último campo salvo, com identificadores validados pelo servidor.

O HTML autônomo é uma referência privada para revisão da autora. Contém o conteúdo completo no arquivo, tem intervalo local pedagógico e não oferece proteção comercial. Persistência local exige consentimento; exporte backup. Não publique esse arquivo como se fosse o app pago.

LÚCIDA: perguntas pedagógicas e ponte explícita ao chat existente, sem transmissão automática de respostas nem inferência simulada. A ponte envia título e objetivo revisáveis mediante consentimento; o backend atual usa public_catalog, sem leitura integral do protocolo. Chamada real ao provedor ainda precisa de homologação.

## Estado de testes

Testes de lógica, rotas com SQLite/identidades sintéticas, TypeScript, lint focado, build e exclusão do manuscrito no bundle cliente executados. Não equivalem a tráfego real, teste de eficácia ou homologação de iPhone. Chromium indisponível e instalação oficial falhou; visual mobile/Safari e leitor de tela seguem pendentes. PDFs inspecionados por renderização, amostras e limites de página.

## Critérios para publicar

1. Revisão autoral de voz e lembranças por Sol, sem exigir reenvio de fontes recuperadas.
2. Homologação visual e de interação em iPhone/Safari e leitura assistiva.
3. Confirmar acesso comercial e política de revisão/remoção de registros.
4. Homologar contexto consentido de LÚCIDA e fluxo real de acesso.
5. Aprovar merge/publicação explicitamente; manter o status público em revisão até então.
