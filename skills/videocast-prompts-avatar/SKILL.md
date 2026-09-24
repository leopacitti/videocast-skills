---
name: videocast-prompts-avatar
description: Gera prompts consistentes (em inglês) para criar os clipes dos avatares do videocast Pais de Primeira Viagem no Veo/Google Flow ou em ferramentas de lip sync. Use depois da decupagem, para produzir a lista de clipes de um episódio.
---

# Prompts dos avatares do videocast

Objetivo: clipes curtos em que marido e esposa **pareçam sempre os mesmos** — mesmo rosto, roupa, cenário e luz — de um clipe para o outro.

## 1. Ficha fixa (preencher uma vez e reutilizar sempre)

Mantenha estes blocos em um arquivo `ficha_avatares.md` e **cole-os literalmente** em todo prompt. Nunca reescreva com outras palavras: variações de texto geram variações visuais.

```
[STYLE] Stylized 3D cartoon animation, soft Pixar-like shading, warm color palette, 16:9, cinematic depth of field.
[STUDIO] Cozy home podcast studio: wooden desk, two black broadcast microphones on boom arms, acoustic foam panels in sage green, a bookshelf with baby books and a small plush toy, warm neon sign reading "Pais de Primeira Viagem", soft key light from the left, warm practical lamps in the background.
[WIFE] Woman in her early 30s, <cabelo: cor, comprimento, penteado>, <olhos>, <traços marcantes>, wearing <roupa fixa>.
[HUSBAND] Man in his early 30s, <cabelo>, <barba/sem barba>, <óculos?>, wearing <roupa fixa>.
[NEGATIVE] No text overlays, no subtitles, no extra people, no logo changes, consistent faces, no camera shake.
```

Use as fotos de referência (imagem inicial / "ingredients" no Flow) sempre que a ferramenta aceitar — isso segura a consistência mais do que o texto.

## 2. Modelos de prompt por plano

- **ABERTO**: `[STYLE] [STUDIO] Medium-wide shot of both hosts at the desk. [WIFE] on the left, [HUSBAND] on the right. They talk naturally, <gesto>. Static camera. [NEGATIVE]`
- **CLOSE_ESPOSA**: `[STYLE] Close-up of [WIFE] speaking into the microphone, <gesto/expressão>. Background: [STUDIO], softly blurred. Static camera. [NEGATIVE]`
- **CLOSE_MARIDO**: igual, trocando por [HUSBAND].
- **REACAO_<X>**: `... Close-up of <X> listening attentively, <nodding / smiling / raising eyebrows>, mouth closed. ...`

## 3. Sincronia labial — decisão importante

Clipes de texto-para-vídeo (Veo) **não sincronizam a boca com o áudio do NotebookLM**. Escolha uma estratégia por episódio:

- **A. Estilo VTuber (recomendado para começar):** gere poucos clipes-base em loop (cada avatar falando genericamente, ouvindo, rindo) e aplique a animação de boca no CapCut ou em um avatar 2D/3D animado pelo áudio. Barato e consistente.
- **B. Lip sync por trecho:** para cada cena de close, envie a imagem do avatar + o trecho de áudio correspondente a uma ferramenta de lip sync (ex.: Hedra, HeyGen, D-ID). Mais realista, mais trabalho e custo.
- **C. Veo puro:** aceitável só em planos abertos/reações sem boca visível em destaque.

## 4. Saída

Para cada episódio, a partir do `mapa_cenas.csv`:
1. Deduplicar: cenas com mesmo plano + gesto reutilizam o mesmo clipe.
2. Entregar `lista_clipes.csv`: `clipe_id | plano | gesto | duracao_alvo | prompt_completo | cenas_que_usam`.
3. Nomear arquivos gerados como `EP01_C03_CLOSE_ESPOSA_explicando.mp4` para a montagem.
