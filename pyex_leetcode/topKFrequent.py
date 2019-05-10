from symbolic.args import symbolic, concrete
@symbolic(in0="abcdefg")
@symbolic(in1="abcdefg")
def topKFrequent( in0, in1, k):
    words = [in0, in1]
    count = collections.Counter(words)
    heap = [(-freq, word) for word, freq in count.items()]
    heapq.heapify(heap)
    return [heapq.heappop(heap)[1] for _ in xrange(k)]
