# transcription service
import whisper

import os
import json


def transcribe(
    filepath: str, output_dir: str = "generated_subtitles", language: str = "en"
):
    model = whisper.load_model("base")

    result = model.transcribe(filepath, language=language, fp16=False)

    segments = []

    for i, seg in enumerate(result["segments"]):
        segment = {
            "index": i + 1,
            "start": round(seg["start"], 3),
            "end": round(seg["end"], 3),
            "text": seg["text"].strip(),
        }

        segments.append(segment)

    transcript_json = {
        "filename": filepath,
        "language": language,
        "segments": segments,
    }

    os.makedirs(output_dir, exist_ok=True)
    base_name = os.path.splitext(os.path.basename(filepath))[0]
    json_path = os.path.join(output_dir, f"{base_name}.json")

    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(transcript_json, f, ensure_ascii=False, indent=2)

    return transcript_json
