#!/usr/bin/python3

lower_bound = 124075
upper_bound = 580769
valid_passwords = []

for password in range(lower_bound, upper_bound + 1):
    password_s = str(password)
    double = False
    monotonic = True
    for index in range(0, len(password_s) - 1):
        if password_s[index] is password_s[index + 1]:
            if password_s.count(password_s[index]) == 2: # Part 2
                double = True
        if password_s[index + 1] < password_s[index]:
            monotonic = False
    if double and monotonic:
        valid_passwords.append(password)

print("Number of valid passwords:", len(valid_passwords))
