def get_grade(marks):
    if marks >= 90:
        return 'A'
    elif marks >=87:
        return 'A-'
    elif marks >= 84:
        return 'B+'
    elif marks >=80:
        return 'B'
    elif marks >=77:
        return 'B-'
    elif marks >= 74:
        return 'C+'
    elif marks >= 70:
        return 'C'
    elif marks >= 67:
        return 'C-'
    elif marks >= 64:
        return 'D+'
    elif marks >= 62:
        return 'D'
    elif marks >= 60:
        return 'D-'
    else:
        return 'F'