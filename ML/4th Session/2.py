marks = {
    "Math" : 90,
    "Chemistry" : 87,
    "Physics" : 95, 
    "Biology" : 79
}

max_key = max(marks, key=marks.get)
print(max_key)