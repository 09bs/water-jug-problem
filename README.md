
# Water Jug Problem

The Water Jug Problem is a classic puzzle in artificial intelligence involving two jugs, one with a capacity of 'x' liters and the other 'y' liters, and a unlimited water source. The goal is to measure a specific 'z' liters of water using these jugs, with no volume markings.


## Example: Water Jug Problem


#### Problem Statement
You are given two jugs, a 4-liter jug and a 3-liter jug. You need to measure exactly 2 liters of water using only these jugs. You can fill the jugs with water, empty them, or pour water from one jug to another.

#### Solution

- Fill the 4-liter jug: (4,0)
- Pour water from the 4-liter jug into the 3-liter jug until it's full: (1,3)
- Empty the 3-liter jug: (1,0)
- Pour the remaining 1 liter from the 4-liter jug into the 3-liter jug: (0,1)
- Fill the 4-liter jug again: (4,1)
- Pour water from the 4-liter jug into the 3-liter jug until it's full. This will leave 2 liters in the 4-liter jug: (2,3)
- Done! You now have exactly 2 liters of water in the 4-liter jug.

| Step | (4-liter Jug, 3-liter Jug) | Action                          |
|------|-------------------------------|---------------------------------|
| 1    | (4,0)                         | Fill the 4-liter jug          |
| 2    | (1,3)                         | Pour water into the 3-liter jug from the 4-liter jug until full |
| 3    | (1,0)                         | Empty the 3-liter jug         |
| 4    | (0,1)                         | Pour remaining water from the 4-liter jug into the 3-liter jug |
| 5    | (4,1)                         | Fill the 4-liter jug again    |
| 6    | (2,3)                         | Pour water into the 3-liter jug from the 4-liter jug until full |


## Water Jug Problem Code Explanation

### Function `path_finder(path: list)`

This function takes a list `path` as input, which contains the sequence of steps taken to solve the problem. It reconstructs the final path by tracing back from the final state to the initial state using the information stored in the `path` list.

#### Parameters:
- `path`: A list containing tuples representing the state of the jugs and the action taken in each step.

#### Returns:
- `final`: A list containing tuples representing the sequence of states from the initial state to the final state.

### Function `water_jug(x: int, y: int, z: int)`

This function determines whether it is possible to measure a specific quantity `z` using two jugs with capacities `x` and `y`. It utilizes a breadth-first search algorithm to explore all possible states and actions until the target quantity is achieved.

#### Parameters:
- `x`: Capacity of the first jug.
- `y`: Capacity of the second jug.
- `z`: Required quantity to be measured.

#### Returns:
- `True` if it's possible to measure the required quantity using the given jugs, along with printing the sequence of actions.
- `False` if it's not possible to measure the required quantity using the given jugs.

#### Algorithm:
1. Initialize a deque `que` with the initial state `(0, 0, 'start', -1)` representing both jugs being empty, along with an action `'start'` and `-1` indicating no previous action.
2. Use a dictionary `visited` to keep track of visited states to avoid revisiting.
3. Use a list `path` to store the sequence of states and actions taken to reach each state.
4. Perform a breadth-first search by exploring all possible actions:
   - Fill the first jug.
   - Fill the second jug.
   - Empty the first jug.
   - Empty the second jug.
   - Pour water from one jug to another.
5. If the target quantity `z` is reached, print the sequence of actions using the `path_finder` function and return `True`.
6. If the target quantity `z` cannot be reached, print "Not Possible" and return `False`.

## Authors

- [@09bs](https://www.github.com/09bs)
- [@bhargavsai-lingampalli](https://www.github.com/bhargavsai-lingampalli)


## License
[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://github.com/09bs/water-jug-problem/blob/main/LICENSE)

