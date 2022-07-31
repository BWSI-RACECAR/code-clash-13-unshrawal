"""
Copyright MIT BWSI Autonomous RACECAR Course
MIT License
Summer 2022

Code Clash #13 - Matrix Multiplication (matmux.py)


Author: Ainsley Ward

Difficulty Level: 6/10

Prompt: You want to get ahead in your linear analysis class, so you decide to make a program 
that calculates the product of two 2x2 matrices. Your inputs should be two arrays, each 
representing a 2x2 matrix to be multiplied. (Don’t use numpy to solve this!!)

Test Cases:
input: m1 = [[4, 2],[3, 1]]; m2 = [[5, 6], [3, 8]]; output = [[26, 40], [18, 26]]
input: m1 = [[0, 0],[0, 0]]; m2 = [[5, 6], [3, 8]]; output = [[0, 0], [0, 0]]
input: m1 = [[14, 2],[7, 1]]; m2 = [[8, 6], [0, 8]]; output = [[112, 100], [56, 50]]
"""

class Solution:
    def matrix_mult(self,m1, m2):
        # type m1: list
        # type m2: list
        # return: List[List[int]]
        a1 = m1[0][0]
        a2 = m1[0][1]
        a3 = m1[1][0]
        a4 = m1[1][1]

        b1 = m2[0][0]
        b2 = m2[0][1]
        b3 = m2[1][0]
        b4 = m2[1][1]

        tl = a1*b1+a2*b3
        tr = a1*b2+a2*b4
        bl = a3*b1+a4*b3
        br = a3*b2+a4*b4

        return [[tl, tr], [bl, br]]
        # TODO: Write code below to return a nested list with the solution to the prompt
        pass

def main():
    array1 = input().split(" ")
    array2 = input().split(" ")
    array3 = input().split(" ")
    array4 = input().split(" ")

    for x in range (0, len(array1)):
        array1[x] = int(array1[x])

    for x in range (0, len(array2)):
        array2[x] = int(array2[x])

    for x in range (0, len(array3)):
        array3[x] = int(array3[x])

    for x in range (0, len(array4)):
        array4[x] = int(array4[x])

    ary1 = [array1,array2]
    ary2 = [array3,array4]

    tc1 = Solution()
    ans = tc1.matrix_mult(ary1,ary2)
    print(ans)

if __name__ == "__main__":
    main()