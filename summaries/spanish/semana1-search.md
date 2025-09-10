# Semana 1 - Introducción a la Inteligencia Artificial

## Introducción al Curso
**Instructor:** Brian Yu

**Curso:** Introduction to Artificial Intelligence with Python

*“La IA no es magia; es una combinación de técnicas lógicas, estadísticas y computacionales que permiten simular el razonamiento humano.”*

### ¿Qué es IA?
IA abarca cualquier técnica que haga que una computadora actúe de manera inteligente o racional, como:
- Reconocimiento facial
- Jugar juegos mejor que humanos
- Comprender el lenguaje humano (como asistentes de voz)

## Temas cubiertos en el curso:
- **Search**: Enseñar a una IA cómo buscar soluciones a problemas (ej: routing, jugar juegos como tic-tac-toe)
- **Knowledge**: Representar y razonar con información para hacer inferencias lógicas
- **Uncertainty**: Manejar eventos inciertos usando probabilidad
- **Optimization**: Encontrar mejores (o las mejores) soluciones a problemas
- **Machine Learning**: Programar computadoras para aprender de datos y experiencia
- **Neural Networks**: Inspiradas en el cerebro humano, permiten resolver tareas complejas
- **Natural Language Processing**: Cómo las computadoras entienden y responden al lenguaje humano

## Introducción a la Inteligencia Artificial
La Inteligencia Artificial (IA) permite a las computadoras realizar tareas que típicamente requieren inteligencia humana, como reconocer patrones, resolver problemas y tomar decisiones. Este campo abarca algoritmos de búsqueda, representación de conocimiento, machine learning, redes neurales y procesamiento de lenguaje natural.

Los algoritmos de búsqueda forman la base de muchas aplicaciones de IA, desde sistemas de navegación hasta programas que juegan juegos. Estos algoritmos ayudan a encontrar caminos óptimos o secuencias de acciones para lograr objetivos específicos.

## Fundamentos de Problemas de Búsqueda
Los problemas de búsqueda involucran varios componentes clave:

- **Agent**: Entidad que percibe y actúa sobre su entorno
- **State**: Configuración del entorno en un momento dado  
- **Initial State**: Punto de inicio del proceso de búsqueda
- **Actions**: Movimientos posibles disponibles en cada estado
- **Transition Model**: Define cómo las acciones cambian estados
- **Goal Test**: Determina si un estado es la solución deseada
- **Path Cost**: Costo numérico asociado con caminos de solución

El proceso general de búsqueda sigue este patrón:
```pseudocode
function GENERAL-SEARCH(problem):
    frontier = {initial state}
    explored = empty set
    
    while frontier is not empty:
        node = remove node from frontier
        if node.state is goal state:
            return solution (reconstruct path from node)
        add node.state to explored set
        for each action in Actions(node.state):
            child = Result(node.state, action)
            if child not in explored and not in frontier:
                add child to frontier
                
    return failure (no solution found)
```

## Estrategias de Búsqueda No Informadas

### Depth-First Search (DFS)
DFS explora lo más profundamente posible a lo largo de cada rama antes de retroceder, usando una estructura de datos stack.
```pseudocode
function DFS(problem):
    frontier = stack containing initial state
    explored = empty set
    
    while frontier not empty:
        node = frontier.pop()  # Remove last node added
        if node.state is goal:
            return solution
        explored.add(node.state)
        for each action in Actions(node.state):
            child = Result(node.state, action)
            if child not in explored and not in frontier:
                frontier.push(child)
```

**Características:**
- Eficiente en memoria (solo almacena camino actual)
- Puede encontrar soluciones no óptimas
- Puede explorar ramas profundas innecesarias
- Mejor cuando la memoria es limitada

**Ejemplo del mundo real**: Como buscar llaves revisando minuciosamente una habitación completa antes de pasar a la siguiente.

### Breadth-First Search (BFS)
BFS explora todos los nodos en la profundidad actual antes de moverse más profundo, usando una estructura de datos queue.
```pseudocode
function BFS(problem):
    frontier = queue containing initial state
    explored = empty set
    
    while frontier not empty:
        node = frontier.dequeue()  # Remove first node added
        if node.state is goal:
            return solution
        explored.add(node.state)
        for each action in Actions(node.state):
            child = Result(node.state, action)
            if child not in explored and not in frontier:
                frontier.enqueue(child)
```

**Características:**
- Garantizado encontrar solución óptima
- Intensivo en memoria (almacena todos los caminos explorados)  
- Explora sistemáticamente nivel por nivel
- Ideal cuando el camino óptimo es crítico

**Ejemplo del mundo real**: Como revisar rápidamente un lugar en cada habitación primero, luego volver para una búsqueda más minuciosa.

### Comparación

