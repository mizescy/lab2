import statistics


def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    num_list = get_user_input()
    print("Min and Max:", find_min_max(num_list))
    print("Average:", calc_average(num_list))
    sorted_temps = sort_temperature(num_list)
    print("Sorted Temperatures:", sorted_temps)
    median = calc_median_temperature(sorted_temps)
    print("Median Temperature:", median)

def display_main_menu():
    print("Enter some numbers serparated by commas")

def calc_average(num_list):
    print("calc_average")
    return sum(num_list) / len(num_list)

def get_user_input():
    print("get_user_input")
    input_string = input()
    string_list = input_string.split(',')
    float_list = [float(item.strip()) for item in string_list]
    return float_list

def find_min_max(num_list):
    print("find_min_max")
    return [min(num_list), max(num_list)]

def sort_temperature(num_list):
    print("sort_temperature")
    return sorted(num_list)

def calc_median_temperature(num_list):
    print("calc_median_temperature")
    return statistics.median(num_list)

if __name__ == "__main__":
    main()
