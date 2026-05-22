import json
from arista import Arista


class Grafo:

    def __init__(self):
        self.adj_list = {}
        self.aristas = []

    # Crear nodo
    def add_node(self, nodo):

        if nodo not in self.adj_list:
            self.adj_list[nodo] = []

    # Crear arista
    def add_edge(self, origen, destino):

        arista = Arista(origen, destino)
        self.aristas.append(arista)

        self.adj_list[origen].append(destino)
        self.adj_list[destino].append(origen)

    # Cargar desde JSON
    def load_from_json(self, file_path):

        with open(file_path, "r") as file:
            data = json.load(file)

        # Crear nodos
        for nodo in data["nodes"]:
            self.add_node(nodo)

        # Crear conexiones
        for origen, destino in data["edges"]:
            self.add_edge(origen, destino)

    # Mostrar grafo
    def show_graph(self):

        print("GRAFO DEL VIDEOJUEGO:\n")

        for nodo, vecinos in self.adj_list.items():
            print(f"{nodo}: {vecinos}")