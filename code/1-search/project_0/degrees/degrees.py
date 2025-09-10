import csv
import sys
import time

from util import Node, StackFrontier, QueueFrontier

# Maps names to a set of corresponding person_ids
names = {}

# Maps person_ids to a dictionary of: name, birth, movies (a set of movie_ids)
people = {}

# Maps movie_ids to a dictionary of: title, year, stars (a set of person_ids)
movies = {}


def load_data(directory):
    """
    Load data from CSV files into memory.
    """
    # Load people
    with open(f"{directory}/people.csv", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            people[row["id"]] = {
                "name": row["name"],
                "birth": row["birth"],
                "movies": set()
            }
            if row["name"].lower() not in names:
                names[row["name"].lower()] = {row["id"]}
            else:
                names[row["name"].lower()].add(row["id"])

    # Load movies
    with open(f"{directory}/movies.csv", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            movies[row["id"]] = {
                "title": row["title"],
                "year": row["year"],
                "stars": set()
            }

    # Load stars
    with open(f"{directory}/stars.csv", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                people[row["person_id"]]["movies"].add(row["movie_id"])
                movies[row["movie_id"]]["stars"].add(row["person_id"])
            except KeyError:
                pass


def main():
    if len(sys.argv) > 2:
        sys.exit("Usage: python degrees.py [directory]")
    directory = sys.argv[1] if len(sys.argv) == 2 else "large"

    # Load data from files into memory
    print("Loading data...")
    load_data(directory)
    print("Data loaded.")

    source = person_id_for_name(input("Name: "))
    if source is None:
        sys.exit("Person not found.")
    target = person_id_for_name(input("Name: "))
    if target is None:
        sys.exit("Person not found.")

    path = shortest_path(source, target)

    if path is None:
        print("Not connected.")
    else:
        degrees = len(path)
        print(f"{degrees} degrees of separation.")
        path = [(None, source)] + path
        for i in range(degrees):
            person1 = people[path[i][1]]["name"]
            person2 = people[path[i + 1][1]]["name"]
            movie = movies[path[i + 1][0]]["title"]
            print(f"{i + 1}: {person1} and {person2} starred in {movie}")
    
def shortest_path(source, target, max_degrees=6):
    """
    Returns the shortest list of (movie_id, person_id) pairs
    that connect the source to the target.
    If no possible path, returns None.
    """
    
    # Si son la misma persona, retornar camino vacío
    if source == target:
        return []
    
    # Inicializar la frontera con el nodo de origen
    frontier = QueueFrontier()
    start_node = Node(state=source, parent=None, action=None, depth=0)
    frontier.add(start_node)
    
    # Conjunto para mantener registro de nodos explorados
    explored = set()

    # Contadores para estadísticas
    nodes_explored = 0
    start_time = time.time()
    skipped_deep_nodes = 0
    
    
    # Búsqueda por amplitud
    while not frontier.empty():
        # Remover nodo de la frontera
        current_node = frontier.remove()
        nodes_explored += 1

        # LÍMITE DE PROFUNDIDAD - Saltar nodos muy profundos
        if current_node.depth >= max_degrees:
            skipped_deep_nodes += 1
            if skipped_deep_nodes % 1000 == 0:
                # print(f"Saltados {skipped_deep_nodes} nodos por profundidad > {max_degrees}")
                print()
            continue
            
        # Log cada 1000 nodos explorados
        """
        if nodes_explored % 1000 == 0:
            elapsed = time.time() - start_time
            print(f"Nodos explorados: {nodes_explored:,} | Profundidad: {current_node.depth} | Frontera: {len(frontier.frontier)} | Tiempo: {elapsed:.1f}s")
        """

        # Marcar nodo como explorado
        explored.add(current_node.state)
        
        # Obtener todos los vecinos (co-estrellas)
        neighbors = neighbors_for_person(current_node.state)

        # Log detallado cada 500 nodos
        """
        if nodes_explored % 500 == 0:
            print(f"Nodo {nodes_explored}: Actor {current_node.state} a profundidad {current_node.depth} tiene {len(neighbors)} vecinos")
        """

        for movie_id, person_id in neighbors:
            # Si encontramos el objetivo, reconstruir el camino
            if person_id == target:
                elapsed = time.time() - start_time
                # print(f"OBJETIVO ENCONTRADO en {elapsed:.2f}s después de {nodes_explored} nodos")
                # print(f"Profundidad final: {current_node.depth + 1} grados")
                
                path = []
                # Agregar este último paso
                path.append((movie_id, person_id))
                # Retroceder por los padres para reconstruir el camino completo
                node = current_node
                while node.parent is not None:
                    path.append((node.action, node.state))
                    node = node.parent
                path.reverse()

                # print(f"Camino encontrado: {len(path)} grados")
                return path
            
            # Si no es el objetivo y no ha sido explorado ni está en la frontera
            if person_id not in explored and not frontier.contains_state(person_id):
                # Mantener registro de profundidad
                new_node = Node(state=person_id, parent=current_node, 
                              action=movie_id, depth=current_node.depth + 1)
                frontier.add(new_node)

                # Log cada 1000 nodos agregados a la frontera
                """
                if len(frontier.frontier) % 1000 == 0:
                    print(f"Frontera: {len(frontier.frontier)} nodos | Profundidad máxima: {current_node.depth + 1}")
                """
    
    # Si no se encontró camino
    """
    elapsed = time.time() - start_time
    print(f"NO SE ENCONTRÓ CAMINO después de {elapsed:.1f}s")
    print(f"Estadísticas: {nodes_explored} nodos explorados, {skipped_deep_nodes} nodos saltados por profundidad")
    """
    return None

def person_id_for_name(name):
    """
    Returns the IMDB id for a person's name,
    resolving ambiguities as needed.
    """
    person_ids = list(names.get(name.lower(), set()))
    if len(person_ids) == 0:
        return None
    elif len(person_ids) > 1:
        print(f"Which '{name}'?")
        for person_id in person_ids:
            person = people[person_id]
            name = person["name"]
            birth = person["birth"]
            print(f"ID: {person_id}, Name: {name}, Birth: {birth}")
        try:
            person_id = input("Intended Person ID: ")
            if person_id in person_ids:
                return person_id
        except ValueError:
            pass
        return None
    else:
        return person_ids[0]


def neighbors_for_person(person_id):
    """
    Returns (movie_id, person_id) pairs for people
    who starred with a given person.
    """
    movie_ids = people[person_id]["movies"]
    neighbors = set()
    for movie_id in movie_ids:
        for person_id in movies[movie_id]["stars"]:
            neighbors.add((movie_id, person_id))
    return neighbors


if __name__ == "__main__":
    main()
