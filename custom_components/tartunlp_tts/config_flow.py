"""Config flow for Tartu NLP TTS integration."""
import logging
import voluptuous as vol

from homeassistant import config_entries
from homeassistant.core import callback
import homeassistant.helpers.config_validation as cv

from .const import (
    CONF_API_KEY,
    CONF_VOICE,
    CONF_SPEED,
    CONF_URL,
    DEFAULT_URL,
    DOMAIN,
    VOICES,
    UNIQUE_ID
)

_LOGGER = logging.getLogger(__name__)

def generate_unique_id(user_input: dict) -> str:
    """Generate a unique id from user input."""
    url = urlparse(user_input[CONF_URL])
    return f"{url.hostname}_{user_input[CONF_VOICE]}"

async def validate_user_input(user_input: dict):
    """Validate user input fields."""
    if user_input.get(CONF_VOICE) is None:
        raise ValueError("Voice is required")

class TartuNLPConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for Tartu NLP TTS."""

    VERSION = 1

    data_schema = vol.Schema({
        vol.Optional(CONF_API_KEY): str,
        vol.Optional(CONF_URL, default="https://api.tartunlp.ai/text-to-speech/v2"): str,
        vol.Optional(CONF_SPEED, default=1.0): vol.Coerce(float),
        vol.Required(CONF_VOICE, default="mari"): selector({
            "select": {
                "options": VOICES,
                "mode": "dropdown",
                "sort": True,
                "custom_value": True
            }
        })
    })

    async def async_step_user(self, user_input: dict[str, Any] | None = None):
        """Handle the initial step."""
        errors = {}
        if user_input is not None:
            try:
                await validate_user_input(user_input)
                unique_id = generate_unique_id(user_input)
                user_input[UNIQUE_ID] = unique_id
                await self.async_set_unique_id(unique_id)
                self._abort_if_unique_id_configured()
                hostname = urlparse(user_input[CONF_URL]).hostname
                return self.async_create_entry(title=f"TartuNLP TTS ({hostname}, {user_input[CONF_VOICE]})", data=user_input)
            except data_entry_flow.AbortFlow:
                return self.async_abort(reason="already_configured")
            except HomeAssistantError as e:
                _LOGGER.exception(str(e))
                errors["base"] = str(e)
            except ValueError as e:
                _LOGGER.exception(str(e))
                errors["base"] = str(e)
            except Exception as e:  # pylint: disable=broad-except
                _LOGGER.exception(str(e))
                errors["base"] = "unknown_error"
        return self.async_show_form(step_id="user", data_schema=self.data_schema, errors=errors, description_placeholders=user_input)