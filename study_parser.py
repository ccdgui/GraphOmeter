import json 
from collections import defaultdict
import networkx as nx
import matplotlib.pyplot as plt


with open('/home/StrobiHealth/GraphOmeter/graph.json') as json_data:
    forum_data = json.load(json_data)
    
#based on json data from the scaper creates nodes and edges and returns graph 
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
