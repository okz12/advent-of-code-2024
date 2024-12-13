from collections import Counter

if __name__ == "__main__":
    with open("input.txt") as f:
        left, right = zip(*(map(int, line.split()) for line in f))
    
    right_counts = Counter(right)
    print(sum(abs(x - y) for x, y in zip(sorted(left), sorted(right))))
    print(sum(x * right_counts[x] for x in left))
