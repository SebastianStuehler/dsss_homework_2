import random


def ComputeRandomInteger(min, max):
    """
        Compute a random integer between a minimal and maximal value.

        Parameters
        ----------
        min : int
            The lower boundary for random integer selcetion.
        max : int
            The upper boundary for random integer selection.
        
        Returns
        -------
        int
            The random integer between the lower and the upper boundary.
    """

    # This method will return a random integer value between the given 
    # mininmal (min) and maximal (ma) value.
    return random.randint(min, max)


def ChooseRandomOperation():
    """
        Randomly choose between an addition (+), subtraction (-), and 
        multiplication (*).

        Returns
        -------
        str
            The choosen operator.
    """

    # This method will randomly choose between the three mathematical 
    # operations addition(+), subtraction(-), and multiplication(*) and
    # return the selected operation.
    return random.choice(['+', '-', '*'])


def PerformComputation(FirstNumber, SecondNumber, Operation):
    """
        Provide a string with the Problem and the resulting answer.

        Parameters
        ----------
        FirstNumber : int 
            The first number used for the computation.
        SecondNumber : Int
            The second number used for the computation.
        Operation : str
            The mathematical operation.

        Returns
        -------
        str
            The concatenated string containing the problem of the quiz.
        int
            The computed result of the problem.
    """

    # Build a string out of the two input values and tha mathematical 
    # operation.
    Problem = f"{FirstNumber} {Operation} {SecondNumber}"

    # Safe the computed value based on the given mathematical operation in
    # the varibale Answer.
    if Operation == '+': Answer = FirstNumber + SecondNumber
    elif Operation == '-': Answer = FirstNumber - SecondNumber
    else: Answer = FirstNumber * SecondNumber
    # Return the concatenated problem string and the result of the problem.
    return Problem, Answer

def RunMathQuiz():
    """
        Perform all necessary steps and function calls to run the math quiz.
    """

    # Initialize the Score at the beginning of the game and the maximal
    # amount of games.
    Score = 0
    AmountOfGames = 3

    # Provide some output to the user, that explains the game.
    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the "
        "correct answers.")

    # Run and rerun the game until the maximal amount of games is reached.
    for NumGames in range(AmountOfGames):
        # Compute two randon integer values and store it for later use. 
        FirstNumber = ComputeRandomInteger(1, 10)
        SecondNumber = ComputeRandomInteger(1, 5)
        # Randomly choose the mathematical operator.
        Operation = ChooseRandomOperation()

        # Compute the result of the problem and safe the problem and the answer
        # of the problem.
        PROBLEM, ANSWER = PerformComputation(FirstNumber, SecondNumber, Operation)
        # Provide the user the chosen problem by printing it.
        print(f"\nQuestion: {PROBLEM}")
        # Inform the user to insert his answer.
        useranswer = input("Your answer: ")
        try:
            useranswer = int(useranswer)
        except ValueError:
            print("The provided intput is not of type integer.\n"
                  "Please insert an integer value!")

        # Check wehther the users answer matches the computed answer.
        if useranswer == ANSWER:
            # If the answer is correct, inform the user and increase the score.
            print("Correct! You earned a point.")
            Score += 1
        else:
            # If the answer is incorrect, also inform the user.
            print(f"Wrong answer. The correct answer is {ANSWER}.")

    # When the maximal amount of games is reached, inform the user that the
    # game is over.
    print(f"\nGame over! Your score is: {Score}/{AmountOfGames}")

if __name__ == "__main__":
    # Run the main program, which starts the math quiz.
    RunMathQuiz()
