import tkinter as tk
from tkinter import scrolledtext
import datetime

responses = {
    "admission": "For admissions, visit the university admissions office or check the official website. Applications usually open in January and July.",
    "apply": "You can apply online through the university portal. Make sure to have your matric and intermediate certificates ready.",
    "eligibility": "Eligibility criteria varies by program. Generally you need at least 60% marks in intermediate for engineering programs.",
    "fee": "Fee structures vary by department. You can get the exact fee challan from the accounts office or student portal.",
    "scholarship": "Scholarships are available for students with high merit and financial need. Visit the scholarship office or apply online through HEC.",
    "dues": "You can check and pay your dues through the student portal or visit the accounts office directly.",
    "timetable": "Timetables are usually posted on the department notice board and student portal at the start of each semester.",
    "class": "Class schedules are available on the student portal. Contact your department coordinator for any changes.",
    "exam": "Exam schedules are announced 2 weeks before exams on the notice board and student portal.",
    "result": "Results are usually announced within 4 weeks after exams. Check the student portal or your department notice board.",
    "library": "The library is open Monday to Saturday, 8am to 8pm. You can borrow up to 3 books at a time with your student ID.",
    "hostel": "Hostel applications open at the start of each semester. Contact the hostel office for availability and fee details.",
    "transport": "University transport routes and timings are posted on the transport office notice board. Routes are updated each semester.",
    "cafeteria": "The cafeteria is open from 8am to 6pm on weekdays. It is located in the main block ground floor.",
    "contact": "You can contact the university at info@nfciet.edu.pk or call 061-9220123 during office hours.",
    "holiday": "The academic calendar including holidays is posted on the student portal at the start of each semester.",
    "complaint": "For complaints, visit the student affairs office or submit your complaint through the official student portal.",
}

def get_response(user_input):
    user_input = user_input.lower()
    for keyword, response in responses.items():
        if keyword in user_input:
            return response
    return "I'm sorry, I don't have information on that. Please visit the student affairs office or call 061-9220123 for help."

class ChatbotGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("NFC IET Student Query Chatbot")
        self.root.geometry("500x600")
        self.root.configure(bg="#f0f0f0")
        self.root.resizable(False, False)

        # Header
        header = tk.Frame(root, bg="#1a73e8", pady=15)
        header.pack(fill=tk.X)
        tk.Label(header, text="NFC IET Student Chatbot",
                 bg="#1a73e8", fg="white",
                 font=("Arial", 14, "bold")).pack()
        tk.Label(header, text="Ask me anything about campus life",
                 bg="#1a73e8", fg="#cce0ff",
                 font=("Arial", 9)).pack()

        # Chat area
        self.chat_area = scrolledtext.ScrolledText(
            root, wrap=tk.WORD, state=tk.DISABLED,
            bg="white", font=("Arial", 10),
            relief=tk.FLAT, padx=10, pady=10
        )
        self.chat_area.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Tag colors for messages
        self.chat_area.tag_config("user", foreground="#1a73e8", font=("Arial", 10, "bold"))
        self.chat_area.tag_config("bot", foreground="#333333", font=("Arial", 10))
        self.chat_area.tag_config("time", foreground="#999999", font=("Arial", 8))

        # Input area
        input_frame = tk.Frame(root, bg="#f0f0f0", pady=8)
        input_frame.pack(fill=tk.X, padx=10)

        self.input_field = tk.Entry(
            input_frame, font=("Arial", 11),
            relief=tk.SOLID, bd=1
        )
        self.input_field.pack(side=tk.LEFT, fill=tk.X, expand=True, ipady=8)
        self.input_field.bind("<Return>", self.send_message)

        send_btn = tk.Button(
            input_frame, text="Send", bg="#1a73e8", fg="white",
            font=("Arial", 10, "bold"), relief=tk.FLAT,
            padx=15, pady=8, cursor="hand2",
            command=self.send_message
        )
        send_btn.pack(side=tk.LEFT, padx=(8, 0))

        # Welcome message
        self.add_message("Chatbot", "Hello! I am the NFC IET Student Assistant. Ask me about admissions, fees, exams, library, hostel, or anything about campus life!", is_user=False)

    def add_message(self, sender, message, is_user=True):
        self.chat_area.config(state=tk.NORMAL)
        time = datetime.datetime.now().strftime("%H:%M")

        if is_user:
            self.chat_area.insert(tk.END, f"\nYou ({time}):\n", "user")
        else:
            self.chat_area.insert(tk.END, f"\nChatbot ({time}):\n", "user" if is_user else "time")

        self.chat_area.insert(tk.END, f"{message}\n", "user" if is_user else "bot")
        self.chat_area.config(state=tk.DISABLED)
        self.chat_area.see(tk.END)

    def send_message(self, event=None):
        user_input = self.input_field.get().strip()
        if not user_input:
            return

        self.add_message("You", user_input, is_user=True)
        self.input_field.delete(0, tk.END)

        response = get_response(user_input)
        self.add_message("Chatbot", response, is_user=False)

root = tk.Tk()
app = ChatbotGUI(root)
root.mainloop()