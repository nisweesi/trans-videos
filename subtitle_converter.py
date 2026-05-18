import argparse
import json
from datetime import timedelta
from pathlib import Path
from typing import Any

import srt

from models import Segment


def _seconds_to_timedelta(seconds: float) -> timedelta:
    return timedelta(milliseconds=round(seconds * 1000))


def _load_segments(json_path: str | Path) -> list[Segment]:
    with open(json_path, encoding="utf-8") as f:
        data: Any = json.load(f)

    if isinstance(data, dict):
        data = data.get("segments")

    if not isinstance(data, list):
        raise ValueError(
            "Translated JSON must be a list of segments or contain a 'segments' list."
        )

    return [Segment.model_validate(segment) for segment in data]


def convert_json_to_srt(
    json_path: str | Path, output_path: str | Path | None = None
) -> Path:
    json_path = Path(json_path)
    output_path = (
        Path(output_path) if output_path is not None else json_path.with_suffix(".srt")
    )

    subtitles = [
        srt.Subtitle(
            index=segment.index,
            start=_seconds_to_timedelta(segment.start),
            end=_seconds_to_timedelta(segment.end),
            content=segment.text.strip(),
        )
        for segment in _load_segments(json_path)
    ]

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(srt.compose(subtitles), encoding="utf-8")
    return output_path


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Convert translated subtitle JSON to SRT."
    )
    parser.add_argument("json_path", help="Path to translated JSON file from main.py")
    parser.add_argument("output_path", nargs="?", help="Optional output .srt path")
    args = parser.parse_args()

    srt_path = convert_json_to_srt(args.json_path, args.output_path)
    print(f"Saved SRT subtitles to {srt_path}")


if __name__ == "__main__":
    main()
