---
name: videocast-montagem
description: Prepara o roteiro de montagem no CapCut de um episódio do videocast Pais de Primeira Viagem, casando o áudio completo com os clipes gerados, legendas e vinhetas. Use quando os clipes do episódio já estiverem gerados.
---

# Montagem do episódio no CapCut

## Entrada
- Áudio completo do episódio (trilha mestre — nunca cortar).
- `mapa_cenas.csv` (skill `videocast-decupagem`) e `lista_clipes.csv` (skill `videocast-prompts-avatar`).
- Clipes gerados, nomeados pelo `clipe_id`.

## Passo a passo

1. **Checar insumos:** todo `clipe_id` do mapa tem arquivo? Liste os faltantes antes de montar.
2. **Gerar a lista de corte** (`corte_capcut.md`), uma linha por cena, na ordem:
   `inicio → fim | arquivo | ajuste` (ajuste = aparar, repetir em loop, desacelerar até 0,8x para cobrir a duração).
3. **Instruções de timeline** para o Leonardo seguir no CapCut:
   - Faixa 1: áudio mestre, travado.
   - Faixa 2: clipes na ordem da lista de corte; cortes secos na troca de locutor, transição cruzada de 6–10 quadros só entre cenas do mesmo locutor.
   - Faixa 3: legendas automáticas do CapCut em português, revisando termos técnicos (ex.: nomes de vacinas, "berço", "síndrome da morte súbita").
   - Faixa 4: vinheta de abertura (até 5 s), cartela com o tema do episódio, vinheta de encerramento.
   - Opcional: se usar a estratégia VTuber, aplicar o efeito de boca/movimento guiado pelo áudio nos closes.
4. **Exportar:** 1080p, 30 fps, versão 16:9 (YouTube) e, se pedido, cortes 9:16 de 30–60 s dos melhores trechos para Reels/Shorts — indique quais trechos do mapa rendem bons cortes.

## Checklist final
- Nenhum trecho do áudio sem imagem.
- Boca fechada em planos de reação.
- Rostos e roupas iguais em todos os clipes (se algum destoar, regenerar só aquele).
- Conteúdo de saúde do bebê revisado: o videocast informa, não substitui orientação pediátrica — incluir essa frase na descrição do vídeo.
