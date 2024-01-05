import re


def read_file_and_return_calibration_sum(file_path: str) -> int:
    cordinates_sum = 0

    try:
        with open(file_path, "r") as file:
            for line in file:
                line.strip()
                numbers = [int(match) for match in re.findall(r"\d", line)]
                cordinates = str(numbers[0]) + str(numbers[-1])
                cordinates_sum += int(cordinates)

    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

    return cordinates_sum


if __name__ == "__main__":
    print(read_file_and_return_calibration_sum("day-01/input.txt"))
