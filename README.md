# Dynamic Pathfinding Agent

## Overview
Ye project ek **Dynamic Pathfinding Agent** implement karta hai jo **grid-based environment** me move karta hai aur obstacles ke saath deal karta hai. Agent ka target fixed hota hai aur agar koi new obstacle aata hai to agent **real-time re-planning** karta hai.  

## Features
- Dynamic grid sizing (Rows × Columns)  
- Single Start node, multiple Goal nodes  
- Wall creation and removal with mouse clicks  
- Random map generation (`R` key)  
- Clear grid (`C` key)  
- **Algorithms**:
  - **A*** (f(n) = g(n) + h(n))  
  - **Greedy Best-First Search** (f(n) = h(n))  
- Dynamic Mode (toggle with `D`) → obstacles spawn randomly while agent moves  
- Visualization:  
  - Frontier nodes = Yellow  
  - Visited nodes = Blue  
  - Path = Green  
  - Start = Green with 'S', Goal = Red with 'G'  
- Metrics printed in console:
  - Nodes Visited  
  - Path Cost  
  - Execution Time  

## Controls
- **Left Click** → Place wall (unless Start/Goal mode active)  
- **Right Click** → Remove wall/Start/Goal  
- **S key** → Select Start node (only 1 allowed)  
- **G key** → Add Goal node(s)  
- **1 key** → Select A* Search  
- **2 key** → Select Greedy Best-First Search  
- **SPACE** → Run the selected algorithm  
- **D key** → Toggle Dynamic Mode  
- **R key** → Random map generation (30% obstacles)  
- **C key** → Clear grid  

## Screenshots
- **Best Case** → Screenshot showing minimal exploration and fast path 
- **Worst Case** → Screenshot showing maximum exploration  
- **A* Search** → Example screenshot using A*  
- **GBFS** → Example screenshot using Greedy Best-First Search  
- **Dynamic Replanning** → Screenshot showing obstacles appearing while agent is moving and agent re-planning the path  

## How to Run
1. Install dependencies:
```bash
pip install pygame

python dynamic_pathfinding.py


---

# 📸 **Screenshots Plan**

1. **Best Case**  
   - Open grid, few obstacles, agent finds goal quickly.  
   - Save screenshot as `best_case.png`.

2. **Worst Case**  
   - Dense obstacles, agent has to explore almost entire grid.  
   - Save as `worst_case.png`.

3. **A* Search**  
   - Run A*, capture path & metrics.  
   - Save as `astar_example.png`.

4. **GBFS**  
   - Run GBFS, capture path & metrics.  
   - Save as `gbfs_example.png`.

5. **Dynamic Replanning**  
   - Turn on **Dynamic Mode (D key)**  
   - Run algorithm, wait for obstacles to appear **on the current path**  
   - Agent will re-plan path to goal  
   - Capture screenshot where agent is **changing path due to obstacle**  
   - Save as `dynamic_replanning.png`

**Tip for Dynamic Screenshot:**  
- Turn on Dynamic Mode  
- Run algorithm  
- Use a dense-ish grid so obstacles appear in real-time  
- Wait until agent’s path changes → then take the screenshot  

---

Agar chaho, mai aap ke liye **final README ready with screenshot placeholders** bana doon jahan aap **images folder** me add karke directly push kar sako GitHub par.  

Kya mai woh bhi ready kar doon?
