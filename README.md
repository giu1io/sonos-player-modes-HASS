# Sonos Player Modes
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
- `mode`: playback mode. Supported modes: `NORMAL`, `REPEAT_ALL`, `REPEAT_ONE`, `SHUFFLE`, `SHUFFLE_NOREPEAT`
