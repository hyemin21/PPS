def solution(x: int) -> bool:
    return x % sum(int(digit) for digit in str(x)) == 0
