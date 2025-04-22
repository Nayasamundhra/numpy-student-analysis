# NumPy Project: Analyzing Student Exam Scores
import numpy as np

# Each row represents a student: [Math, English, Science]
scores = np.array([
    [85, 78, 92],
    [76, 88, 85],
    [90, 70, 78],
    [65, 80, 75],
    [95, 89, 91],
    [72, 68, 80],
    [88, 76, 84],
    [79, 82, 90],
    [81, 74, 77],
    [93, 91, 95],
    [68, 72, 70],
    [77, 79, 82],
    [86, 85, 88],
    [69, 73, 76],
    [84, 80, 83],
    [91, 87, 89],
    [74, 69, 73],
    [67, 75, 71],
    [89, 92, 94],
    [70, 65, 68]
])

#Average Score in each subject
m,e,s=np.mean(scores,axis=0)
print("--Average Scores--")
print("Math: ",m)
print("English: ",e)
print("Science: ",s)
print()

#Student with highest total score
high=np.max(np.sum(scores,axis=1))
print("Student with Highest Total Score:",high)
print()

#Variance in Science
c=np.var(scores[:,2])
print(f"Variance in Science: {c:.2f}")
print()

#Median in English
b=np.median(scores[:,1])
print("Median in English: ",b)
print()

#What is the total score for each student across all subjects?
total=np.sum(scores,axis=1)
print("Total Scores: ",total)
print()

#What is the standard deviation in Math, English, and Science scores?
x,y,z=np.std(scores,axis=0)
print("--Standard Deviation--")
print(f"Math: {x:.2f}")
print(f"English: {y:.2f}")
print(f"Science: {z:.2f}")
print()

#Which student has the lowest total score?
print("Student with lowest total score: ",np.argmin(np.sum(scores,axis=1)))
print()

#How many students scored more than 90 in Science?
val=scores[:,2]>90
print("Total Students who scored greater than 90 in Science: ",np.sum(val))
print()

#How many students passed in all three subjects (assuming the pass mark is 40)?
passed=np.sum(np.all(scores>=40,axis=1))
print("number of students passed in all 3 subjects: ",passed)
print()

#Who are the top 3 students based on total scores?
total_scores=np.sum(scores,axis=1)
sort_scores=np.argsort(total_scores)
p=sort_scores[::-1][:3]
print("Top 3 performers are: ",p)
print("--Total Scores--")
print(p[0],"=",total_scores[p[0]])
print(p[1],"=",total_scores[p[1]])
print(p[2],"=",total_scores[p[2]])

