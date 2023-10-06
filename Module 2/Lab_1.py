# Prompt the user to enter the number of students
num_students = int(input("Enter the number of students: "))
student_data = []

# Collect data for each student
for i in range(num_students):
    name = input(f"Enter the name of student {i + 1}: ")
    scores = []

    # Collect three scores per student
    for j in range(3):
        score = float(input(f"Enter score {j + 1} for {name}: "))
        scores.append(score)

    # Store the student's name and scores as a tuple and append it to student_data
    student_data.append((name, scores))

# Define the threshold for exceptional students
threshold = 90
exceptional_students = []

# Calculate individual average scores and identify exceptional students
for name, scores in student_data:
    avg_score = sum(scores) / len(scores)

    # Check if the student's average score is above or equal to the threshold
    if avg_score >= threshold:
        exceptional_students.append(name)

# Display the results
for name, scores in student_data:
    avg_score = sum(scores) / len(scores)

    # Print student name, scores, and average score
    print(f"Student: {name}")
    print(f"Scores: {', '.join(map(str, scores))}")  # Convert scores to strings and join them with a comma
    print(f"Average Score: {avg_score}\n")  # Print the average score

# Print the names of exceptional students
print("Exceptional Students:")
for name in exceptional_students:
    print(name)
