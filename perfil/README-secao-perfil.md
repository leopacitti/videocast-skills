## 🎙️ Projeto: Pais de Primeira Viagem — videocast animado com IA

Videocast sobre paternidade/maternidade de primeira viagem, apresentado por dois avatares animados. Todo o fluxo é orquestrado com ferramentas de IA generativa e documentado como skills reutilizáveis em [`videocast-skills`](https://github.com/leopacitti/videocast-skills).

**Competências**

- **Generative AI Video Workflows** — criação de clipes de avatares com Veo / Google Flow e ferramentas de lip sync.
- **AI Prompt Engineering** — fichas visuais fixas para manter rostos, roupas, cenário e luz consistentes entre dezenas de clipes.
- **Decupagem e mapeamento de áudio** — transcrição com Whisper (fork próprio), identificação de locutores e mapa de cenas com tempos.
- **Audiovisual Post-Production** — montagem e sincronização no CapCut, legendas, vinhetas e cortes verticais para redes.
- **Roteiro com IA** — geração do áudio dos episódios no NotebookLM a partir de fontes selecionadas.

**Fluxo**

`NotebookLM (áudio)` → `Whisper (transcrição)` → `mapa de cenas` → `Veo/Flow + lip sync (clipes)` → `CapCut (montagem)`
