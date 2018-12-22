#libraries
import pickle
import json
import math as m
import statistics as stat
import collections

#bfs algorithm to find the shortest path between one node and all the nodes reachble from that node
def bfs(graph, root, shortest):
    queue = collections.deque()
    visited = set()
    visited.add(root)
    queue.append((root,0))
    depth = 0
    while queue:
        r,d = queue.popleft() #we keep the fist elements of the queue
        if d > depth: # increase depth only when we face the first node in the next depth               
            depth += 1
        try:
            for node in graph[r]:
                if node not in visited:
                    visited.add(node)
                    queue.append((node,depth+1)) #update the queue
                    shortest[node] += [depth+1] #update dictionary
        except:
            pass
    return shortest

#compute median over the shortest path lists, and make a rank of the categories
def distances_vector(cat_dict, dict_path, str_input, C0, isolated_nod):
    vector = [(str_input, -1, 0)]

    for key, value in cat_dict.items():
        distances = []
        if key != str_input:
            for art in value:
                distances += dict_path[art]
            total = len(value)*len(C0)
            if len(distances) != total: #there are infinite values (i.e. not connected nodes)
                #compute how many inf
                diff = (total - len(distances)) + isolated_nod[key]
                #add them to distances
                distances += diff*[m.inf]
            med_dist = stat.median(distances) #compute median
            n = distances.count(m.inf)
            n = n/len(distances)
            cat = (key, med_dist, round(n, 4))
            vector.append(cat)

    return vector

#save list in a .txt file
def save_list(file_name, list_):
    with open(file_name, "wb") as fp:
        pickle.dump(list_, fp)
    return

#load from .txt file as a list type
def load_saved_list(file_name):
    with open(file_name, "rb") as fp:   
        list_ = pickle.load(fp)
    return list_

#save dictionary in a .txt file
def save_dict(file_name, dict_):
    with open(file_name, 'w') as f:
        f.write(json.dumps(dict_))
    return

#load from .txt file as a dict type
def load_saved_dict(file_name):
    dict_ = json.load(open(file_name, 'rb'))
    return dict_