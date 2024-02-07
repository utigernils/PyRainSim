import PyRainSim as main

def preload_thunder_sounds():
    main.pygame.mixer.init()
    return [
        main.pygame.mixer.Sound("media/thunder1.mp3"),
        main.pygame.mixer.Sound("media/thunder2.mp3"),
        main.pygame.mixer.Sound("media/thunder3.mp3"),
        main.pygame.mixer.Sound("media/thunder4.mp3")
    ]

def play_rain():
    while True:
        rain_chanell_1 = rain_sound.play()
        rain_chanell_1.set_volume(1)
        main.t.sleep(18)

        rain_chanell_2 = rain_sound.play()
        rain_chanell_2.set_volume(0)

        for i in range(11):
            volume_1 = 1 - (i / 10)
            volume_2 = i / 10
            rain_chanell_1.set_volume(volume_1)
            rain_chanell_2.set_volume(volume_2)
            main.t.sleep(0.2)


def init_sonos(sonos_ip):
    global client_ip
    client_ip = sonos_ip

    global thunder_sounds, rain_sound
    thunder_sounds = preload_thunder_sounds()
    rain_sound = main.pygame.mixer.Sound("media/rain.mp3")
    print("Preloaded samples.")

if __name__ == "__main__":
    print("Please start this software with 'PyRainSim.py'")