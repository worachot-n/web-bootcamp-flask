numbers = [1, 3, 5]
doubled = [num * 2 for num in numbers]

# for num in numbers:
#     doubled.append(num * 2)

print(doubled)

friends = ["Rolf", "Sam", "Samantha", "Saurabh", "Jen"]
start_s = [friend for friend in friends if friend.startswith("S")]

# for friend in friends:
#     if friend.startswith("S"):
#         start_s.append(friend)

print(start_s)
print(start_s is friends)
