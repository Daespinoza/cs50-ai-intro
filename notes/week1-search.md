# Week 1 – Introduction to Artificial Intelligence with Python

## Cornell Notes

### Introduction

Questions | Notes
--- | ---
Who is the instructor? | Brian Yu is the instructor.
What is this course about? | Introduction to Artificial Intelligence using Python. Covers ideas, techniques, and algorithms foundational to AI.
What is AI? | AI is when a computer appears intelligent: recognizing faces, playing games, understanding language, etc.
What topics will be covered? | 
🔹 **Search** | AI finding solutions to problems (e.g., route from A to B, best move in Tic-Tac-Toe).
🔹 **Knowledge** | Representing and reasoning with information; making inferences.
🔹 **Uncertainty** | Handling incomplete information using probability.
🔹 **Optimization** | Finding the best solution among many possible ones.
🔹 **Machine Learning** | Learning from data and experience (e.g., spam detection in email).
🔹 **Neural Networks** | Drawing inspiration from the brain to design intelligent algorithms.
🔹 **Natural Language** | Understanding and processing human language.

### Summary
This course explores foundational topics in AI such as search, knowledge representation, uncertainty, optimization, machine learning, neural networks, and natural language processing. Through examples and code in Python, it demonstrates how computers can be designed to act intelligently.

### Basic Conceps

Questions | Notes
--- | ---
**What is a search problem in AI?** | A problem where an agent must determine a sequence of actions to move from an initial state to a goal state. Examples include puzzles, maze navigation, and driving directions.
**What is an agent?** | An entity that perceives its environment and takes actions to achieve goals. E.g., a self-driving car or a puzzle solver.
**What is a state?** | A specific configuration of the environment and agent. In puzzles, this is the arrangement of tiles.
**What is the initial state?** | The state from which the agent begins. It serves as the starting point for the search algorithm.
**What are actions?** | Choices available to an agent in a given state. Defined formally as a function: `actions(s)` returns all valid actions in state `s`.
**What is the transition model?** | Describes the outcome of performing an action in a state. Formally: `result(s, a)` returns the new state after applying action `a` to state `s`.
**How are state and transitions visualized?** | Through a **state space**: a graph where nodes are states and edges are actions leading to other states.
**What is the state space?** | The complete set of all reachable states from the initial state via any sequence of actions.
**What is a goal test?** | A function that checks whether a given state meets the criteria for being a goal state. E.g., correct puzzle order or reaching a destination.
**What is path cost?** | A numerical value representing the cost of a path (e.g., time, distance, effort). Helps determine better solutions.
**What is an optimal solution?** | A solution with the lowest possible path cost among all solutions. There may be multiple optimal solutions.

### Summary
AI search problems involve defining a structured environment with an agent, initial state, possible actions, and a goal. The AI uses a transition model to explore the state space and attempts to find a **solution** — a series of actions — that leads from the initial state to the goal. The best (optimal) solution is one that minimizes the total path cost. Understanding these components is essential to designing effective search algorithms in artificial intelligence.

### Solving Search Problems

Questions | Notes
--- | ---
**What is a node?** | A data structure that stores key information during search: current state, parent node, action taken, and path cost.
**What is a state (in a node)?** | The current position or configuration being evaluated in the search process.
**What is a parent (in a node)?** | The node that led to the current node. Used to reconstruct the path from the start to the goal.
**Why is tracking the parent important?** | It enables backtracking from the goal node to the initial state to retrieve the full sequence of actions.
**What is an action (in a node)?** | The specific step taken to move from the parent state to the current state.
**What is the path cost?** | A numerical value representing the total cost from the initial state to the current state.
**What is the frontier?** | A data structure (e.g., queue, stack, or priority queue) that stores all nodes that are available to explore but haven't been visited yet.
**What happens if the frontier is empty?** | It means there are no more nodes to explore and no solution exists for the problem.
**What is the general approach to solving search problems?** | 1. Initialize the frontier with the initial state.<br>2. While the frontier is not empty:<br>→ Remove a node.<br>→ If it contains the goal, return the solution.<br>→ Else, expand the node and add neighbors to the frontier.
**What does it mean to expand a node?** | Generating all successor nodes by applying valid actions from the current state and adding them to the frontier.
**What triggers the goal check?** | When a node is removed from the frontier, it's checked against the goal test to determine if a solution has been found.

### Summary
To solve a search problem, AI uses a node-based data structure that tracks the current state, its parent, the action taken, and the cumulative path cost. Nodes are explored via a loop using the **frontier**, which holds unexplored states. The algorithm continues removing and expanding nodes until the **goal is found** or the **frontier is empty**. This structured approach allows AI to systematically explore potential paths to reach a solution.

