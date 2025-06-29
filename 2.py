def load_students(filename):
    students = []
    with open(filename, "r") as file:
        lines = file.readlines()
        for line in lines:
            name, m1, m2, m3 = line.strip().split(",")
            students.append({
                "name": name,
                "marks": [int(m1), int(m2), int(m3)]
            })
    return students

students = load_students("students.txt")
def calculate_grade(average):
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    else:
        return "C"

def view_all_students(student_list):
    print("\n--- All Students ---")
    for student in student_list:
        name = student["name"]
        marks = student["marks"]
        avg = round(sum(marks) / len(marks), 2)
        grade = calculate_grade(avg)
        print(f"{name} → Marks: {marks} | Avg: {avg} | Grade: {grade}")
def show_class_average(student_list):
    total = 0
    count = 0
    for student in student_list:
        total += sum(student["marks"])
        count += len(student["marks"])
    avg = round(total / count, 2)
    print(f"\nClass Average Marks: {avg}")
topper = ("", 0)
def show_topper(student_list):
    topper = ("", 0)  # (name, avg)
    for student in student_list:
        avg = sum(student["marks"]) / len(student["marks"])
        if avg > topper[1]:
            topper = (student["name"], avg)
    print(f"\n🏅 Topper: {topper[0]} with {round(topper[1], 2)} average marks")


while True:
    print("\n===== Student Report Menu =====")
    print("1. View All Students")
    print("2. Show Class Average")
    print("3. Show Topper")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("Showing all students...")
        view_all_students(students)
    elif choice == "2":
        print("Calculating class average...")
        show_class_average(students)
    elif choice == "3":
        print("Finding topper...")
        show_topper(students)
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
