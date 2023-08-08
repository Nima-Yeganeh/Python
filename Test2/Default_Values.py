def display_course(course_topic='Online Course', course_name='Unknown', course_hours = 0):
    """Display information about course"""
    print(f"\nCourse Topic : {course_topic}")
    print(f"Course Name  : {course_name}")
    print(f"Course Hours : {course_hours} Hours")

display_course(course_hours=5,course_topic="Python",course_name="Mastering Python")
display_course("R Programming", "R Programming Masterclass by Nima",10)
display_course("Java Course")
