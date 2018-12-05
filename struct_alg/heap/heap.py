import heapq

H = [21, 1, 45, 78, 3, 5]
# Use heapify to rearrange the elements
heapq.heapify(H)
print(H)

heapq.heappush(H, 8)
print(H)

heapq.heappush(H, 89)
print(H)

heapq.heappop(H)
print(H)

heapq.heappop(H)
print(H)

heapq.heapreplace(H, 655)
print(H)
