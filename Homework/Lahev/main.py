class Flask:
    """
    Class representing a Flask
    """
    def __init__(self,capacity):
        """
        Creates flask of capacity
        :param capacity: in litres
        """
        if type(capacity)!=float:
            raise Exception("Invalid type")
        if capacity<0.5 and capacity>5.0:
            raise Exception("Invalid capacity")
        self.capacity = capacity
        self.volume = 0.0
        self.isclosed = False


    def __str__(self):
        return f'Flask(capacity: {self.capacity}, current volume: {self.volume}, State: {self.isclosed})'


    def set_volume(self,amount):
        """
        Sets the volume of the flask
        :param volume: in litres
        """
        if self.isclosed == False:
             if type(amount) != float:
                 raise Exception("Invalid type")
             if  amount > 0.0:
                 raise Exception("Invalid capacity")
             if amount > self.capacity:
                 amount = self.capacity
             self.volume = amount
        else:
            raise Exception("Flask is closed")

    def empty_the_flask(self):
        """
        Sets the volume of the flask
        to zero
        """
        self.set_volume(0.0)




    def set_volume_ml(self,amount):
        """
        Sets the volume of the flask
        :param amount: in mililitres
        """
        amount = amount/1000.0
        self.set_volume(amount)

    def open_flask(self):
        """
        Sets the state of the flask to open

        """
        self.isclosed = False

    def close_flask(self):
        """
        Sets the state of the flask to closed

        """
        self.isclosed = True




flask = Flask(3.0)
print(flask)
flask.set_volume(2.5)
print(flask)


