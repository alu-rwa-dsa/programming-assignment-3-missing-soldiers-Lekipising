# Write your code here
# Number of barriers
TotalBarriers = int(input())

# hold the barriers coordinates
barriers = []

# get the coordinates from the user
for i in range(TotalBarriers):
    x, y, d = map(int, input().strip().split())
    barriers.append((x, x + d))

# sort the barriers
barriers.sort()

# initialize blocked ants counter
BlockedAnts = b_point = 0

# block ants in the coordinates
for barrier in barriers:
    if barrier[0] >= b_point:
        b_point = barrier[0]
        if b_point < barrier[1]:
            BlockedAnts += (barrier[1] - b_point) + 1
            b_point = barrier[1] + 1
    elif b_point <= barrier[1]:
        BlockedAnts += (barrier[1] - b_point) + 1
        b_point = barrier[1] + 1

print(BlockedAnts)
