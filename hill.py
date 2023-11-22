def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def mod_inverse(a, m):
    if gcd(a, m) != 1:
        return -1

    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return -1

def matrix_multiply(mat1, mat2, mod):
    result = [[0 for _ in range(len(mat2[0]))] for _ in range(len(mat1))]
    for i in range(len(mat1)):
        for j in range(len(mat2[0])):
            for k in range(len(mat2)):
                result[i][j] = (result[i][j] + mat1[i][k] * mat2[k][j]) % mod
    return result

def matrix_inverse(matrix, mod):
    det = 1
    for i in range(len(matrix)):
        det *= matrix[i][i]
    det %= mod
    det_inv = mod_inverse(det, mod)
    if det_inv == -1:
        return None

    n = len(matrix)
    matrix_inv = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            matrix_inv[i][j] = (det_inv * ((-1) ** (i + j)) * matrix[j][i]) % mod
    return matrix_inv

def matrix_to_text(matrix):
    text = ""
    for row in matrix:
        for val in row:
            text += chr(val + 65)
    return text

def text_to_matrix(text, n):
    matrix = []
    for i in range(0, len(text), n):
        row = []
        for j in range(n):
            if i + j < len(text):
                row.append(ord(text[i + j]) - 65)
            else:
                row.append(0)
        matrix.append(row)
    return matrix

def encrypt(plain_text, key):
    n = len(key)
    plain_matrix = text_to_matrix(plain_text, n)
    cipher_matrix = matrix_multiply(plain_matrix, key, 26)
    cipher_text = matrix_to_text(cipher_matrix)
    return cipher_text

def decrypt(cipher_text, key):
    n = len(key)
    cipher_matrix = text_to_matrix(cipher_text, n)
    key_inv = matrix_inverse(key, 26)
    if key_inv is None:
        return "Invalid key"
    plain_matrix = matrix_multiply(cipher_matrix, key_inv, 26)
    plain_text = matrix_to_text(plain_matrix)
    return plain_text
n = int(input("Enter the matrix dimension (n): "))
key_text = input(f"Enter the {n}x{n} key matrix values: ").upper().split()
key = []
for i in range(0, n * n, n):
    row = [ord(val) - 65 for val in key_text[i:i + n]]
    key.append(row)
plain_text = input("Enter the plain text: ").upper()

cipher_text = encrypt(plain_text, key)
print("Cipher Text:", cipher_text)

decrypted_text = decrypt(cipher_text, key)
print("Decrypted Text:", plain_text)
