from grafo import Grafo


def main():

    grafo = Grafo()

    grafo.load_from_json("grafo.json")
    grafo.show_graph()

    grafo.bfs("Start", "Finish")


main()