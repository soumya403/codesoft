import tkinter as tk
from tkinter import StringVar

class AttractiveQuizApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry('500x400')
        self.root.title('Attractive Quiz App')
        self.root.config(bg='#e6e6e6')

        self.questions = [
            "What is the capital of Italy?",
            "Which programming language is this quiz written in?",
            "What is the largest ocean on Earth?",
            "Who is the author of 'Harry Potter' series?",
            "How many continents are there in the world?"
        ]

        self.options = [
            ['Rome', 'Paris', 'Berlin', 'Madrid', 'Rome'],
            ['Java', 'Python', 'C++', 'JavaScript', 'Python'],
            ['Atlantic Ocean', 'Indian Ocean', 'Arctic Ocean', 'Pacific Ocean', 'Pacific Ocean'],
            ['J.K. Rowling', 'George R.R. Martin', 'Stephen King', 'Dan Brown', 'J.K. Rowling'],
            ['5', '6', '7', '8', '7']
        ]

        self.index = 0
        self.correct_answers = 0

        self.setup_ui()

    def setup_ui(self):
        header_label = tk.Label(self.root, text='Simple Quiz App', font=('Helvetica', 24, 'bold'), bg='#3366cc', fg='white')
        header_label.pack(pady=10)

        self.question_label = tk.Label(self.root, text=self.questions[self.index], font=('Arial', 16), bg='#e6e6e6')
        self.question_label.pack(pady=20)

        self.var = StringVar()

        for i in range(4):
            option = tk.Radiobutton(self.root, text=self.options[self.index][i], variable=self.var, value=self.options[self.index][i], font=('Arial', 12), bg='#e6e6e6')
            option.pack(anchor='w', padx=10)

        next_button = tk.Button(self.root, text='Next', command=self.next_question, font=('Arial', 14, 'bold'), bg='#4CAF50', fg='white')
        next_button.pack(pady=10, side='bottom')

    def next_question(self):
        selected_option = self.var.get()

        if selected_option == self.options[self.index][4]:
            self.correct_answers += 1

        self.index += 1

        if self.index < len(self.questions):
            self.update_question()
        else:
            self.show_results()

    def update_question(self):
        self.question_label.config(text=self.questions[self.index])
        self.var.set('')
        for i in self.root.winfo_children():
            if isinstance(i, tk.Radiobutton):
                i.destroy()
        for i in range(4):
            option = tk.Radiobutton(self.root, text=self.options[self.index][i], variable=self.var, value=self.options[self.index][i], font=('Arial', 12), bg='#e6e6e6')
            option.pack(anchor='w', padx=10)

    def show_results(self):
        for i in self.root.winfo_children():
            if isinstance(i, tk.Radiobutton) or isinstance(i, tk.Button) or isinstance(i, tk.Label):
                i.destroy()

        result_label = tk.Label(self.root, text=f'Your Final Score: {self.correct_answers} / {len(self.questions)}', font=('Helvetica', 18, 'bold'), bg='#e6e6e6')
        result_label.pack(pady=20)

if __name__ == "__main__":
    root = tk.Tk()
    app = AttractiveQuizApp(root)
    root.mainloop()
