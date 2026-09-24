---
name: videocast-decupagem
description: Decupa o áudio de um episódio do videocast Pais de Primeira Viagem (gerado no NotebookLM) em um mapa de falas com tempos, locutor e tipo de plano. Use ao receber o áudio ou a transcrição de um episódio novo.
---

# Decupagem de áudio do videocast

Transforma o áudio do episódio em um **mapa de cenas**: quem fala, de quando a quando, e qual plano de vídeo cobre aquele trecho. É a base para gerar os clipes e montar no CapCut.

## Entrada
- Áudio do episódio (.mp3/.wav/.m4a, exportado do NotebookLM), ou um .mp4 do qual se extrai o áudio.
- Opcional: roteiro/tema do episódio (ex.: "O que realmente protege o recém-nascido").

## Passo a passo

1. **Extrair o áudio** (se vier em vídeo):
   `ffmpeg -i episodio.mp4 -vn -ac 1 -ar 16000 episodio.wav`
2. **Transcrever com tempos** em português com Whisper: `scripts/transcrever.py` do repositório `leopacitti/videocast-skills` (saída `episodio.segments.json` + `episodio.srt`) ou, direto, `whisper episodio.wav --language pt --output_format all`. Se o download dos pesos oficiais estiver bloqueado, instale o fork do Leonardo no GitHub.
3. **Atribuir o locutor** a cada segmento. O NotebookLM gera dois apresentadores que se alternam; mapeie:
   - Voz feminina → `ESPOSA`
   - Voz masculina → `MARIDO`
   Quando não houver diarização automática, deduza pelo conteúdo (quem pergunta / quem responde, tratamento, mudanças de turno) e pela alternância. Marque trechos incertos com `?` para o Leonardo conferir ouvindo.
4. **Agrupar em cenas** de 4 a 10 segundos (limite prático dos clipes de vídeo de IA). Uma fala longa vira várias cenas do mesmo locutor.
5. **Escolher o plano** de cada cena:
   - `CLOSE_ESPOSA` / `CLOSE_MARIDO` — quando só um fala.
   - `ABERTO` — abertura, encerramento, risadas, diálogo rápido (troca em menos de 3 s), e a cada ~45 s para dar respiro.
   - `REACAO_<LOCUTOR>` — ocasionalmente, mostrar quem ouve reagindo (acenando, sorrindo).
6. **Entregar** o mapa como tabela (e CSV `mapa_cenas.csv`) com colunas:
   `cena | inicio | fim | duracao | locutor | plano | resumo_da_fala | gesto_sugerido`

## Regras
- Tempos no formato `MM:SS.s`; nenhuma lacuna nem sobreposição entre cenas.
- `resumo_da_fala` com no máximo 12 palavras — serve para orientar o gesto e a expressão, não é legenda.
- `gesto_sugerido` coerente com a fala (explicando → mãos abertas; dúvida → cabeça inclinada; alerta de segurança → expressão séria).
- Ao final, informe: duração total, número de cenas por plano, e quantos clipes únicos precisam ser gerados (ver skill `videocast-prompts-avatar`).
