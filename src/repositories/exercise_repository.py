from pathlib import Path
from entities.exercise import Exercise
from repositories.user_repository import user_repository


class ExerciseRepository:

    """Luokka kuvaa tehtävien tallennusta .csv tiedostoon

    filepath: merkkijonoarvo, kertoo mihin ja millä nimellä tiedosto tallennetaan.
    """

    def __init__(self, filepath):
        self._filepath = filepath

    # Luetaan ja palautetaan koko tiedoston sisältö
    def readall(self):
        return self._read()

    # Luodaan uusi tehtävä
    def create(self, exercise):
        exercises = self.readall()

        exercises.append(exercise)

        self._write(exercises)

        return exercise

    # Etsitään tehtäviä nimellä
    def findname(self, username):
        exercises = self.readall()
        
        exercises_by_user = filter(lambda exercise: exercise.user and exercise.user[0] == username, exercises)

        return list(exercises_by_user)

    # Tarkastetaan onko tiedosto olemassa, jos ei ole luodaan se
    def _checkingfile(self):
        Path(self._filepath).touch()

    # Luetaan Tiedosto ja palautetaan sen sisältö
    def _read(self):
        exercises = []

        self._checkingfile()

        with open(self._filepath) as f:
            for row in f:
                row = row.replace('\n', '')
                parts = row.split(';')

                question = parts[0]
                answer = parts[1]
                username = parts[2]

                user = user_repository.findname(username) if username else None

                exercises.append(Exercise(question, answer, user))

        return exercises

    # Tallennetaan tietoa tiedostoon
    def _write(self, exercises):
        self._checkingfile()

        with open(self._filepath, 'w') as f:
            for exercise in exercises:
                try:
                    username = exercise.user[0] if exercise.user else ''
                except:
                    username = exercise.user.username if exercise.user else ''

                row = f'{exercise.question};{exercise.answer};{username}'

                f.write(row+'\n')

# Tiedoston sijainti ja tyyppi
exercise_repository = ExerciseRepository("data/exercises.csv") #C:\\Users\\Markus\\AppData\\Local\\Packages\\CanonicalGroupLimited.UbuntuonWindows_79rhkp1fndgsc\\LocalState\\rootfs\\home\\markus\\ot-harjoitustyo\\
