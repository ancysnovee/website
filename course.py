def website():
    courses = ["maths","kannada","english","social","science"]
    student_course=[]
    user = int(input("enter your role: \npress 1 if student \npress 2 if instructor \npress 3 if admin \n"))
    if user==1:
        print("the available courses are: ")
        for i in courses:
            print(i)
        print("press 1 if entered all your course")
        course=2
        while course != "1":
            course= input("enter your course: ")
            if course in courses:
                student_course.append(course)
            else:
                print("invalid input")
        return f"you have enrolled successfully in the following course:\n{student_course}"

    if user == 2:
        new_course = input("enter the course name")
        courses.append(new_course)
        return f"the course have been added successfully: {courses}"
    


if __name__=="__main__":
    print(website())
