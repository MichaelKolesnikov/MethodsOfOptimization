import random

def generate_random_matrix(n):
    matrix = [[random.randint(1, 9) for j in range(n)] for i in range(n)]
    return matrix

def print_markdown_matrix(matrix):
    m = len(matrix[0])
    print("| " * m + "|")
    print("| --- " * m + "|")
    for i in range(len(matrix)):
        print(f"|", end='')
        for j in range(len(matrix[i])):
            print(matrix[i][j], end='|')
        print()
    print()

def input_matrix(n):
    matrix = []
    for i in range(n):
        row = list(map(int, input().split()))
        matrix.append(row)
    return matrix

def main():
    generate = input()
    N = int(input())
    n = N + 1
    if generate:
        matrix = generate_random_matrix(n)
    else:
        matrix = input_matrix(n)
    for i in range(n):
        matrix[i][0] = i
    for j in range(n):
        matrix[0][j] = 0
    print_markdown_matrix(matrix)
    phi = [[0 for j in range(n)] for i in range(n)]
    x_ = [[0] * n for _ in range(n)]
    print(r"\[\phi_1(x)=\max\{f_1(x_1) \colon x_1 \in \overline{0,x}\}\]")
    for x in range(n):
        set_ = [matrix[i][1] for i in range(x + 1)]
        for item_number in range(len(set_)):
            if set_[item_number] > set_[x_[1][x]]:
                x_[1][x] = item_number
        phi[1][x] = max(phi[1][x - 1], matrix[x][1])
        print(fr"\[\phi_1({x})={phi[1][x]}, x_1^0={x_[1][x]}\]")
    print()
    for number in range(2, n):
        print(rf"\[\phi_{number}(x)=\max" + r"\{" + fr"f_{number}(x_{number}) + \phi_{number - 1}(x - x_{number})" + r"\colon " +  f"x_{number}"  + r"\in \overline{0,x}\}\]")
        for x in range(1, n):
            set_ = [matrix[i][number] + phi[number - 1][x - i] for i in range(x + 1)]
            for item_number in range(len(set_)):
                if set_[item_number] > set_[x_[number][x]]:
                    x_[number][x] = item_number
            phi[number][x] = max(set_)
            print(r"\[" + r"\text{Текущее множество: }" + f"{tuple(set_)}" + r" \quad ")
            print(fr"\phi_{number}({x})={phi[number][x]}, x_{number}^0={x_[number][x]}\]")
        print()
    S = N
    i = N
    x_o = [0] * n
    print(r"\[")
    while S > 0:
        x_o[i] = x_[i][S]
        print(f"{i}->{x_[i][S]}" + r" \quad ", end='')
        S -= x_[i][S]
        print(fr"S={S}" + r" \quad ", end='')
        i -= 1
    print(r"\]")
    print(rf"\[x^o=({", ".join(map(str, x_o[1:]))})\]")
    print(r"\[" + "+".join(str(matrix[x_o[i]][i]) for i in range(1, n)) + rf" = {phi[N][N]}\]")


if __name__ == "__main__":
    main()

'''
possible inputs:
4
0 0 0 0 0
1 3 4 5 7
2 8 2 3 10
3 5 6 2 1
4 4 3 3 2

3
0 0 0 0
1 2 3 2
2 4 5 7
3 6 8 8

6
0 0 0 0 0 0 0
1 3 4 7 7 2 3
2 4 3 5 8 1 2
3 8 5 1 9 2 5
4 2 7 2 4 9 6
5 9 3 3 6 2 9
6 4 7 5 9 1 1
'''