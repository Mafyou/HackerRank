# Complete the staircase function below.
def staircase(n):
    for tall in range(n):
        weight = 0
        for weight in range(n - tall - 1):
            print(' ', end='')
        for _ in range(n - weight - 1):
            print('#', end='')
        if tall != n - 1:
            print('')
    print('#')
if __name__ == '__main__':
    n = int(input())
    staircase(n)