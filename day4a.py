import numpy as np
import os

def check_rows_sum(masks):
    width, height = masks.shape[1], masks.shape[2]
    vec = np.ones((masks.shape[1], 1))
    arr = np.concatenate(masks)
    prod = arr @ vec
    return np.where(prod == width)[0] // height


def check_cols_sum(masks):
    width, height = masks.shape[1], masks.shape[2]
    vec = np.ones((masks.shape[2], 1))
    arr = np.concatenate(masks, axis=1).T
    prod = arr @ vec
    return np.where(prod == width)[0] // width


with open(os.path.join("data", "day4.txt"), mode="r") as f:
    input_numbers = [int(num) for num in next(f).strip().split(',')]
    boards = np.loadtxt(f)
    boards = boards.reshape((-1, boards.shape[1], boards.shape[1]))

masks = np.zeros(boards.shape)

for curr_num in input_numbers:
    masks = np.add(masks, boards == curr_num)
    finished_arrays = np.concatenate((check_rows_sum(masks), check_cols_sum(masks)))
    if len(finished_arrays) == 0:
        continue
    winner = boards[finished_arrays[0]]
    winner_mask = masks[finished_arrays[0]]
    winner_negated_mask = np.where(winner_mask==1, 0, 1)
    print(int(curr_num * np.sum(np.multiply(winner, winner_negated_mask))))
    break
