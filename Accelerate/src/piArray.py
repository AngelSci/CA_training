import numpy as np
import sys
import builtins
profile = getattr(builtins, "profile", lambda x: x)

@profile
def piArray(n):
  series=np.arange(1,n)**2*4.
  series/=(series-1)
  return 2.*series.prod()

if __name__ == "__main__":
  print(piArray(int(sys.argv[1])))
