
import builtins
profile = getattr(builtins, "profile", lambda x: x)

@profile
def sum_of_sums(size=20000):
    ints = list(range(size))
    sums = []
    for index in range(size):
        sum_to_end=sum(ints[index:])
        sums.append(sum_to_end)

if __name__ == "__main__":
    sum_of_sums()
