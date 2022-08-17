class AnonymousSurvey:
    """Collect anonymous answers to a simple question"""

    def __init__(self, question) -> None:
        """Store a question, prepares to store a response"""
        self.question = question
        self.responses = []

    def show_question(self) -> None:
        """Show the survey question"""
        print(self.question)

    def store_response(self, new_response) -> None:
        """Store a single response to the survey"""
        self.responses.append(new_response)

    def show_results(self) -> None:
        """Show all the responses that have been given"""
        print("Survey results:")
        for response in self.responses:
            print(f"- {response}")

