import pygame
import random
import threading
import time
from phue import Bridge

bridge = Bridge('192.168.1.45')
bridge.connect()

configON = {'transitiontime': 0, 'on': True, 'bri': 254}
configOFF = {'transitiontime': 3, 'on': False, 'bri': 254}

def preload_thunder_sounds():
    pygame.mixer.init()
    return [
        pygame.mixer.Sound("media/thunder1.mp3"),
        pygame.mixer.Sound("media/thunder2.mp3"),
        pygame.mixer.Sound("media/thunder3.mp3"),
        pygame.mixer.Sound("media/thunder4.mp3")
    ]

def preload_lights(group_name):
    global lights

    groups = bridge.get_group()
    group_id = None
    for group in groups:
        if groups[group]['name'] == group_name:
            group_id = group
            break

    if group_id is None:
        print(f"Group '{group_name}' not found.")

    lights = groups[group_id]['lights']

def play_rain():
    while True:
        rain_chanell_1 = rain_sound.play()
        rain_chanell_1.set_volume(1)
        time.sleep(18)

        rain_chanell_2 = rain_sound.play()
        rain_chanell_2.set_volume(0)

        for i in range(11):
            volume_1 = 1 - (i / 10)
            volume_2 = i / 10
            rain_chanell_1.set_volume(volume_1)
            rain_chanell_2.set_volume(volume_2)
            time.sleep(0.2)

def play_thunder():
    thunder_sound = random.choice(thunder_sounds)
    thunder_sound.play()

def display_thunder():
    random_light_id = random.choice(lights)

    print(random_light_id)

    bridge.set_light(int(random_light_id), configON)
    time.sleep(0.3)
    bridge.set_light(int(random_light_id), configOFF)

def make_thunder():
    while True:
        time.sleep(random.randint(4, 14))
        play_thunder()
        time.sleep(7)
        display_thunder()


def main():
    global thunder_sounds
    global rain_sound

    preload_lights('Zimmer Nils')
    thunder_sounds = preload_thunder_sounds()
    rain_sound = pygame.mixer.Sound("media/rain.mp3")

    rain_thread = threading.Thread(target=play_rain)
    thunder_thread = threading.Thread(target=make_thunder)

    rain_thread.start()
    thunder_thread.start()

    while True:
        time.sleep(1)

if __name__ == "__main__":
    main()
