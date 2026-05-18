import json
import os

import asyncio

from transcription_service import transcribe
from translation_service import translate
from subtitle_converter import convert_json_to_srt


async def main():
    transcript = transcribe("mrbeast.mp4")
    translated = await translate(transcript)
    basename = os.path.splitext(os.path.basename(translated.filename))[0]
    filename = f"{basename}_{translated.language_to}.json"
    segments_dict = [seg.model_dump() for seg in translated.segments]

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(segments_dict, f, ensure_ascii=False, indent=2)

    convert_json_to_srt(filename, "generated_subtitle_srt")


if __name__ == "__main__":
    asyncio.run(main())
