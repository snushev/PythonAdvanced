def students_credits(*args):
    courses = {}
    for current_course in args:
        course, course_credits, max_points, student_points = current_course.split('-')
        course_credits, max_points, student_points = int(course_credits), int(max_points), int(student_points)
        current_credits = course_credits * student_points / max_points
        courses[course] = current_credits

    result = []

    total_points = sum(courses.values())
    if total_points >= 240:
        result.append(f"Diyan gets a diploma with {total_points:.1f} credits.")
    else:
        result.append(f"Diyan needs {240 - total_points:.1f} credits more for a diploma.")

    sorted_courses = sorted(courses.items(), key=lambda x: -x[1])
    for course, points in sorted_courses:
        result.append(f"{course} - {points:.1f}")
    return '\n'.join(result)


print(
    students_credits(
        "Discrete Maths-40-500-450",
        "AI Development-20-400-400",
        "Algorithms Advanced-50-700-630",
        "Python Development-15-200-200",
        "JavaScript Development-12-500-480",
        "C++ Development-30-500-405",
        "Game Engine Development-70-100-70",
        "Mobile Development-25-250-225",
        "QA-20-300-300",
    )
)
