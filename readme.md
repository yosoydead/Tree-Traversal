* In this repo I'll put some code to show how to traverse a tree.
* I used a BST to perform these two types of traversing.
* **!Disclaimer** I did not add any edge test cases for the tree at the moment.
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
    * Depth-First Search (going up or down visiting nodes, depending on the approach you chose):
        1. DFS - PreOrder (recursively):
            - create a variable to store the values of nodes visited
            - store the root of the BST in a variable called *current*
            - write a helper function which accepts a node
                * push the value of the node to the variable that stores the values
                * if the node has a left property, call the helper function with the left property on the node
                * if the node has a right property, call the helper function with the right property on the node
            - invoke the helper function with the *current* variable
            - return the array of values
        2. DFS - PostOrder (recursively) -> by using this method, the root note is the last node to be visited. Also, it is very similar to the PreOrder variant:
            - create a variable to store the values of nodes visited
            - store the root of the BST in a variable called *current*
            - write a helper function which accepts a node
                * if the node has a left property, call the helper function with the left property on the node
                * if the node has a right property, call the helper function with the right property on the node
                * push the value of the note to the variable that stores the values
            - invoke the helper function with the currrent variable
            - return the array of values
