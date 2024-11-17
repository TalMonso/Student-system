import pandas as pd 
import matplotlib.pyplot as plt 
import numpy as np 




def courses_table():
    cnumber = int(input("How many courses do you have at this Semester (Maximum 7)"))
    if cnumber > 7:
        print("The maximum number of courses is 7, setting number of courses to 7")
        cnumber = 7
    courses_list = []
    lessons = np.zeros((cnumber, 7))
    
    for index in range(cnumber):
        course_name = input("Enter your course name")
        courses_list.append(course_name)
        print("Enter the number of lesson hours per day (counting start from Sunday)")
        for i in range(7):
            lessons[index, i] = int(input(f"Number of lesson hours on day {i+1}: "))
            
    df = pd.DataFrame(lessons, index= courses_list, columns= ['Sunday','monday','Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'])
    print(df)
    
    
def grades_graph():
    courses = {}
    while True:
        course_name = input("Enter course name or 'finish' to stop: ")
        if course_name.lower() == 'finish':
            break
        
        grade = input("Enter the grade of this course: ")
        try:
            grade = float(grade)
        except ValueError:
            print("Please enter valid grade")
            continue
        courses[course_name] = grade
        
    average = sum(courses.values()) / len(courses)
    df = pd.DataFrame(list(courses.items()), columns=['Courses', 'Grade'])
    plt.figure(figsize=(10,5))
    plt.bar(df['Courses'], df['Grade'], color='Green')
    plt.style.use('dark_background')
    plt.xlabel('Courses')
    plt.ylabel('Grade')
    plt.title(f"Grades graph - average: {average}")
    plt.tight_layout()
    plt.show()
    
        


print("Welcome to Student Data base System")
print("Choose option by number:")
print("1.Courses table")
print("2.Grades graph")
choice = int(input("What is your choice ?"))
if choice == 1:
    courses_table() 
elif choice == 2:
    grades_graph()
else:
    print("You have choose 1 or 2 only.")
     
                
            

        
    
