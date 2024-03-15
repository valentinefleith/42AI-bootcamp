from my_minipack.loading import ft_progress
import time

if __name__ == "__main__":
    listy = range(1000)
    ret = 0
    for elem in ft_progress(listy):
        ret += (elem + 3) % 5
        time.sleep(0.001)
    print()
    print(ret)
