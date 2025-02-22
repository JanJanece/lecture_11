import os
import json

# get current working directory path
cwd_path = os.getcwd()


def read_data(file_name, field):
    """
    Reads json file and returns sequential data.
    :param file_name: (str), name of json file
    :param field: (str), field of a dict to return
    :return: (list, string),
    """
    file_path = os.path.join(cwd_path, file_name)
    if field not in {"unordered_numbers", "ordered_numbers", "dna_sequence"}:
        return None

    with open(file_path, "r") as json_file:
        dict = json.load(json_file)

    return dict[field]


def linear_search(seq, num):
    count = 0
    list_of_positions = []
    for idx, number in enumerate(seq):
        if number == num:
            count += 1
            list_of_positions.append(idx)
    return {"positions": list_of_positions, "count": count}


def main():
    sequential_data = read_data("sequential.json", "unordered_numbers")
    print(sequential_data)

    result_1 = linear_search(sequential_data, 13)
    print(result_1)

if __name__ == '__main__':
    main()