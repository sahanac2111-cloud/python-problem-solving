student = {
    "name": "Sanah",
    "age": 22,
    "skills": ["Python", "HTML", "CSS"]
}
print(student["name"])
student["course"]="Msc.datascience"
student["age"]=19
for keys,values in student.items():
    print(keys,":",values)
for skills in student["skills"]:
    print("Skills:",skills)
