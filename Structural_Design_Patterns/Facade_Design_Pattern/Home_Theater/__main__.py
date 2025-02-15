class Lights():
    def dim_lights(self, amount):
        print(f"Lights level changed to {amount}%")

class Speakers():
    def on(self):
        print(f"Switching on speakers")
    def off(self):
        print(f"Switching off speakers")

class DVDPlayer():
    def on(self):
        print("Starting the DVD Player")
    def off(self):
        print("Starting the DVD Player")
    def play(self, name):
        print(f"Playing movie {name}")

class Projector():
    def on(self):
        print("Starting the Projector")
    
    def off(self):
        print("Switcing off the Projector")


class HomeTheater():
    def __init__(self):
        self._projector = Projector()
        self._dvdPlayer = DVDPlayer()
        self._speakers = Speakers()
        self._lights = Lights()
    
    def start_movie(self, name):
        self._lights.dim_lights(10)
        self._projector.on()
        self._speakers.on()
        self._dvdPlayer.on()
        self._dvdPlayer.play(name)
        print("Enjoy the movie...")
    
    def stop_movie(self):
        print("Hope you enjoyed the movie...")
        self._lights.dim_lights(100)
        self._projector.off()
        self._speakers.off()
        self._dvdPlayer.off()

if __name__ == "__main__":
    homeTheater = HomeTheater()
    homeTheater.start_movie("The Batman")
    homeTheater.stop_movie()