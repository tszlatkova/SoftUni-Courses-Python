# Write a program that finds the longest intersection. You will be given a number N. On
# each of the next N lines you will be given two ranges in the format: "{first_start},
# {first_end}-{second_start},{second_end}". You should find the intersection of these two
# ranges. The start and end numbers in the ranges are inclusive.
# Finally, you should find the longest intersection of all N intersections, print the
# numbers that are included and its length in the format: "Longest intersection is
# [{longest_intersection_numbers}] with length {length_longest_intersection}"
# Note: in each range, there will always be an intersection. If there are two equal
# intersections, print the first one.

number_lines = int(input())
len_intersection = 0
longest_intersection = set()

for _ in range(number_lines):
    ranges = input().split('-')
    first_start, first_end = [int(item) for item in ranges[0].split(',')]
    second_start, second_end = [int(item) for item in ranges[1].split(',')]

    first_set = set(i for i in range(first_start, first_end+1))
    second_set = set(j for j in range(second_start, second_end+1))

    intersection = first_set.intersection(second_set)

    if len(intersection) > len_intersection:
        len_intersection = len(intersection)
        longest_intersection = intersection

longest_intersection = list(str(item) for item in longest_intersection)
print(f"Longest intersection is [{', '.join(longest_intersection)}] "
      f"with length {len_intersection}")
