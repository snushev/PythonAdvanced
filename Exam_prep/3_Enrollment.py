def gather_credits(total, *args):
    courses = set()
    points = 0

    for course, current_points in args:

        if points >= total:
            break
        if course not in courses and current_points > 0:
            courses.add(course)
            points += current_points



    sorted_courses = sorted(courses)
    if points < total:
        return f"You need to enroll in more courses! You have to gather {total - points} credits more."
    else:
        return f"Enrollment finished! Maximum credits: {points}.\nCourses: {', '.join(sorted_courses)}"
