# Import the grade_calculator module
import grade_calculator

# Sample dataset of student scores
student_scores = [85, 92, 78, 95, 88, 75, 98, 60]

# Calculate the mean score
mean_score = grade_calculator.calculate_mean(student_scores)

# Calculate the median score
median_score = grade_calculator.calculate_median(student_scores)

# Display the input student scores
print("Student Scores:")
for i, score in enumerate(student_scores, 1):
    print(f"Student {i}: Score {score}")

# Display the calculated mean and median scores
print(f"Mean Score: {mean_score:.2f}")
print(f"Median Score: {median_score:.2f}")
