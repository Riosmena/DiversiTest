# ========================================================
# File: DiversiTest.py
# Author: José Emiliano Riosmena Castañón - A01704245
# Date: Friday, November 22th, 2023
# To run: py DiversiTest.py
# ========================================================

# Libraries needed
import os

# Function to make the test and get the answers
def make_test():
    # List of questions
    questions = [
        "1. ¿Estás de acuerdo con la idea de que todas las personas, independientemente de su raza, deberían\ntener las mismas oportunidades en la vida?",
        "2. ¿Consideras que las diferencias culturales enriquecen la sociedad?",
        "3. ¿Crees que las políticas de inclusión y diversidad son importantes en el entorno laboral?",
        "4. ¿Estás de acuerdo en que es fundamental educarse sobre la historia y las experiencias de diferentes\ngrupos étnicos?",
        "5. ¿Piensas que las bromas o comentarios basados en la raza son inapropiados?",
        "6. ¿Estás de acuerdo en que la discriminación racial es un problema que persiste en la sociedad actual?",
        "7. ¿Crees que las instituciones deberían implementar medidas específicas para abordar la discriminación\nracial?",
        "8. ¿Consideras que las personas deben confrontar sus propios prejuicios para contribuir a la eliminación\ndel racismo?",
        "9. ¿Estás de acuerdo en que la representación diversa en los medios de comunicación es importante para\ncombatir estereotipos?",
        "10. ¿Piensas que la conversación abierta sobre el racismo es esencial para su erradicación en la sociedad?"
    ]

    # List of answers
    answers = [
        "a. Totalmente en desacuerdo",
        "b. En desacuerdo",
        "c. Neutral",
        "d. De acuerdo",
        "e. Totalmente de acuerdo"
    ]

    # Create a list to store the answers
    user_answers = []

    # Loop to ask the questions and get the answers
    for question in questions:

        # Clear the screen
        os.system('cls' if os.name == 'nt' else 'clear')

        # Print the question and the possible answers
        print(question)
        print("")
        for answer in answers:
            print(answer)
        print("")

        # Loop to check if the answer is valid
        while True:

            # Ask for the answer
            selection = input("Introduce tu respuesta: ")

            # Check if the answer is valid
            if selection in ['a', 'b', 'c', 'd', 'e']:
                break
            else:
                print("Respuesta inválida. Inténtalo de nuevo.")
        
        # Add the answer to the list
        user_answers.append(selection)

    # Call the function to analyse the answers
    analyse_answers(user_answers)

# Function to analyse the answers and give a result
def analyse_answers(user_answers):

    # Calculate the score
    score = sum(score_answer(answer) for answer in user_answers)
    
    # Clear the screen
    os.system('cls' if os.name == 'nt' else 'clear')

    # Print the results
    print("Resultados:")
    print("")
    if score >= 45:
        print("Tu puntaje sugiere que hay aspectos críticos en los que podrías mejorar tu comprensión\ny actitud hacia la diversidad racial. Es fundamental reflexionar sobre tus respuestas y comprometerte\nactivamente en la lucha contra el racismo, educándote y promoviendo la inclusión.")
    if score >= 30 and score < 45:
        print("Hay áreas donde tus respuestas indican posibles actitudes que podrían considerarse\nproblemáticas. Reflexiona sobre tus respuestas y considera la posibilidad de explorar más sobre diversidad\ny cómo puedes contribuir a un entorno más inclusivo.")
    if score >= 15 and score < 30:
        print("Has mostrado una actitud relativamente neutral hacia la diversidad. Podrías reflexionar\nsobre algunas áreas donde tu comprensión podría mejorarse. Considera educarte más sobre experiencias y\nperspectivas raciales para fortalecer tu conciencia.")
    if score < 15:
        print("¡Felicidades! Tu puntaje refleja una fuerte conciencia y apertura hacia la diversidad.\nPareces tener una actitud positiva y respetuosa hacia personas de diferentes razas. Continúa fomentando\nla inclusión y la comprensión en tu vida diaria.")

# Function to score the answers
def score_answer(answer):
    if answer == 'a':
        return 5
    elif answer == 'b':
        return 4
    elif answer == 'c':
        return 3
    elif answer == 'd':
        return 2
    else:
        return 1

# Main function
def main():
    # Clear the screen
    os.system('cls' if os.name == 'nt' else 'clear')

    # Print the welcome message
    print("Bienvenido al Test de Reflexión sobre Racismo")
    print("Este test te ayudará a reflexionar sobre tus actitudes hacia la diversidad racial.")
    print("Para cada pregunta, selecciona la respuesta que mejor refleje tu opinión.")
    print("¡Comencemos!")
    print("")
    input("Presiona ENTER para continuar")
    make_test()

main()