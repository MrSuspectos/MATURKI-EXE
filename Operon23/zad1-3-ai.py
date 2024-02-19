def read_intervals_from_file(file_name):
    with open(file_name, 'r') as file:
        intervals = []
        for line in file:
            line = line.strip()
            lewy = line[0]
            prawy = line[-1]
            a = int(line.split(lewy)[1].split(',')[0])
            b = int(line.split(prawy)[0].split(',')[1])

            liczby = []
            for i in range(a, b):
                liczby.append(i)

            if lewy == '(':
                liczby.pop(0)
            if prawy == '>':
                liczby.append(b)

            intervals.append((min(liczby), max(liczby)))
        return intervals

def merge_intervals(intervals):
    sorted_intervals = sorted(intervals, key=lambda x: x[0])

    merged_intervals = []
    current_start, current_end = sorted_intervals[0]

    for interval in sorted_intervals[1:]:
        if interval[0] <= current_end:
            current_end = max(current_end, interval[1])
        else:
            merged_intervals.append((current_start, current_end))
            current_start, current_end = interval

    merged_intervals.append((current_start, current_end))

    return merged_intervals

def find_longest_continuous_interval(intervals):
    longest_interval = max(intervals, key=lambda x: x[1] - x[0])
    return longest_interval

file_name = 'przedzialy.txt'
intervals = read_intervals_from_file(file_name)
merged_intervals = merge_intervals(intervals)
longest_interval = find_longest_continuous_interval(merged_intervals)

print("Merged Intervals:", merged_intervals)
print("Longest Continuous Interval:", longest_interval)