* In this repo I'll put some code to show how to traverse a tree.
* I used a BST to perform these two types of traversing.
* There are **two** ways to traverse a tree:
    * Breadth-First Search (visiting each node horizontally/visit every node/sibling on each level before moving down). 
        1. Iterative steps:
            - create a queue (it can be an array) and a variable to store the values of nodes visited
            - place the root node in the queue
            - loop as long as there is anything in the queue
                - dequeue a node from the queue and push the value of the node into the variable that stores the nodes
                - if there is a left property on the node dequeued - add it to the queue
                - if there is a right property on the node dequeued - add it to the queue
            - return the variable that stores the values
    * Depth-First Search (going up or down visiting nodes, depending on the approach you chose)