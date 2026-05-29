# 🚨 Emergency Evacuation System Using Graph Algorithms

---

## 📌 Project Overview

This project simulates an intelligent emergency evacuation system using Graph Theory. It models real-world environments such as buildings, campuses, or cities as weighted graphs where:

- Nodes represent locations (rooms, intersections, exits)
- Edges represent paths between locations
- Weights represent distance, time, or risk level

The system dynamically computes the safest and shortest evacuation routes during emergencies like fire, flood, or earthquake.

---

## 🎯 Objectives

- To model real-world evacuation scenarios using graphs  
- To find shortest safe paths using graph algorithms  
- To handle blocked or unsafe routes dynamically  
- To analyze all possible paths between locations  

---

## 🧠 Algorithms Used

### 1. Dijkstra’s Algorithm
Used to find the shortest path from a single source node to all other nodes efficiently using a greedy approach.

### 2. Floyd-Warshall Algorithm
Used to compute shortest paths between all pairs of nodes using dynamic programming.

---

## ⚙️ Features

- Graph creation using adjacency matrix  
- Add routes between locations  
- Block unsafe routes dynamically  
- Shortest path computation with path tracking  
- All-pairs shortest path analysis  

---

## 🏗️ System Design

The system is divided into three main modules:

### 📌 Graph Module
Handles creation of graph, edge insertion, and route blocking.

### 📌 Algorithm Module
Implements Dijkstra and Floyd-Warshall algorithms.

### 📌 Control Module
Handles user interaction using a menu-driven interface.

---

## 🔄 Working Principle

1. User defines number of locations (nodes)  
2. Graph is initialized  
3. Routes are added between nodes  
4. Unsafe routes can be blocked dynamically  
5. Algorithms compute optimal evacuation paths  
6. Output displays safest and shortest routes  

---

## 📊 Applications

- Fire evacuation systems in buildings  
- Disaster management systems  
- Smart city safety planning  
- Industrial hazard response systems  
- Flood and earthquake evacuation planning  

---

## 🚀 Future Enhancements
 
- GUI-based visualization system  
- AI-based hazard prediction system  
- Mobile app-based evacuation guidance  
- GPS-based dynamic routing  

---

## 🏁 Conclusion

The Emergency Evacuation System demonstrates the practical application of graph algorithms in real-world safety systems. It efficiently computes optimal evacuation routes while adapting to dynamic hazards such as blocked or unsafe paths. This project strengthens understanding of graph theory and algorithm design in real-world problem solving.

---
