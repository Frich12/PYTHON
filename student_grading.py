def grade_student (mark):
    if mark>=80:
      return "Distinction"
    elif mark >= 60 and mark <80:
       return "Credit"   
    elif mark >= 40 and mark <60:
       return "Fair"
    else:
       return "Fail"

student_mark=50
result= grade_student(student_mark)
print(f"The student scored {student_mark} marks, which is graded as {result}.")
 