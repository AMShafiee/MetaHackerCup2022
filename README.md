# MetaHackerCup2022
My answers to some problems in https://www.facebook.com/codingcompetitions/hacker-cup/2022/qualification-round

The second_friend.py is my implementation for the B1 problem. 
On each iteration of the main loop (for each case), I call the second_friend method and print the return value.
In the second_friend method, I first receive the number of rows (R) and columns (C) as well as the canvas map (tree or temp for each space).
Then, I return "Impossible" if the number of rows or columns is 1, and there is at least one tree on the canvas. If there isn't any tree, then we can consider that we also don't have any tree in the solution (so, I change the filled_with variable with "." instead of "^"), and as a result, there isn't any lonely tree there.
Finally, in the returned value, we have a canvas with a tree in each of the cells of spaces, or the canvas is completely free of trees.

The second_second_friend.py is my implementation for the B2 problem. 
On each iteration of the main loop (for each case), I call the second_second_friend method and print the return value.
In the second_friend method, I first receive the number of rows (R) and columns (C) as well as the canvas map (tree, temp, or rock for each space).
At the first step of providing the solution, a new canvas named altered_canvas is created with all of the cells (spaces) filled with trees except those which contain rock in it and then removing any tree that doesn't have at least two tree neighbours. We need to keep in mind that removing any tree can affect its neighbours in a way that converts a space with at least 2 tree neighbours to a space with one or zero tree neighbors. So, we need to keep the number of tree neighbours somewhere like in number_of_possible_tree_neighbors and make necessary changes after remocing any tree. If we have a new tree space with the number of possible tree neighbours less than 2, we have to append it to the list of trees that are going to be removed or tree_list_to_be_removed.
