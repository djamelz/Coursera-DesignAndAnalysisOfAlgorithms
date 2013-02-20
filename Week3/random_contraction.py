__author__ = 'Djamel'

import random
import datetime


def compute(file, iteration_number=None):
    vertices, edges = build_graph(file)

    min_cut = 0
    x = 0
    if iteration_number is None:
        iteration_number = len(vertices) ** 2
    for i in xrange(iteration_number):
        print datetime.datetime.now(), "(start, iteration #", i, "mincut:", min_cut, "last:", x, ")"
        x = random_contraction(list(vertices), list(edges))
        if x < min_cut or min_cut == 0: min_cut = x
    return min_cut


def build_graph(file):
    vertices = []
    edges = []
    with open(file) as f:
        for line in f:
            values = line.rstrip("\n").rstrip("\r").rstrip("\t").split("\t")
            vertices.append(values[0])
            for i in xrange(1, len(values)):
                edges.append((values[0], values[i]))
    return vertices, edges


def random_contraction(vertices, edges):
    graph_size = len(vertices)
    if graph_size < 3:
        return get_edge_size(vertices[0], edges)

    r_vertex, l_vertex = edges[random.randint(0, len(edges) - 1)]

    new_vertex = str(r_vertex) + "-" + str(l_vertex)
    new_edges = []

    for i in xrange(len(edges)):
        if edges[i][0] == r_vertex or edges[i][0] == l_vertex:
            if edges[i][1] != r_vertex and edges[i][1] != l_vertex:
                new_edges.append((new_vertex, edges[i][1]))
        elif edges[i][1] == r_vertex or edges[i][1] == l_vertex:
                new_edges.append((edges[i][0], new_vertex))
        else:
            new_edges.append(edges[i])

    vertices.remove(r_vertex)
    vertices.remove(l_vertex)
    vertices.append(new_vertex)

    return random_contraction(vertices, new_edges)


def get_edge_size(vertex, edges):
    edge_count = 0
    for edge in edges:
        if edge[0] == vertex: edge_count += 1
    return edge_count
