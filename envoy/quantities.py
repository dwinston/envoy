from abc import ABC, abstractmethod


class Quantity(ABC):
    def __init__(self, mid, mdb):
        self.mid = mid
        self.mdb = mdb

    @property
    @abstractmethod
    def deps(self):
        raise NotImplementedError

    def get(self, dep):
        if dep.name not in self.deps:
            raise Exception(f"{dep.name} not in {self.name}'s deps.")
        return dep().get_me()

    @abstractmethod
    def get_me(self):
        raise NotImplementedError

    @classmethod
    def name(cls):
        return cls.__qualname__

    def is_true(self):
        """Return a new Objective."""
        pass

    def is_false(self):
        """Return a new Objective."""
        pass

    def is_greater_than(self):
        """Return a new Objective."""
        pass


class PrimitiveQuantity(Quantity):
    @property
    def deps(self):
        return frozenset()

    def get_me(self):
        doc = self.mdb[self.name].find_one({"_id": self.mid})
        if doc is None:
            doc = self.get_me_from_source()
            if doc is None:
                raise Exception(f"Can't find property {self.name} for material {self.mid}.")
            doc["_id"] = self.mid
            self.mdb[self.name].insert_one(doc)
        return doc

    def get_me_from_source(self):
        raise NotImplementedError
