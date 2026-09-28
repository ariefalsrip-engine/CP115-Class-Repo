speed = int(input("Enter speed (-1 to stop) :"))
total_readings = 0
longest_streak = 0


while speed != -1:
    total_readings += 1
    if speed < 20 :
        longest_streak += 1
    speed = int(input("Enter speed (-1 to stop) :"))


print(total_readings)
print(longest_streak)