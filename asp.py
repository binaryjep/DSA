def activity_selection(start:list, finish:list): 

    n = len(start)

    # Sort activities by their finish time 
    activities = sorted(zip(finish, start))

    selected_activities = [activities[0]]  # Select the first activity

    for i in range(1, n):  # Iterate through the remaining activities
        
        if activities[i][1] >= selected_activities[-1][0]:
            selected_activities.append(activities[i])

    return selected_activities

if __name__ == '__main__':

    start_time = []
    finish_time = []

    n_activities = int(input("How many activities do you have? "))

    for i in range(n_activities): 
        s_input = int(input("\033[92mStart Time: \033[0m"))  
        start_time.append(s_input)

        f_input = int(input("\033[91mFinish Time: \033[0m")) 
        finish_time.append(f_input)

    selected = activity_selection(start_time, finish_time)

    print("\n\033[93mSelected Activities:\033[0m") 

    for i, activity in enumerate(selected): 
        print("Activity {} \033[92mStart: {}\033[0m, \033[91mFinish: {}\033[0m".format(i +1,activity[1], activity[0]))  

    print(f"\nThe number of activities selected are \033[93m{len(selected)}\033[0m")