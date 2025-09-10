# Week 1 – Introduction to Artificial Intelligence with Python

## Introduction

Questions | Notes
--- | ---
Who is the instructor? | Brian Yu is the instructor.
What is this course about? | Introduction to Artificial Intelligence using Python. Covers ideas, techniques, and algorithms foundational to AI.
What is AI? | AI is when a computer appears intelligent: recognizing faces, playing games, understanding language, etc.
What topics will be covered? | 
🔹 **Search** | AI finding solutions to problems (e.g., route from A to B, best move in Tic-Tac-Toe).
🔹 **Knowledge** | Representing and reasoning with information; making inferences.
🔹 **Uncertainty** | Handling incomplete information using probability.
🔹 **Optimization** | Finding not only a correct way to solve a problem, but a better—or the best—way to solve it.
🔹 **Machine Learning** | Learning from data and experience (e.g., spam detection in email).
🔹 **Neural Networks** | Drawing inspiration from the human brain to design intelligent algorithms.
🔹 **Natural Language** | Understanding and processing human language.

### Summary
This course explores foundational topics in AI such as search, knowledge representation, uncertainty, optimization, machine learning, neural networks, and natural language processing. Through examples and code in Python, it demonstrates how computers can be designed to act intelligently.

## Basic Concepts of Search Problems

Questions | Notes
--- | ---
**What is a search problem in AI?** | A problem where an agent must determine a sequence of actions to move from an initial state to a goal state. Examples include puzzles, maze navigation, and driving directions.
**What is an agent?** | An entity that perceives its environment and acts upon that environment. In a navigator app, the agent would be a representation of a car that needs to decide on which actions to take.
**What is a state?** | A configuration of an agent in its environment. In a 15 puzzle, a state is any one way that all the numbers are arranged on the board.
**What is the initial state?** | The state from which the search algorithm starts. In a navigator app, that would be the current location.
**What are actions?** | Choices that can be made in a state. Formally: `Actions(s)` returns the set of actions that can be executed in state `s`.
**What is the transition model?** | Describes what state results from performing any action in any state. Formally: `Results(s, a)` returns the state resulting from performing action `a` in state `s`.
**What is the state space?** | The set of all states reachable from the initial state by any sequence of actions. Can be visualized as a directed graph with states as nodes and actions as arrows.
**What is a goal test?** | The condition that determines whether a given state is a goal state.
**What is path cost?** | A numerical cost associated with a given path. The algorithm aims to minimize this cost.
**What is a solution?** | A sequence of actions that leads from the initial state to the goal state.
**What is an optimal solution?** | A solution that has the lowest path cost among all solutions.

### Summary
AI search problems involve defining a structured environment with an agent, initial state, possible actions, and a goal. The AI uses a transition model to explore the state space and attempts to find a solution that leads from the initial state to the goal while minimizing path cost.

## Solving Search Problems

### Theory

Questions | Notes
--- | ---
**What is a node?** | A data structure that contains: a state, its parent node, the action that was applied to get to this node, and the path cost from the initial state.
**Why are nodes useful?** | They allow reconstructing the complete path from initial to goal state by tracking parent nodes.
**What is the frontier?** | A data structure that manages which nodes to explore next.
**What is the general search process?** | 1. Initialize frontier with initial state<br>2. While frontier not empty:<br>   - Remove a node<br>   - If it contains goal, return solution<br>   - Else, expand node and add to explored set
**What does "expand a node" mean?** | Generating all new nodes that can be reached from the current node by applying valid actions.

