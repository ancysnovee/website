
from course import website

def test_website():
   
    result = website(1, selected_courses=["maths", "english"])
    assert result == "you have enrolled successfully in the following course:\n['maths', 'english']", f"Test failed: {result}"

    
    result = website(2, new_course="history")
    assert result == "the course has been added successfully: ['maths', 'kannada', 'english', 'social', 'science', 'history']", f"Test failed: {result}"




if __name__ == "__main__":
    test_website()
