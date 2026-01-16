import re
import datetime
import pyjokes

def chatbot_response(user_input):
    user_input = user_input.lower().strip()

    if re.search(r"\b(hi|hello|hey)\b", user_input):
        return "Heyy Learner!! \n I am your chatbot buddy \n What’s your command?"


    elif re.search(r"\b(your name|who are you)\b", user_input):
        return "I am a Rule-Based Chatbot built using Python."

    elif re.search(r"\b(time|current time)\b", user_input):
        now = datetime.datetime.now().strftime("%H:%M:%S")
        return f"The current time is {now}"

    elif re.search(r"\b(date|today)\b", user_input):
        today = datetime.datetime.now().strftime("%d-%m-%Y")
        return f"Today's date is {today}"

    elif re.search(r"\bpython\b", user_input):
        return "Python is a popular language used for AI, Web Development, and Automation."

    elif re.search(r"\b(ai|artificial intelligence)\b", user_input):
        return "AI means Artificial Intelligence. It helps machines think and learn like humans."

    elif re.search(r"\b(help|support)\b", user_input):
        return "I can do math, answer science & social questions, tell jokes, and more 😊"

    elif re.search(r"\b(who created you|your creator|who made you)\b", user_input):
        return "I was created by a Python learner using rule-based logic."

    elif re.search(r"\b(weather)\b", user_input):
        return "I cannot check live weather, but you can use Google or a weather app ☁️"

    elif re.search(r"\b(thank you|thanks)\b", user_input):
        return "You're welcome! 😊"

    elif re.search(r"\b(calculate|solve|what is)\b", user_input):
        try:
            # Extract math expression
            expression = re.findall(r"[-+*/().\d]+", user_input)
            if expression:
                result = eval(expression[0])
                return f"The answer is: {result}"
            else:
                return "Please provide a valid math expression."
        except:
            return "I couldn't calculate that. Try something like: 5+3 or 10/2."
    
    elif re.search(r"\b(photosynthesis)\b", user_input):
        return "Photosynthesis is the process by which plants make food using sunlight, carbon dioxide, and water."

    elif re.search(r"\b(gravity)\b", user_input):
        return "Gravity is the force that pulls objects toward the Earth."

    elif re.search(r"\b(evaporation)\b", user_input):
        return "Evaporation is when liquid changes into vapor due to heat."

    elif re.search(r"\b(cell)\b", user_input):
        return "A cell is the basic structural and functional unit of life."

    elif re.search(r"\b(electricity)\b", user_input):
        return "Electricity is the flow of electric charge, usually through wires."
    
    elif re.search(r"\b(what is democracy)\b", user_input):
        return "Democracy is a form of government where people choose their leaders by voting."

    elif re.search(r"\b(independence of india|indian independence)\b", user_input):
        return "India became independent on 15th August 1947."

    elif re.search(r"\b(who is mahatma gandhi|gandhi)\b", user_input):
        return "Mahatma Gandhi was the leader of India's freedom movement and believed in non-violence."

    elif re.search(r"\b(capital of india)\b", user_input):
        return "The capital of India is New Delhi."

    elif re.search(r"\b(geography)\b", user_input):
        return "Geography is the study of Earth's land, water, climate, and people."

    elif re.search(r"\b(joke|funny)\b", user_input):
        return pyjokes.get_joke()

    elif re.search(r"\b(bye|exit|quit)\b", user_input):
        return "Goodbye 👋 Have a great day!"

    else:
        return "Sorry, I didn't understand. Try asking math, science, or social questions 😊"

print(" 🤖 Pattern Matching Chatbot")
print("How can I help you today?\n")

while True:
    user = input("You: ")
    response = chatbot_response(user)
    print("Bot:", response)

    if re.search(r"\b(bye|exit|quit)\b", user.lower()):
        break
