import cvxpy as cp
import numpy as np
# Arad Zekler 305600579
# Problem data.
matrix1 = [[81, 19, 0], [80, 0, 20]]

def egalitarianFunction(matrix):
    npMat = np.asmatrix(matrix)
    minimalValsArray = npMat.min(axis=1) # find minimal values of each row in matrix.
    minimalValsArrayNumPy = np.asmatrix(minimalValsArray)
    topMinimalCoeff = minimalValsArrayNumPy.max(axis=0)
    numOfRows = 0
    for i in range(0, len(minimalValsArray)):
        if minimalValsArray[i] == topMinimalCoeff:
            numOfRows = i
    resultArray = matrix[numOfRows]
    resultArray = np.squeeze(np.asarray(resultArray))
    x = cp.Variable()
    polyExp = resultArray[0]*x
    for want in range(1, len(resultArray)):
        polyExp += resultArray[want]
    resultProblem = cp.Problem(cp.Maximize(cp.log(polyExp)) , [x >= 0, x <= 1])  # construct the problem.
    resultProblem.solve()
    print(polyExp)
    print("status:", resultProblem.status)
    print("optimal value:", resultProblem.value)
    print("optimal x:", x.value)


egalitarianFunction(matrix1)
