import numpy as np
path = []
def banker( allocated , available, need , pNo, rNo):

        visited = [False]*len(pNo)
        for i in pNo:
                for j in pNo:    
                        flag = False 
                        # for each process if there is any needed resource that has bigger amount than available resources 
                        # then set flag to true wich means process can not execute
                        for k in rNo:
                                if need[j][k] > available[k] or visited[j]:
                                        flag = True
                        if flag == False:
                                visited[j] = True
                                path.append(j)
                                for k in rNo:
                                        available[k] += allocated[j][k]
                                print(available)
                                if not (False in visited):
                                        print("path ",path)
                                        return
                                        
        print("there is not a path to safe state")
          
print("Enter number of processes")
pNo = int(input())
print("Enter number of resources")
rNo =  int(input())
max =   [[7, 5, 3], 
        [3, 2, 2],
        [9, 0, 2],
        [2, 2, 2],
        [4, 3, 3]]

allocated = [[0, 1, 0],
             [2, 0, 0],
             [3, 0, 2], 
             [2, 1, 1],
             [0, 0, 2]] 

available = [3, 3, 2] 

pNo = range(0,pNo)
rNo = range(0,rNo)
# print("Enter maximum resources needed for each process")
# for i in pNo:
#         print("prosess "+ str(i+1))
#         input_string = input("resources")
#         max[i] = input_string.split()
#         for j in rNo:
#                 max[i][j] = int(max[i][j])


# print("Enter allocated resources to each process")
# for i in pNo:
#         print("prosess "+ str(i+1))
#         input_string = input("resources")
#         allocated[i] = input_string.split()
#         for j in rNo:
#                 allocated[i][j] = int(allocated[i][j])
# print("Enter available resources")
# for j in rNo:
#         print("resource " + str(j+1))
#         available[j] = int(input())
ar1 = np.array(max)
ar2 = np.array(allocated)
need = np.subtract(ar1,ar2)
print(need, '\n')

banker(allocated,available,need, pNo, rNo)

                