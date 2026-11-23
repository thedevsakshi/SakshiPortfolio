


from itertools import permutations

# Travel time in minutes between locations
graph = {
    "A": {"B": 10, "C": 15, "D": 20, "E": 18},
    "B": {"A": 10, "C": 35, "D": 25, "E": 30},
    "C": {"A": 15, "B": 35, "D": 30, "E": 20},
    "D": {"A": 20, "B": 25, "C": 30, "E": 15},
    "E": {"A": 18, "B": 30, "C": 20, "D": 15}
}

def minimum_route():
    locations = [place for place in graph if place != "A"]
    best_route = None
    minimum_time = float("inf")

    for order in permutations(locations):
        route = ["A"] + list(order) + ["A"]
        total_time = sum(graph[route[i]][route[i + 1]]
                         for i in range(len(route) - 1))
        if total_time < minimum_time:
            minimum_time = total_time
            best_route = route

    return best_route, minimum_time

route, travel_time = minimum_route()
print("Best delivery route:", " -> ".join(route))
print("Minimum total travel time:", travel_time, "minutes")

1 . librarybook

from collections import Counter
n = int(input("Enter number of books: "))
if n <= 0:
    print("Please enter at least one book.")
    raise SystemExit
books = []
for i in range(n):
    books.append(input(f"Enter book {i + 1} name: "))
borrow_counts = []
for book in books:
    count = int(input(f"Enter borrowing count for {book}: "))
    borrow_counts.append(count)
average = sum(borrow_counts) / n
max_count = max(borrow_counts)
min_count = min(borrow_counts)
print("\\nAverage borrowing count:", average)
print("Highest borrowed book(s):")
for i, count in enumerate(borrow_counts):
    if count == max_count:
        print(books[i], "-", count)
print("Lowest borrowed book(s):")
for i, count in enumerate(borrow_counts):
    if count == min_count:
        print(books[i], "-", count)
print("Books not borrowed:", borrow_counts.count(0))
frequency = Counter(borrow_counts)
highest_frequency = max(frequency.values())
modes = [value for value, freq in frequency.items()
         if freq == highest_frequency]
print("Most frequent borrowing count(s):", modes)

