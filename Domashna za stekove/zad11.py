from collections import deque

names = input("Enter the names of all participants: ").split(' ')
elimination_count = int(input("Enter the elimination count: "))


participants = deque(names)

while len(participants) > 1:
    for _ in range(elimination_count - 1):
        participants.append(participants.popleft())  
    eliminated = participants.popleft()
    print(f"{eliminated} is eliminated!")


print(f"The winner is {participants[0]}!")