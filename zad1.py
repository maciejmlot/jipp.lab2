weights = list(map(int, input("Podaj wagi paczek po przecinku ").split(",")))
maxWeight = -1
while maxWeight < max(weights):
    maxWeight = int(input("Podaj górną granice wagi "))

courses = []

for pack in weights:
    packed = False

    for course in courses:
        if sum(course) + pack <= maxWeight:
            course.append(pack)
            packed = True
            break

    if not packed:
        courses.append([pack])

print("liczba: ", len(courses), "\n kursy: ", courses)