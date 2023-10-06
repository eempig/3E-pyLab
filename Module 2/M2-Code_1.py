# Variables and Data Structures for Practical Applications


#Example 1: Using Lists for Student Records
# Creating a list of student records
# student_records = [
#     {"name": "Alice", "age": 18, "grade": 90},
#     {"name": "Bob", "age": 17, "grade": 85},
#     {"name": "Charlie", "age": 18, "grade": 88},
# ]

# # Adding a new student record
# new_student = {"name": "David", "age": 17, "grade": 92}
# student_records.append(new_student)

# # Updating a student's grade
# student_records[1]["grade"] = 87

# # Retrieving a student's information
# alice_info = student_records[0]
# print()
# print()
# print(f"Name: {alice_info['name']}, Age: {alice_info['age']}, Grade: {alice_info['grade']}")
# print()




# Example 2: Exploring Dictionary for Data Analysis

# Creating a dictionary of exam scores

# from statistics import mean, median, mode

# # Creating a dictionary of exam scores
# exam_scores = {
#     "Math": 90,
#     "Science": 88,
#     "History": 85,
#     "English": 92,
# }

# # Calculating the average score
# total_score = sum(exam_scores.values())
# average_score = total_score / len(exam_scores)
# print(f"Average Score: {average_score:.2f}")

# # Calculating the median score
# scores_list = list(exam_scores.values())
# sorted_scores = sorted(scores_list)
# median_score = median(sorted_scores)
# print(f"Median Score: {median_score:.2f}")

# # Calculating the mode score
# try:
#     mode_score = mode(scores_list)
#     print(f"Mode Score: {mode_score:.2f}")
# except StatisticsError:
#     print("No unique mode found.")





# Example 2.3: Using Tuples for Immutable Data

# Creating a tuple for student's personal information
# student_info = ("Alice", 18, "123 Main St")

# # Accessing elements of the tuple
# name, age, address = student_info

# # Displaying the student's information
# print("Student Information:")
# print(f"Name: {name}")
# print(f"Age: {age}")
# print(f"Address: {address}")

# # Attempting to update a tuple element (will result in an error)
# try:
#     student_info[1] = 19  # This will raise a TypeError
# except TypeError:
#     print("Tuples are immutable, so updating an element is not allowed.")






# 2. 2. Conditional Statements (if, elif, else) in Transdisciplinary Contexts
# Example 1: Grading Students (Education Context)

# Get the student's score
# score = int(input("Enter the student's score: "))

# # Determine the grade based on the score using conditional statements
# if 99 <= score <= 100:
#     grade = '1.00'
# elif 96 <= score < 99:
#     grade = '1.25'
# elif 93 <= score < 96:
#     grade = '1.50'
# elif 90 <= score < 93:
#     grade = '1.25'
# elif 87 <= score < 90:
#     grade = '2.00'
# elif 84 <= score < 87:
#     grade = '2.25'
# elif 81 <= score < 84:
#     grade = '2.50'
# elif 78 <= score < 81:
#     grade = '2.75'
# elif 75 <= score < 78:
#     grade = '3.00'
# elif 51 <= score < 75:
#     grade = 'INC'
# elif 0 <= score < 51:
#     grade = '5.00'
# else:
#     grade = 'Invalid Score'

# # Provide feedback to the student based on the grade using conditional statements
# if grade == '1.00':
#     feedback = 'Excellent!'
# elif grade == '1.25':
#     feedback = 'Excellent!'
# elif grade == '1.50':
#     feedback = 'Very Good!'
# elif grade == '2.00':
#     feedback = 'Good!'
# elif grade == '2.25':
#     feedback = 'Good!'
# elif grade == '2.50':
#     feedback = 'Satisfactory.'
# elif grade == '2.75':
#     feedback = 'Satisfactory.'
# elif grade == '3.00':
#     feedback = 'Passed.'
# elif grade == 'INC':
#     feedback = 'Incomplete.'
# elif grade == '5.00':
#     feedback = 'Failed.'
# else:
#     feedback = 'Invalid Score'

# # Display the calculated grade and feedback
# print(f"Grade: {grade}")
# print(f"Feedback: {feedback}")




#Example 2: Data Filtering (Data Science Context)
# Sample dataset of student scores

# student_scores = [85, 92, 78, 95, 88, 75, 98, 60]

# # Define a threshold for exceptional students
# threshold = 90

# # Display exceptional students with correct numbering
# print("Exceptional Students:")
# for i, score in enumerate(student_scores, 1):
#     if score >= threshold:
#         print(f"Student {i}: Score {score}")




# 3. Loops (for and while) with Examples from Various Fields

# Example 1: Counting Votes (Political Science Context)
# In a political science context, you can create a program that counts votes in an election using a for loop.


# Sample list of votes
# votes = ["Candidate A", "Candidate B", "Candidate A", "Candidate C", "Candidate A", "Candidate B"]

# # Initialize counters for each candidate
# candidate_a_votes = 0
# candidate_b_votes = 0
# candidate_c_votes = 0

# # Count the votes using a for loop
# for vote in votes:
#     if vote == "Candidate A":
#         candidate_a_votes += 1
#     elif vote == "Candidate B":
#         candidate_b_votes += 1
#     elif vote == "Candidate C":
#         candidate_c_votes += 1

# # Display the election results
# print("Election Results:")
# print(f"Candidate A: {candidate_a_votes} votes")
# print(f"Candidate B: {candidate_b_votes} votes")
# print(f"Candidate C: {candidate_c_votes} votes")




# Example 2: Calculating Interest (Finance Context)
# In a finance context, you can use a while loop to calculate compound interest over time.

# Initial investment amount
# principal = 1000

# # Annual interest rate (as a decimal)
# annual_rate = 0.05

# # Number of years to calculate interest
# years = 5

# # Calculate compound interest using a while loop
# year = 1
# while year <= years:
#     principal *= (1 + annual_rate)
#     year += 1

# # Display the final amount
# print(f"Final amount after {years} years: ${principal:.2f}")



