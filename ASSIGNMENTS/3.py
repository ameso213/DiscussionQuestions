# Using loop of your choice, WITI  has tasked you to automate a simple grading system. 
# As a python student, write a program using functions and conditions to display the grades that 
# the students will be receiving. 




def get_grade(score):
    """Return the grade based on the score."""
    if 90 <= score <= 100:
        return 'A'
    elif 80 <= score < 90:
        return 'B'
    elif 70 <= score < 80:
        return 'C'
    elif 60 <= score < 70:
        return 'D'
    elif 50 <= score < 60:
        return 'E'
    else:
        return 'Fail'

def main():
    # List of student scores
    scores = [95, 82, 74, 61, 55, 48, 90]

    # Display the grades for each score
    print("Student Grades:")
    for score in scores:
        grade = get_grade(score)
        print(f"Score: {score}, Grade: {grade}")

if __name__ == "__main__":
    main()
