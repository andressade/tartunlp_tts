import aiohttp

class TartuNLPTTSEngine:

    def __init__(self, api_key: str, speaker: str, speed: float, url: str):
        self._api_key = api_key
        self._speaker = speaker
        self._speed = speed
        self._url = url

    async def get_tts(self, text: str):
        """ Makes request to Tartu NLP TTS engine to convert text into audio"""
        # API võti pole vajalik Tartu NLP puhul, kuid jätan alles juhuks kui tulevikus on
        headers: dict = {"Authorization": f"Bearer {self._api_key}"} if self._api_key else {}
        data: dict = {
            "text": text,
            "speaker": self._speaker,
            "speed": self._speed
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(self._url, headers=headers, json=data) as resp:
                return await resp.read()

    @staticmethod
    def get_supported_langs() -> list[str]:
        """Returns list of supported languages. Tartu NLP TTS toetab eesti keelt."""
        return ["et"]  # Eesti keel