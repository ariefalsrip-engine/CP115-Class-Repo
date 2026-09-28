target_points = int(input())

points = 0
total_points = 0
rounds_played = 0

while points < target_points:

    points = int(input("Enter Points:"))
    total_points = points + total_points
    rounds_played += 1
print(total_points)
print(rounds_played)
