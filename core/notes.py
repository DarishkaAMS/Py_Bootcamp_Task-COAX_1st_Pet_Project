
class Notes:

    def __init__(self, note: str, author_name:str, rating: float):
        self.note = note
        self.author_name = author_name
        self.rating = rating

    # def rating2person(self):

    def add(self):
        """Add note to author"""
        doc = open("Notes.txt", "a")  # create the file OR a???
        note_au_rating = self.author_name + "-" + str(self.rating) + '\n' #STR pt Float and back again
        doc.write(note_au_rating)  # only 1 argument
        doc.close()

    def read(self):
        doc = open("Notes.txt", "r")
        print(doc.read())
        doc.close()


# eco_note = Notes("Best day reading", "Umberto Eco", 0.7)
# print(eco_note.note)
# eco_note.add()
# eco_note .read()

eco_note = Notes("Best night reading", "J. K. Roling", 0.6)
print(eco_note.note)
eco_note.add()
eco_note.read()