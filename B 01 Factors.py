# Generates headings
def statement_generator(statement, decoration):
    print(f"\n{decoration * 5} {statement} {decoration * 5}")


# Displays instructions
def instructions():
    statement_generator(statement="Instructions", decoration="-")

    print('''Enter a number between 1~200''')


# enter a number that is more than zero
def num_check(question):
    error = "Please enter a number that is between 1 and 200 inclusive\n"
    while True:

        response = input(question).lower()
        if response == "xxx":
            return response

        try:
            # ask the user for a number
            response = int(response)

            # check that the number is more than zero
            if 1 <= response <= 200:
                return response
            else:
                print(error)

        except ValueError:
            print(error)


# Main routine goes here
statement_generator(statement="The Ultimate Factor Finder", decoration="-")

# Display instructions if requested
want_instructions = input("\nPress <enter> to read the instructions "
                          "or any key to continue")

if want_instructions == "":
    instructions()

while True:
    factors_list = []  # initialize the list at the start of each loop

    to_factor = num_check("To factor: ")
    print("You chose to factor", to_factor)

    if to_factor == "xxx":
        break

    if to_factor == 1:
        print("ONE is UNITY")
    else:
        # factorize it!
        stop = to_factor

        for item in range(1, stop + 1):  # include stop in the range
            if to_factor % item == 0:
                # if we have a factor, find the second number in the pair
                partner = to_factor // item

                # append factors to list
                factors_list.append(item)
                factors_list.append(partner)

            # sort the factors and remove duplicates
        factors_list = sorted(set(factors_list))
        print(f"Factors of {to_factor}: {factors_list}")

    # Do not return inside the loop
print("Goodbye!")
