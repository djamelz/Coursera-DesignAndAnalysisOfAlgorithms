__author__ = 'Djamel'

import custom_heap as ch


def compute(file, filtered_result=False):
    graph = dict()
    with open(file) as f:
        for line in f:
            vertex_and_length = []
            items = line.rstrip("\n").rstrip("\r").rstrip("\t").split("\t")
            for item in items[1:]:
                l = item.split(",")
                vertex_and_length.append((l[0], int(l[1])))
            graph[items[0]] = vertex_and_length

    shortest_paths = djikstra2(graph, "1")
    filtered_shortest_paths = ""

    if filtered_result:
        index = ["7", "37", "59", "82", "99", "115", "133", "165", "188", "197"]
        filtered_shortest_paths += "".join(str(shortest_paths[x]) + "," for x in index)
    else:
        filtered_shortest_paths += "".join(str(shortest_paths[x]) + "," for x in sorted(shortest_paths.iterkeys()))

    return filtered_shortest_paths.rstrip(',')


def djikstra2(graph, source):

    shortest_path = dict()
    shortest_path[source] = 0

    for destination in graph:

        if not destination in shortest_path:

            heap = ch.CustomHeap()
            visited = set()

            for vertex_and_length in graph[source]:
                heap.insert((vertex_and_length[1], vertex_and_length[0]))
                visited.add((vertex_and_length[0], source))

            heap_item = heap.pop_min()

            while heap_item is not None and heap_item[1] != destination:

                for vertex_and_length in graph[heap_item[1]]:
                    length = heap_item[0] + vertex_and_length[1]
                    vertex = vertex_and_length[0]
                    if (not (vertex, heap_item[1]) in visited) or (vertex == destination):
                        heap.insert((length, vertex))
                        visited.add((vertex, heap_item[1]))

                heap_item = heap.pop_min()

            if heap_item is None:
                shortest_path[destination] = 1000000
            else:
                shortest_path[destination] = heap_item[0]
    return shortest_path