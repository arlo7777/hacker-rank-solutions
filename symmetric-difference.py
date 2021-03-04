# Practice / Python / Basic Data Types / Symmetric Difference 

a = int(input())
set_a = set(input().split())
b = int(input())
set_b = set(input().split())
set_diff = set_a^set_b

print(*sorted(set_diff, key=int), sep='\n')
