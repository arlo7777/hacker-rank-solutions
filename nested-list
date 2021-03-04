# Practice / Python / Basic Data Types / Nested Lists

duplet = []
scores = []

if __name__ == '__main__':
    for _ in range(int(input())):
        name = input()
        score = float(input())
        
        duplet+=[[name, score]]
        scores+=[score]
    
        #we only need 1 value here, 
        #second to last which is at the beginning of the list, 
        #bc its a set    
    x=sorted(set(scores))[1] 
    
    for n, s in sorted(duplet):
        if s==x:
            print(n)
