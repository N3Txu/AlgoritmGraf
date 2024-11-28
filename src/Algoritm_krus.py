class Grafo:
    def __init__(self, vertices):
        self.V = vertices
        self.grafo = []

    def agregar_arista(self, u, v, w):
        self.grafo.append([u, v, w])

    def encontrar(self, padre, i):
        if padre[i] == i:
            return i
        return self.encontrar(padre, padre[i])

    def union(self, padre, rango, x, y):
        raiz_x = self.encontrar(padre, x)
        raiz_y = self.encontrar(padre, y)

        if rango[raiz_x] < rango[raiz_y]:
            padre[raiz_x] = raiz_y
        elif rango[raiz_x] > rango[raiz_y]:
            padre[raiz_y] = raiz_x
        else:
            padre[raiz_y] = raiz_x
            rango[raiz_x] += 1

    def kruskal_mst(self):
        resultado = []
        i = 0
        e = 0

        self.grafo = sorted(self.grafo, key=lambda item: item[2])

        padre = []
        rango = []

        for nodo in range(self.V):
            padre.append(nodo)
            rango.append(0)

        while e < self.V - 1:
            u, v, w = self.grafo[i]
            i = i + 1
            x = self.encontrar(padre, u)
            y = self.encontrar(padre, v)

            if x != y:
                e = e + 1
                resultado.append([u, v, w])
                self.union(padre, rango, x, y)

        costo_minimo = 0
        print("Aristas en el árbol generador mínimo:")
        for u, v, peso in resultado:
            costo_minimo += peso
            print(f"{u} -- {v} == {peso}")
        print(f"Costo del árbol generador mínimo: {costo_minimo}")

# Ejemplo de uso:
g = Grafo(4)
g.agregar_arista(0, 1, 10)
g.agregar_arista(0, 2, 6)
g.agregar_arista(0, 3, 5)
g.agregar_arista(1, 3, 15)
g.agregar_arista(2, 3, 4)

g.kruskal_mst()