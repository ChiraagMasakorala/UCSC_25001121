def main():
    # Input student name
    name = input("Enter student name: ")

    # Input marks for 3 subjects
    try:
        subject1 = float(input("Enter marks for Subject 1: "))
        subject2 = float(input("Enter marks for Subject 2: "))
        subject3 = float(input("Enter marks for Subject 3: "))
    except ValueError:
        print("Error: Please enter valid numeric marks.")
        return

    # Calculate average
    average = (subject1 + subject2 + subject3) / 3

    # Display results
    print(f"\nStudent Name: {name}")
    print(f"Average Marks: {average:.2f}")

    # Grading logic
    if average >= 75:
        print("Grade: A")
    elif average >= 60:
        print("Grade: B")
    elif average >= 40:
        print("Grade: C")
    else:
        print("Status: Fail")

if __name__ == "__main__":
    main()

