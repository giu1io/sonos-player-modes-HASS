""" Sonos Player Modes """
import logging
from homeassistant.components import sonos

_LOGGER = logging.getLogger(__name__)

DOMAIN = "sonos_player_modes"

DEPENDENCIES = ["sonos"]


def setup(hass, config):
    """Set up is called when Home Assistant is loading our component."""

    sonos_player_data = SonosPlayerData(hass)
    hass.services.register(DOMAIN, "set_mode", sonos_player_data.set_mode)

    _LOGGER.debug("Started Sonos Player Modes")

    return True


class SonosPlayerData(object):
    """Controls Sonos Speakers discovered by the Sonos Integration."""

    def __init__(self, hass):
        """Initialize the data object."""
        self.hass = hass

    def get_soco_from_entity_id(self, entity_id):
        """Returns the SoCo object of the entity that corresponds to the given entity_id"""
        data_sonos = self.hass.data[sonos.media_player.DATA_SONOS]

        if hasattr(data_sonos, 'media_player_entities'):
            """HA 2021.5 Support"""
            for entity in data_sonos.media_player_entities.items():
                if entity[1].entity_id == entity_id:
                    return entity[1].soco
            
        else:
            """Legacy Support"""
            for entity in data_sonos.entities:
                if entity.entity_id == entity_id:
                    return entity.soco
        
        _LOGGER.error("No entity found for entity_id: %s", entity_id)
        return None

    def set_mode(self, call):
        """Handle the service call."""
        mode = call.data.get("mode", "NORMAL")
        entity_id = call.data.get("entity_id", "media_player.bedroom")

        device = self.get_soco_from_entity_id(entity_id)

        if device is not None:
            device.play_mode = mode
