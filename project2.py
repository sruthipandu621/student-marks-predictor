
# Student_marks_predictor (project)
print("welcome to student_marks_predictor:")
#Take inputs from user
person=input("enter your name:")
assignment_marks=float(input("enter your assignment (out of 5):"))
internal_marks=float(input("enter your internal (out of 30):"))
external_marks=float(input("enter your external (out of 30):"))
attendance=float(input("enter your attedance percentage (0-100):"))
records=float(input("enter your record marks (out of 5):"))
Mid1=float(input("enter your mid1 marks (out of 30):"))
Mid2=float(input("enter your mid2 marks (out of 30):"))
#normalize all marks
assignment_percentage= (assignment_marks/5)*100
internal_percentage=(internal_marks/30)*100
external_percentage=(external_marks/30)*100
attendance_percentage=(attendance/100)*100
records_percentage=(records/5)*100
mid1_percentage=(Mid1/30)*100
mid2_percentage=(Mid2/30)*100
#calculate the weights
assignment_weight=5/230
internal_weight=30/230
external_weight=30/230
attendance_weight=100/230
records_weight=5/230
Mid1_weight=29/230
Mid2_weight=28/230
#use weights to calculate average
final_score=(assignment_percentage*assignment_weight)+(internal_percentage*internal_weight)+(external_percentage*external_weight)+(attendance_percentage*attendance_weight)+(records_percentage*records_weight)+(mid1_percentage*Mid1_weight)+(mid2_percentage*Mid2_weight)
#convert to cgpa
cgpa=final_score/10
#display marks of student
print(f"\nHello {person}")
print(f"your predicted final marks:{final_score:2f} out of 100")
print(f"your cgpa:{cgpa:2f} (out of 10)")