### Example: Pathfinding from Node A to Node E

We want to find a path from node **A** (initial state) to node **E** (goal state) using a basic search algorithm.

#### Graph Representation

- **A → B**  
- **B → C, D**  
- **C → E**  
- **D → F**

#### Algorithm Steps (Simple Search)

1. **Initialize the Frontier**  
   Start with the initial node `A` in the frontier.  
   → `Frontier = [A]`

2. **Repeat Until Solution Found or Frontier is Empty:**

   a. **Remove a node** from the frontier.  
   → Current: `A`

   b. **Check if it's the goal** (`E`)  
   → `A ≠ E` → Continue

   c. **Expand** the current node:  
   → `A → B` → Add `B` to frontier  
   → `Frontier = [B]`

   d. **Remove `B`**, not the goal → Expand:  
   → `B → C, D` → Add to frontier  
   → `Frontier = [C, D]`

   e. **Remove `C`**, not the goal → Expand:  
   → `C → D` → Add `D` again  
   → `Frontier = [D, D]`

   f. **Remove `D`**, not the goal → Expand:  
   → `D → E` → Add `E`  
   → `Frontier = [D, E]`

   g. **Remove `E`**, check goal:  
   → `E == Goal` → **Return the path**

---

#### Final Result

We found a path from **A → B → C/D → E**.  
The algorithm works by **expanding nodes** and **checking for the goal** step by step.

---

### Key Takeaways

- The **frontier** stores possible paths.
- We **expand** nodes to discover new states.
- Once the **goal node** is found, we stop and return the solution.
- This basic search lays the foundation for BFS, DFS, A*, etc.

---

### Depth-First Search and Breadth-First Search

Questions | Notes
--- | ---
**What is the problem with basic uninformed search?** | Without tracking visited states, the agent can revisit nodes (e.g., A ↔ B loop), leading to infinite cycles and no progress.
**How is this fixed?** | By keeping an **explored set** to remember already visited nodes, preventing re-visitation.
**What is the frontier?** | A data structure holding nodes to explore next. The way we manage it affects the algorithm's behavior.
**What is a stack in search?** | A **Last In, First Out (LIFO)** structure. The most recently added node is explored first. Used in **Depth-First Search (DFS)**.
**What is Depth-First Search (DFS)?** | A search that explores **as deep as possible** into the search tree before backtracking. Uses a **stack** for the frontier.
**What is a queue in search?** | A **First In, First Out (FIFO)** structure. The earliest added node is explored first. Used in **Breadth-First Search (BFS)**.
**What is Breadth-First Search (BFS)?** | A search that explores the **shallowest nodes first**, layer by layer. Uses a **queue** for the frontier.
**How do DFS and BFS differ in exploration?** | DFS goes deep first (risking dead ends), while BFS expands level by level (guaranteeing shortest path if costs are equal).
**What structures are needed for safe search?** | A **frontier** (stack or queue), and an **explored set** to track visited states and avoid loops.

#### Other Notes

- **DFS** is efficient for memory but can get lost in deep branches.
- **BFS** is reliable for finding shortest paths but uses more memory.
- Both require tracking **explored nodes** to avoid loops.
- The key difference lies in how the **frontier** is structured:
  - DFS → **Stack (LIFO)**
  - BFS → **Queue (FIFO)**

Use DFS when space is limited and you're okay with non-optimal paths. Use BFS when shortest paths are critical.

### DFS & BFS in Action: Maze 

Questions | Notes
--- | ---
**What is the agent trying to do?** | The agent is trying to go from **start (A)** to **goal (B)** by performing actions (up, down, left, right).
**How does DFS behave in a maze?** | DFS follows one path **as deeply as possible**. At forks, it arbitrarily picks a direction. If it hits a dead end, it **backtracks** to the last choice point and explores an alternative.
**Is DFS guaranteed to find a solution?** |  **Yes**, **if the state space is finite**. DFS will eventually explore all reachable paths.  **No guarantee in infinite graphs** (e.g., looping grids).
**Does DFS always find the best solution?** |  **No**. DFS may find **non-optimal paths** if it picks the wrong direction first. It doesn't prioritize short paths.
**How does BFS behave differently?** | BFS explores **all nodes one step away first**, then two steps away, then three, and so on—level by level. It doesn't dive deep early.
**What makes BFS powerful?** | **BFS always finds the shortest path** (in terms of steps) if all actions have equal cost. It systematically expands outward from the start.
**What’s the trade-off between DFS and BFS?** | - **DFS**: Lower memory usage, possibly fast, but not guaranteed optimal. <br> - **BFS**: Guaranteed optimal (shortest path), but **much higher memory usage**.
**In maze solving, what do we observe visually?** | - DFS: A narrow, deep path with frequent backtracking. <br> - BFS: A wide, expanding front, covering many paths at once.

