# 1. create file called hello.txt and write "this is my first handling exercise"
# 2. append another line

# blocks work like functions, you have different functions for different actions to keep it simple and clean
# works the same with blocks, allows you to do a certain action whenever its needed
#with open('hello.txt','w+') as file:
    #file.write("This is my first file handling exercise!")

#with open('hello.txt','a+') as file:
    #file.write("\nThis is another line")

    #file.seek(0)
    #contents = file.read()
    #print(contents)


# Made a mini "function" visual with trial and error to implement real examples of how I would write these blocks

#def student_list():                                return needed --> function that produces data
    #students = {
        #"John": "Pass",
        #"Richard": "Fail"}
    #return students

#def storing_grades(students):                      function that doesn't return data (stores results) --> no need for "return"
    #with open('students-grade.txt','w+') as file:
        #for student, grade in students.items():
            #file.write(f"{student}:{grade}\n" ) 
        
#def show_grade():                                  function that doesn't return data (prints results) --> no need for "return"
    #with open('students-grade.txt','r') as file:
        #contents = file.read()
        #print(f"Students results:")
        #print(contents)

#def run_program():
    #students = student_list()
    #storing_grades(students)
    #show_grade()
#run_program()