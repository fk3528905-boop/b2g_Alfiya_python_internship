student_record ={
    "Name" : "Alfiya",
    "Age" : "19",
    "Marks" : 85.5
}

print(f"Original record: {student_record}")

student_record["Marks"] = 92.0

student_record["Grade"] = "A"

print(f"Update record: {student_record}")