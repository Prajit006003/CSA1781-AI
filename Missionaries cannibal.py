from collections import deque
def is_valid_state(state):
    missionaries_left, cannibals_left, boat_left = state
    missionaries_right = 3 - missionaries_left
    cannibals_right = 3 - cannibals_left
    if missionaries_left < 0 or missionaries_right < 0 or cannibals_left < 0 or cannibals_right < 0:
        return False
    if (missionaries_left > 0 and missionaries_left < cannibals_left) or \
       (missionaries_right > 0 and missionaries_right < cannibals_right):
        return False
    return True
def solve_missionaries_cannibals():
    initial_state = (3, 3, 1) 
    goal_state = (0, 0, 0)      
    visited = set()
    queue = deque([(initial_state, [])])
    while queue:
        current_state, actions = queue.popleft()
        if current_state == goal_state:
            return actions
        visited.add(current_state)
        for missionary_move in range(3):
            for cannibal_move in range(3):
                if 1 <= missionary_move + cannibal_move <= 2:
                    new_state = (
                        current_state[0] - missionary_move,
                        current_state[1] - cannibal_move,
                        1 - current_state[2]
                    )
                    if is_valid_state(new_state) and new_state not in visited:
                        new_actions = actions + [(missionary_move, cannibal_move)]
                        queue.append((new_state, new_actions))
    return None
if __name__ == "__main__":
    solution = solve_missionaries_cannibals()
    if solution:
        print("Solution:")
        for step, (missionaries, cannibals) in enumerate(solution, start=1):
            boat_side = "left" if step % 2 == 1 else "right"
            print(f"Step {step}: Move {missionaries} missionaries and {cannibals} cannibals to the {boat_side} bank.")
    else:
        print("No solution found.")
