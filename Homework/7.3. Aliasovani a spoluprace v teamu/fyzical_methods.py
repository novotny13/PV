def calc_current(Voltage : int , Resistance : int):
    """
    Calculates the value of current

    :param Resistance: Represents value of resistance in Ohms
    :param Voltage: Represents value of voltage in Volts
    :return: returns the result in a new variable
    """
    if not isinstance(Resistance, int) and not isinstance(Voltage, int) and Resistance <= 0:
        raise ValueError("Invaild Input")
    current = Voltage/Resistance
    return current


def calc_voltage(Resistance : int , Ampers : int):
    """
    Calculates the value of voltage

    :param Resistance: Represents value of resistance in Ohms
    :param Ampers: Represents value of Current in Amps
    :return: returns the result in a new variable
    """
    if not isinstance(Ampers, int) and not isinstance(Resistance, int):
        raise ValueError("Invaild Input")
    voltage = Ampers*Resistance
    return voltage


def calc_resistance(Voltage : int , Ampers  : int):
    """
    Calculates the value of resistance

    :param Ampers: Represents value of Current in Amps
    :param Voltage: Represents value of voltage in Volts
    :return: returns the result in a new variable
    """
    if not isinstance(Ampers, int) and not isinstance(Voltage, int) and Ampers <=0 :
        raise ValueError("Invaild Input")

    resistance = Voltage/Ampers
    return resistance


def calc_columb_law(q1 : int, q2 : int , r : int , epsilon_r : int):
    """
    Calculates the value of force between charges
    :param q1: Represents value of q1
    :param q2: Represents value of q2
    :param r: Represents distance between charges in meters
    :param epsilon_r: Represents value of  relative permittivity
    """
    if not isinstance(q1, int) and not isinstance(q2, int) and not isinstance(r, int) and not isinstance(epsilon_r, int) and epsilon_r <= 0 and r <= 0:
        raise ValueError("Invaild Input")
    epsilon_0 = 0.00000000000885  #permitivitata vakua

    #vypocet
    epsilon = epsilon_0 * epsilon_r  # Celková permitivita prostředí
    force = (1 / (4 * 3.14 * epsilon)) * abs(q1 * q2) / (r ** 2) #Sila v Newtonech
    return force

