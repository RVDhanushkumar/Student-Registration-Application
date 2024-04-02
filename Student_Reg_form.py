import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
from reportlab.lib.styles import ParagraphStyle, TA_CENTER
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib import colors
from datetime import datetime
import re
import os


def check():
    if name.get() == "" or AICTE_id.get() == "" or email.get() == "" or phone_no.get() == "" or col_name.get() == "":
        messagebox.showerror("Missing", "All Entries are required!!")
        return

    if name.get().isdigit():
        messagebox.showerror("Error", "Name should contain only alphabets")
        return

    if not phone_no.get().isdigit() or len(phone_no.get()) != 10:
        messagebox.showerror("Error", "Invalid Phone number!!")
        return

    if not validate_email(email.get()):
        messagebox.showerror("Error", "Invalid Email address!!")
        return

    save_student_data()


def validate_email(email):
    # Regular expression for basic email validation
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(pattern, email)


def save_student_data():
    conn = sqlite3.connect('student_data.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS students
                 (name TEXT, AICTE_id TEXT, email TEXT, phone_no TEXT, col_name TEXT, registration_date DATE)''')

    current_date = datetime.now().strftime("%d-%m-%Y")
    c.execute("INSERT INTO students VALUES (?, ?, ?, ?, ?, ?)",
              (name.get(), AICTE_id.get(), email.get(), phone_no.get(), col_name.get(), current_date))

    conn.commit()
    conn.close()
    generate_pdf()


def generate_pdf():
    conn = sqlite3.connect('student_data.db')
    c = conn.cursor()
    c.execute("SELECT * FROM students")
    student_data = c.fetchall()
    conn.close()

    # Generate PDF
    output_file = "student_data.pdf"
    doc = SimpleDocTemplate(output_file, pagesize=letter)

    # Add heading
    heading = "Student Details"
    heading_style = ParagraphStyle(name='Heading1', fontSize=24, alignment=TA_CENTER,fontname='Times-Bold')
    heading_text = Paragraph(heading, heading_style)

    # Add table with the date column
    table_data = [["Name", "AICTE ID", "Email", "Phone Number", "College Name", "Registration Date"]] + student_data
    table = Table(table_data)

    # Define table style
    style = TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.purple),
                        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
                        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                        ('TOPPADDING', (0, 0), (-1, 0), 12),
                        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                        ('GRID', (0, 0), (-1, -1), 1, colors.black)])

    # Apply table style
    table.setStyle(style)

    # Add space between heading and table
    blank_space = Paragraph("<br/><br/><br/><br/><br/>", heading_style)

    # Build PDF
    content = [heading_text, blank_space, table]
    doc.build(content)

    messagebox.showinfo("Success", f"Student data saved to {output_file}")


def load_student_data(table_view):
    for row in table_view.get_children():
        table_view.delete(row)

    conn = sqlite3.connect('student_data.db')
    c = conn.cursor()
    c.execute("SELECT * FROM students")
    student_data = c.fetchall()
    conn.close()

    for student in student_data:
        table_view.insert("", "end", values=student)


def delete_student_data():
    def confirm_delete():
        selected_item = table_view.selection()
        if not selected_item:
            messagebox.showerror("Error", "Please select a student to delete!")
            return

        response = messagebox.askyesno("Confirmation", "Are you sure you want to delete this student's data?")
        if response == tk.YES:
            conn = sqlite3.connect('student_data.db')
            c = conn.cursor()
            student_name = table_view.item(selected_item, "values")[1]
            c.execute("DELETE FROM students WHERE AICTE_id=?", (student_name,))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "Student data deleted successfully!")
            load_student_data(table_view)
            delete_window.destroy()

    delete_window = tk.Toplevel(window)
    delete_window.title("Delete Student Data")

    table_view = ttk.Treeview(delete_window, columns=("Name", "AICTE ID", "Email", "Phone Number", "College Name", "Registration Date"), show='headings')
    table_view.heading("Name", text="Name")
    table_view.heading("AICTE ID", text="AICTE ID")
    table_view.heading("Email", text="Email")
    table_view.heading("Phone Number", text="Phone Number")
    table_view.heading("College Name", text="College Name")
    table_view.heading("Registration Date", text="Registration Date")
    table_view.pack(pady=10)

    load_student_data(table_view)

    delete_button = tk.Button(delete_window, text="Delete", command=confirm_delete)
    delete_button.pack(pady=10)


def clear_data():
    for entry in (name, AICTE_id, email, phone_no, col_name):
        entry.delete('0', tk.END)


def open_pdf():
    pdf_file = "student_data.pdf"
    if os.path.exists(pdf_file):
        os.system(f'start {pdf_file}')
    else:
        messagebox.showerror("Error", "PDF file not found!")


if __name__ == "__main__":
    window = tk.Tk()
    window.title("Student Registration Form")

    l1 = tk.Label(window, text="Application Form.\n Please fill the details properly!!", font="20", fg="Blue")
    l1.pack(pady=10)

    f1 = tk.Frame(window)
    f1.pack()

    l2 = tk.Label(f1, text="Enter Name: ")
    l2.pack(side=tk.LEFT,pady=10)

    name = tk.Entry(f1, width=20)
    name.pack(side=tk.LEFT, padx=0)

    f2 = tk.Frame(window)
    f2.pack()

    l3 = tk.Label(f2, text="Enter AICTE id: ")
    l3.pack(side=tk.LEFT, pady=0)

    AICTE_id = tk.Entry(f2, width=20)
    AICTE_id.pack(side=tk.LEFT, padx=0)

    f3 = tk.Frame(window)
    f3.pack()

    l4 = tk.Label(f3, text="Enter Email: ")
    l4.pack(side=tk.LEFT, pady = 10)

    email = tk.Entry(f3, width=20)
    email.pack(side=tk.LEFT, padx=10)

    f4 = tk.Frame(window)
    f4.pack()

    l5 = tk.Label(f4, text="Enter Phone no: ")
    l5.pack(side=tk.LEFT, pady=0)

    phone_no = tk.Entry(f4, width=20)
    phone_no.pack(side=tk.LEFT, padx=10)

    f5 = tk.Frame(window)
    f5.pack()

    l6 = tk.Label(f5, text="Enter College name: ")
    l6.pack(side=tk.LEFT,pady=10)

    col_name = tk.Entry(f5, width=20)
    col_name.pack(side=tk.LEFT, padx=10)

    f6 = tk.Frame(window)
    f6.pack(pady=20)

    sb = tk.Button(f6, text="Add Data", command=check)
    sb.pack(side=tk.LEFT)

    sb1 = tk.Button(f6, text="Delete Student Data", command=delete_student_data)
    sb1.pack(side=tk.LEFT, padx=15)

    f7 = tk.Frame(window)
    f7.pack(pady=0)

    sb2 = tk.Button(f7, text='Clear', command=clear_data)
    sb2.pack(side=tk.LEFT)

    sb3 = tk.Button(f7, text='Open PDF',command=open_pdf)
    sb3.pack(side=tk.LEFT, padx=20)

    window.geometry('400x400')
    window.mainloop()
