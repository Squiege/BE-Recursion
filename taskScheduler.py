# list of tasks and n represents the number of tasks inside of our list
def schedule_tasks(task_hierarchy, n=None):
    # Unless provided, n is set to the length of the list of dictionaries
    if n is None:
        n = len(task_hierarchy)

    # Base case - Only 1 task
    if n <= 1:
        return task_hierarchy

    # I am using bubble sort to order them so the time complexity is O(n^2) and the space complexity is O(n) depending on the number of tasks
    # I can use other sorting methods depending on the size of the data to create more efficient sorting.
    # Sorting tasks based on priority

    # Getting the entire list
    for i in range(n - 1):
        # Using my get priority function to gather the priority of the target task and the one next in line
        if get_priority(task_hierarchy[i]) > get_priority(task_hierarchy[i + 1]):
            # Swap the elements if they are in the wrong order
            task_hierarchy[i], task_hierarchy[i + 1] = task_hierarchy[i + 1], task_hierarchy[i]

    # Organizing subtasks with recursion
    for task in task_hierarchy:
        # Checking if there are any subtasks, without this I was recieving a KeyError
        if 'subtasks' not in task:
            task['subtasks'] = []
        # Using recursion to bubble sort the subtasks 
        if task['subtasks']: 
            task['subtasks'] = schedule_tasks(task['subtasks'])

    # Recursively call the function
    return task_hierarchy

# Gathers the priority of a given task
def get_priority(task):
    return task["priority"]

# Task hierarchy with parent and subtasks, predefined data
task_hierarchy = [
    {"id": 1, "name": "cleaning", "subtasks": [
        {"id": 4, "name": "bathroom", "priority": 2},
        {"id": 5, "name": "closet", "priority": 3},
        {"id": 6, "name": "bedroom", "priority": 1}
    ], "priority": 2},
    {"id": 2, "name": "washing", "subtasks": [
        {"id": 7, "name": "laundry", "priority": 1},
        {"id": 8, "name": "dishes", "priority": 2}
    ], "priority": 1},
    {"id": 3, "name": "organizing", "subtasks": [
        {"id": 9, "name": "files", "priority": 3},
        {"id": 10, "name": "desk", "priority": 1},
        {"id": 11, "name": "bedroom", "priority": 2}
    ], "priority": 3}
]

# Sort tasks based on priority
sorted_tasks = schedule_tasks(task_hierarchy)

# Print the tasks and subtasks in order of priority
def print_tasks(tasks):
    for task in tasks:
        print(f"Task: {task['name']}, Priority: {task['priority']}")
        if task['subtasks']:
            print("  Subtasks:")
            print_tasks(task['subtasks'])

print_tasks(sorted_tasks)
