import heapq


class Element:
    __compare = None
    def __init__(self, element, compare):
        self.element = element
        if Element.__compare == None:
            Element.__compare = compare

    def __lt__(self, other: Element):
        # to create max heap
        return not Element.__compare(self.element, other.element)

class PQ:
    def __init__(self, compare):
        self.__queue = []
        self.__compare = compare

    def push_back(self, element):
        heapq.heappush(self.queue, Element(element, self.__compare))

    def pop_back(self):
        heapq.heappop(self.__queue)

    def __len__(self):
        return len(self.__queue)
