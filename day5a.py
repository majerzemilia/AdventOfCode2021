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
    coord_min = fun(lines_dict, key=lambda t: fun(t[coord + "0"], t[coord + "1"]))
    return fun(coord_min[coord + "0"], coord_min[coord + "1"])


def access_idx(x, y):
    return x - x_min, y - y_min


lines = load_file()
lines_hor_vec = list(filter(lambda t: t["x0"] == t["x1"] or t["y0"] == t["y1"], lines))

x_min = get_end(lines_hor_vec, "x", min)
x_max = get_end(lines_hor_vec, "x", max)
y_min = get_end(lines_hor_vec, "y", min)
y_max = get_end(lines_hor_vec, "y", max)

vents = np.zeros((y_max - y_min + 1, x_max - x_min + 1))

for line in lines_hor_vec:
    x0, y0 = access_idx(line["x0"], line["y0"])
    x1, y1 = access_idx(line["x1"], line["y1"])
    if x0 == x1:
        vents.T[x0][min(y0, y1): max(y0, y1) + 1] += 1
    else:
        vents[y0][min(x0, x1): max(x0, x1) + 1] += 1

print(np.sum(vents > 1))
