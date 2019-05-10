from symbolic.args import symbolic, concrete
@symbolic(message="abcdefg")
@symbolic(message="abcdefg")
def __init__(self):
    """
    Initialize your data structure here.
    """
    heap = []
    cache = {}
def shouldPrintMessage( timestamp, message):
    """
    Returns true if the message should be printed in the given timestamp, otherwise returns false.
    If this method returns false, the message will not be printed.
    The timestamp is in seconds granularity.
    :type timestamp: int
    :type message: str
    :rtype: bool
    """
    while len(heap):
        if heap[0][0] <= timestamp:
            temp = heapq.heappop(heap)
            cache.pop(temp[1])
        else:
            break
    if timestamp < cache.get(message, 0):
        return False
    cache[message] = timestamp + 10
    heapq.heappush(heap, (timestamp + 10, message))
    return True