| Aspecto | DFS | BFS |
|---------|-----|-----|
| Estructura de Datos | Stack (LIFO) | Queue (FIFO) |
| Exploración | Primero profundo | Primero ancho |
| Optimalidad | Sin garantía | Garantizado óptimo |
| Uso de Memoria | Menor | Mayor |
| Mejor Caso de Uso | Memoria limitada | Camino óptimo requerido |

## Estrategias de Búsqueda Informadas

### Greedy Best-First Search
Usa funciones heurísticas para guiar la búsqueda hacia direcciones prometedoras. Siempre expande el nodo que parece más cercano al objetivo.

**Heurística de Distancia Manhattan**: ```h(n) = |x_current - x_goal| + |y_current - y_goal|```


**Cómo funciona**: Siempre elige el camino que parece más directo hacia el objetivo, como siempre tomar calles que parecen llevar directamente a tu destino.

**Riesgos**: Puede ser engañado por heurísticas pobres y puede no encontrar caminos óptimos.

### Algoritmo A* Search
Combina el costo real hasta ahora (g(n)) con el costo estimado al objetivo (h(n)) usando f(n) = g(n) + h(n).

**Condiciones de Optimalidad**:
- **Heurística admisible**: Nunca sobrestima el costo real
- **Heurística consistente**: El costo estimado disminuye suavemente hacia el objetivo

**Ejemplo**: Como navegación que considera tanto la distancia recorrida como la distancia restante en línea recta.

## Búsqueda Adversarial (Game Playing)

### Minimax Algorithm
Usado para juegos de dos jugadores con información perfecta. Asume juego óptimo de ambos jugadores.
```pseudocode
function MAX-VALUE(state):
    if TERMINAL(state):
        return UTILITY(state)
    v = -∞
    for each action in ACTIONS(state):
        v = MAX(v, MIN-VALUE(RESULT(state, action)))
    return v

function MIN-VALUE(state):
    if TERMINAL(state):
        return UTILITY(state)
    v = +∞
    for each action in ACTIONS(state):
        v = MIN(v, MAX-VALUE(RESULT(state, action)))
    return v
```

**Cómo funciona**: Evalúa recursivamente todos los movimientos posibles, con el jugador Max eligiendo movimientos de mayor valor y el jugador Min eligiendo movimientos de menor valor.

### Alpha-Beta Pruning
Técnica de optimización que elimina ramas que no pueden afectar la decisión final.

```pseudocode
function ALPHA-BETA-SEARCH(state):
    return MAX-VALUE(state, -∞, +∞)

function MAX-VALUE(state, α, β):
    if TERMINAL(state): return UTILITY(state)
    v = -∞
    for each action in ACTIONS(state):
        v = MAX(v, MIN-VALUE(RESULT(state, action), α, β))
        if v ≥ β: return v  # Prune
        α = MAX(α, v)
    return v
```

**Beneficios**: Puede reducir la complejidad de tiempo de O(bᵈ) a O(bᵈ⸍²) con buen ordenamiento de movimientos.

### Depth-Limited Minimax
Usado para juegos complejos donde la búsqueda completa es imposible. Busca hasta una profundidad fija, luego usa funciones de evaluación.

```pseudocode
function DEPTH-LIMIMED-MINIMAX(state, depth):
    if depth == 0 or TERMINAL(state):
        return EVALUATION(state)
    # ... continue with minimax ...
```


**Funciones de evaluación**: Estiman la calidad de la posición usando factores como balance de material, movilidad de piezas y ventajas posicionales.

## Implementación Práctica

Patrones clave de implementación:

1. **Clase Node**: Almacena estado, nodo padre, acción y costo de camino
2. **Gestión de Frontier**: Diferentes estructuras de datos para diferentes estrategias de búsqueda
3. **Conjunto Explored**: Previene loops infinitos y re-visitación de estados
4. **Reconstrucción de camino**: Retroceso desde el objetivo al estado inicial

**Consideraciones de rendimiento**:
- DFS: Buena eficiencia de memoria, puede explorar caminos innecesarios
- BFS: Soluciones óptimas, alto uso de memoria  
- A*: Más eficiente con buenas heurísticas
- Minimax: Computacionalmente costoso, requiere optimizaciones

## Conclusión

Los algoritmos de búsqueda proporcionan herramientas fundamentales para la resolución de problemas de inteligencia artificial. La elección del algoritmo depende de requisitos específicos:

- Usar **DFS** cuando la memoria es limitada y la optimalidad no es crítica
- Usar **BFS** cuando se requieren soluciones óptimas garantizadas
- Usar **búsqueda informada** (A*) cuando hay buenas heurísticas disponibles  
- Usar **búsqueda adversarial** (Minimax) para escenarios de juego
- Aplicar **optimizaciones** (poda alpha-beta, limitación de profundidad) para problemas complejos

Entender estos algoritmos y sus compensaciones es esencial para diseñar sistemas de IA efectivos que puedan navegar entornos complejos, resolver puzzles y tomar decisiones óptimas.