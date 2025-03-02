"""Config flow for Tartu NLP TTS integration."""
import logging
import voluptuous as vol

from homeassistant import config_entries
from homeassistant.core import callback
import homeassistant.helpers.config_validation as cv

from .const import (
    CONF_API_KEY,
    CONF_SPEAKER,
    CONF_SPEED,
    CONF_URL,
    DEFAULT_URL,
    DOMAIN,
    SPEAKERS,
    UNIQUE_ID
)

_LOGGER = logging.getLogger(__name__)

class TartuNLPConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for Tartu NLP TTS."""

    VERSION = 1

    async def async_step_user(self, user_input=None):
        """Handle the initial step."""
        errors = {}

        if user_input is not None:
            # Jätame valideerimise lihtsamaks
            return self.async_create_entry(
                title=f"Tartu NLP TTS - {user_input[CONF_SPEAKER]}",
                data=user_input,
            )

        # Kiirus on float tüüpi, võimaldades 0.5-2.0 vahel väärtuseid
        data_schema = vol.Schema(
            {
                vol.Optional(CONF_API_KEY): cv.string,
                vol.Required(CONF_SPEAKER, default=SPEAKERS[0]): vol.In(SPEAKERS),
                vol.Required(CONF_SPEED, default=1.0): vol.All(vol.Coerce(float), vol.Range(min=0.5, max=2.0)),
                vol.Required(CONF_URL, default=DEFAULT_URL): cv.string,
                vol.Optional(UNIQUE_ID): cv.string,
            }
        )

        return self.async_show_form(
            step_id="user", data_schema=data_schema, errors=errors
        )

    @staticmethod
    @callback
    def async_get_options_flow(config_entry):
        """Get options flow for this handler."""
        return TartuNLPOptionsFlow(config_entry)


class TartuNLPOptionsFlow(config_entries.OptionsFlow):
    """Handle options."""

    def __init__(self, config_entry):
        """Initialize options flow."""
        self.config_entry = config_entry

    async def async_step_init(self, user_input=None):
        """Manage the options."""
        if user_input is not None:
            return self.async_create_entry(title="", data=user_input)

        return self.async_show_form(
            step_id="init",
            data_schema=vol.Schema(
                {
                    vol.Required(
                        CONF_SPEED,
                        default=self.config_entry.data.get(CONF_SPEED, 1.0),
                    ): vol.All(vol.Coerce(float), vol.Range(min=0.5, max=2.0)),
                }
            ),
        )