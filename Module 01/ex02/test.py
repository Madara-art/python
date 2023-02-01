from vector import Vector

v1 = Vector([[1.], [2.], [3.]])
v2 = Vector([[1.0, 2.0, 3.0]])
# # print(v1.T().values)
# # print(v1.dot(v1))
# # v1.T()
# # print(v1.values)
# v1 = Vector([[0.0], [1.0], [2.0], [3.0]])
# v2 = v1 * 5
# print(v2)
# # Expected output:
# # Vector([[0.0], [5.0], [10.0], [15.0]])
# # Row vector of shape 1 * n
# v1 = Vector([[0.0, 1.0, 2.0, 3.0]])
# v2 = v1 * 5
# print(v2)
# # Expected output
# # Vector([[0.0, 5.0, 10.0, 15.0]])
# v2 = v1 / 2.0
# print(v2)
# # Expected output
# # Vector([[0.0], [0.5], [1.0], [1.5]])
# # v1 / 0.0
# # # Expected ouput
# # # ZeroDivisionError: division by zero.
# v2 / v1
# # Expected output:
# # NotImplementedError: Division of a scalar by a Vector is not defined here.
# # 8
print(eval(repr(v1)).shape)
