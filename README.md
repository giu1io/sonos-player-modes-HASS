# Sonos Player Modes

## Update 2021-07-24

As [noted by jeremywillans](https://github.com/giu1io/sonos-player-modes-HASS/issues/5) this no longer works in HA 2021.7+. In October of last year the core `media_player` service has been updated and has added some of the functionality ([repeat](https://www.home-assistant.io/integrations/media_player/#service-media_playerrepeat_set), [shuffle](https://www.home-assistant.io/integrations/media_player/#service-media_playershuffle_set)) that this plugin provided. This repository will be archived and it's no longer supported.

## Custom Component For Home Assistant
[![hacs_badge](https://img.shields.io/badge/HACS-Custom-orange.svg)](https://github.com/custom-components/hacs)

This component creates a service `sonos_player_modes.set_mode` that lets you change playback modes on any one of your Sonos speakers. Requires the `sonos` component to be already setup.

## Install
1. Copy the `custom_components` forlder in your HA configuration folder (or install with [HACS](https://github.com/custom-components/hacs)).
2. Add
    ```
    sonos_player_modes:
    ```
    to the `configuration.yaml`

## Service Parameters
- `entity_id`: entity id of the speaker  (eg. `media_player.bedroom`)
- `mode`: playback mode. Supported modes: `NORMAL`, `REPEAT_ALL`, `REPEAT_ONE`, `SHUFFLE`, `SHUFFLE_NOREPEAT`, `SHUFFLE_REPEAT_ONE` 
