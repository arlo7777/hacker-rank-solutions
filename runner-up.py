# Practice / Python / Basic Data Types / Find the Runner-Up Score!

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    ordered = sorted(list(set(arr)))
    print(ordered[-2])
