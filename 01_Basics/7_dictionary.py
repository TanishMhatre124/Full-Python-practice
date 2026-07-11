#dictionary
programming__dictionary={
    "bug":"an error in program",
    "123":"numbars",
    "loop":"doing something again and again" 
}

print(programming__dictionary["bug" ])

programming__dictionary["loop"]="doing something again and again" 
print(programming__dictionary)


empty_dictonary={}

#wipe existing dictionary
programming__dictionary={}
print(programming__dictionary)

#edit in dictionary
programming__dictionary["loop"]="its a looop" 
print(programming__dictionary)

#loop through programming

for key in programming__dictionary:
    print(key)
    print(programming__dictionary[key])

#-------------------------------------------------------------------------------------------------------------
#example problem 

student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62
}

student_grades = {}

for student, score in student_scores.items():
    if score >= 91:
        student_grades[student] = "Outstanding"
    elif score >= 81:
        student_grades[student] = "Exceeds Expectations"
    elif score >= 71:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"

print(student_grades)
#----------------------------------------------------------------------------------------------------------

#nesting list and dictionary 
capitals={
    "france":"paris",
    "germany":"berlin"   
}

travel_log={
    "france":["paris","lille","dijon"],
    "germany":["berlin"]
}
print(travel_log["france"])


#nested 
nested_list=["a","b",["c","d"]] 
print(nested_list[2])