def readinput():
    K = int(input().strip())
    values = {}
    for _ in range(K):
        key, value = input().split()
        values[key] = int(value)
        
    A = input().strip()
    B = input().strip()
    return values, A, B

def dynamic_programming(values, A, B):
    rows = len(A) + 1
    cols = len(B) + 1
    
    dp = [[0 for i in range(cols)] for j in range(rows)] # 2d table for manipulation
    
    for i in range(1, rows):
        for j in range(1, cols):
            #goes through each cell in the table, 
            if A[i-1] == B[j-1]:
                # chooses best value at i j by taking the max between skipping A, skipping B, or matching characters and adding
                dp[i][j] = max(dp[i-1][j], dp[i][j-1],dp[i-1][j-1]+values[A[i-1]])
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp 

def reconstruction(dp, values, A, B):
    i = len(A)
    j = len(B)
    result = []
    # start from bottom-right of DP table
    while i > 0 and j > 0:
        
        # checks if the characters match and were used to find the optimal
        if A[i-1] == B[j-1] and dp[i][j] == dp[i-1][j-1] + values[A[i-1]]:
            result.append(A[i-1])
            i -= 1
            j -= 1
        #checks if value came from skipping A
        elif dp[i][j] == dp[i-1][j]:
            i -= 1
        #skips b
        else:
            j -= 1
    return ''.join(reversed(result))

def main():
    values, A, B = readinput()
    dp = dynamic_programming(values, A, B)
    answer = reconstruction(dp, values, A, B)
    print(dp[len(A)][len(B)])
    print(answer)
    
    
    
if __name__ == "__main__":
    main()