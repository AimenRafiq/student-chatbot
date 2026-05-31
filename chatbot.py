# Student Query Chatbot
# Answers common questions students have about university life

import datetime

# Knowledge base - all questions and answers
responses = {
    # Admission related
    "admission": "For admissions, visit the university admissions office or check the official website. Applications usually open in January and July.",
    "apply": "You can apply online through the university portal. Make sure to have your matric and intermediate certificates ready.",
    "eligibility": "Eligibility criteria varies by program. Generally you need at least 60% marks in intermediate for engineering programs.",

    # Fee related
    "fee": "Fee structures vary by department. You can get the exact fee challan from the accounts office or student portal.",
    "scholarship": "Scholarships are available for students with high merit and financial need. Visit the scholarship office or apply online through HEC.",
    "dues": "You can check and pay your dues through the student portal or visit the accounts office directly.",

    # Schedule related
    "timetable": "Timetables are usually posted on the department notice board and student portal at the start of each semester.",
    "class": "Class schedules are available on the student portal. Contact your department coordinator for any changes.",
    "exam": "Exam schedules are announced 2 weeks before exams on the notice board and student portal.",
    "result": "Results are usually announced within 4 weeks after exams. Check the student portal or your department notice board.",

    # Campus related
    "library": "The library is open Monday to Saturday, 8am to 8pm. You can borrow up to 3 books at a time with your student ID.",
    "hostel": "Hostel applications open at the start of each semester. Contact the hostel office for availability and fee details.",
    "transport": "University transport routes and timings are posted on the transport office notice board. Routes are updated each semester.",
    "cafeteria": "The cafeteria is open from 8am to 6pm on weekdays. It is located in the main block ground floor.",

    # General
    "contact": "You can contact the university at info@nfciet.edu.pk or call 061-9220123 during office hours.",
    "holiday": "The academic calendar including holidays is posted on the student portal at the start of each semester.",
    "complaint": "For complaints, visit the student affairs office or submit your complaint through the official student portal.",
}

def get_response(user_input):
    user_input = user_input.lower()

    # Check if any keyword matches
    for keyword, response in responses.items():
        if keyword in user_input:
            return response

    # Default response if nothing matches
    return "I'm sorry, I don't have information on that. Please visit the student affairs office or call 061-9220123 for help."

def save_chat(history):
    filename = f"chat_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    with open(filename, "w") as f:
        for line in history:
            f.write(line + "\n")
    print(f"\nChat saved to {filename}")

def main():
    print("=" * 50)
    print("   NFC IET Student Query Chatbot")
    print("=" * 50)
    print("Ask me anything about admissions, fees,")
    print("exams, library, hostel, or campus life.")
    print("Type 'save' to save chat history.")
    print("Type 'quit' to exit.")
    print("=" * 50)
    print()

    history = []

    while True:
        user_input = input("You: ").strip()

        if not user_input:
            continue

        if user_input.lower() == "quit":
            print("Chatbot: Goodbye! Good luck with your studies.")
            break

        if user_input.lower() == "save":
            save_chat(history)
            continue

        response = get_response(user_input)

        history.append(f"You: {user_input}")
        history.append(f"Chatbot: {response}")

        print(f"Chatbot: {response}")
        print()

if __name__ == "__main__":
    main()