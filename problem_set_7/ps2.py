# 6.0002 Problem Set 5
# Graph optimization
# Name: Azeez
# Collaborators:
# Time:

#
# Finding shortest paths through MIT buildings
#

import unittest
from graph import Digraph, Node, WeightedEdge

#
# Problem 2: Building up the Campus Map
#
# Problem 2a: Designing your graph


# Problem 2b: Implementing load_map
def load_map(map_filename):
    """
    Parses the map file and constructs a directed graph

    Parameters:
        map_filename : name of the map file

    Assumes:
        Each entry in the map file consists of the following four positive
        integers, separated by a blank space:
            From To TotalDistance DistanceOutdoors
        e.g.
            32 76 54 23
        This entry would become an edge from 32 to 76.

    Returns:
        a Digraph representing the map
    """

    map_features = []
    map_mit = Digraph()
    print("Loading map from file...")

    # readinfg file and place content in a list of list
    infile = open(map_filename, 'r')
    for i in infile:
        temp = list(i.rstrip().split(' '))
        map_features.append(temp)
    # Creating the graph object9
    for val in map_features:
        # Creating and adding nodes
        src, dest, total_distance, outdoor_distance = Node(val[0]), Node(val[1]), int(val[2]), int(val[3])
        if map_mit.has_node(src) == False:
            map_mit.add_node(src)
        if map_mit.has_node(dest) == False:
            map_mit.add_node(dest)
        # Creating and adding edges #problem locarion
        w1 = WeightedEdge(src, dest, total_distance, outdoor_distance)
        map_mit.add_edge(w1)
    return(map_mit)

x = load_map('mit_map.txt')

# Problem 2c: Testing load_map
# Include the lines used to test load_map below, but comment them out

#
# Problem 3: Finding the Shorest Path using Optimized Search Method
#
# Problem 3a: Objective function
#
# What is the objective function for this problem? What are the constraints?
#
# Answer: Find the shortest path using DFS
# Constraint maximum distance outside must not be exceeded
#

# Problem 3b: Implement get_best_path
def get_best_path(digraph, start, end, path, max_dist_outdoors, best_dist,
                  best_path):
    """
    Finds the shortest path between buildings subject to constraints.

    Parameters:
        digraph: Digraph instance
            The graph on which to carry out the search
        start: string
            Building number at which to start
        end: string
            Building number at which to end
        path: list composed of [[list of strings], int, int]
            Represents the current path of nodes being traversed. Contains
            a list of node names, total distance traveled, and total
            distance outdoors.
        max_dist_outdoors: int
            Maximum distance spent outdoors on a path
        best_dist: int
            The smallest distance between the original start and end node
            for the initial problem that you are trying to solve
        best_path: list of strings
            The shortest path found so far between the original start
            and end node.

    Returns:
        A tuple with the shortest-path from start to end, represented by
        a list of building numbers (in strings), [n_1, n_2, ..., n_k],
        where there exists an edge from n_i to n_(i+1) in digraph,
        for all 1 <= i < k and the distance of that path.

        If there exists no path that satisfies max_total_dist and
        max_dist_outdoors constraints, then return None.
    """
    # Raise error if either start or end isn't in the graph
    if not (digraph.has_node(Node(start)) and digraph.has_node(Node(end))):
        raise ValueError('Node not in graph')

    # Seperating Path into it contituent variable
    path_nodes, path_dist, path_outdoor_dist = path
    # path_nodes = path_nodes + [start]
    path_nodes.append(start)
    # print(path_nodes, path_dist, path_outdoor_dist)

    # Recursion Base Case
    if start == end:
        # if path_outdoor_dist <= max_dist_outdoors:
        #     best_path = path_nodes
        #     # print(best_path)
        #     return (best_path)
        if path_dist <= best_dist:
            best_dist = path_dist
            best_path = path_nodes
            return (best_path, best_dist)

    for edge in digraph.get_edges_for_node(start):
        node = edge.get_destination()

        # print(type(path_nodes[0]))
        # print(path_nodes)
        if (node not in path_nodes):
            # Updating the distances
            path_dist = path_dist + edge.get_total_distance()
            path_outdoor_dist = path_outdoor_dist + edge.get_outdoor_distance()
            outdoor_distance_left = max_dist_outdoors - path_outdoor_dist
            # if best_path == None or path_dist < ...:
            new_path = get_best_path(digraph, node, end, [path_nodes, path_dist, path_outdoor_dist], max_dist_outdoors, best_dist, best_path)
            if new_path != None:
                best_path = new_path

    return (best_path, best_dist)
