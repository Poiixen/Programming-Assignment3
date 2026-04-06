def readinput():
    K = int(input().strip())
    values = {}
    for i in range(K):
        key, value = input().split()
        values[key] = int(value)
        
    A = input().strip()
    B = input().strip()
    return values, A, B

def dynamic_programming(values, A, B):
    rows = len(A) + 1
    cols = len(B) + 1
    
    dp = [[0 for i in range(cols)] for j in range(rows)]
    
    for i in range(1, rows):
        for j in range(1, cols):
            if A[i-1] == B[j-1]:
                # chooses best value at i j by taking the max between skipping A, skipping B, or matching characters and adding
                dp[i][j] = max(dp[i-1][j], dp[i][j-1],dp[i-1][j-1]+values[A[i-1]])
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp 

def main():
    values, A, B = readinput()
    #print(values)
    #print(A)
    #print(B)
    dp = dynamic_programming(values, A, B)
    
    #prints the dp table VVV
    for row in dp:
        print(row)
        
        
    #prints max value VVV    
    print(dp[len(A)][len(B)])
    
    
if __name__ == "__main__":
    main()