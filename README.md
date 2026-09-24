# videocast-skills

Skills de IA para produzir o videocast animado **Pais de Primeira Viagem** a partir dos áudios gerados no NotebookLM.

| Etapa | Skill | Entrega |
|---|---|---|
| 1. Decupagem | [`videocast-decupagem`](skills/videocast-decupagem/SKILL.md) | `mapa_cenas.csv` — quem fala, quando, qual plano |
| 2. Clipes | [`videocast-prompts-avatar`](skills/videocast-prompts-avatar/SKILL.md) | `lista_clipes.csv` — prompts consistentes para Veo/Flow e lip sync |
| 3. Montagem | [`videocast-montagem`](skills/videocast-montagem/SKILL.md) | `corte_capcut.md` — lista de corte e checklist para o CapCut |

`scripts/transcrever.py` gera a transcrição com tempos (Whisper, português).

## Como usar com o Claude
Cada pasta em `skills/` segue o formato de Agent Skills (um `SKILL.md` com `name` e `description`). Adicione as skills na sua conta do Claude ou peça, em uma sessão com este repositório vinculado: "use a skill videocast-decupagem neste áudio".

## Fluxo
NotebookLM (áudio) → Whisper (transcrição) → mapa de cenas → Veo/Flow + lip sync (clipes) → CapCut (montagem)
