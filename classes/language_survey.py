from survey import AnonymousSurvey

# Define a question and make a survey
question = "What language did you first learn to speak"
my_survey = AnonymousSurvey(question)

my_survey.show_question()
print("Enter q to quit.")

while True:
    response = input("Language: ")
    if response == 'q':
        break
    my_survey.store_response(response)

#Show the survey results
print("\n Thank you to everyone for participating in the result")
my_survey.show_results()
