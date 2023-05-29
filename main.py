def upper_triangle(matrix):
    n = len(matrix)
    det = 1

    for i in range(n):
        if matrix[i][i] == 0:
            # Jika elemen diagonal utama nol, tukar baris dengan baris di bawahnya yang memiliki elemen diagonal tidak nol
            for j in range(i+1, n):
                if matrix[j][i] != 0:
                    matrix[i], matrix[j] = matrix[j], matrix[i]
                    det *= -1
                    break

        if matrix[i][i] == 0:
            # Jika tidak ada baris di bawahnya dengan elemen diagonal tidak nol, determinan menjadi nol
            return 0

        for j in range(i+1, n):
            factor = matrix[j][i] / matrix[i][i]
            for k in range(i, n):
                matrix[j][k] -= factor * matrix[i][k]

    # Hitung determinan dari matriks segitiga atas dengan mengalikan elemen diagonal utama
    for i in range(n):
        det *= matrix[i][i]

    return det

# Main program
n = int(input("Masukkan ukuran matriks: "))

matrix = []
print("Masukkan elemen-elemen matriks:")
for _ in range(n):
    row = list(map(float, input().split()))
    matrix.append(row)

determinant = upper_triangle(matrix)
print("Determinan matriks:", determinant)