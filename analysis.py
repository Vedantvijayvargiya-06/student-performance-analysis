import pandas as pd
import matplotlib.pyplot as plt

# Sample Data
data = {
    "Name": ["A", "B", "C", "D", "E"],
    "StudyHours": [2, 5, 3, 6, 4],
    "Marks": [50, 80, 60, 90, 70]
}

# Create DataFrame
df = pd.DataFrame(data)

print("Dataset:")
print(df)

# Average Marks
avg_marks = df["Marks"].mean()
print("\nAverage Marks:", avg_marks)

# Plot Graph
plt.bar(df["Name"], df["Marks"])
plt.xlabel("Students")
plt.ylabel("Marks")
plt.title("Student Performance")
plt.show()

# Highest scorer
topper = df.loc[df["Marks"].idxmax()]
print("\nTopper:", topper["Name"])

# Study hours vs marks
plt.scatter(df["StudyHours"], df["Marks"])
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.title("Study Hours vs Marks")
plt.show()