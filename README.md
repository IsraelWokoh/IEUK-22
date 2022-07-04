# Amazon Coding Challenge: Pathfinding
**Bright Network Internship, June 2022**


# Overview:
In this challenge, you are going to implement Amazon’s pathfinding algorithm for Amazon’s self-driving delivery vehicles. The self-driving vehicle will need to create a path on a 2D-grid that contains a **starting point** `(x0,y0)`, a **delivery point** `(xN,yN)` and a number of **obstacles**.

Your vehicle can navigate to any of the adjacent squares (even diagonally), as long as the squares are within bounds and do not contain an obstacle.

## Phase 1
Implement a **10x10 grid** with:
- **starting point** `(0,0)`,
- **delivery point** `(9,9)`,
- **obstacles** at `(9,7)`, `(8,7)`, `(6,7)`, `(6,8)`.

**Calculate a path that avoids obstacles and reaches the delivery point.**

Your solution should print the path in the format `[(x0, y0), (x1, y1),...,(xN, yN)]` and the number of steps.

## Phase 2
**Insert an additional 20 obstacles at random locations**, ensuring they don't overlap existing ones or lie at the start and delivery points. Print their locations using the format `[(x1, y1), (x2, y2),...,(xK, yK)]`.

**Again, find a valid path to the delivery point, avoiding any obstacles.**

## BONUS
In the event that your vehicle is unable to reach its destination, your algorithm should print `"Unable to reach delivery point"`.

**Identify the least amount of obstacles to be removed** in order for the vehicle to reach the end point, using the format `[(x1, y1), (x2, y2),...,(xK, yK)]`.
