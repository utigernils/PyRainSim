# PyRainSim - Not Uploaded Yet

PyRainSim is a software that simulates rain by generating random lightning strikes with varying brightness depending on the distance and thunder occurring at different intervals. These lightning strikes are then displayed on any lamp in the specified room using the Philips Hue Bridge, while simultaneously playing custom thunder through the HTTP stream for the Sonos system.

It is recommended to run PyRainSim on a small server such as the Raspberry Pi to ensure smooth operation.

## Features

- Connection with Philips Hue Bridge and Sonos system
- Generation of random lightning strikes with variable brightness based on distance
- Playback of custom thunder through the Sonos system
- Automatic retrieval of rooms and lamps contained therein from the Philips Hue Bridge

## Installation

1. Clone this repository onto your Raspberry Pi:

```
git clone https://github.com/utigernils/PyRainSim.git
```

2. Install the required Python dependencies:

```
pip install -r requirements.txt
```

3. Configure the Philips Hue Bridge and Sonos system in the `config.json` file.

4. Press the link button on the Philips Hue Bridge.

5. Run the `pyrainsim.py` file to start PyRainSim:

```
python pyrainsim.py
```

## Configuration

In the `config.json` file, you can adjust the following parameters:

- `sonos_ip`: The IP address of your Sonos system.
- `hue_bridge_ip`: The IP address of your Philips Hue Bridge.
- `hue_bridge_username`: The username to authenticate with the Philips Hue Bridge. (Auto configured if the link button was pressed.)
- `room`: The room where the lamps for the lightning simulation should be.
- `lightning_color`: The color of the lightning simulation.
- `lightning_brightness`: The brightness of the lightning simulation.
- `lightning_maxtravel`: The maximum of lamps that can flash per lightning.
- `light_id` (Optional): If this parameter is set theres only one lamp used for the lightning simulation.

## Example

```json
{
  "sonos_ip": "192.168.1.101",
  "hue_bridge_ip": "192.168.1.100",
  "hue_bridge_username": "yourusername",
  "room": "bed_room",
  "lightning_color": "200,0,255",
  "lightning_brightness": 255,
  "lightning_maxtravel": 5,
  "lightning_probability": 15,
}
```

Enjoy the soothing atmosphere of a simulated rainy night with PyRainSim! For questions or issues, please open an issue on GitHub.
