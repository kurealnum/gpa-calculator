import argparse
from gpa_calc import gpa_calc

parser = argparse.ArgumentParser(description="GPA calculator")
parser.add_argument(
    "--semester",
    help="combine & average two semester grades into a year long grade (recommended)",
    action="store_true",
)
args = parser.parse_args()

scale = input("Enter the desired scale (4 or 5): ")
if scale == "4" or scale == "four":
    grade_sum = total = 0
    while True:
        res = 0.0

        if args.semester:
            first_semester = float(
                input("Enter your grade for the first semester of class X: ")
            )
            if first_semester == -1.0 or first_semester is None:
                break

            second_semester = float(
                input("Enter your grade for the second semester of class X: ")
            )

            if second_semester == -1.0 or first_semester == -1.0:
                pass
            else:
                avg = (first_semester + second_semester) / 2
                res = gpa_calc(avg)

        else:
            cur = float(input("Enter a grade from 0-100 (enter -1 to exit): "))
            res = gpa_calc(cur)

        if res == -1.0:
            break
        elif res is None:
            pass
        else:
            grade_sum += res

        total += 1

    gpa = grade_sum / total
    print(f"You entered {total} classes.")
    print(f"Your final GPA is {gpa}.")
