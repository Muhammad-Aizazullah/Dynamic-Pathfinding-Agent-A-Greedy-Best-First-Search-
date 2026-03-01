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
