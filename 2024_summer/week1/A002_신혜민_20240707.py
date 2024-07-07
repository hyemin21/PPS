'''
A002 - Pascal's Triangle
파스칼 삼각형의 rowNumber가 주어졌을 때, 그 삼각형의 각 값을 배열의 형태로 return하는 함수 작성한다.
'''
def generate(numRows):
    triangle = []
    for i in range(numRows):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = triangle[i-1][j-1] + triangle[i-1][j]
        triangle.append(row)
    return triangle

numRows = 5
print(generate(numRows))  
