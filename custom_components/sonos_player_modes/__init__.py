from soco.discovery import by_name
import logging

_LOGGER = logging.getLogger(__name__)

DOMAIN = 'sonos_player_modes'

def setup(hass, config):
    """Set up is called when Home Assistant is loading our component."""

    def set_mode(call):
        """Handle the service call."""
        mode = call.data.get('mode', 'NORMAL')
        device_name = call.data.get('device_name', 'Bedroom')

        device = by_name(device_name)

        device.play_mode = mode

    hass.services.register(DOMAIN, 'set_mode', set_mode)

    # Return boolean to indicate that initialization was successfully.
    return True