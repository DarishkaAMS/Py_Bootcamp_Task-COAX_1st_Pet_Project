from typing import List
# from .notes import Notes

class Author:

    def __init__(self, name:str, genre:str, descr:str, notes): #List[Note] = None)
        self.name = name
        self.genre = genre
        self.descr = descr
        self.notes = notes

    # def to_dict(self):
    #     return {name:"name", genre:"genre", descr:"descr", notes:"notes"} # Reference to notes.py?

    def dateframe(self):
        pass

    def add(self):
        """Add note to author"""
        doc = open("Author.txt", "a")#create the file OR a???
        au_note = self.name + "-" + self.notes + '\n'
        doc.write(au_note) #only 1 argument
        doc.close()

    def avg(self):
        """ Calculation average """
        avg_list=[]
        doc_avg = open("Notes.txt", "r")

        for line in doc_avg.read():
            for ch in line:
                if ch == "-":
                    print(line[line.index(ch)+1::])
                    # avg_list.append(float(line[line.index(ch)+1::]))
        # reference to notes.txt?

    #to-delete
    def read(self):
        doc = open("Author.txt", "r")
        print(doc.readline())
        doc.close()

#Demo
au = Author ("Umberto Eco", "novels", "Historical base novels", "Best day reading")
print (au.descr)
# au.add()
# au.read()
au.avg()



