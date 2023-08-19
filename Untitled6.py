#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np

def calculate_grade(percentage):
    if percentage >= 90:
        return 'A+'
    elif percentage >= 80:
        return 'A'
    elif percentage >= 70:
        return 'B+'
    elif percentage >= 60:
        return 'B'
    elif percentage >= 50:
        return 'C'
    else:
        return 'F'

def main():
    num_students = int(input("Enter the number of students: "))
    num_subjects = int(input("Enter the number of subjects: "))

    marks = np.zeros((num_students, num_subjects))

    for i in range(num_students):
        for j in range(num_subjects):
            marks[i][j] = float(input(f"Enter marks for student {i+1}, subject {j+1}: "))

    total_marks = np.sum(marks, axis=1)

    total_subjects = num_subjects * 100
    percentages = (total_marks / total_subjects) * 100
    grades = np.array([calculate_grade(percentage) for percentage in percentages])

    print("\nStudent\tTotal Marks\tPercentage\tGrade")
    print("------------------------------------------")
    for i in range(num_students):
        print(f"{i+1}\t\t{total_marks[i]}\t\t{percentages[i]:.2f}%\t\t{grades[i]}")

if __name__ == "__main__":
    main()


# In[ ]:




