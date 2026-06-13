def get_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 80:
        return "B"
    elif marks >= 70:
        return "C"
    else:
        return "Fail"
    
print(f"Marks 95 --> Grade: {get_grade(95)}")
print(f"Marks 82 --> Grade: {get_grade(82)}")
print(f"Marks 52 --> Grade: {get_grade(52)}")
