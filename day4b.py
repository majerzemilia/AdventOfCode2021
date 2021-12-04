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
    arr = np.concatenate([mask.T for mask in masks])
    prod = arr @ vec
    return np.where(prod == width)[0] // width

boards = []
curr_arr = None

with open(os.path.join("data", "day4.txt"), mode="r") as f:
    for i, line in enumerate(f):
        line = line.strip()
        if i == 0:
            input_numbers = [int(num) for num in line.split(',')]
            continue
        if line == '':
            if curr_arr is not None:
                boards.append(curr_arr)
            curr_arr = []
            continue
        curr_input = [int(number) for number in line.split()]
        curr_arr.append(curr_input)
    boards.append(curr_arr)
    
boards = np.array(boards)
masks = np.zeros(boards.shape)

finished_arrays = np.array([False] * len(boards))

i = 0
while sum(finished_arrays) < len(boards) and i < len(input_numbers):
    curr_num = input_numbers[i]
    masks = np.add(masks, boards == curr_num)
    finished_arrays_idxes = np.concatenate((check_rows_sum(masks), check_cols_sum(masks)))
    if len(finished_arrays_idxes) != 0:
        last_one_idx = np.where(finished_arrays==False)[0]
        finished_arrays[finished_arrays_idxes] = True
    i += 1

last_one = boards[last_one_idx]
last_one_mask = masks[last_one_idx]
last_one_negated_mask = np.where(last_one_mask==1, 0, 1)
print(int(curr_num * np.sum(np.multiply(last_one, last_one_negated_mask))))
