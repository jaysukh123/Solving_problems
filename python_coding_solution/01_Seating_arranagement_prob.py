"""
Seating Arrangement Problem

You have N guests attending a dinner party. Each guest has exactly two preferred neighbors 
they'd like to sit next to. Your task is to:
 - Accept the number of guests and their neighbor preferences.
 - Determine a valid circular seating arrangement that satisfies all preferences.
 - If no arrangement is possible, clearly state that.

Example Input:
guests = {
    'Alice': ['Bob', 'Carol'],
    'Bob': ['Alice', 'David'],
    'Carol': ['Alice', 'David'],
    'David': ['Bob', 'Carol']
}
"""

from itertools import permutations

def is_valid_seating(order, preferences):
    """
    Checks whether the given circular seating order satisfies all guests' neighbor preferences.

    Parameters:
    - order (list): A list representing a permutation of guests.
    - preferences (dict): A dictionary mapping each guest to a list of two preferred neighbors.

    Returns:
    - bool: True if all guests are seated next to both of their preferred neighbors.
    """
    n = len(order)
    for i in range(n):
        guest = order[i]
        left_neighbor = order[(i - 1) % n]    # Circular left neighbor
        right_neighbor = order[(i + 1) % n]   # Circular right neighbor

        # Check if both preferred neighbors are adjacent (left or right)
        if not (preferences[guest][0] in [left_neighbor, right_neighbor] and
                preferences[guest][1] in [left_neighbor, right_neighbor]):
            return False  # Guest's preference not satisfied
    return True  # All preferences satisfied

def find_seating_arrangement(preferences):
    """
    Tries all permutations to find a valid circular seating arrangement.

    Parameters:
    - preferences (dict): Guest to preferred neighbors mapping.

    Returns:
    - list or None: A valid seating order as a list if found, else None.
    """
    guests = list(preferences.keys())

    for perm in permutations(guests):
        if is_valid_seating(perm, preferences):
            return list(perm)  # Valid arrangement found

    return None  # No valid arrangement found

# ---------------------- Sample Input ---------------------- #
guests = {
    'Alice': ['Bob', 'Carol'],
    'Bob': ['Alice', 'David'],
    'Carol': ['Alice', 'David'],
    'David': ['Bob', 'Carol']
}

# ---------------------- Run & Output ---------------------- #
arrangement = find_seating_arrangement(guests)

if arrangement:
    print("✅ Valid seating arrangement found:")
    print(" -> ".join(arrangement))
else:
    print("❌ No valid seating arrangement is possible.")
