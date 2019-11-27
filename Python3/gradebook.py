# Use of append and zip for lists

last_semester_gradebook = [("politics", 80), ("latin", 96), ("dance", 97), ("architecture", 65)]
subjects = ["physics", "calculus", "poetry", "history"]
grades = [98, 97, 85, 88]

subjects.append("computer science")
grades.append(100)

gradebook = zip(subjects, grades)
gradebook = list(gradebook)
gradebook.append(("visual arts", 93))

full_gradebook = zip(last_semester_gradebook , gradebook )

print(list(gradebook))

print(list(full_gradebook))
