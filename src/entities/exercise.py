class Exercise:

    """Luokka kuvaa tehtävää

    question: Merkkijonoarvo, tehtävän kysymys
    answer: Kokonaislukuarvo, tehtävän vastaus
    user: Merkkijonoarvo, tehtävän omistaja
    """

    def __init__(self, question, answer, user):
        self.question = question
        self.answer = answer
        self.user = user