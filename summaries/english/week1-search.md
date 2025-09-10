# Week 1 – Introduction to Artificial Intelligence

## Course Introduction
**Instructor:** Brian Yu

**Course:** Introduction to Artificial Intelligence with Python

*“AI is not magic; it is a combination of logical, statistical, and computational techniques that allow it to simulate human reasoning.”*

## What is AI?
AI refers to techniques that allow computers to act intelligently or rationally, such as:

- Face recognition
- Playing games better than humans
- Understanding human language (e.g., voice assistants)

Topics covered in the course:

- Search: Teaching an AI how to search for solutions to problems (e.g., routing, playing games like tic-tac-toe).
- Knowledge: Representing and reasoning with information to make logical inferences.
- Uncertainty: Dealing with uncertain events using probability.
- Optimization: Finding better (or the best) solutions to problems with many possibilities.
- Machine Learning: Programming computers to learn from data and experience (e.g., spam detection).
- Neural Networks: Inspired by the human brain, these allow programs to solve complex tasks effectively.
- Natural Language Processing: How computers understand and respond to human (natural) language.

## Introduction to Artificial Intelligence

Artificial Intelligence (AI) enables computers to perform tasks that typically require human intelligence, such as recognizing patterns, solving problems, and making decisions. This field encompasses search algorithms, knowledge representation, machine learning, neural networks, and natural language processing.

Search algorithms form the foundation of many AI applications, from navigation systems to game-playing programs. These algorithms help find optimal paths or sequences of actions to achieve specific goals.

## Search Problem Fundamentals

Search problems involve several key components:

- **Agent**: Entity that perceives and acts upon its environment
- **State**: Configuration of the environment at a given time  
- **Initial State**: Starting point of the search process
- **Actions**: Possible moves available in each state
- **Transition Model**: Defines how actions change states
- **Goal Test**: Determines if a state is the desired solution
- **Path Cost**: Numerical cost associated with solution paths

The general search process follows this pattern:

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

## Uninformed Search Strategies

### Depth-First Search (DFS)

DFS explores as deeply as possible along each branch before backtracking, using a stack data structure.

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

**Characteristics:**
- Memory efficient (only stores current path)
- May find non-optimal solutions
- Can explore unnecessary deep branches
- Best when memory is limited

**Real-world example**: Like searching for keys by thoroughly checking one room completely before moving to the next room.

### Breadth-First Search (BFS)

BFS explores all nodes at current depth before moving deeper, using a queue data structure.

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

**Characteristics:**
- Guaranteed to find optimal solution
- Memory intensive (stores all explored paths)  
- Explores systematically level by level
- Ideal when optimal path is critical

**Real-world example**: Like quickly checking one spot in each room first, then returning for more thorough searching.

### Comparison

| Aspect | DFS | BFS |
|--------|-----|-----|
| Data Structure | Stack (LIFO) | Queue (FIFO) |
| Exploration | Deep first | Wide first |
| Optimality | No guarantee | Guaranteed optimal |
| Memory Usage | Lower | Higher |
| Best Use Case | Memory limited | Optimal path required |

## Informed Search Strategies

### Greedy Best-First Search

Uses heuristic functions to guide search toward promising directions. Always expands the node that appears closest to the goal.

**Manhattan Distance Heuristic**:
```h(n) = |x_current - x_goal| + |y_current - y_goal|```

**How it works**: Always chooses the path that seems most direct toward the goal, like always taking streets that appear to lead straight to your destination.

**Risks**: Can be misled by poor heuristics and may not find optimal paths.

### A* Search Algorithm

Combines actual cost so far (g(n)) with estimated cost to goal (h(n)) using f(n) = g(n) + h(n).

**Optimality Conditions**:
- **Admissible heuristic**: Never overestimates true cost
- **Consistent heuristic**: Estimated cost decreases smoothly toward goal

**Example**: Like navigation that considers both distance traveled and remaining straight-line distance.

## Adversarial Search (Game Playing)

### Minimax Algorithm

Used for two-player games with perfect information. Assumes optimal play from both players.

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

**How it works**: Recursively evaluates all possible moves, with Max player choosing highest-value moves and Min player choosing lowest-value moves.

### Alpha-Beta Pruning

Optimization technique that eliminates branches that cannot affect final decision.

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

**Benefits**: Can reduce time complexity from O(bᵈ) to O(bᵈ⸍²) with good move ordering.

### Depth-Limited Minimax

Used for complex games where full search is impossible. Searches to fixed depth, then uses evaluation functions.

```pseudocode
function DEPTH-LIMIMED-MINIMAX(state, depth):
    if depth == 0 or TERMINAL(state):
        return EVALUATION(state)
    # ... continue with minimax ...
```

**Evaluation functions**: Estimate position quality using factors like material balance, piece mobility, and positional advantages.

## Practical Implementation

Key implementation patterns:

1. **Node class**: Stores state, parent node, action, and path cost
2. **Frontier management**: Different data structures for different search strategies
3. **Explored set**: Prevents infinite loops and re-visiting states
4. **Path reconstruction**: Backtracking from goal to initial state

**Performance considerations**:
- DFS: Good memory efficiency, may explore unnecessary paths
- BFS: Optimal solutions, high memory usage  
- A*: Most efficient with good heuristics
- Minimax: Computationally expensive, requires optimizations

## Conclusion

Search algorithms provide fundamental tools for artificial intelligence problem-solving. The choice of algorithm depends on specific requirements:

- Use **DFS** when memory is limited and optimality isn't critical
- Use **BFS** when guaranteed optimal solutions are required
- Use **informed search** (A*) when good heuristics are available  
- Use **adversarial search** (Minimax) for game-playing scenarios
- Apply **optimizations** (alpha-beta pruning, depth-limiting) for complex problems

Understanding these algorithms and their trade-offs is essential for designing effective AI systems that can navigate complex environments, solve puzzles, and make optimal decisions.