def abi(a: list[int], b: list[int]) -> list[int]:
    """
    Add-Binary-Integers.
    EX 2.1-5
    """
    assert len(a) == len(b), 'Different size arrays...'

    move = 0
    c = []
    for i in range(len(a)):
        v = a[i] + b[i] + move
        move = v // 2
        c.append(v % 2)
    
    return c
