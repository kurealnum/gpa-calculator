def gpa_calc(cur):

    if cur >= 97:
        return 4.0
    elif cur >= 93:
        return 4.0
    elif cur >= 90:
        return 3.7
    elif cur >= 87:
        return 3.3
    elif cur >= 83:
        return 3.0
    elif cur >= 80:
        return 2.7
    elif cur >= 77:
        return 2.3
    elif cur >= 73:
        return 2.0
    elif cur >= 70:
        return 1.7
    elif cur >= 67:
        return 1.3
    elif cur >= 65:
        return 1.0
    elif -1 < cur < 65:
        return 0.0
    elif cur == -1:
        return -1.0
    else:
        print("Error entering value. Please retry.")
        return None
