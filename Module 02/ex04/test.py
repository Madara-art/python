from TinyStatistician import TinyStatistician
tstat = TinyStatistician()
# a = [1, 2, 3, 10, 12, 13, 14]
# print(tstat.median(a))
def median(numbers):
  n = len(numbers)
  s = sorted(numbers)
  return (s[n//2 - 1] + s[n//2]) / 2 if n % 2 == 0 else s[n//2]

b = [1, 42, 300, 10, 59]
# print(median(a))
# print(tstat.mean(a))
# print(tstat.median(a))
# print(tstat.quartiles(a))

import numpy as np

a = np.array(b)

q1 = np.quantile(a, .25,method='midpoint')
q2 = np.quantile(a, .50,method='midpoint')
q3 = np.quantile(a, .75,method='midpoint')


print("Q1:",tstat.quartiles(b)[0])
print("Q2:",tstat.median(b))
print("Q3:",tstat.quartiles(b)[1])
print("Var:",tstat.var(b))
print("std:",tstat.std(b))

# print("Q1:", q1)
# print("Q2:", q2)
# print("Q3:", q3)