import re

def challenge(file_name):
    values = []
    regex_1st_challenge = "[1-9]"

    lines = open(file_name, "r")
    for idx, line in enumerate(lines):

        all_digits = re.findall(regex_1st_challenge, line)

        if len(all_digits) == 1: #if there is a single digit on the line
            calibration_value = int(all_digits[0]) * 10 + int(all_digits[0])
            values.append(calibration_value)

        elif len(all_digits) > 1:
            calibration_value = int(all_digits[0]) * 10 + int(all_digits[-1])
            values.append(calibration_value)

        else:
            print("Line nr {} has no digits\n".format(idx))

    return sum(values)


def main():
    my_sum = challenge(file_name='input.txt')
    print("Final sum is {}".format(my_sum))

main()