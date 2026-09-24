"""Transcreve o áudio de um episódio em português, com tempos por segmento.

Uso:
    pip install openai-whisper        # ou instale o seu fork: pip install git+https://github.com/leopacitti/<fork-do-whisper>
    python transcrever.py episodio.wav [--modelo small]

Saídas (ao lado do áudio):
    episodio.segments.json  -> [{"inicio": 0.0, "fim": 4.2, "texto": "..."}]
    episodio.srt
"""
import argparse
import json
from pathlib import Path


def fmt_srt(t: float) -> str:
    h, rem = divmod(t, 3600)
    m, s = divmod(rem, 60)
    return f"{int(h):02d}:{int(m):02d}:{int(s):02d},{int((s % 1) * 1000):03d}"


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("audio")
    p.add_argument("--modelo", default="small")
    a = p.parse_args()

    import whisper  # importado aqui para o --help funcionar sem o pacote

    audio = Path(a.audio)
    model = whisper.load_model(a.modelo)
    res = model.transcribe(str(audio), language="pt", verbose=False)

    segs = [
        {"inicio": round(s["start"], 2), "fim": round(s["end"], 2), "texto": s["text"].strip()}
        for s in res["segments"]
    ]
    audio.with_suffix(".segments.json").write_text(
        json.dumps(segs, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    srt = "\n".join(
        f"{i}\n{fmt_srt(s['inicio'])} --> {fmt_srt(s['fim'])}\n{s['texto']}\n"
        for i, s in enumerate(segs, 1)
    )
    audio.with_suffix(".srt").write_text(srt, encoding="utf-8")
    print(f"{len(segs)} segmentos, {segs[-1]['fim'] if segs else 0:.1f} s")


if __name__ == "__main__":
    main()
