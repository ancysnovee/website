
def website(user_role, selected_courses=None, new_course=None):
    courses = ["maths", "kannada", "english", "social", "science"]
    student_course = selected_courses if selected_courses else []

    if user_role == 1: 
        if selected_courses is None:
            selected_courses = [] 
        if not selected_courses:  
            student_course.append("maths")  
        return f"you have enrolled successfully in the following course:\n{student_course}"

    if user_role == 2:  
        if new_course:
            courses.append(new_course)
        return f"the course has been added successfully: {courses}"

    if user_role == 3:  
        return "Admin function is not implemented yet."

    return "Invalid role"
