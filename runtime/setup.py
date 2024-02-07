import PyRainSim as main


def run(config_file):
    print(f"The file called '{config_file}' couldn't be found.")
    print("Welcome to the setup wizard!")

    speakers = main.soco.discover()

    if speakers:
        print("Discovered Sonos devices:")
        for i, speaker in enumerate(speakers):
            print(f"{i + 1}. {speaker.player_name}")


        while True:
            try:
                choice = int(input("Enter the number corresponding to the Sonos device you want to use: "))
                if 1 <= choice <= len(speakers):
                    selected_speaker = list(speakers)[choice - 1]
                    print(f"Selected Sonos device: {selected_speaker.player_name} ({selected_speaker.ip_address})")
                    sonos_ip = selected_speaker.ip_address
                    break
                else:
                    print("Invalid choice. Please enter a valid number.")
            except ValueError:
                print("Invalid input. Please enter a number.")


        while True:
            hue_bridge_ip = input("Enter the IP address of the Philips Hue bridge: ")
            if hue_bridge_ip:
                print(f"You entered: {hue_bridge_ip}")
                confirm = input("Press the link button on your Philips Hue bridge, then press F to continue: ")
                if confirm == "F":
                    break
                else:
                    print("Please press Enter after pressing the link button.")
            else:
                print("Please enter a valid IP address.")

        bridge = main.Bridge(hue_bridge_ip)
        try:
            bridge.connect()
            print("Successfully connected to the Philips Hue bridge.")
        except Exception as e:
            print(f"Failed to connect to the Philips Hue bridge: {e}")
            return None, None

        print("Available rooms:")
        rooms = bridge.get_group()
        for room_id, room_info in rooms.items():
            print(f"Room ID: {room_id}, Name: {room_info['name']}")

        while True:
            room_id = input("Enter the ID of the room where the lamps for the lightning simulation should be: ")
            if room_id in rooms:
                print(f"You selected room: {rooms[room_id]['name']}")
                break
            else:
                print("Invalid room ID. Please enter a valid ID.")

        lightning_color = input("Enter the color of the lightning simulation (ex: 200,0,255): ")
        lightning_brightness = input("Enter the brightness of the lightning simulation (0-255): ")
        lightning_maxtravel = input("Enter the maximum number of lamps that can flash per lightning: ")

        config = {
            "sonos_ip": sonos_ip,
            "hue_bridge_ip": hue_bridge_ip,
            "room": rooms[room_id]['name'],
            "lightning_color": lightning_color,
            "lightning_brightness": lightning_brightness,
            "lightning_maxtravel": lightning_maxtravel
        }

        with open('config.json', 'w') as f:
            main.json.dump(config, f, indent=4)
            print("Successfully saved configuration to 'config.json'.")
            print("Restarting PyRainSim")

    else:
        print("No Sonos devices found on the network.")
        return None, None


if __name__ == "__main__":
    print("Please start this software with 'PyRainSim.py'")