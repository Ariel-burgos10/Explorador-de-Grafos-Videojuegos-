from grafo import Grafo


def main():

    grafo = Grafo()

    # Cargar grafo desde archivo
    grafo.load_from_json("../data/grafo.json")

    # Mostrar estructura del grafo
    grafo.show_graph()


if __name__ == "__main__":
    main()