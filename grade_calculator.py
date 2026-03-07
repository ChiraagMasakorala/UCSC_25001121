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

    # Pass/Fail logic
    if average >= 40:
        print("Status: Pass")
    else:
        print("Status: Fail")

if __name__ == "__main__":
    main()

