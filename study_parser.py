import json 
from collections import defaultdict
import networkx as nx
import matplotlib.pyplot as plt


with open('/home/StrobiHealth/GraphOmeter/graph.json') as json_data:
    forum_data = json.load(json_data)
