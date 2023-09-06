#High Score
#Takes a list of scores from the user and outputs the highest among them
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)

max = student_scores[0]
for score in range(1,len(student_scores)):
    if max < student_scores[score]:
        max = student_scores[score]
print(f"The highest score in the class is: {max}")

