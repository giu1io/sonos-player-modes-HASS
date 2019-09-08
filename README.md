# Sonos Player Modes
## Custom Component For Home Assistant

This component creates a service `sonos_player_modes.set_mode` that lets you change playback modes on any one of your Sonos speakers.

## Service Parameters
- `device_name`: name of the device in the Sonos app
- `mode`: playback mode. Supported modes: `NORMAL`, `REPEAT_ALL`, `SHUFFLE`, `SHUFFLE_NOREPEAT`