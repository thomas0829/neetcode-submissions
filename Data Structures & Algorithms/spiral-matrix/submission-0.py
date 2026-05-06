class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        left, right, top, buttom= 0, len(matrix[0]), 0, len(matrix)
        while left < right and top < buttom:
            for i in range(left, right):
                res.append(matrix[top][i])
            top += 1

            for i in range(top, buttom):
                res.append(matrix[i][right - 1])
            right -= 1

            if not (left < right and top < buttom):
                break

            for i in range(right - 1, left - 1, -1):
                res.append(matrix[buttom - 1][i])
            buttom -= 1

            for i in range(buttom - 1, top - 1, -1):
                res.append(matrix[i][left])
            left += 1

        return res
