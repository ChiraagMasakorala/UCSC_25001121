def main():
    while True:
        # Input student name
        name = input("Enter student name (or type 'Exit' to quit): ")
        
        if name.lower() == "exit":
            break

        # Input marks for 3 subjects
        try:
            subject1 = float(input("Enter marks for Subject 1: "))
            subject2 = float(input("Enter marks for Subject 2: "))
            subject3 = float(input("Enter marks for Subject 3: "))
        except ValueError:
            print("Error: Please enter valid numeric marks.")
            continue

        # Calculate average
        average = (subject1 + subject2 + subject3) / 3

        # Grading logic
        if average >= 75:
            grade = "A"
        elif average >= 60:
            grade = "B"
        elif average >= 40:
            grade = "C"
        else:
            grade = "Fail"

        # Display results in clean format
        print("\n------------------------------")
        print(f"Name   : {name}")
        print(f"Average: {average:.1f}")
        if grade == "Fail":
            print(f"Status : {grade}")
        else:
            print(f"Grade  : {grade}")
        print("------------------------------\n")

if __name__ == "__main__":
    main()


