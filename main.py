def parallel_processing(n, m, linija2):
    output = []
    thrd = [[0, f] for f in range(n)]
    j = 0
    while j < m:
        minvert = min(thrd)
        laiks = linija2[j]
        output.append((minvert[1], minvert[0]))
        minvert[0] += laiks
        j += 1
    return output

def main():
    linija1 = list(map(int, input().strip().split()))
    n, m = linija1[0], linija1[1]
    linija2 = list(map(int, input().strip().split()))
    result = parallel_processing(n, m, linija2)
    for i, j in result:
        print(i, j)

if __name__ == "__main__":
    main()
