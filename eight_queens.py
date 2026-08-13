import random

N = 8

def calculate_conflicts(state):
    conflicts = 0

    for i in range(N):
        for j in range(i + 1, N):

            # Check diagonal conflict
            if abs(state[i] - state[j]) == abs(i - j):
                conflicts += 1

    return conflicts


# Generate neighbouring states
def get_neighbors(state):
    neighbors = []

    for col in range(N):
        for row in range(N):

            if row != state[col]:

                new_state = state.copy()
                new_state[col] = row

                neighbors.append(new_state)

    return neighbors


# Hill Climbing Algorithm
def hill_climbing():

    # Generate a random initial state
    current = [random.randint(0, N - 1) for _ in range(N)]

    while True:

        current_conflicts = calculate_conflicts(current)

        # Goal state
        if current_conflicts == 0:
            return current

        # Generate neighbours
        neighbors = get_neighbors(current)

        # Select the best neighbour
        best = min(neighbors, key=calculate_conflicts)

        best_conflicts = calculate_conflicts(best)

        # Stop if no better neighbour exists
        if best_conflicts >= current_conflicts:
            return current

        current = best


# Display the chess board
def print_board(state):

    for row in range(N):

        for col in range(N):

            if state[col] == row:
                print("Q", end=" ")
            else:
                print(".", end=" ")

        print()


# Run the algorithm
solution = hill_climbing()

print("Eight Queens - Hill Climbing")
print("Solution:", solution)
print("Conflicts:", calculate_conflicts(solution))

print("\nChess Board:")
print_board(solution)
