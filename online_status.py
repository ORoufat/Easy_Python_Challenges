STATUSES = {
    "ALICE": "ONLINE",
    "BOB": "OFFLINE",
    "EVE": "ONLINE",
}


def online_account(people):
    count = 0
    for person, status in people.items():
        if status == "online":
            count += 1
    return count


# SOLUTION_2


def online_count(people):
    return len([p for p in people if people[p] == "online"])


# SOLUTION_3

count = 0


def absences():
    global count
    for keys, values in STATUSES.items():
        if values == "offline":
            count += 1
    return count


print(absences())

