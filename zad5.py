def select(tasks):
    tasks.sort(key=lambda x: x[1])

    maxReward = 0
    selectedTasks = []
    lastEndTime = 0

    for start, end, reward in tasks:
        if start >= lastEndTime:
            selectedTasks.append((start, end, reward))
            maxReward += reward
            lastEndTime = end

    return maxReward,selectedTasks

untupledTasks = list(map(int, input("podaj zadania jako start1, koniec1, nagroda1, start2, koniec2, nagroda2, ... ").split(",")))
tasks = []
for i in range(0, len(untupledTasks) - 1, 3):
    tasks.append((untupledTasks[i], untupledTasks[i+1], untupledTasks[i+2]))

print("Maksymalna nagroda i harmonogram: ", select(tasks))