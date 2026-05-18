# transcription service
import whisper


def transcribe(filepath: str):
    model = whisper.load_model("base")

    result = model.transcribe(filepath, language="en", fp16=False)

    text = result["text"]

    print(result)

    return text


transcribe("mrbeast.mp4")
