def merge(intervals):
	result = []
	for interval in sorted(intervals):
		if result and interval[0] <= result[-1][1]:
			result[-1][1] = max(result[-1][1], interval[1])
		else:
			result.append(interval)
			
	return result

intervals = [[1,3],[2,6],[8,10],[15,18]]
print(merge(intervals))
