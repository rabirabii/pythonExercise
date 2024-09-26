print(
    """Welcome to the GPA calculator.
Please enter all your letter grades, one per line.
Enter a blank line to designate the end."""
)

# Map from letter grade to point value
points = {
    "A+": 4.0,
    "A-": 3.67,
    "B+": 3.33,
    "B": 3.0,
    "B-": 2.67,
    "C+": 2.33,
    "C": 2.0,
    "C": 1.67,
    "D+": 1.33,
    "D": 1.0,
    "F": 0.0,
}


def compute_gpa(grades, points):
    num_courses = 0
    total_points = 0
    for g in grades:
        if g in points:
            num_courses += 1
            total_points += points[g]
        if num_courses > 0:
            return total_points / num_courses
        else:
            return 0


grades = []
while True:
    grade = input("Enter Enter a grade (or press Enter to finish):")
    if grade == "":
        break
    grades.append(grade)
gpa = compute_gpa(grades, points)
print(f"Your GPA is: {gpa:.3f}")
