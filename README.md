# Code-Graph
A visualization tool for graphing relationships of a C/Cpp code base

## Overview
This project is heavily inspired by the Obsidian Graph view tool. To visualize one's knowledge/notes. And I thought it be fun to do the same for source codes.

I personally have always tried to maintain a mental image of the source code of any project I have worked on. This is often useful for large to medium sized projects, and often the best way to become familiar with a new project. But it was always very time consuming and I have to go through a lot of source files and reading a lot of code to very slowly build a high level mental picture of the relationship or dependency between different parts of the source.

The code graph is an attempt at aiding tool to visualize overall dependency and relationships between different source files.

## Current status

### v0.0

v0 Initial draft proof of concept version for [libusb](https://hantianjz.github.io/Code-Graph/publish_graph/libusb_graph.html)
![v0 Graph](/resources/9Yq9zxpT72ttfSa.png)

**Feature**
- Each source file represent a single node
- Edges are connected by symbol references between each source files, and are weighted based on occurrences

## Future TODO
- Single command line to generate graph
- Publish graph for different code base
- Identify + map detailed symbol references and type or kind
- Define node based on something other than source file
- To search/filter on:
	- prefix string?
	- Reference type
	- Reference to function call
	- Reference to variables
	- Reference to header file
- Tool bar to configure and change the physics
- More diverse color for edges
- Live update of graph
- How to make it extensible?
- Graph traversing almost like a function call
- Represent IPC somehow and define them
