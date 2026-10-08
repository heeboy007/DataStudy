
A, B = {1, 2, 3, 4}, {3, 4, 5}
print(A | B, A & B, A - B, A ^ B)
# {1, 2, 3, 4, 5}, {3, 4}, {1, 2}, {1, 2, 5}
print({3, 4} <= A, A <= B)
# True False
print(type({}), type(set()))
# dict set

edges = [(1, 2), (2, 1), (2, 3), (3, 2), (1, 2)]
print(len(set(edges)))
# 4
print(len({ frozenset(e) for e in edges }))
# 2 
