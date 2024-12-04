from functools import reduce

def dispatch(tasks:int):
    optimalOrder = sorted(tasks, key=lambda x: x[0])

    currentTime = 0
    waitingTimes = []
    for time, _ in optimalOrder:
        currentTime += time
        waitingTimes.append(currentTime)

    totalTime = reduce(lambda acc, x: acc + x, waitingTimes, 0)

    return optimalOrder, totalTime


timeAndRewardCollection = list(map(int, input("podaj zadania jako czas1, nagroda1, czas2, nagroda2, ... ").split(",")))
tasks = []

for i in range(0, len(timeAndRewardCollection) - 1, 2):
    tasks.append((timeAndRewardCollection[i], timeAndRewardCollection[i+1]))

order, time = dispatch(tasks)
print("Optymalna kolejność zadań: ", order, "\nCałkowity czas oczekiwania: ", time)