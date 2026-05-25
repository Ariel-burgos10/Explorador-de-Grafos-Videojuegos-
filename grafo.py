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
    


    def dfs(self, start, finish):
        """
        Implementación de Búsqueda en Profundidad (DFS).
        Retorna el orden de visita y el camino encontrado.
        """
        visitados = set()
        # La pila guarda tuplas:
        pila = [(start, [start])]
        orden_visita = []

        while pila:
            # LIFO: Last In, First Out (Sacamos el último elemento añadido)
            nodo_actual, camino = pila.pop()

            if nodo_actual not in visitados:
                visitados.add(nodo_actual)
                orden_visita.append(nodo_actual)

                # Si encontramos el objetivo, mostramos los resultados y terminamos
                if nodo_actual == finish:
                    print("\n" + "="*40)
                    print("RESULTADOS DFS (Búsqueda en Profundidad)")
                    print("="*40)
                    print(f"Orden de exploración: {orden_visita}")
                    print(f"Camino encontrado: {' -> '.join(camino)}")
                    print(f"Número de aristas (pasos): {len(camino) - 1}")
                    print("NOTA: Este camino encontrado por DFS puede NO ser el más corto.")
                    print("="*40 + "\n")
                    return orden_visita, camino

                # Buscamos los vecinos. 
                # Usamos reversed() para que el comportamiento en la pila siga el orden lógico 
                vecinos = self.adj_list.get(nodo_actual, [])
                for vecino in reversed(vecinos):
                    if vecino not in visitados:
                        # Añadimos a la pila el vecino y el nuevo camino actualizado
                        pila.append((vecino, camino + [vecino]))

        # Si la pila se vacía y no encontramos el 'finish'
        print("\nDFS: No se encontró ningún camino hacia el destino.")
        return orden_visita, None