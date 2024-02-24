subject_marks=int(input("enter your marks: "))
grading_scale={"gradeA":range(80,90),"gradeA+":range(90,100),"gradeB":range(70,80),"gradeC":range(60,70),"gradeD":range(1,59)}
for key, value in grading_scale.items():
    if subject_marks in  value:
        print(key)
    