```text
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

### Example: Pathfinding from Node A to Node E

Imagine we need to find a path from node A to node E in this graph structure:
- A connects to B
- B connects to C and D  
- C connects to E
- D connects to F

The search algorithm starts with only node A in the frontier. It removes A, checks if it's the goal (it's not), then expands A by adding its neighbor B to the frontier.

Now the frontier contains only B. The algorithm removes B, checks if it's the goal (no), then expands B by adding its neighbors C and D to the frontier.

The frontier now contains C and D. The algorithm removes C (the order depends on the search strategy), checks if it's the goal (no), then expands C. Since C connects to D and E, it adds these to the frontier.

This process continues until eventually the algorithm removes E from the frontier, recognizes it as the goal state, and returns the solution path by backtracking through parent nodes.

### Summary
To solve a search problem, AI uses a node-based data structure that tracks the current state, its parent, the action taken, and the cumulative path cost. Nodes are explored via a loop using the **frontier**, which holds unexplored states. The algorithm continues removing and expanding nodes until the **goal is found** or the **frontier is empty**. This structured approach allows AI to systematically explore potential paths to reach a solution.

## Depth-First Search (DFS) and Breadth-First Search (BFS)

### Theory

Questions | Notes
--- | ---
**What determines which node to remove?** | The data structure used for the frontier determines the search strategy.
**What is a stack?** | Last-In-First-Out (LIFO) data structure. Last item added is first removed.
**What is Depth-First Search?** | Uses stack for frontier. Explores as deep as possible in one direction before backtracking.
**What is a queue?** | First-In-First-Out (FIFO) data structure. First item added is first removed.
**What is Breadth-First Search?** | Uses queue for frontier. Explores all nodes at current depth before going deeper.
**What are the advantages of DFS?** | Can be fastest if it gets lucky with path choice. Uses less memory.
**What are the disadvantages of DFS?** | May find non-optimal solutions. Can get stuck in deep branches.
**What are the advantages of BFS?** | Guaranteed to find optimal solution (shortest path) if all actions have equal cost.
**What are the disadvantages of BFS?** | Uses more memory. May explore many unnecessary nodes.

```text
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

```text
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

### Example: Maze Navigation with DFS and BFS

**DFS Behavior in a Maze:**
Depth-First Search behaves like a determined explorer who commits fully to one path. Imagine you're in a maze with multiple junctions. DFS would choose one direction and follow it relentlessly until it hits a dead end. Only then would it backtrack to the last decision point and try a different path. This approach can be efficient in memory usage since it only needs to remember the current path, but it might take you on a long, winding route even if a shorter path exists.

**BFS Behavior in a Maze:**
Breadth-First Search behaves more systematically. It explores all immediate options first before going deeper. In our maze example, BFS would check all paths one step away from the start, then all paths two steps away, and so on. This guarantees that when it finds the exit, it has found the shortest possible path. However, this method requires remembering all the paths being explored, which can use significant memory in large mazes.

**Real-world Analogy:**
- **DFS**: Searching for your keys by thoroughly checking one room (every drawer, shelf, and pocket) before moving to the next room.
- **BFS**: Searching for your keys by quickly checking one spot in each room first, then going back for a more thorough search if needed.

### Code Implementation Differences
```python
# DFS removes the last node added (stack behavior)
node = self.frontier[-1]          # Get last item
self.frontier = self.frontier[:-1] # Remove last item

