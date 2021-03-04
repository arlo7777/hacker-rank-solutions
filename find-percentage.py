# Practice / Python / Basic Data Types / Finding the percentage 

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    summ=[]
    summ += student_marks[query_name]
    average = (sum(summ)/len(summ))
      
    average_formatted = "{:.2f}".format(average)
    
    print(average_formatted)
