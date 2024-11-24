scale = input("Enter the desired scale (4 or 5): ")
if scale == "4" or scale == "four":
    grade_sum = total = cur = 0
    while cur != -1:
        cur = float(input("Enter a grade from 0-100 (enter -1 to exit): "))

        if cur >= 97:
            grade_sum += 4.0
        elif cur >= 93:
            grade_sum += 4.0
        elif cur >= 90:
            grade_sum += 3.7
        elif cur >= 87:
            grade_sum += 3.3
        elif cur >= 83:
            grade_sum += 3.0
        elif cur >= 80:
            grade_sum += 2.7
        elif cur >= 77:
            grade_sum += 2.3
        elif cur >= 73:
            grade_sum += 2.0
        elif cur >= 70:
            grade_sum += 1.7
        elif cur >= 67:
            grade_sum += 1.3
        elif cur >= 65:
            grade_sum += 1.0
        elif -1 < cur < 65:
            grade_sum += 0.0
        elif cur == -1:
            break
        else:
            print("Error entering value. Please retry.")

        total += 1

    gpa = grade_sum / total
    print(f"You entered {total} classes.")
    print(f"Your final GPA is {gpa}.")
