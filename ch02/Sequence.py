from abc import ABCMeta, abstractmethod


class Sequence(metaclass=ABCMeta):
    """Custom version of collections.sequence abstract base class"""

    @abstractmethod
    def __len__(self):
        pass

    @abstractmethod
    def __getitem__(self, item):
        pass

    def __contains__(self, item):
        for j in range(len(self)):
            if self[j] == item:
                return True
        return False

    def index(self, item):
        """Return leftmost index at which item is found - or raise ValueError"""
        for j in range(len(self)):
            if self[j] == item:
                return j
        raise ValueError('Value not in sequence')

    def count(self, item):
        """Return the number of elements equal to given value"""
        k = 0
        for j in range(len(self)):
            if self[j] == item:
                k += 1
        return k
