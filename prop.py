import tkinter as tk


def calculate_proportion():
    try:
        numerator1 = float(entry_numerator1.get())
        numerator2 = float(entry_numerator2.get())
        denominator2 = float(entry_denominator2)
        result = (numerator1*denominator2) / numerator2
        result_label.config(text="Result:{:.2f}".format(result))
    except ValueError:
        (result_label.config(text="Enter numbers"))


root = tk.Tk()
root.title("Proportion calculator")

entry_denominator2 = 4

label_numerator1 = tk.Label(root, text="Wound surface area(px):")
label_numerator1.pack()
entry_numerator1 = tk.Entry(root)
entry_numerator1.pack()

label_numerator2 = tk.Label(root, text="Sample area(px):")
label_numerator2.pack()
entry_numerator2 = tk.Entry(root)
entry_numerator2.pack()

calculate_button = tk.Button(root, text="Count", command=calculate_proportion)
calculate_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
