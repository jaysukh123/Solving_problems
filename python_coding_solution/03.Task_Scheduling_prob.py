# Problem:
# A software engineer has several tasks, each with a deadline (day) and a duration (how many days it takes).
# The goal is to find the maximum number of tasks that can be completed without missing their deadlines.
# Return the list of tasks that can be done on time.
# Function to get max number of tasks that can be done before their deadlines
def schedule_tasks(tasks):
    # Sort tasks by deadline (earliest first)
    tasks.sort(key=lambda x: x['deadline'])

    time_spent = 0
    selected_tasks = []

    for task in tasks:
        if time_spent + task['duration'] <= task['deadline']:
            selected_tasks.append(task)
            time_spent += task['duration']
    
    return selected_tasks

# Sample input
tasks = [
    {'name': 'Task 1', 'deadline': 4, 'duration': 2},
    {'name': 'Task 2', 'deadline': 3, 'duration': 1},
    {'name': 'Task 3', 'deadline': 2, 'duration': 1},
    {'name': 'Task 4', 'deadline': 1, 'duration': 2},
]

# Run the function
result = schedule_tasks(tasks)

# Print the result
print("Tasks that can be completed without missing deadlines:")
for task in result:
    print(f"{task['name']} (Deadline: {task['deadline']}, Duration: {task['duration']})")