# BFS removes the first node added (queue behavior)  
node = self.frontier[0]           # Get first item
self.frontier = self.frontier[1:]  # Remove first item
```

### Summary

| Aspect | DFS | BFS |
|--------|-----|-----|
| Data Structure | Stack (LIFO) | Queue (FIFO) |
| Exploration | Deep first, then wide | Wide first, then deep |
| Optimality | No guarantee | Guaranteed optimal |
| Memory Usage | Lower | Higher |
| Best Use Case | When memory is limited | When optimal path is critical |

## Greedy Best-First Search

### Theory

Questions | Notes
--- | ---
**What is informed search?** | Search algorithms that use additional knowledge about the problem through heuristic functions.
**What is a heuristic function?** | A function h(n) that estimates the cost from node n to the goal.
**What is Greedy Best-First Search?** | Always expands the node that appears closest to the goal based on heuristic h(n).
**Is GBFS optimal?** | No. It doesn't guarantee finding the optimal solution.
**Is GBFS complete?** | No. It can get stuck in loops or miss the optimal path.
**What is the main advantage?** | Can be very fast and use less memory when the heuristic is good.
**What is the main risk?** | Poor heuristics can lead the algorithm astray.

### Example: Manhattan Distance Heuristic

In grid-based navigation problems, a common heuristic is the **Manhattan Distance**. This heuristic calculates the distance between two points by summing the absolute differences of their coordinates:

h(n) = |x_current - x_goal| + |y_current - y_goal|

This is called "Manhattan Distance" because it resembles how you would navigate in a city with a grid layout - you can only move horizontally and vertically, not diagonally.

**How GBFS Works:**
Greedy Best-First Search always chooses the path that seems most promising based on the heuristic. Imagine you're trying to get to a destination downtown. GBFS would always choose the street that appears to lead most directly toward your destination, without considering if that street might have heavy traffic or dead ends.

**The Risk:**
The algorithm can be easily misled. If the heuristic suggests a path that looks straight but actually has a river blocking the way (which the heuristic didn't account for), GBFS might waste time exploring that dead end while ignoring a slightly longer but actually faster route.

### Summary
Greedy Best-First Search uses heuristics to guide search toward promising directions. While often efficient, it can be misled by inaccurate heuristics and doesn't guarantee optimal solutions.

## A* (A-Star) Search Algorithm

### Theory

Questions | Notes
--- | ---
**What is A* search?** | An algorithm that combines actual cost so far (g(n)) with estimated cost to goal (h(n)).
**What does A* minimize?** | The total cost f(n) = g(n) + h(n), where g(n) is actual cost from start, h(n) is estimated cost to goal.
**When is A* optimal?** | When the heuristic h(n) is admissible and consistent.
**What is an admissible heuristic?** | Never overestimates the true cost to reach the goal. h(n) ≤ actual cost to goal.
**What is a consistent heuristic?** | For every node n and successor n' with step cost c: h(n) ≤ h(n') + c
**What are the advantages?** | Finds optimal solutions efficiently when guided by good heuristics.
**What are the disadvantages?** | Memory usage can be high. Performance depends heavily on heuristic quality.

### Why Consistency Matters

A consistent heuristic ensures that the estimated cost to the goal decreases smoothly as we move toward it. This property prevents the algorithm from making poor decisions based on erratic estimates. Think of it like a GPS that always shows decreasing distance as you approach your destination - if the distance suddenly increased as you got closer, you might doubt the directions!

### Example: Navigation with A*

Imagine you're driving with two pieces of information:
1. **g(n)**: The actual distance you've traveled so far (from your odometer)
2. **h(n)**: The straight-line distance to your destination (from GPS)

A* combines these: f(n) = distance traveled + straight-line distance remaining

This helps the algorithm choose routes that are both efficient so far and promising for the future. Unlike Greedy search, which might choose a seemingly direct route that's actually slow, A* balances what you've already invested with what remains.

### Optimality Conditions

For A* to guarantee optimal solutions, the heuristic must be:
- **Admissible**: Never overestimates the true cost (optimistic but realistic)
- **Consistent**: The estimated cost decreases smoothly as you approach the goal

The Manhattan distance is both admissible and consistent for grid navigation problems.

### Summary
A* search optimally combines actual progress with estimated remaining cost. Its effectiveness depends on having heuristics that are both admissible (never overestimate) and consistent (smoothly decreasing).

## Adversarial Search and Minimax Algorithm

### Theory

Questions | Notes
--- | ---
**What is adversarial search?** | Search against an opponent with opposing goals, commonly used in game playing.
**What is Minimax?** | Algorithm for two-player, deterministic, perfect-information games.
**Who are the players?** | Max player tries to maximize score, Min player tries to minimize score.
**How are outcomes represented?** | Utility values: Max wins = +1, Min wins = -1, Draw = 0.
**What are the required functions?** | Initial state, Player(s), Actions(s), Result(s,a), Terminal(s), Utility(s)

```text
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

### Example: Tic-Tac-Toe Decision Making

