""" Constants for Tartu NLP TTS custom component"""

DOMAIN = "tartunlp_tts"
CONF_API_KEY = 'api_key'  # Jätan alles, kuigi pole kindel kas API vajab võtit
CONF_SPEAKER = 'speaker'  # Varasem CONF_VOICE
CONF_SPEED = 'speed'
CONF_URL = 'url'
UNIQUE_ID = 'unique_id'
SPEAKERS = ["mari", "tambet", "liisu", "kalev", "meelis", "albert", "külli", "peeter", "indrek", "vesta", "riina", "eva", "tõnu"]  # Tartu NLP kõnelejad
DEFAULT_URL = "https://api.tartunlp.ai/text-to-speech/v2"