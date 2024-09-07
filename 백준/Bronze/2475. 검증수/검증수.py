input_data = input()
A, B, C, D, E = input_data.split()
A, B, C, D, E = int(A), int(B), int(C), int(D), int(E)

verify_num = ((A ** 2) + (B ** 2) + (C ** 2) + (D ** 2) + (E ** 2)) % 10
print(verify_num)