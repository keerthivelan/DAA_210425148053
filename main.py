import tkinter as tk
from tkinter import ttk, messagebox

# =====================================================
# NAIVE STRING MATCHING
# =====================================================
def naive_search(text, pattern):
    n = len(text)
    m = len(pattern)

    matches = []
    comparisons = 0

    for i in range(n - m + 1):
        j = 0
        while j < m:
            comparisons += 1
            if text[i + j] != pattern[j]:
                break
            j += 1

        if j == m:
            matches.append(i)

    return matches, comparisons


# =====================================================
# COMPUTE LPS FOR KMP
# =====================================================
def compute_lps(pattern):
    m = len(pattern)
    lps = [0] * m

    length = 0
    i = 1

    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1

    return lps


# =====================================================
# KMP
# =====================================================
def kmp_search(text, pattern):
    n = len(text)
    m = len(pattern)

    lps = compute_lps(pattern)

    matches = []
    comparisons = 0

    i = 0
    j = 0

    while i < n:

        comparisons += 1

        if text[i] == pattern[j]:
            i += 1
            j += 1

        if j == m:
            matches.append(i - j)
            j = lps[j - 1]

        elif i < n and text[i] != pattern[j]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    return matches, comparisons


# =====================================================
# RABIN KARP
# =====================================================
def rabin_karp(text, pattern, q=101):

    n = len(text)
    m = len(pattern)

    d = 256

    matches = []
    comparisons = 0

    h = pow(d, m - 1, q)

    p_hash = 0
    t_hash = 0

    for i in range(m):
        p_hash = (d * p_hash + ord(pattern[i])) % q
        t_hash = (d * t_hash + ord(text[i])) % q

    for s in range(n - m + 1):

        if p_hash == t_hash:

            for k in range(m):
                comparisons += 1

                if text[s + k] != pattern[k]:
                    break
            else:
                matches.append(s)

        if s < n - m:
            t_hash = (
                d * (t_hash - ord(text[s]) * h)
                + ord(text[s + m])
            ) % q

            if t_hash < 0:
                t_hash += q

    return matches, comparisons


# =====================================================
# SEARCH BUTTON FUNCTION
# =====================================================
def search():

    text = text_entry.get()
    pattern = pattern_entry.get()

    if text == "" or pattern == "":
        messagebox.showerror("Error", "Please enter both Text and Pattern.")
        return

    table.delete(*table.get_children())

    naive_match, naive_comp = naive_search(text, pattern)
    kmp_match, kmp_comp = kmp_search(text, pattern)
    rk_match, rk_comp = rabin_karp(text, pattern)

    table.insert("", "end", values=("Naive", str(naive_match), naive_comp))
    table.insert("", "end", values=("KMP", str(kmp_match), kmp_comp))
    table.insert("", "end", values=("Rabin-Karp", str(rk_match), rk_comp))


# =====================================================
# GUI
# =====================================================

root = tk.Tk()

root.title("String Matching Algorithm Visualizer")
root.geometry("900x600")

title = tk.Label(
    root,
    text="STRING MATCHING ALGORITHM VISUALIZER",
    font=("Arial", 20, "bold")
)

title.pack(pady=20)

text_label = tk.Label(
    root,
    text="Enter Text",
    font=("Arial", 12)
)

text_label.pack()

text_entry = tk.Entry(
    root,
    width=80,
    font=("Arial", 12)
)

text_entry.pack(pady=5)

pattern_label = tk.Label(
    root,
    text="Enter Pattern",
    font=("Arial", 12)
)

pattern_label.pack()

pattern_entry = tk.Entry(
    root,
    width=35,
    font=("Arial", 12)
)

pattern_entry.pack(pady=5)

search_button = tk.Button(
    root,
    text="Search",
    width=15,
    font=("Arial", 12),
    command=search
)

search_button.pack(pady=15)

columns = ("Algorithm", "Matches", "Comparisons")

table = ttk.Treeview(
    root,
    columns=columns,
    show="headings",
    height=6
)

table.heading("Algorithm", text="Algorithm")
table.heading("Matches", text="Match Positions")
table.heading("Comparisons", text="Comparisons")

table.column("Algorithm", width=180, anchor="center")
table.column("Matches", width=400, anchor="center")
table.column("Comparisons", width=180, anchor="center")

table.pack(pady=20)

root.mainloop()