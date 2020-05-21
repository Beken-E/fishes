list1 = [4,3,2,1,5]
list2 = [0,1,0,0,0]
def solution(A, B):
    result = 0
    stack = []
    for i in range(0, len(A)):
        if B[i] == 1:
            stack.append(A[i])
            result += 1
    else:

        while(stack and A[i] > stack[-1]):
            stack.pop()
            result -= 1
        if(not stack):
            result += 1

    return result
    # upstream = {}
    # downstream = {}
    # commmon = zip(A,B)
    # counter = 0
    # for i in commmon:
    #     if i[1] == 0:
    #         upstream.update({counter: i[0]})
    #         counter += 1
    #     else:
    #         downstream.update({counter: i[0]})
    #         counter += 1
    # print(upstream)
    # print(downstream)
    # ualive = 0
    # dalive = 0
    # for i in A:
    #     if A.index(i) in upstream.keys():
    #         ualive +=1
    #     elif A.index(i) in downstream.keys():
    #         if A.index(i) < len(A) and A.index(i + 1) not in downstream.keys():
    #             dalive += 1
    #         elif A.index(i) == len(A):





    



print(solution(list1, list2))