### DFS vs. BFS in Maze Navigation

#### Depth-First Search (DFS)

- Start at A
- Follow one path until dead end
-  Backtrack to last decision
- Explore another path
- Eventually find goal (maybe not optimal)

So, DFS:

- Uses a **stack (LIFO)**
- Risk of **long detours**
- **Memory-efficient**, since it only stores the current path

#### Breadth-First Search (BFS)

- Step 1: Start at A
- Step 2: Explore all neighbors 1 step away → B
- Step 3: Explore nodes 2 steps away → C, D
- Step 4: Explore nodes 3 steps away → E
- Goal found at E (Shortest path: A → B → C → E)

So, BFS:

- Uses a **queue (FIFO)**
- **Finds optimal path**
- **Memory-heavy**, especially in wide mazes

---

### Example Outcome

Let’s say there are **two paths** from A to B:

- Short: 4 steps
- Long: 12 steps

If DFS chooses the long one first:
- It **may reach B**, but **not via the shortest route**.

If BFS runs:
- It **will find the 4-step path** first.

> So: DFS is faster when you're lucky, but BFS is **more reliable** for shortest-path problems.

---

### Summary

| Aspect                | DFS                         | BFS                           |
|-----------------------|-----------------------------|-------------------------------|
| Data Structure        | Stack (LIFO)                | Queue (FIFO)                  |
| Explores              | Deepest path first          | Shallowest path first         |
| Guarantees solution   | Yes (if finite space)       | Yes (if finite space)         |
| Guarantees optimality | No                          |  Yes                          |
| Memory Usage          |  Lower                      |  Higher                       |
| Use Case              | Fast exploration            | Reliable, shortest path       |

---

## Code

| **Cue (Main Idea)** | **Notes (Details and Explanation)** |
|---------------------|--------------------------------------|
| **Node Class** | Represents a state in the maze, keeping track of the state, its parent (previous state), and the action taken to reach it. Path cost isn't tracked as it's computed after finding the goal. |
| **StackFrontier Class** | A stack-based data structure (LIFO) used to manage the frontier. Includes methods: `add`, `contains_state`, `empty`, and `remove`. |
| **Classes in Python** | Object-oriented programming concept used to encapsulate data (frontier) and related methods. |
| **Frontier Implementation** | Frontier starts as an empty list. Nodes are appended. The last item (`[-1]`) is removed during search, simulating a stack. |
| **QueueFrontier Class** | Inherits from `StackFrontier`. Overrides `remove` to use FIFO (removes first item `[0]`) instead of LIFO. Used for BFS. |
| **Maze Class** | Parses maze from a `.txt` file (walls = `#`, start = `A`, goal = `B`). Handles maze solving. |
| **Solve Function** | Core search logic. Tracks explored states. Starts with a node for the start state. Uses a frontier (stack or queue depending on search algorithm). |
| **Search Algorithm (DFS)** | Depth-First Search uses a stack. Explores deep paths first. May explore unnecessary paths and backtrack often. |
| **Goal Test** | Checks if the current node's state matches the goal. If so, reconstructs path by backtracking via parent nodes and actions. |
| **Backtracking** | Builds solution path and action list from goal to start, then reverses them to show path from start to goal. |
| **Exploration** | If a node isn't the goal, it's added to the explored set. Neighbors are added to the frontier if not already explored or in the frontier. |
| **Visualization** | Program generates a `.png` of the maze. Red = start, Green = goal, Yellow = path, Red cells (optional) = all explored states. |
| **DFS on Complex Maze** | May explore hundreds of states (e.g., 399 for `maze2.txt`) and still find the optimal path, but inefficiently. |
| **BFS on Complex Maze** | More efficient: explores fewer states (e.g., 77 for `maze2.txt`) and still finds the optimal solution. |
| **DFS vs BFS** | Both may find the same solution, but BFS is more efficient in terms of states explored. DFS might find non-optimal solutions. |
| **Maze3.txt Example** | BFS finds a 4-step optimal solution. DFS finds a longer path depending on exploration order. |
| **Algorithm Trade-offs** | DFS can explore deeply and get stuck; BFS guarantees shortest path but may still explore many nodes if the goal is far. |
| **Human Intuition** | A human might choose the direction that feels closer to the goal. Inspired the idea of a more intelligent algorithm. |
| **Intelligent Search** | Suggests algorithms that consider direction or distance to the goal (e.g., heuristic-based like Greedy or A*). |
