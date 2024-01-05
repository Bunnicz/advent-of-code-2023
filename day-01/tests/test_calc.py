from calc import read_file_and_return_calibration_sum


def test_read_file_and_return_calibration_sum():
    assert read_file_and_return_calibration_sum("day-01/example_test_data.txt") == 496
