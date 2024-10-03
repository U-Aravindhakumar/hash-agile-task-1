def Arrayrotation(a, b, k):
    k = k % b
    for i in range(0, b):
        if(i < k):
            print(a[b + i - k], end = " ")
        else:
            print(a[i - k], end = " ")
    print("\n")
Array = [5,3,6,2,8,9]
N = len(Array)
K = int(input("Enter K value : "))
Arrayrotation(Array, N, K)
