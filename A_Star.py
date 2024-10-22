import queue 
def getHeuristics():
    heuristics = {}
    f = open("heuristics.txt")
    for i in f.readlines():
        node_heuristic_val = i.split()
        heuristics[node_heuristic_val[0]] = int(node_heuristic_val[1])

    return heuristics

def getCity () :
    city = {}
    citiesCode = {}
    f = open("cities.txt")
    j = 1
    for i in f.readlines() : 
        node_city_val = i.split()
        city[node_city_val[0]] = [int(node_city_val[1]), int(node_city_val[2])]
        citiesCode[j] = node_city_val[0]
        j += 1
    return city , citiesCode

def createGraph () :
    graph = {}
    f = open("citiesGraph.txt")
    for i in f.readlines() :
        node_val = i.split()
        
        if node_val[0] in graph and node_val[1] in graph :
            v = graph.get(node_val[0])
            v.append([node_val[1] , node_val[2]])
            graph.update({node_val[0] : v})
            
            v = graph.get(node_val[1])
            v.append([node_val[0] , node_val[2]])
            graph.update({node_val[1] : v})
            
        elif node_val[0] in graph :
            v = graph.get(node_val[0])
            v.append([node_val[1] , node_val[2]])
            graph.update({node_val[0] : v})
            
            graph[node_val[1]] = [[node_val[0] , node_val[2]]]
            
        elif node_val[1] in graph :
            v = graph.get(node_val[1])
            v.append([node_val[0] , node_val[2]])
            graph.update({node_val[1] : v})
            
            graph[node_val[0]] = [[node_val[1] , node_val[2]]]
            
        else :
            graph[node_val[1]] = [[node_val[0] , node_val[2]]]
            graph[node_val[0]] = [[node_val[1] , node_val[2]]]
            
    return graph
def a_star (start , heur , graph , goal = 'Bucharest') :
    priorityQueue = queue.PriorityQueue()
    distance = 0 
    path = []
    
    priorityQueue.put((heur[start] + distance , [start , 0]))
    while priorityQueue.empty() == False :
        c = priorityQueue.get()[1]
        path.append(c[0])
        distance += int(c[1])
        
        if c[0] == goal:
            break
            
        priorityQueue = queue.PriorityQueue()   
        
        for i in graph[c[0]] :
            if i[0] not in path :
                priorityQueue.put((heur[i[0]] + int(i[1]) + distance , i ))
    return path
def main () :
    heuristic = getHeuristics()
    graph = createGraph()
    city , citiesCode = getCity()
    
    for i,j in citiesCode.items():
        print(i,j)
        
    while True:
        inputCode = int(input("Enter your city's Number (0 to Exit) : "))
        
        if inputCode == 0 :
            break
        cityName = citiesCode[inputCode]
        aStar = a_star(cityName , heuristic , graph)
        print(f"A* => {aStar}")
main()