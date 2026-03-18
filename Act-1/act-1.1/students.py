class Student:

    def __init__(self, student_id, first_name, last_name, course, birth_date, phone_number, address):
        self.student_number = student_id
        self.first_name = first_name
        self.last_name = last_name
        self.course = course
        self.birth_date = birth_date
        self.phone_number = phone_number
        self.address = address

    def __str__(self):
        return f"{self.student_number} - {self.last_name}, {self.first_name} ({self.course})"

    @classmethod
    def read_student_file(cls, filename):
        students = []
        try:
            with open(filename, "r") as file:
                for line in file:
                    data = line.strip().split(",")

                    if len(data) == 7:
                        student = cls(*data)
                        students.append(student)

            print(f"\n\tLoaded file: {filename}")

        except FileNotFoundError:
            print("\n\tERROR: File not found!")

        return students

    @classmethod
    def save_student_file(cls, filename, students):
        try:
            with open(filename, "w") as file:
                for s in students:
                    file.write(
                        f"{s.student_number},{s.first_name},{s.last_name},{s.course},{s.birth_date},{s.phone_number},{s.address}\n"
                    )

            print("\n\tStudent data saved successfully!")

        except Exception as e:
            print("\n\tError saving file:", e)

    @classmethod
    def generate_report(cls, students, output_file="student_report.txt"):

        course_stats = {}

        for s in students:
            course_stats[s.course] = course_stats.get(s.course, 0) + 1

        total_students = len(students)

        try:
            with open(output_file, "w") as file:

                file.write("STUDENT REPORT\n")
                file.write("====================\n\n")

                file.write("Students per Course\n")

                for course, count in course_stats.items():
                    file.write(f"{course}: {count}\n")

                file.write("\n")
                file.write(f"Total Students: {total_students}\n")

            print(f"\n\tReport successfully written to '{output_file}'")

        except Exception as e:
            print("\n\tError writing report:", e)

    @classmethod
    def add_student(cls, students):

        print("\n\tAdd New Student")

        student_id = input("Student ID: ")
        first_name = input("First Name: ")
        last_name = input("Last Name: ")
        course = input("Course: ")
        birth_date = input("Birth Date (YYYY-MM-DD): ")
        phone_number = input("Phone Number: ")
        address = input("Address: ")

        new_student = cls(
            student_id,
            first_name,
            last_name,
            course,
            birth_date,
            phone_number,
            address
        )

        students.append(new_student)

        print(f"\n\tStudent {first_name} {last_name} added successfully!")

    @classmethod
    def remove_student(cls, students):

        student_no = input("\n\tEnter Student ID to remove: ")

        for student in students:
            if student.student_number == student_no:
                students.remove(student)
                print(f"\n\tStudent {student.first_name} {student.last_name} removed.")
                return

        print("\n\tStudent not found.")

    @classmethod
    def count_by_course(cls, students):

        course_stats = {}

        for s in students:
            course_stats[s.course] = course_stats.get(s.course, 0) + 1

        print("\n\tStudents per Course")

        for course, count in course_stats.items():
            print(f"\t{course}: {count}")

    @classmethod
    def count_all_students(cls, students):

        total = len(students)

        print(f"\n\tTotal Students: {total}")


def print_students(students):

    print("\n\tStudent List\n")

    if not students:
        print("\tNo students found.")
        return

    for student in students:
        print(f"\t{student}")


def main():

    print("\n\n\tWelcome To Student Data Handling Program\n")

    filename = input("\tEnter student file path: ")

    students = Student.read_student_file(filename)

    while True:

        print("\n")
        print("\tA. View Students")
        print("\tB. Perform Basic Queries")
        print("\tC. Load Another File")
        print("\tQ. Exit Program")

        choice = input("\n\tEnter choice: ").upper()

        if choice == "A":

            print_students(students)

        elif choice == "B":

            while True:

                print("\n\tBasic Queries")
                print("\t1. Add Student")
                print("\t2. Remove Student")
                print("\t3. Count Students by Course")
                print("\t4. Count All Students")
                print("\tB. Back to Main Menu")

                query = input("\n\tEnter choice: ")

                if query == "1":
                    Student.add_student(students)

                elif query == "2":
                    Student.remove_student(students)

                elif query == "3":
                    Student.count_by_course(students)

                elif query == "4":
                    Student.count_all_students(students)

                elif query.upper() == "B":
                    break

                else:
                    print("\n\tInvalid choice.")

        elif choice == "C":

            filename = input("\n\tEnter new file path: ")
            students = Student.read_student_file(filename)

        elif choice == "Q":

            print("\n\tSaving data...")

            Student.save_student_file(filename, students)

            Student.generate_report(students)

            print("\tExiting Program.")
            break

        else:
            print("\n\tInvalid choice.")


if __name__ == "__main__":
    main()