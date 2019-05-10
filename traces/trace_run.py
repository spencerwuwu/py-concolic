
import trace
from romanToInt import romanToInt

tracer = trace.Trace(count=True, trace=True)
tracer.runfunc(romanToInt, "IV")

results = tracer.results()
