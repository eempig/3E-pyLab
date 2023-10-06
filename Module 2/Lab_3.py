import pandas as pd
import matplotlib.pyplot as plt

# Attempt to load the dataset
try:
    df = pd.read_csv('student_scores.csv')

    # Display the first few rows of the dataset
    print(df.head())

    # Calculate summary statistics
    mean_score = df['Score'].mean()
    median_score = df['Score'].median()
    std_deviation = df['Score'].std()

    print(f"Mean Score: {mean_score:.2f}")
    print(f"Median Score: {median_score:.2f}")
    print(f"Standard Deviation: {std_deviation:.2f}")

    # Create a histogram of the scores
    plt.hist(df['Score'], bins=10, edgecolor='k')
    plt.xlabel('Score')
    plt.ylabel('Frequency')
    plt.title('Distribution of Exam Scores')
    plt.show()

    threshold = 85
    above_threshold = df[df['Score'] > threshold]

    print("Students scoring above the threshold:")
    print(above_threshold)

except FileNotFoundError:
    print("Error: File 'student_scores.csv' not found.")
except KeyError:
    print("Error: 'Score' column not found in the dataset.")
except Exception as e:
    print(f"An error occurred: {e}")
