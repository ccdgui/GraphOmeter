# GraphOmeter
## Graph presentation of patient interactions inside a Health Forum. 

### Overview 

GraphOmeter is a network study and visualization project to analyze interactions between users inside a Health Forum about migraine (message board). Participation inequality is a well-known concept in social media and online communities: user participation is often concentrated among few very active participants (the "90 - 9 - 1 rule"). The purpose of GraphOmeter is to identify the active participants and analyze how they are distributed and connected inside a Graph. 

### Output 
Graph representation of a health forum using Matplotlib. Each node represents a user, each edge represents a message posted to another user.

![network_health](https://user-images.githubusercontent.com/25650135/36640314-03d8e0fa-19ea-11e8-8bdc-a1f1dfa012e6.PNG)


### Outline 

The script graph_generator.py contains two main elements: 

  * graph_parser: this function parses the source json data, creates nodes and edges and returns dictionary. 

  * Class Object Graph: Object generates a Graph object using the networkx python package. Methods attached to this object: 
     * call() object generates graph edges using the 'add_edges_from()' helper function. 
     * incoming() method return a list of income edge for the node passed as argument.
     * plot_graph() generate parameters for plotting the grap. The val_map dictionary contain color parameter for each node 
     * summarize() method flags the most active nodes in the graph (2 outcoming edges or more) with a color code (yellow, orange, red)           and plots network graph. 
  
