import json
from arista import Arista
from collections import deque


class Grafo:

    def __init__(self):

        self.adj_list = {}
        self.aristas = []
    # CREAR NODO

    def add_node(self, nodo):

        if nodo not in self.adj_list:

            self.adj_list[nodo] = []

 
    # CREAR ARISTA


    def add_edge(self, origen, destino):

        self.add_node(origen)
        self.add_node(destino)

        arista = Arista(origen, destino)

        self.aristas.append(arista)

        # Grafo dirigido
        self.adj_list[origen].append(destino)


    # CARGAR DESDE JSON


    def load_from_json(self, file_path):

        with open(file_path, "r") as file:

            data = json.load(file)

        # Crear nodos
        for nodo in data["nodes"]:

            self.add_node(nodo)

        # Crear aristas
        for origen, destino in data["edges"]:

            self.add_edge(origen, destino)


    def show_graph(self):

        print("\n===== GRAFO DEL VIDEOJUEGO =====\n")

        for nodo, vecinos in self.adj_list.items():

            print(f"{nodo} -> {vecinos}")


# Modelo bfs
    def bfs(self, inicio, objetivo):

        cola = deque()

        cola.append(inicio)

        visitados = set()

        visitados.add(inicio)

        padre = {}

        orden_visita = []

        while cola:

            actual = cola.popleft()

            orden_visita.append(actual)

            # Si encontramos el objetivo
            if actual == objetivo:

                camino = []

                while actual != inicio:

                    camino.append(actual)

                    actual = padre[actual]

                camino.append(inicio)

                camino.reverse()

                print("\n===== BFS =====")

                print("\nOrden de exploracion:")
                print(orden_visita)

                print("\nCamino mas corto:")
                print(" -> ".join(camino))

                print("\nNumero de pasos:")
                print(len(camino) - 1)

                return camino

            # Explorar vecinos
            for vecino in self.adj_list[actual]:

                if vecino not in visitados:

                    visitados.add(vecino)

                    padre[vecino] = actual

                    cola.append(vecino)

        print("\nNo existe camino")

        return None