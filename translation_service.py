import os

from xai_sdk import AsyncClient
from xai_sdk.chat import system

from models import transcription_response


async def translate(
    translation_json, language_from: str = "English", language_to: str = "Arabic"
):
    client = AsyncClient(
        api_key=os.getenv("XAI_API_KEY"),
    )

    prompt = f"""

    You're a professional Translator from {language_from} to {language_to}, You know how to trnasalte every word and sentence
    accurately, as well as, not using less or more words in the {language_to} than {language_from}
    Do not make mistakes, make the translation as accurate as possible, don't use new words, and only use a different phrasing when nothing else can be accurate
    Do not use Egyption or Saudi slang, only use Modern Standard Arabic
    Make sure to follow the formart which is JSON, and save the timestamps accurately

    Here is the subtitle:
    {translation_json}

    """

    chat = client.chat.create(model="grok-4.3", response_format=transcription_response)

    chat.append(system(prompt))

    response = await chat.sample()

    translated_response = transcription_response.model_validate_json(response.content)

    return translated_response
