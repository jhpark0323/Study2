N = int(input())
coordinates = list(map(int, input().split()))

sorted_unique_coords = sorted(set(coordinates))

coord_dict = {value: idx for idx, value in enumerate(sorted_unique_coords)}

compressed_coords = [coord_dict[x] for x in coordinates]

print(' '.join(map(str, compressed_coords)))
