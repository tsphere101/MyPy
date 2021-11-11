class FC:
    def __init__(self, info_str):
        name, wins, loss, draws, scored, conceded = info_str.split(",")
        self.name = name
        self.wins = int(wins)
        self.loss = int(loss)
        self.draws = int(draws)
        self.scored = int(scored)
        self.conceded = int(conceded)
        self.points = 3 * self.wins + 0 * self.loss + 1 * self.draws
        self.goal_diff = self.scored - self.conceded

    def __lt__(self, o):
        if self.points != o.points:
            return self.points < o.points
        else:
            return self.goal_diff < o.goal_diff

    def __gt__(self, o):
        if self.points != o.points:
            return self.points > o.points
        else:
            return self.goal_diff > o.goal_diff

    def __str__(self):
        return f"['{self.name}', {{'points': {self.points}}}, {{'gd': {self.goal_diff}}}]"


def quicksort(data):
    if len(data) <= 1:
        return data

    left = []
    mid = []
    right = []

    pivot = data[len(data)//2]
    for d in data:
        if d < pivot:
            left.append(d)
        elif d > pivot:
            right.append(d)
        else:
            mid.append(d)

    return quicksort(left) + mid + quicksort(right)


if __name__ == "__main__":

    inp = input("Enter Input : ").split("/")

    teams = []
    for data in inp:
        teams.append(FC(data))

    teams = quicksort(teams)[::-1]
    print("== results ==")
    for data in teams:
        print(data)
