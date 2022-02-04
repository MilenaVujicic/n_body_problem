from model import Point, State

gravitational_constant = 6.67E-10
time_step = 0.01


def initialization():
    """
    Initializes a system to be simulated with dummy data

    Returns
    -------
    all_states: [[Point]]
        Array that contains all the historical states of the system
    current_state: [Point]
        Array that contains current states of all the bodies
    """
    all_states = []
    current_state = []

    position1 = Point(0, 0, 0)
    velocity1 = Point(0.01, 0, 0)
    position2 = Point(1, 1, 0)
    velocity2 = Point(0, 0, 0.02)
    position3 = Point(0, 1, 1)
    velocity3 = Point(0.01, -0.01, -0.01)

    s1 = State("Body1", 0, 1, position1, velocity1, None)
    s2 = State("Body2", 0, 0.1, position2, velocity2, None)
    s3 = State("Body3", 0, 0.01, position3, velocity3, None)

    current_state.append(s1)
    current_state.append(s2)
    current_state.append(s3)

    all_states.append(current_state)

    return current_state, all_states


def calculate_acceleration(init=True, c_state=None, a_states=None):
    """
    Calculates the acceleration the bodies have at the current moment.

    Parameters
    ----------
    init : bool
        Is the simulation being run for the first time.
    c_state : [Point]
        Array that contains current states of all the bodies
    a_states : [[Point]]
        Array that contains current states of all the bodies

    Returns
    --------
        The values in the system after the acceleration has been calculated.

    all_states: [[Point]]
        Array that contains all the historical states of the system
    current_state: [Point]
        Array that contains current states of all the bodies
    """
    current_state = []
    all_states = []
    if init:
        current_state, all_states = initialization()
    else:
        current_state = c_state
        all_states = a_states

    acceleration = Point(0, 0, 0)
    for i in range(0, 3):
        for j in range(0, 3):
            if i == j:
                continue
            constants_product = gravitational_constant * current_state[i].mass * current_state[j].mass
            resulting_displacement = current_state[i].position - current_state[j].position
            displacement_modulus = resulting_displacement.modulus() ** 3
            scale_factor = constants_product / displacement_modulus
            acc = resulting_displacement * scale_factor
            current_state[i].acceleration = acc

    return current_state, all_states


def calculate_new_velocities(c_state = None, a_states = None):
    """
    Calculates the velocity of the bodies in the next step of simulation.

    Parameters
    ----------
    c_state : [Point]
        Array that contains current states of all the bodies
    a_states : [[Point]]
        Array that contains current states of all the bodies

    Returns
    --------
        The values in the system after the velocity has been calculated.

    all_states: [[Point]]
        Array that contains all the historical states of the system
    current_state: [Point]
        Array that contains current states of all the bodies
    """
    current_state = c_state
    all_states = a_states
    for i in range(0, 3):
        current_state[i].velocity = current_state[i].velocity + current_state[i].acceleration
    return current_state, all_states


def calculate_new_positions(c_state=None, a_states=None):
    """
    Calculates the position of the bodies in the next step of simulation.

    Parameters
    ----------
    c_state : [Point]
        Array that contains current states of all the bodies
    a_states : [[Point]]
        Array that contains current states of all the bodies

    Returns
    --------
    The values in the system after the position has been calculated.

    all_states: [[Point]]
        Array that contains all the historical states of the system
    current_state: [Point]
        Array that contains current states of all the bodies
    """
    current_state = c_state
    all_states = a_states
    for i in range(0, 3):
        current_state[i].position = current_state[i].position + current_state[i].velocity
    return current_state, all_states


def simulate():

    """
    Calls functions for the simulation of the problem.
    """

    current_state, all_states = calculate_acceleration()
    current_state, all_states = calculate_new_velocities(current_state, all_states)
    current_state = calculate_new_positions(current_state, all_states)

    print(current_state[0][0])
