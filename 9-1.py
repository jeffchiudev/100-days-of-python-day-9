student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

#TODO-2: Write your code below to add the grades to student_grades.👇

for key in student_scores:
    student_grades.update({key: student_scores[key]}) 

for key in student_grades:
    if student_grades[key] > 90:
        student_grades[key] = "Outstanding"
    elif (student_grades[key] > 80) and (student_grades[key] <= 90):
        student_grades[key] = "Exceeds Expectations"
    elif (student_grades[key] > 70) and (student_grades[key] <= 80):
        student_grades[key] = "Acceptable"
    else:
        student_grades[key] = "Fail"

# 🚨 Don't change the code below 👇
print(student_grades)