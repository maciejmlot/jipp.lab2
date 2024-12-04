def knapsack(items, capacity):
    n = len(items)
    dp = [[0] * (capacity + 1) for _ in range(n+1)]

    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            weight, value = items[i - 1]
            if weight <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weight] + value)
            else: 
                dp[i][w] = dp[i - 1][w]

    w = capacity
    selected = []
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i-1][w]:
            selected.append(items[i-1])
            w -= items[i-1][0]

    return dp[n][capacity], selected

weightAndPriceCollection = list(map(int, input("podaj przedmioty jako waga1, wartosc1, waga2, wartosc2, ... ").split(",")))
items = []
for i in range(0, len(weightAndPriceCollection) - 1, 2):
    items.append((weightAndPriceCollection[i], weightAndPriceCollection[i+1]))

capacity = int(input("Podaj pojemność plecaka "))

max, content = knapsack(items, capacity)

print("maksymalna wartość to ", max, "\nzawartość to ", content)