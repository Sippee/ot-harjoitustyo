from tkinter import *
from tkinter import ttk, StringVar, constants
from functools import partial
from services.service import service

class ExercisesView:
    def __init__(self, root, exercises):
        self._root = root
        self._exercises = exercises
        self._frame = None
        
        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize_exercise_item(self, exercise):
        item_frame = ttk.Frame(master=self._frame)
        item_frame.grid_columnconfigure(0, weight=1)
        item_frame.pack(fill=constants.X)

        questions = ttk.Label(master=item_frame, text=exercise.question)
        answers = ttk.Label(master=item_frame, text=exercise.answer)

        questions.grid(row=0, column=0, padx=5, pady=5, sticky=constants.W)
        answers.grid(row=0, column=1, padx=5, pady=5, sticky=constants.W)


    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        for exercise in self._exercises:
            self._initialize_exercise_item(exercise)


class ExerciseView:
    def __init__(self, root, handle_logout):
        self._root = root
        self._handle_logout = handle_logout
        self._user = service.get_user()
        self._frame = None
        self._create_question = None
        self._create_answer = None
        self._exercises_frame = None
        self._exercises_view = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _logout_handler(self):
        service.logout()
        self._handle_logout()

    def _initialize_exercises(self):
        if self._exercises_view:
            self._exercises_view.destroy()

        exercises = service.get_exercises()

        self._exercises_view = ExercisesView(self._exercises_frame, exercises)

        self._exercises_view.pack()

    def _handle_create_exercise(self):
        exercise_question = self._create_question.get()
        exercise_answer = self._create_answer.get()

        if exercise_question and exercise_answer:
            service.create_exercise(exercise_question, exercise_answer)
            self._initialize_exercises()
            self._create_question.delete(0, constants.END)
            self._create_answer.delete(0, constants.END)

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        self._exercises_frame = ttk.Frame(master=self._frame)

        logout_button = ttk.Button(master=self._frame, text='Logout', command=self._logout_handler)
        logout_button.grid(row=0, column=1, padx=5, pady=5, sticky=constants.W)

        self._initialize_exercises()

        question = Label(self._frame, text="Question")
        question.grid(row=0, column=0, padx=5, pady=5, sticky=constants.W)

        answer = Label(self._frame, text="Answer")
        answer.grid(row=2, column=0, padx=5, pady=5, sticky=constants.W)
        
        create_exercise_button = ttk.Button(master=self._frame, text='Create', command=self._handle_create_exercise)
        create_exercise_button.grid( row=3, column=1, padx=5, pady=5, sticky=constants.EW)
        
        self._create_question = ttk.Entry(master=self._frame)
        self._create_question.grid(row=1, column=0, padx=5, pady=5, sticky=constants.EW)
        
        self._create_answer = ttk.Entry(master=self._frame)
        self._create_answer.grid(row=3, column=0, padx=5, pady=5, sticky=constants.EW)

        questions = Label(self._frame, text="Questions")
        questions.grid(row=5, column=0, padx=5, pady=5, sticky=constants.W)

        answers = Label(self._frame, text="Answers")
        answers.grid(row=5, column=1, padx=5, pady=5, sticky=constants.W)

        self._exercises_frame.grid(row=6, column=0, columnspan=2, sticky=constants.EW)

        self._frame.grid_columnconfigure(0, weight=0, minsize=400)
        self._frame.grid_columnconfigure(1, weight=0)
