import json 
import networkx as nx
import matplotlib.pyplot as plt

with open('/home/StrobiHealth/GraphOmeter/graph.json') as json_data:
    forum_data = json.load(json_data)
    
# step 1: based on source json data this function creates nodes and edges and returns a graph dictionary 
def graph_parser(forum_data): 
    graph = dict()
    for vertex in forum_data: 
        node = vertex['node1']
        edge = vertex['node2']
        if node in graph:
            if edge in graph[node]:
                pass
            else: 
                graph[node].append(edge)
        else: 
            graph[node] = list()
            graph[node].append(edge)
    return graph

# step 2: the class object Graph has 3 main methods: call (generate edges), incoming (compute number of incoming edges) and summarize. 
class Graph(object):
    def __init__(self, input_dict):
        self.input_dict = input_dict
        self.nodes = input_dict.items()
        self.neighbors = input_dict.values()
        self.graph = nx.Graph()
 
    def __call__(self): 
        edge_list = []
        for node in self.input_dict:
            for neighbour in self.input_dict[node]:
                edge_list.append((node, neighbour))
        self.graph.add_edges_from(edge_list)  
 
    def incoming(self, node): 
        in_coming = []
        for item in self.nodes:
            if node in item[1]: 
                in_coming.append(item[0])
        return in_coming 
    
    def plot_graph(self, val_map): 
        display_graph = self.graph
        print(display_graph)
        #print(self.nodes)
        values = [val_map.get(node, 'gray') for node in self.graph.nodes()]
        options = {
        'node_size': 50,
        'width': 1,
        }        
        nx.draw(display_graph, cmap=plt.get_cmap('jet'), node_color=values, **options)
        plt.show()  

    def summarize(self):
        val_map = {}
        print("Most active forum participants:")
        for node in self.nodes:
            outcoming = node[1]
            incoming = self.incoming(node[0])
            if len(outcoming) == 2: 
                val_map[node[0]] = 'yellow'
            elif len(outcoming) == 3: 
                val_map[node[0]] = 'orange'             
            if len(outcoming) > 3: 
                val_map[node[0]] = 'red'                  
                print("{} --> {} outcoming edges and {} incoming edges".format(node[0],len(outcoming),len(incoming)))
        self.plot_graph(val_map)
        print("node color code based on number of outcoming edges. yellow: 2, orange: 3, red: 4 or more")