print(get_best_path(x, Node(1), Node(14), [[], 0, 0], 1000, 0, None))

"""
Optimization for Minimum distanc e outside 
Optimization for shortest path taking into consideration the lenght of tthe paths
Passing the Unit test (meeting the output criterias)
One MIT lecture
Understand what the unit test is actually doing
a 3K RUN 
"""

# Problem 3c: Implement directed_dfs
def directed_dfs(digraph, start, end, max_total_dist, max_dist_outdoors):
    """
    Finds the shortest path from start to end using a directed depth-first
    search. The total distance traveled on the path must not
    exceed max_total_dist, and the distance spent outdoors on this path must
    not exceed max_dist_outdoors.

    Parameters:
        digraph: Digraph instance
            The graph on which to carry out the search
        start: string
            Building number at which to start
        end: string
            Building number at which to end
        max_total_dist: int
            Maximum total distance on a path
        max_dist_outdoors: int
            Maximum distance spent outdoors on a path

    Returns:
        The shortest-path from start to end, represented by
        a list of building numbers (in strings), [n_1, n_2, ..., n_k],
        where there exists an edge from n_i to n_(i+1) in digraph,
        for all 1 <= i < k

        If there exists no path that satisfies max_total_dist and
        max_dist_outdoors constraints, then raises a ValueError.
    """
    # TODO
    pass


# ================================================================
# Begin tests -- you do not need to modify anything below this line
# ================================================================

# class Ps2Test(unittest.TestCase):
#     LARGE_DIST = 99999

#     def setUp(self):
#         self.graph = load_map("mit_map.txt")

#     def test_load_map_basic(self):
#         self.assertTrue(isinstance(self.graph, Digraph))
#         self.assertEqual(len(self.graph.nodes), 37)
#         all_edges = []
#         for _, edges in self.graph.edges.items():
#             all_edges += edges  # edges must be dict of node -> list of edges
#         all_edges = set(all_edges)
#         self.assertEqual(len(all_edges), 129)

#     def _print_path_description(self, start, end, total_dist, outdoor_dist):
#         constraint = ""
#         if outdoor_dist != Ps2Test.LARGE_DIST:
#             constraint = "without walking more than {}m outdoors".format(
#                 outdoor_dist)
#         if total_dist != Ps2Test.LARGE_DIST:
#             if constraint:
#                 constraint += ' or {}m total'.format(total_dist)
#             else:
#                 constraint = "without walking more than {}m total".format(
#                     total_dist)

#         print("------------------------")
#         print("Shortest path from Building {} to {} {}".format(
#             start, end, constraint))

#     def _test_path(self,
#                    expectedPath,
#                    total_dist=LARGE_DIST,
#                    outdoor_dist=LARGE_DIST):
#         start, end = expectedPath[0], expectedPath[-1]
#         self._print_path_description(start, end, total_dist, outdoor_dist)
#         dfsPath = directed_dfs(self.graph, start, end, total_dist, outdoor_dist)
#         print("Expected: ", expectedPath)
#         print("DFS: ", dfsPath)
#         self.assertEqual(expectedPath, dfsPath)

#     def _test_impossible_path(self,
#                               start,
#                               end,
#                               total_dist=LARGE_DIST,
#                               outdoor_dist=LARGE_DIST):
#         self._print_path_description(start, end, total_dist, outdoor_dist)
#         with self.assertRaises(ValueError):
#             directed_dfs(self.graph, start, end, total_dist, outdoor_dist)

#     def test_path_one_step(self):
#         self._test_path(expectedPath=['32', '56'])

#     def test_path_no_outdoors(self):
#         self._test_path(
#             expectedPath=['32', '36', '26', '16', '56'], outdoor_dist=0)

#     def test_path_multi_step(self):
#         self._test_path(expectedPath=['2', '3', '7', '9'])

#     def test_path_multi_step_no_outdoors(self):
#         self._test_path(
#             expectedPath=['2', '4', '10', '13', '9'], outdoor_dist=0)

#     def test_path_multi_step2(self):
#         self._test_path(expectedPath=['1', '4', '12', '32'])

#     def test_path_multi_step_no_outdoors2(self):
#         self._test_path(
#             expectedPath=['1', '3', '10', '4', '12', '24', '34', '36', '32'],
#             outdoor_dist=0)

#     def test_impossible_path1(self):
#         self._test_impossible_path('8', '50', outdoor_dist=0)

#     def test_impossible_path2(self):
#         self._test_impossible_path('10', '32', total_dist=100)

# if __name__ == "__main__":
#     # unittest.main()
#     ...
