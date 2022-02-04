import dataclasses
import math


class Point:
    """
    Class that defines 3D vector with a point

    Attributes
    ----------
    x : float
        x component of a vector
    y : float
        y component of a vector
    z : float
        z component of a vector
    """
    x: float
    y: float
    z: float

    def __init__(self, x=0, y=0, z=0):
        """
        Initializes a vector. If arguments are not passed, the default arguments are used

        Parameters
        ----------

        x : float
            x component of a vector to be initialized
        y : float
            y component of a vector to be initialized
        z : float
            z component of a vector to be initialized

        """
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        """
        Returns
        -------
            Formatted string representation of a point
        """
        return "[{}, {}, {}]".format(self.x, self.y, self.z)

    def __add__(self, other):
        """
        Adds the value of the second operand onto the value of the first operand

        Parameters
        ----------
        other: Point
            The vector to be added to the value of a vector

        Raises
        ------
        Exception
            If the argument other is not of the type Point

        Returns
        -------
            The value of first operand after the addition

        """
        if not isinstance(other, Point):
            raise Exception
        self.x += other.x
        self.y += other.y
        self.z += other.z

        return self

    def __sub__(self, other):
        """
        Subtracts the value of the second operand from the value of the first operand

        Parameters
        ----------
        other: Point
            The vector to be subtracted from the value of a vector

        Raises
        ------
        Exception
            If the argument other is not of the type Point

        Returns
        -------
            The value of first operand after the subtraction

        """
        if not isinstance(other, Point):
            raise Exception
        self.x -= other.x
        self.y -= other.y
        self.z -= other.z
        return self

    def __mul__(self, other):
        """
        Scales a vector with a number value

        Parameters
        ----------
        other: float | int
           The scalar to be multiplied with the vector

        Returns
        -------
            The value of vector after scaling

        """

        self.x *= other
        self.y *= other
        self.z *= other

        return self

    def modulus(self):
        """
        Returns
        -------
            The value of modulus of a vector
        """
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    def __eq__(self, other):
        """
        Check if the two vectors are equal
        Parameters
        ----------
        other: Point
            The vector to be compared with the current vector

        Raises
        ------
        Exception
            If the argument other is not of the type Point

        Returns
        -------
            True if the vectors are equal, False if the vectors are not equal
        """
        if not isinstance(other, Point):
            raise Exception
        if self.x == other.x and self.y == other.y and self.z == other.z:
            return True
        return False


class State:
    """
    Class that models the state of a vector in the system
    Attributes
    ----------
    label : str
        The string label that identifies the vector
    time : int
        Discrete timestamp at which the state is valid
    mass : float
        Mass of the object
    position : Point
        Vector of the position of the body
    velocity : Point
        Vector of the velocity of the body
    acceleration : Point
        Vector of the acceleration of the body
    """
    label: str
    time: int
    mass: float
    position: Point
    velocity: Point
    acceleration: Point

    def __init__(self, label="", time=0, mass=0, position=None, velocity=None, acceleration=None):
        """
        Initializes a state. If arguments are not passed, the default arguments are used

        Parameters
        ----------
        label : str
            The string label that identifies the vector
        time : int
            Discrete timestamp at which the state is valid
        mass : float
            Mass of the object
        position : Point
            Vector of the position of the body
        velocity : Point
            Vector of the velocity of the body
        acceleration : Point
            Vector of the acceleration of the body
        """
        self.label = label
        self.time = time
        self.mass = mass
        self.position = position
        self.velocity = velocity
        self.acceleration = acceleration

    def __str__(self):
        """
               Returns
               -------
                   Formatted string representation of a state
               """
        return "[{}, {}] Current state is:\n[mass: {}\n positon: {}\n velocity: {}\n acceleration: {}]"\
            .format(self.label, self.time, self.mass, str(self.position), str(self.velocity), str(self.acceleration))
