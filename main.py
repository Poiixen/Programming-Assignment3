def readinput():
    K = int(input().strip())
    values = {}
    for i in range(K):
        key, value = input().split()
        values[key] = int(value)
        
    A = input().strip()
    B = input().strip()
    return values, A, B



def main():
    values, A, B = readinput()
    print(values)
    print(A)
    print(B)
    
if __name__ == "__main__":
    main()