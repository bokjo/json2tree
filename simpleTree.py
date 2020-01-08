### File Name: Tkinter ttk Treeview Simple Demo
### Reference: http://knowpapa.com/ttk-treeview/

from tkinter import *
from tkinter import ttk
import json 

with open('example.json') as json_file:
    data = json.load(json_file)
    # print(data)
    print(json.dumps(data, indent=4))

for (k, v) in data[0].items():
   print("Key: " + k)
   print("Value: " + str(v)) 

quiz = data[0]
print(quiz['quiz']['sport']['q1']['options'])
print(type(quiz['quiz']['sport']['q1']['options']))
root = Tk()
root.title('json2tree')
root.geometry('800x800')


tree = ttk.Treeview(root, height = 15)

tree["columns"] = ("one", "two")
tree.column("one", width=300)
tree.column("two", width=300)
tree.heading("one", text="column A")
tree.heading("two", text="column B")


### insert format -> insert(parent, index, iid=None, **kw)
### reference: https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Treeview
tree.insert("", 0, text="Line 1", values=("1A", "1b"))
tree.insert("", "end", text="sub dir 2", values=("2A", "2B"))

### insert sub-item, method 1
id2 = tree.insert("", "end", "dir2", text="Dir 2")
tree.insert(id2, "end", text="sub dir 2-1", values=("2A", "2B"))
tree.insert(id2, "end", text="sub dir 2-2", values=("2A-2", "2B-2"))

### insert sub-item, method 2
tree.insert("", "end", "dir3", text="Dir 3")
tree.insert("dir3", "end", text=" sub dir 3", values=("3A", "3B"))

### insert quiz
tree.insert("", "end", "quiz", text="quiz")
tree.insert("quiz", "end", "sport", text="sport")
tree.insert("quiz", "end", "maths", text="maths")

tree.insert("sport", "end", "q1", text="q1")

tree.insert("q1", "end", "question", text="question")
tree.insert("question", "end", text="Which one is correct team name in NBA?")

tree.insert("q1", "end", "options", text="options")
tree.insert("options", "end", text="New York Bulls")
tree.insert("options", "end", text="Los Angeles Kings")
tree.insert("options", "end", text="Golden State Warriors")
tree.insert("options", "end", text="Huston Rocket")

tree.insert("q1", "end", "answer", text="answer")
tree.insert("answer", "end", text="Huston Rocket")


tree.pack()
root.mainloop()