import heapq

def dijkstra(grafo, inicio, fin):
    # Cola de prioridad para almacenar tuplas (distancia, vértice)
    cola = [(0, inicio)]
    # Diccionario para almacenar la distancia más corta a cada vértice
    distancias = {vertice: float('inf') for vertice in grafo}
    distancias[inicio] = 0
    # Diccionario para almacenar el camino
    vertices_previos = {vertice: None for vertice in grafo}
    
    while cola:
        distancia_actual, vertice_actual = heapq.heappop(cola)
        
        # Si llegamos al vértice final, podemos detenernos
        if vertice_actual == fin:
            break
        
        # Si se ha encontrado un camino más corto al vértice_actual, saltar este
        if distancia_actual > distancias[vertice_actual]:
            continue
        
        # Explorar vecinos
        for vecino, peso in grafo[vertice_actual].items():
            distancia = distancia_actual + peso
            
            # Solo considerar este nuevo camino si es mejor
            if distancia < distancias[vecino]:
                distancias[vecino] = distancia
                vertices_previos[vecino] = vertice_actual
                heapq.heappush(cola, (distancia, vecino))
        
        # Imprimir pasos intermedios
        print(f"Vértice actual: {vertice_actual}, Distancias: {distancias}")
    
    # Reconstruir el camino más corto
    camino, vertice_actual = [], fin
    while vertices_previos[vertice_actual] is not None:
        camino.append(vertice_actual)
        vertice_actual = vertices_previos[vertice_actual]
    camino.append(inicio)
    camino = camino[::-1]
    
    # Imprimir el camino más corto y la distancia total
    print("\nCamino más corto:", " → " .join(camino))
    print("Distancia total:", distancias[fin])
# Ejemplo de grafo
grafo = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1, 'E': 3},
    'E': {'D': 3, 'F': 2},
    'F': {'E': 2, 'G': 1},
    'G': {'F': 1, 'H': 2},
    'H': {'G': 2}
}

# Ejecutar el algoritmo de Dijkstra
dijkstra(grafo, 'A', 'H') # Salida esperada: ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'], 12

