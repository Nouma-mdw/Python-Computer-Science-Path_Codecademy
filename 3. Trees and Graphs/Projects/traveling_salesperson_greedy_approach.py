import random
from random import randrange
from Graph import Graph
from Vertex import Vertex

def print_graph(graph):
  for vertex in graph.graph_dict:
    print("")
    print(vertex + " connected to")
    vertex_neighbors = graph.graph_dict[vertex].edges
    if len(vertex_neighbors) == 0:
      print("No edges!")
    for adjacent_vertex in vertex_neighbors:
      print("=> " + adjacent_vertex)

def build_tsp_graph(directed):
  g = Graph(directed)
  vertices = []
  for val in ['a', 'b', 'c', 'd']:
    vertex = Vertex(val)
    vertices.append(vertex)
    g.add_vertex(vertex)

  g.add_edge(vertices[0], vertices[1], 3)
  g.add_edge(vertices[0], vertices[2], 4)
  g.add_edge(vertices[0], vertices[3], 5)
  g.add_edge(vertices[1], vertices[0], 3)
  g.add_edge(vertices[1], vertices[2], 2)
  g.add_edge(vertices[1], vertices[3], 6)
  g.add_edge(vertices[2], vertices[0], 4)
  g.add_edge(vertices[2], vertices[1], 2)
  g.add_edge(vertices[2], vertices[3], 1)
  g.add_edge(vertices[3], vertices[0], 5)
  g.add_edge(vertices[3], vertices[1], 6)
  g.add_edge(vertices[3], vertices[2], 1)
  return g

# Define your functions below:
# print_graph(build_tsp_graph(True))

# helper funtion for identifying visited vertices
def visited_vertices(container_visited_vertices):
  for vertex in container_visited_vertices:
    if container_visited_vertices[vertex] == "unvisited":
      return False
  return True

def traveling_salesperson(graph):
  path = ""
  # dp_caché: keep count of visited vertices to prevent repetitions
  visited_dict = {x: "unvisited" for x in graph.graph_dict}
  # print(list(graph.graph_dict))
  current_vertex = random.choice(list(graph.graph_dict))
  visited_dict[current_vertex] = "visited"
  path += current_vertex
  # return False as long as unvisited vertices exists
  visited_all = visited_vertices(visited_dict)
  # iretate while unvisited vertices exist
  while not visited_all:
    # access edges over attributes (instructions use methods)
    current_vertex_edge_weight = {edge: weight  for edge, weight in graph.graph_dict[current_vertex].edges.items()}
    # get next vertex
    found_next_vertex = False
    next_vertex = ""
    while not found_next_vertex:
      if current_vertex_edge_weight is None:
        break # danger: infinite loop
      # greedy approach to next vertex, by choosing vertix with shortest edge (edge with lowest weight)
      min_edge_vertex = min(current_vertex_edge_weight, key=current_vertex_edge_weight.get)
        # print to check method
      print("Get weight from min_edge_vertex:", current_vertex_edge_weight.get(min_edge_vertex))

      # select vertex with min edge among unvisted vertices
      if visited_dict[min_edge_vertex] == "unvisited":
        # end inner loop and update next_vertex
        found_next_vertex = True
        next_vertex = min_edge_vertex
      else:
        current_vertex_edge_weight.pop(min_edge_vertex)
      # check if last vertex has been reached, to end the outer loop
      if current_vertex_edge_weight is None:
        visited_all_vertices = True
      else:
        # update current_vertex, mark as visited and add to tsp path
        current_vertex = next_vertex
        visited_dict[current_vertex] = "visited"
        path += "\n" + current_vertex
        visited_all = visited_vertices(visited_dict)
  print(path)
        
# testing
route = build_tsp_graph(True)

# calling TSP
traveling_salesperson(route)







