import spacy

# Load English tokenizer, tagger, parser, NER, and word vectors
nlp = spacy.load("en_core_web_sm")

# Define pairs of patterns and responses
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, how can I help you today?",]
    ],
    [
        r"What is your name?",
        ["My name is HealthBot and I'm here to assist you with healthcare queries.",]
    ],
    [
        r"(.*) health",
        ["I'm a chatbot, so I don't have health, but I can help you with health-related questions.",]
    ],
    [
        r"(.*) (hospital|clinic|doctor)",
        ["You can find the nearest hospital by searching online or using a healthcare app.",]
    ],
    [
        r"(.*) (headache|fever|cough|cold)",
        ["You might be experiencing symptoms of a common cold. I recommend getting rest and staying hydrated.",]
    ],
    [
        r"(.*) (prescription|medication)",
        ["I'm not a doctor, but you should consult a healthcare professional for prescriptions.",]
    ],
    [
        r"quit",
        ["Goodbye, take care. Feel free to reach out if you have more questions.",]
    ],
]

# Create a function to match patterns and generate responses
def healthcare_chatbot():
    print("Welcome! I'm HealthBot. How can I assist you today?")
    while True:
        user_input = input()
        if user_input.lower() == 'quit':
            print("Goodbye, take care. Feel free to reach out if you have more questions.")
            break
        response = generate_response(user_input)
        print(response)

def generate_response(user_input):
    for pattern, responses in pairs:
        match = spacy_match(pattern, user_input)
        if match:
            response = responses[0]  # Select the first response
            return response.replace('%1', match.group(1))  # Replace %1 with matched group
    return "I'm sorry, I didn't understand that."

def spacy_match(pattern, user_input):
    doc = nlp(user_input)
 
 