Let's examine how Minimax thinks through a Tic-Tac-Toe position. Imagine it's X's turn in this situation:

```text
 X | O | 
---+---+---
   | X | 
---+---+---
 O |   | 
```

The algorithm considers every possible move X could make. For each move, it thinks: "If I move here, what would O do in response? And then how would I respond to that? And so on until the game ends."

This recursive thinking continues until all possible game outcomes are evaluated. X chooses the move that leads to the best possible outcome, assuming O will always make the best move for themselves.

**How the Recursion Works:**
- **Max player's turn**: "I'll choose the move that gives me the highest score, assuming my opponent will play optimally against me."
- **Min player's turn**: "I'll choose the move that gives me the lowest score (which is bad for Max), assuming Max will play optimally against me."

This mutual assumption of optimal play leads to very conservative, mathematically sound decisions.

### The Minimax Value

For any game state, the Minimax value represents the best outcome that the current player can guarantee, assuming optimal play from both players. In Tic-Tac-Toe with perfect play, the Minimax value of the initial empty board is 0 (draw).

### Summary
Minimax enables optimal play in two-player games by recursively considering all possible moves and assuming optimal play from both players. It's fundamental to game-playing AI but can be computationally expensive for complex games.

## Alpha-Beta Pruning

### Theory

Questions | Notes
--- | ---
**Why is pruning needed?** | Minimax can explore exponentially many states. Pruning reduces computation by eliminating irrelevant branches.
**What is alpha-beta pruning?** | An optimization that skips evaluating branches that cannot affect the final decision.
**What is alpha?** | The best value that the maximizer can guarantee at current level or above.
**What is beta?** | The best value that the minimizer can guarantee at current level or above.
**When can we prune?** | When α ≥ β, we can stop evaluating the current branch.
**Does pruning affect optimality?** | No. The result is identical to full minimax, just computed more efficiently.
**How much does it help?** | In best case, reduces time complexity from O(bᵈ) to O(bᵈ⸍²)

```text
function ALPHA-BETA-SEARCH(state):
    return MAX-VALUE(state, -∞, +∞)

function MAX-VALUE(state, α, β):
    if TERMINAL(state): return UTILITY(state)
    v = -∞
    for each action in ACTIONS(state):
        v = MAX(v, MIN-VALUE(RESULT(state, action), α, β))
        if v ≥ β: return v  # Prune remaining actions
        α = MAX(α, v)
    return v

function MIN-VALUE(state, α, β):
    if TERMINAL(state): return UTILITY(state)
    v = +∞
    for each action in ACTIONS(state):
        v = MIN(v, MAX-VALUE(RESULT(state, action), α, β))
        if v ≤ α: return v  # Prune remaining actions
        β = MIN(β, v)
    return v
```

### Example: Pruning in Action

Imagine Max is evaluating moves and has already found one move that guarantees a score of at least 4. Now Max starts evaluating another move branch.

As Max explores this new branch, it looks at Min's possible responses. The first response Min could make leads to a position where Max can get at most 3.

Here's the key insight: since 3 is worse than the already guaranteed 4, Max knows this move branch is inferior regardless of what other responses Min might have. There's no need to explore Min's other possible responses - that entire branch can be "pruned" (skipped).

This is like realizing one restaurant has mediocre reviews while you already know another has excellent food - no need to read all the reviews for the mediocre place.

### The Pruning Conditions

**Max node pruning**: If v ≥ β, prune. This happens when Max finds something so good that Min would never allow this path.
**Min node pruning**: If v ≤ α, prune. This happens when Min finds something so bad that Max would never choose this path.

### Complexity Impact

The effectiveness of alpha-beta pruning depends on the order in which moves are considered. With perfect ordering (best moves first), it can reduce the number of nodes evaluated from O(bᵈ) to O(bᵈ⸍²) - a massive improvement for deep searches.

### Summary
Alpha-beta pruning dramatically improves minimax efficiency by eliminating branches that cannot affect the final decision, while guaranteeing the same optimal result. It's essential for making complex game AI feasible.

