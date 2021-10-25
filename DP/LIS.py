#Longest_Increasing_subsequence
#sequence length n
#length of the longest increasing subsequence 

#example 3,1,8,2,5
#example_Ans 1,2,5

#First. Focus on Length 
#Second, (Find an appropriate subproblem)
#Here, Subproblem: LIS[k] = LIS ending at index k
#Find relationships among subprobelms
#Find the longest increasing subproblem ending at index k
#discovered that if you wanna find the LIS ending at index 4
#you would need max{LIS[0],LIS[1],LIS[3]}, since 0,1,3 are the ones connected to index 4
#Generalize the relationship
#LIS[n] = a+ max{LIS[k]|k<n,A[k] < A[n]}

def lis(A):
    L = [1] * len(A)
    for i in range(1, len(L)):
        subproblems = [L[k] for k in range(i) if A[k] < A[i]]
        print ("subproblems", subproblems)
        L[i] = 1 + max(subproblems, default = 0)
    return max(L, default=0)

"""
EXAMPLE: A = [3,1,8,2,5]
FIRST FIND SUBPROBLEM
    LIS for A[4] = 1 + maxLIS{A[0],A[1],A[3]}
GENERALIZE THE RELATIONSHIP
    LIS For A[k] = 1 + maxLIS{A[m]| m < k and A[m] < A[k]}
CODE

"""

def test():
    A = [3,1,8,2,5]
    lis(A)
test()
