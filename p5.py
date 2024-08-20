'''
Accept average score from the student of his exam and print his result as follows:

0 to 49 is Fail
50 to 74 is second class
75 to 90 is first class
91 to 100 is distinction
Also check for invalid score
'''

student_marks = int(input('Enter the marks obtained by the student:'))
if student_marks < 0 or student_marks > 100:
    print('invalid marks')
elif student_marks >= 91:
    print('The student passed with distinction.')
elif student_marks >= 75:
    print('The student passed with first class.')
elif student_marks >= 50:
    print('The student passed with second class.')
else:
    print('The student is failed')