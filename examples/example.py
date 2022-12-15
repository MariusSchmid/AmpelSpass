"""This module is for car calculations."""


class Car:
    """this is a car
    """

    def __init__(self, position=0, distance=100, speed=5):

        self.speed = speed  # start speed in m/s (1 m/s = 3.6 km/h)
        # (individual) reaction time of the driver in seconds
        self.reactiontime = .2
        self.length = 5  # meter
        self.distance = distance  # distance to the car in front of the driver
        self.position = position  # position on the current road
        # Individual "confi" speed multiplier. Driver wants to drive speedlimit * speedfactor on a free road
        self.acceleration = .5  # Undimensional for know, should become meter/second²
        self.speedlimit = 100/3.6  # in meter/second
        self.timestepsize = .005  # in seconds
        self.speedhistory = []
        self.positionhistory = []
        self.distancehistory = [self.distance] * \
            int(self.reactiontime/self.timestepsize+1)

    def update(self):
        """this is a function
        """

        self.speedhistory.append(self.speed)
        self.positionhistory.append(self.position)
        self.distancehistory.append(self.distance)
        # Hier könnte man z.B. einen Runge-Kutta Step machen oder einen Memory-Term einfügen
        self.position = self.position + self.timestepsize*self.speed
