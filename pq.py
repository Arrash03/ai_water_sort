import heapq


class Element:
    __compare = None
    def __init__(self, element, compare):
        self.element = element
        if Element.__compare == None:
            Element.__compare = compare

    def __lt__(self, other):
        # to create max heap
        return not Element.__compare(self.element, other.element)

class PQ:
    def __init__(self, compare):
        self.__queue = []
        self.__compare = compare
        self.__current = 0

    def push_back(self, element):
        heapq.heappush(self.__queue, Element(element, self.__compare))

    def pop_back(self):
        heapq.heappop(self.__queue)

    def remove(self, element):
        tmp_element = Element(element)
        self.__queue.remove(tmp_element)
        heapq.heapify(self.__queue)

    def __len__(self):
        return len(self.__queue)

    def __iter__(self):
        return self.__queue

    def __next__(self):
        if self.__current < (len(self.__queue) - 1):
            next = self.__current
            self.__current += 1
            return self.__queue[next]
        else:
            raise StopIteration
