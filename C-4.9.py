def max_min(seq, n):
    """
    Finds maximum and minimum element in list recursively.
    :param seq: list of numbers
    :param n: size of said list
    :return: max and min number in the given list
    """
    if n == 0:
        print("n==0")
        return 0
    elif n == 1:
        print("n==1")
        return seq[0]
    elif n == 2:
        print("n==2", seq)
        if seq[0] >= seq[1]:
            return seq[0]
        else:
            return seq[1]
    else:
        print("n > 2", seq)
        if seq[0] >= seq[1]:
            return max_min(seq[:1]+seq[2:], n - 1)
        else:
            return max_min(seq[1:], n - 1)


if __name__ == "__main__":
    s = [int(i) for i in input().split()]
    print("maximum: ", max_min(s, len(s)))
    # similarly function for minimum