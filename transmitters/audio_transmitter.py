import PyRainSim as main

def preload_thunder_sounds():
    main.pygame.mixer.init()
    return [
        main.pygame.mixer.Sound("media/thunder1.mp3"),
        main.pygame.mixer.Sound("media/thunder2.mp3"),
        main.pygame.mixer.Sound("media/thunder3.mp3"),
        main.pygame.mixer.Sound("media/thunder4.mp3")
    ]
def init_sonos(sonos_ip):
    global client_ip
    client_ip = sonos_ip

    global thunder_sounds
    thunder_sounds = preload_thunder_sounds()
    print("Preloaded samples.")

if __name__ == "__main__":
    print("Please start this software with 'PyRainSim.py'")