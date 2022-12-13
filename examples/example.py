class Car:

    def __init__(self, position=0, distance=100, speed=5):

        self.speed = speed  # start speed in m/s (1 m/s = 3.6 km/h)
        # (individual) reaction time of the driver in seconds
        self.reactiontime = .2
        self.length = 5  # meter
        self.distance = distance  # distance to the car in front of the driver
        self.position = position  # position on the current road
        # Individual "confi" speed multiplier. Driver wants to drive speedlimit * speedfactor on a free road
        self.speedfactor = random.random()/10+1
        self.acceleration = .5  # Undimensional for know, should become meter/second²
        self.speedlimit = 100/3.6  # in meter/second
        self.timestepsize = .005  # in seconds
        self.speedhistory = []
        self.positionhistory = []
        self.distancehistory = [self.distance] * \
            int(self.reactiontime/self.timestepsize+1)

    def update(self):

        self.speedhistory.append(self.speed)
        self.positionhistory.append(self.position)
        self.distancehistory.append(self.distance)
        gradient = self.calculate_gradient_hamiltonian()
        self.speed = self.speed + self.timestepsize*gradient*self.acceleration*2 + \
            (random.random() - 0.5) / \
            10  # Mulitplikator entspricht der Beschleunigung

        # Hier könnte man z.B. einen Runge-Kutta Step machen oder einen Memory-Term einfügen
        self.position = self.position + self.timestepsize*self.speed

    def car_length(self):
        # https://www.rnd.de/wirtschaft/datenanalyse-autos-werden-nicht-erst-seit-dem-suv-boom-grosser-6GTM66RRNJEC7EYHR3FQS7Y24Y.html
        return np.random.standard_normal() + 4.6  # Mean = 4.6 meter und Std = 1 meter

    def calculate_gradient_hamiltonian(self):

        gradient = self.speed_hamiltonian(self.speed - 1) - self.speed_hamiltonian(
            self.speed + 1) + self.distance_hamiltonian(self.speed - 1) - self.distance_hamiltonian(self.speed + 1)

        # IMPLEMENT RUNGE KUTTA

        return gradient

    def speed_hamiltonian(self, speed):

        if speed > self.speedfactor * self.speedlimit:
            hamiltonian = (speed - self.speedfactor *
                           self.speedlimit)**4 / self.speedlimit

        else:
            hamiltonian = (speed - self.speedfactor *
                           self.speedlimit)**2 / self.speedlimit

        return hamiltonian
