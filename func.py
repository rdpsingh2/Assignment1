def assignment():
    input_data = input("Enter the element:")
    original_list = [int(each) for each in input_data]
    sorted_list = sorted(original_list)
    second_largest = sorted_list[-2]
    print("value:", second_largest)
    index_posn = original_list.index(second_largest)
    print("position :", index_posn + 1)
if __name__ == "__main__":
    result = assignment()


