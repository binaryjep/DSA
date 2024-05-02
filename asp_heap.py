import heapq

def activity_selection_with_heap(start, finish):
    n = len(start)
    activities = [(finish[i], start[i]) for i in range(n)]
    heapq.heapify(activities)  # Convert the list into a min-heap based on finish times
    
    selected_activities = []
    last_finish_time = -float('inf')  # Initialize with negative infinity
    
    while activities:
        finish_time, start_time = heapq.heappop(activities)
        if start_time >= last_finish_time:
            # If the current activity starts after or at the same time as the last selected activity finishes,
            # select the current activity
            selected_activities.append((start_time, finish_time))
            last_finish_time = finish_time
    
    return selected_activities

# Example usage
start_times = [1, 3, 0, 5, 8, 5]
finish_times = [2, 4, 6, 7, 9, 9]

selected = activity_selection_with_heap(start_times, finish_times)

print("Selected Activities:")
for activity in selected:
    print("Start:", activity[0], "Finish:", activity[1])
