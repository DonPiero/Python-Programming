class Matrix:
    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.data = [[0] * m for _ in range(n)]

    def get(self, i, j):
        return self.data[i][j]

    def set(self, i, j, val):
        self.data[i][j] = val

    def transpose(self):
        self.data = [[self.data[j][i] for j in range(self.n)] for i in range(self.m)]
        self.n, self.m = self.m, self.n

    def multiply(self, other):
        if self.m != other.n:
            raise ValueError("Number of columns (first matrix) must be equal to the number of rows (second matrix)!")
        result = Matrix(self.n, other.m)
        for i in range(self.n):
            for j in range(other.m):
                for k in range(self.m):
                    result.data[i][j] += self.data[i][k] * other.data[k][j]
        return result

    def apply(self, transformation):
        for i in range(self.n):
            for j in range(self.m):
                self.data[i][j] = transformation(self.data[i][j])

    def __str__(self):
        return "\n".join([" ".join(map(str, n)) for n in self.data])


firstMatrix = Matrix(2, 3)
secondMatrix = Matrix(3, 2)

firstMatrix.set(0, 0, 1)
firstMatrix.set(0, 1, 3)
firstMatrix.set(0, 2, 5)
firstMatrix.set(1, 0, 7)
firstMatrix.set(1, 1, 9)
firstMatrix.set(1, 2, 11)

secondMatrix.set(0, 0, 2)
secondMatrix.set(0, 1, 4)
secondMatrix.set(1, 0, 6)
secondMatrix.set(1, 1, 8)
secondMatrix.set(2, 0, 10)
secondMatrix.set(2, 1, 12)

print("First matrix:")
print(firstMatrix)
print("\nSecond Matrix:")
print(secondMatrix)

print("\nFirst matrix * Second matrix:")
print(firstMatrix.multiply(secondMatrix))

firstMatrix.transpose()
print("\nFirst matrix transposed:")
print(firstMatrix)

firstMatrix.apply(lambda x: x * 2)
print("\nFirst matrix transformed:")
print(firstMatrix)
