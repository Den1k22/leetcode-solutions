"""
An image smoother is a filter of the size 3 x 3 that can be applied to each cell of an image by rounding down the average of the cell and the eight surrounding cells (i.e., the average of the nine cells in the blue smoother). If one or more of the surrounding cells of a cell is not present, we do not consider it in the average (i.e., the average of the four cells in the red smoother).

Given an m x n integer matrix img representing the grayscale of an image, return the image after applying the smoother on each cell of it.

Constraints:
m == img.length
n == img[i].length
1 <= m, n <= 200
0 <= img[i][j] <= 255
"""
from typing import List

class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        dictionary_for_4 = {}
        dictionary_for_6 = {}
        dictionary_for_9 = {}

        m = len(img)
        n = len(img[0])

        if (m == 1 and n == 1):
            return img

        result =[[0] * n for _ in range(m)]

        if (m == 1):
            for j in range(n):
                if (j == 0):
                    result[0][j] = (img[0][0] + img[0][1]) // 2
                elif(j == n - 1):
                    result[0][j] = (img[0][j] + img[0][j - 1]) // 2
                else:
                    result[0][j] = (img[0][j] + img[0][j - 1] + img[0][j + 1]) // 3

            return result
        elif (n == 1):
            for i in range(m):
                if (i == 0):
                    result[i][0] = (img[0][0] + img[1][0]) // 2
                elif(i == m - 1):
                    result[i][0] = (img[i][0] + img[i - 1][0]) // 2
                else:
                    result[i][0] = (img[i][0] + img[i - 1][0] + img[i + 1][0]) // 3

            return result


        for i in range(m):
            for j in range(n):
                sum = 0
                if (i == 0):
                    if (j == 0):
                        sum += img[0][0]
                        sum += img[0][1]
                        sum += img[1][0]
                        sum += img[1][1]

                        if sum not in dictionary_for_4:
                            dictionary_for_4[sum] = sum // 4

                        result[i][j] = dictionary_for_4[sum]
                    elif (j == n - 1):
                        sum += img[i][j]
                        sum += img[i][j - 1]
                        sum += img[i + 1][j]
                        sum += img[i + 1][j - 1]

                        if sum not in dictionary_for_4:
                            dictionary_for_4[sum] = sum // 4

                        result[i][j] = dictionary_for_4[sum]
                    else:
                        sum += img[i][j - 1]
                        sum += img[i][j]
                        sum += img[i][j + 1]
                        sum += img[i + 1][j - 1]
                        sum += img[i + 1][j]
                        sum += img[i + 1][j + 1]

                        if sum not in dictionary_for_6:
                            dictionary_for_6[sum] = sum // 6

                        result[i][j] = dictionary_for_6[sum]
                elif (i == m - 1):
                    if (j == 0):
                        sum += img[i][0]
                        sum += img[i][1]
                        sum += img[i - 1][0]
                        sum += img[i - 1][1]

                        if sum not in dictionary_for_4:
                            dictionary_for_4[sum] = sum // 4

                        result[i][j] = dictionary_for_4[sum]
                    elif (j == n - 1):
                        sum += img[i][j]
                        sum += img[i][j - 1]
                        sum += img[i - 1][j]
                        sum += img[i - 1][j - 1]

                        if sum not in dictionary_for_4:
                            dictionary_for_4[sum] = sum // 4

                        result[i][j] = dictionary_for_4[sum]
                    else:
                        sum += img[i][j - 1]
                        sum += img[i][j]
                        sum += img[i][j + 1]
                        sum += img[i - 1][j - 1]
                        sum += img[i - 1][j]
                        sum += img[i - 1][j + 1]

                        if sum not in dictionary_for_6:
                            dictionary_for_6[sum] = sum // 6

                        result[i][j] = dictionary_for_6[sum]
                elif (j == 0):
                    sum += img[i - 1][j]
                    sum += img[i][j]
                    sum += img[i + 1][j]
                    sum += img[i - 1][j + 1]
                    sum += img[i][j + 1]
                    sum += img[i + 1][j + 1]

                    if sum not in dictionary_for_6:
                        dictionary_for_6[sum] = sum // 6

                    result[i][j] = dictionary_for_6[sum]
                elif (j == n - 1):
                    sum += img[i - 1][j]
                    sum += img[i][j]
                    sum += img[i + 1][j]
                    sum += img[i - 1][j - 1]
                    sum += img[i][j - 1]
                    sum += img[i + 1][j - 1]

                    if sum not in dictionary_for_6:
                        dictionary_for_6[sum] = sum // 6

                    result[i][j] = dictionary_for_6[sum]
                else:
                    sum += img[i - 1][j - 1]
                    sum += img[i - 1][j]
                    sum += img[i - 1][j + 1]
                    sum += img[i][j - 1]
                    sum += img[i][j]
                    sum += img[i][j + 1]
                    sum += img[i + 1][j - 1]
                    sum += img[i + 1][j]
                    sum += img[i + 1][j + 1]

                    if sum not in dictionary_for_9:
                        dictionary_for_9[sum] = sum // 9

                    result[i][j] = dictionary_for_9[sum]
        
        return result

"""
Example 1:
Input: img = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[0,0,0],[0,0,0],[0,0,0]]
Explanation:
For the points (0,0), (0,2), (2,0), (2,2): floor(3/4) = floor(0.75) = 0
For the points (0,1), (1,0), (1,2), (2,1): floor(5/6) = floor(0.83333333) = 0
For the point (1,1): floor(8/9) = floor(0.88888889) = 0

Example 2:
Input: img = [[100,200,100],[200,50,200],[100,200,100]]
Output: [[137,141,137],[141,138,141],[137,141,137]]
Explanation:
For the points (0,0), (0,2), (2,0), (2,2): floor((100+200+200+50)/4) = floor(137.5) = 137
For the points (0,1), (1,0), (1,2), (2,1): floor((200+200+50+200+100+100)/6) = floor(141.666667) = 141
For the point (1,1): floor((50+200+200+200+200+100+100+100+100)/9) = floor(138.888889) = 138
"""

img = [[100,200,100],[200,50,200],[100,200,100]]

print(Solution().imageSmoother(img))


img = [[2,3]]
print(Solution().imageSmoother(img))

