import PyRainSim as main


def rgb_to_xy(red, green, blue):

    red = pow((red + 0.055) / (1.0 + 0.055), 2.4) if red > 0.04045 else (red / 12.92)
    green = pow((green + 0.055) / (1.0 + 0.055), 2.4) if green > 0.04045 else (green / 12.92)
    blue = pow((blue + 0.055) / (1.0 + 0.055), 2.4) if blue > 0.04045 else (blue / 12.92)

    x = red * 0.649926 + green * 0.103455 + blue * 0.197109
    y = red * 0.234327 + green * 0.743075 + blue * 0.022598
    z = green * 0.053077 + blue * 1.035763

    x = x / (x + y + z)
    y = y / (x + y + z)

    return [x, y]


def build_command(state):
    command = {'transitiontime': 0, 'on': True, 'bri': 254}

    command['xy'] = rgb_to_xy(lightning_color[0], lightning_color[1], lightning_color[2])
    command['bri'] = lightning_brightness
    command['on'] = state

    return command

def flash_lamp(id):
    bridge.set_light(id, on_command)
    main.t.sleep(0.5)
    bridge.set_light(id, off_command)

def init_bridge(hue_bridge_ip, room, color, brightness, maxtravel):
    global bridge, room_id, lightning_color, lightning_brightness, lightning_maxtravel, on_command, off_command
    try:
        bridge = main.hue.Bridge(hue_bridge_ip)
        bridge.connect()
        print("Successfully connected to the Philips Hue bridge.")

        room_id = room
        lightning_color = color
        lightning_brightness = brightness
        lightning_maxtravel = maxtravel

        on_command = build_command(True)
        off_command = build_command(False)

        print("Successfully prepared the customized lamp commands from the json file.")


    except Exception as e:
        print(f"Failed to connect to the Philips Hue bridge: {e}")


if __name__ == "__main__":
    print("Please start this software with 'PyRainSim.py'")