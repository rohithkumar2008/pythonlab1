def marks():
    English = int(input("Enter your English marks: "))
    Tamil = int(input("Enter your Tamil marks: "))
    Maths = int(input("Enter your Maths marks: "))
    Science = int(input("Enter your Science marks: "))
    Social = int(input("Enter your Social marks: "))
    return English + Tamil + Maths + Science + Social

def Average(tot):
    return tot / 5

def percentage(tot):
    return (tot / 500) * 100

def Grade(percent):
    if percent >= 80:
        return 'A'
    elif percent >= 70:
        return 'B'
    elif percent >= 60:
        return 'C'
    elif percent >= 40:
        return 'D'
    else:
        return 'E'

def main():
    Student_DB = {}
    print("Spectra School Database")
    stud_db = int(input("Enter the total number of student entries: "))

    for x in range(stud_db):
        studentrollno = int(input("\nEnter Roll Number: "))
        studentName = input("Enter Student Name: ")
        print("Enter marks for five subjects:")
        
        Total = marks()
        Avg = Average(Total)
        percent = percentage(Total)
        grade = Grade(percent)

        print("\n--- Student Report ---")
        print("Roll Number:", studentrollno)
        print("Name:", studentName)
        print("Total Marks:", Total)
        print("Average:", Avg)
        print("Percentage:", percent)
        print("Grade:", grade)

        Student_DB[studentrollno] = {
            "StudentName": studentName,
            "StudentRollNo": studentrollno,
            "TotalMarks": Total,
            "Average": Avg,
            "Percentage": percent,
            "Grade": grade
        }

    print("\n--- Final Student Database ---")
    print(Student_DB)

main()
