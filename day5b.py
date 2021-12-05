import numpy as np
import os


def load_file():
	lines = []
	with open(os.path.join("data", "day5.txt")) as f:
		for line in f:
			start, end = line.strip().split(" -> ")
			x0, y0 = start.split(',')
			x1, y1 = end.split(',')
			lines.append({
				"x0": int(x0),
				"y0": int(y0),
				"x1": int(x1),
				"y1": int(y1)
			})
	return lines

		
def get_end(lines_dict, coord, fun):
    coord_min = fun(lines_dict, key = lambda t: fun(t[coord+"0"], t[coord+"1"]))
    return fun(coord_min[coord+"0"], coord_min[coord+"1"])

	
def access_idx(x, y):
    return x - x_min, y - y_min
	

def inclusive_range(start, stop, step):
    return range(start, stop+step, step)
	

lines = load_file()

x_min = get_end(lines, "x", min)
x_max = get_end(lines, "x", max)
y_min = get_end(lines, "y", min)
y_max = get_end(lines, "y", max)

vents = np.zeros((y_max - y_min + 1, x_max - x_min + 1))

for line in lines:
    x0, y0 = access_idx(line["x0"], line["y0"])
    x1, y1 = access_idx(line["x1"], line["y1"])
    if x0 == x1:
        vents.T[x0][min(y0, y1) : max(y0, y1) + 1] += 1
    elif y0 == y1:
        vents[y0][min(x0, x1) : max(x0, x1) + 1] += 1
    else:
        for x, y in zip(inclusive_range(x0, x1, 1-2*(x1<x0)), inclusive_range(y0, y1, 1-2*(y1<y0))):  # 1-2*(c1<c0) for step equaling 1 or -1
            vents[y][x] += 1
		
print(np.sum(vents > 1))
