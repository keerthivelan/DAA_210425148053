import tkinter as tk

# Student Data
students = [
    [101, "Arun"],
    [102, "Bala"],
    [103, "Charan"],
    [104, "Deepak"],
    [105, "Eswar"]
]

# Search Function
def search_student():
    roll = entry.get()

    if roll == "":
        result.config(text="Please Enter Roll Number", fg="red")
        return

    try:
        roll = int(roll)

        for student in students:
            if student[0] == roll:
                result.config(
                    text=f"✅ Student Found\n\nRoll No : {student[0]}\nName : {student[1]}",
                    fg="green"
                )
                return

        result.config(text="❌ Student Not Found", fg="red")

    except:
        result.config(text="Enter Numbers Only", fg="red")


# Main Window
root = tk.Tk()
root.title("Student Search System")
root.geometry("700x500")
root.configure(bg="#d6ecff")

# Heading
heading = tk.Label(
    root,
    text="🎓 STUDENT SEARCH SYSTEM",
    font=("Arial", 24, "bold"),
    bg="#d6ecff",
    fg="#003366"
)
heading.pack(pady=20)

# White Card
frame = tk.Frame(root, bg="white", bd=3, relief="ridge")
frame.pack(padx=40, pady=20, fill="both", expand=True)

# Label
label = tk.Label(
    frame,
    text="Enter Roll Number",
    font=("Arial", 18, "bold"),
    bg="white"
)
label.pack(pady=20)

# Entry Box
entry = tk.Entry(
    frame,
    font=("Arial", 18),
    width=20,
    justify="center"
)
entry.pack(pady=10)

# Search Button
button = tk.Button(
    frame,
    text="🔍 SEARCH",
    font=("Arial", 18, "bold"),
    bg="#0078D7",
    fg="white",
    width=15,
    command=search_student
)
button.pack(pady=20)

# Result Label
result = tk.Label(
    frame,
    text="",
    font=("Arial", 18, "bold"),
    bg="white"
)
result.pack(pady=20)

root.mainloop()