course_A = {"alice", "bob", "charlie", "david"}
course_B = {"charlie", "eve", "david", "frank"}

# Students in both courses
both_course = course_A & course_B
print("Students in both courses:", both_course)

# Students only in Course A
course_A_only = course_A - both_course
print("Students only in Course A:", course_A_only)

# Students in either Course A or B but not both
either_a_b = course_A ^ course_B
print("Students in either Course A or B but not both:", either_a_b)
