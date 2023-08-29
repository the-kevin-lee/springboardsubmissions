"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    # constructor vvvvvvvvvvvvvvvv
    def __init__(self,start=0):
        """Creates a new generator - beginning at start"""
        self.start = self.nextnum = start

    
    def __repr__(self):
        """Displays what the Generator's inputs are."""
        return f"<SerialGenerator start = {self.start} next = {self.next}>"

    def generate(self):
        """Increments next value to +1 while returning the current value (self.next - 1)"""
        self.nextnum += 1
        return self.nextnum - 1

    def reset(self):
        """Resets the next value back to start"""
        self.nextnum = self.start