## Depth-Limited Minimax

### Theory

Questions | Notes
--- | ---
**Why use depth-limited search?** | Many games have enormous state spaces (chess: ~10²⁹⁰⁰⁰ possible games).
**What is depth-limited minimax?** | Minimax that stops search at a fixed depth rather than going to terminal states.
**What's the problem at cutoff?** | Non-terminal states need evaluation since we don't know the actual outcome.
**What is an evaluation function?** | Estimates the expected utility of non-terminal game states.
**What makes a good eval function?** | Accurate estimation of winning chances based on game features.
**How does it work?** | Search to fixed depth, then use evaluation function instead of utility function.

```python
function DEPTH-LIMITED-MINIMAX(state, depth):
    if depth == 0 or TERMINAL(state):
        return EVALUATION(state)  # Instead of UTILITY for non-terminals
    # ... rest same as regular minimax ...
```

### Example: Chess Evaluation Function

A chess evaluation function typically considers multiple factors:

**Material Balance** (most basic component):
- Queen: 9 points
- Rook: 5 points  
- Bishop: 3 points
- Knight: 3 points
- Pawn: 1 point

The function sums up each player's material and compares them.

**Positional Factors** (more advanced):
- Center control: Pieces controlling central squares are more valuable
- King safety: How exposed is each king?
- Pawn structure: Are pawns well-protected and advancing?
- Piece mobility: How many moves does each piece have?
- Threat detection: Are any pieces under attack?

A simple evaluation might look like:
evaluation = (white_material - black_material) + 0.1*(white_center_control - black_center_control)

More sophisticated functions use machine learning to weight these factors optimally based on thousands of master games.

### The Challenge of Evaluation Functions

The quality of depth-limited minimax depends entirely on the evaluation function's accuracy. A poor evaluation function will lead to poor decisions, no matter how deep the search goes. This is why top chess engines spend enormous effort refining their evaluation functions.

### Practical Implementation

In practice, most game AIs use:
1. Depth-limited minimax with alpha-beta pruning
2. Sophisticated evaluation functions
3. Iterative deepening (search to depth 1, then 2, then 3, etc.)
4. Transposition tables to cache previously computed positions
5. Opening books and endgame tablebases for known positions

### Summary
Depth-Limited Minimax makes complex game AI feasible by searching to manageable depths and using evaluation functions to estimate position quality. The AI's strength depends on both search depth and evaluation function quality, with modern engines achieving superhuman performance through sophisticated evaluation functions and massive computational resources.

## Code Implementation Notes

| Concept | Implementation Details |
|---------|------------------------|
| **Node Class** | Stores state, parent node, action taken to reach state, and path cost |
| **Frontier Base Class** | Manages nodes to be explored with add/remove/empty methods |
| **StackFrontier Class** | Extends frontier with LIFO behavior (stack) for DFS |
| **QueueFrontier Class** | Extends frontier with FIFO behavior (queue) for BFS |
| **Maze Class** | Parses maze files, handles visualization, and coordinates search |
| **Search Algorithm** | Implements the general search process with frontier and explored set |
| **Backtracking** | Reconstructs solution path by following parent pointers from goal to start |
| **Visualization** | Generates images showing path, explored states, and solution |

### Key Implementation Patterns
1. **Node tracking**: Each node remembers its parent and the action that created it
2. **Frontier management**: Different data structures for different search strategies
3. **Explored set**: Prevents re-visiting states and infinite loops
4. **Path reconstruction**: Backtracking from goal node to initial state

### Performance Notes
- **DFS**: May explore many unnecessary paths but uses less memory
- **BFS**: Finds optimal path but can use significant memory in large spaces
- **A***: Most efficient with good heuristics but requires careful implementation

### Key Insight
Tic-Tac-Toe is simple enough for optimal play lookup. Larger games require intelligent search with evaluation functions, pruning, and depth limitations to handle computational complexity.