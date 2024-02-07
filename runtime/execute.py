import PyRainSim as main

def rain():
    while True:
        main.audio.play_rain()

def thunder_and_lightning():
    while True:
        thunder_pause = main.random.randint(2, 10)
        print(F"Next lightning strike in {thunder_pause} seconds!")
        main.t.sleep(thunder_pause)

        for _ in range(main.random.randint(1, lightning_maxtravel)):
            lightning = main.lights.flash_lamp()
            print(f"Struk on lamp {lightning}!")

        main.audio.play_thunder()

def run(max_travel):
    global lightning_maxtravel
    lightning_maxtravel = max_travel

    rain_thread = main.threading.Thread(target=rain)
    thunder_and_lightning_thread = main.threading.Thread(target=thunder_and_lightning)
    print("Defined threads.")

    print("Starting threads...")
    rain_thread.start()
    thunder_and_lightning_thread.start()


if __name__ == "__main__":
    print("Please start this software with 'PyRainSim.py'")