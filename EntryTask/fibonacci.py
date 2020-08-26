def fib(n: int) -> int:
    global cnt
    cnt += 1
    if n < 2:
        return n
    return fib(n-2)+fib(n-1)

memo_dict = {0: 0, 1: 1}
def memo_fib(n: int) -> int:
    global cnt
    cnt += 1
    if n not in memo_dict:
        memo_dict[n] = memo_fib(n-2)+memo_fib(n-1)
    return memo_dict[n]

if __name__ == '__main__':
    cnt = 0
    #straightforward recursion
    print(fib(15), end='')
    print(", count = ", cnt) #very inefficient

    cnt = 0
    #with memoisation
    print(memo_fib(15), end='')
    print(", count = ", cnt) #better than straightforward recursion
