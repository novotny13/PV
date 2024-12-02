class Flask:
    """
    Class representing a Flask with a capacity and volume control.
    """

    def __init__(self, capacity):
        """
        Initializes a Flask with a given capacity in liters and sets it as empty.
        :param capacity: Capacity of the flask in liters (float).
        """
        if not isinstance(capacity, float):
            raise ValueError("Capacity must be a float.")
        if capacity < 0.5 or capacity > 5.0:
            raise ValueError("Capacity must be between 0.5 and 5 liters.")
        self.capacity = capacity
        self.volume = 0.0
        self.isclosed = True

    def __str__(self):
        state = "closed" if self.isclosed else "open"
        return f"Flask(capacity: {self.capacity}L, volume: {self.volume}L, state: {state})"

    def open_flask(self):
        """Opens the flask."""
        self.isclosed = False

    def close_flask(self):
        """Closes the flask."""
        self.isclosed = True

    def set_volume(self, volume):
        """
        Sets the volume of the flask in liters.
        :param volume: Volume in liters (float).
        """
        if self.isclosed:
            raise Exception("Flask is closed. Cannot set volume.")
        if not isinstance(volume, float):
            raise ValueError("Volume must be a float.")
        if volume < 0:
            raise ValueError("Volume cannot be negative.")
        self.volume = min(volume, self.capacity)

    def get_volume(self):
        """Returns the current volume in liters."""
        return self.volume

    def empty_the_flask(self):
        """Empties the flask."""
        self.set_volume(0.0)

    def set_volume_ml(self, volume_ml):
        """
        Sets the volume of the flask in milliliters.
        :param volume_ml: Volume in milliliters (int or float).
        """
        self.set_volume(volume_ml / 1000.0)
