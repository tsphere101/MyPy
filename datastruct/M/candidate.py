print("*** Election ***")
input("Enter a number of voter(s) : ")
candidate = [0 for _ in range(20)]
votes = [int(x) for x in input().split()]

voided = True
for data in votes:
    try :
        if data < 0:
            raise IndexError
        candidate[data-1] += 1
    except IndexError as ignore:
        pass
    else : 
        voided = False

if not voided :
    winner = candidate.index(max(candidate)) + 1
    print(winner)
else :
    print("*** No Candidate Wins ***")