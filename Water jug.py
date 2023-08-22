from collections import deque

def water_jug_problem(jug1_capacity, jug2_capacity, target_amount):

    visited = set()

    queue = deque([(0, 0)])

    while queue:

        jug1_level, jug2_level = queue.popleft()

        if jug1_level == target_amount or jug2_level == target_amount:

            return jug1_level, jug2_level

        if jug1_level < jug1_capacity:

            new_state = (jug1_capacity, jug2_level)

            if new_state not in visited:

                queue.append(new_state)

                visited.add(new_state)

        if jug2_level < jug2_capacity:

            new_state = (jug1_level, jug2_capacity)

            if new_state not in visited:

                queue.append(new_state)

                visited.add(new_state)

        if jug1_level > 0:

            new_state = (0, jug2_level)

            if new_state not in visited:

                queue.append(new_state)

                visited.add(new_state)

        if jug2_level > 0:

            new_state = (jug1_level, 0)

            if new_state not in visited:

                queue.append(new_state)

                visited.add(new_state)

        if jug1_level > 0 and jug2_level < jug2_capacity:

            pour_amount = min(jug1_level, jug2_capacity - jug2_level)

            new_state = (jug1_level - pour_amount, jug2_level + pour_amount)

            if new_state not in visited:

                queue.append(new_state)

                visited.add(new_state)

        if jug2_level > 0 and jug1_level < jug1_capacity:

            pour_amount = min(jug2_level, jug1_capacity - jug1_level)

            new_state = (jug1_level + pour_amount, jug2_level - pour_amount)

            if new_state not in visited:

                queue.append(new_state)

                visited.add(new_state)

    return None

if __name__ == "__main__":

    jug1_capacity = 4

    jug2_capacity = 3

    target_amount = 2

    result = water_jug_problem(jug1_capacity, jug2_capacity, target_amount)

    if result:

        jug1_level, jug2_level = result

        print(f"Jug 1 level: {jug1_level}, Jug 2 level: {jug2_level}")

    else:

        print("Solution not possible.")
