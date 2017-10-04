import numba
import sys
import builtins
profile = getattr(builtins, "profile", lambda x: x)

@profile
@numba.jit
def piNumba(n):
  pi = 2.0
  for i in range(1,n):
    tmp = 4*i**2
    pi*=tmp/(tmp-1)
  return pi

if __name__ == "__main__":
  print(piNumba(int(sys.argv[1])))
