import os
import random
import time as t
import json
import threading

import runtime.setup as setup
import runtime.execute as exec

from phue import Bridge
import phue as hue
import soco

import transmitters.light_transmitter as lights
import transmitters.audio_transmitter as audio
import pygame

config_file = 'config.json'


def load_config(config_file):
    global sonos_ip, hue_bridge_ip, hue_bridge_username, room, lightning_color, lightning_brightness, lightning_maxtravel,

    with open(config_file, 'r') as f:
        config = json.load(f)

    sonos_ip = config["sonos_ip"]
    hue_bridge_ip = config["hue_bridge_ip"]
    room = config["room"]
    lightning_color = [int(x) for x in config["lightning_color"].split(",")]
    lightning_brightness = int(config["lightning_brightness"])
    lightning_maxtravel = int(config["lightning_maxtravel"])

    return config


def initialize():
    print(f"Found '{config_file}'!")

    config = load_config(config_file)
    print("Loaded config:")
    print(json.dumps(config, indent=4))

    lights.init_bridge(hue_bridge_ip, room, lightning_color, lightning_brightness, lightning_maxtravel)
    audio.init_sonos(sonos_ip)


def main():
    print("Welcome to PyRainSim!")
    if not os.path.exists(config_file):
        setup.run(config_file)
        main()
    else:
        initialize()
        exec.run(lightning_maxtravel)

if __name__ == "__main__":
    main()
