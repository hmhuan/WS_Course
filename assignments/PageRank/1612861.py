input_dir = "Data/web-NotreDame.txt"

def readFile(input_dir):
    f = open(input_dir, 'r')

    #read 4 times unnecessary info
    x = f.readline()
    x = f.readline()
    x = f.readline()
    x = f.readline()

    

    #start read graph
    data = f.read().split() #this is a list [(center_1, point_1), (center_2, point_2), ...]
    all_point = len(data) #number of point (maybe have loop)
    #print(data)
    G = dict()
    index = 0 #index of list data
    while(True):
        
        center, point = int(data[index]), int(data[index+1])  #point will point to center
        
        if (center in G) == False:
            G[center] = []
        
        G[center].append(point) #add value
        index += 2 #update index

        if (index == all_point):
            break
    f.close()
    return G



def toy_graph():
    G = dict()

    G[0] = [1, 2, 3]
    G[1] = [0, 3]
    G[2] = [0]
    G[3] = [1, 2]
    
    return G

def pagerank(G, iteration_count=100):
    N = len(G.keys()) 
    next_rank_lst = [1/N for _ in range(N)] 
    current_rank_lst = next_rank_lst[:] 

    for i in range(iteration_count): 
        current_rank_lst, next_rank_lst = next_rank_lst, current_rank_lst 
        for j in range(N): 
            next_rank_lst[j] = 0 
        for node in G: 
            if G[node]: 
                contribution = current_rank_lst[node] / len(G[node])
                # print(contribution)
                # print("next rank list: ",next_rank_lst)
                # print("node: ",node)
                # print("G[node] = ", G[node])
                # print("----------------------------------------")
                for edge in G[node]: 
                    next_rank_lst[edge] += contribution 
                # print("next rank list: ",next_rank_lst)
                # print("----------------------------------------------------------------")
    return next_rank_lst
 







def main():

    G = readFile(input_dir)
    


    #G = toy_graph()
    #print(G[0])
    #rank_lst = pagerank(G)
    #print(rank_lst)
    # print(sum(rank_lst)) # sum = 1


    print("------------FINISH-----------")


if __name__ == '__main__':
    main()


