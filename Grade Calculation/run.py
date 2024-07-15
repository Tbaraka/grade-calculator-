Ndef run ():
    while True:
        user_input = input("Enter marks (or type 'exit' to quit): ")
        if user_input.lower() == 'exit':
            print("Exiting the program.")
            break
        
        try:
            marks = float(user_input)
            if 0 <= marks <= 100:
                grade = get_grade(marks)
                print(f"Marks: {marks}, Grade: {grade}")
            else:
                print("Please enter marks between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a number or 'exit' to quit.")

if __name__ == "__main__":
    run()
