class Objective:
    def __init__(self, quantity, predicate, value):
        self.quantity = quantity
        self.predicate = predicate
        self.value = value

    def and_(self, other):
        """Return a new Objective."""
        pass

    def and_not(self, other):
        """Return a new Objective."""
        pass

    def or_(self, other):
        """Return a new Objective."""
        pass

    def or_not(self, other):
        """Return a new Objective."""
        pass
