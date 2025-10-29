# Import required libraries
import pandas as pd
import matplotlib.pyplot as plt

# Sample dataset
data = {
    'Name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
    'Score': [12.5, 9, 16.5, 15, 9, 20, 14.5, 13, 8, 19],
    'Attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
    'Age': [20, 21, 19, 18, 22, 20, 19, 23, 21, 20]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Display the data
print("Dataset:\n", df)

# 1️⃣ Line Plot - Score vs Name
plt.figure(figsize=(8,5))
plt.plot(df['Name'], df['Score'], marker='o', color='blue')
plt.title('Line Plot: Score of Each Student')
plt.xlabel('Name')
plt.ylabel('Score')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

# 2️⃣ Bar Plot - Attempts vs Name
plt.figure(figsize=(8,5))
plt.bar(df['Name'], df['Attempts'], color='green')
plt.title('Bar Plot: Number of Attempts per Student')
plt.xlabel('Name')
plt.ylabel('Attempts')
plt.xticks(rotation=45)
plt.show()

# 3️⃣ Histogram - Distribution of Scores
plt.figure(figsize=(6,4))
plt.hist(df['Score'], bins=5, color='orange', edgecolor='black')
plt.title('Histogram: Distribution of Scores')
plt.xlabel('Score')
plt.ylabel('Frequency')
plt.show()

# 4️⃣ Scatter Plot - Age vs Score
plt.figure(figsize=(6,4))
plt.scatter(df['Age'], df['Score'], color='red')
plt.title('Scatter Plot: Age vs Score')
plt.xlabel('Age')
plt.ylabel('Score')
plt.grid(True)
plt.show()

# 5️⃣ Box Plot - Spread of Scores
plt.figure(figsize=(4,5))
plt.boxplot(df['Score'])
plt.title('Box Plot: Score Distribution')
plt.ylabel('Score')
plt.show()
