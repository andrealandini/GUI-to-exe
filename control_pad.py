import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
from tkinter import HORIZONTAL, BOTH
import pandas as pd
import os

font_size = 10
window_width = 800
window_height = 600


class ExcelFileSelector:
    def __init__(self, root):
        self.selected_files = []
        self.input_text = tk.StringVar()  # Variable to store the input string
        self.root = root
        #self.root.title("Check Phase")

        self.page1 = tk.Frame(self.root, bg='#182a3d')
        self.page1.place(relwidth=1, relheight=1)  # Take the entire window

        label1 = tk.Label(self.page1, text="Do the thing.", font=("Times New Roman", 40), bg='#182a3d', fg='white')
        label1.place(relx=0.5, rely=0.1, anchor=tk.CENTER)  # Position the label

        button1 = tk.Button(self.page1, text="Browse", command=self.browse_file, width=5, bg='#182a3d', fg='#182a3d', highlightbackground='#182a3d', anchor=tk.CENTER)
        button1.place(relx=0.2, rely=0.3, anchor="w")  # Position the button

        self.deselect_button = tk.Button(self.page1, text="Deselect",width=5, command=self.deselect_file, state=tk.DISABLED, bg='#182a3d', fg='#182a3d', highlightbackground='#182a3d', anchor=tk.CENTER)
        self.deselect_button.place(relx=0.2, rely=0.4, anchor="w")  # Position the button






        # Entry widget for input
        self.input_entry = tk.Entry(self.page1, textvariable=self.input_text, width=20,bg='white', fg='black', highlightbackground='#182a3d')
        self.input_entry.place(relx=0.4, rely=0.2, anchor="w")

        self.input_entry_green = False  # Flag to track if the entry background is green

        # Button to add the input to the list
        self.add_input_button = tk.Button(self.page1, text="Add Key", command=self.add_input,width=5, bg='#182a3d', fg='#182a3d', highlightbackground='#182a3d', anchor=tk.CENTER)
        self.add_input_button.place(relx=0.2, rely=0.2, anchor="w")

        # Listbox to display the added strings
        self.listbox = tk.Listbox(self.page1, selectmode=tk.SINGLE, width=40)
        self.listbox.place(relx=0.2, rely=0.65, anchor="w")


        xscrollbar = tk.Scrollbar(self.page1, orient=HORIZONTAL)
        xscrollbar.place(relx=0.2, rely=0.8, anchor="w", width=363)  # Adjust the position and width

        # Attach the horizontal scrollbar to the listbox
        self.listbox.config(xscrollcommand=xscrollbar.set)
        xscrollbar.config(command=self.listbox.xview)
        
        self.process_button = tk.Button(self.page1, text="Output", command=self.process_files,width=5, bg='#182a3d', fg='#182a3d', highlightbackground='#182a3d', anchor=tk.CENTER)
        self.process_button.place(relx=0.2, rely=0.9, anchor="w")  # Position the button

        self.refresh = tk.Button(self.page1, text="Refresh", command=self.reset_data,width=5, bg='#182a3d', fg='#182a3d', highlightbackground='#182a3d', anchor=tk.CENTER)
        self.refresh.place(relx=0.4, rely=0.9, anchor="w")  # Position the button

        #self.root.minsize(600, 500)
        #self.root.maxsize(800, 800)

    def browse_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Excel Files", "*.xlsx")])
        if file_path:
            self.selected_files.append(file_path)
            self.deselect_button.config(state=tk.NORMAL)
            self.listbox.insert(tk.END, file_path)

    def deselect_file(self):
        selected_index = self.listbox.curselection()
        if selected_index:
            index = selected_index[0]
            self.listbox.delete(index)
            self.selected_files.pop(index)
            if not self.listbox.get(0, tk.END):
                self.deselect_button.config(state=tk.DISABLED)

    #def process_files(self):
    #    print("List of selected files:")
     #   for i, path in enumerate(self.selected_files):
      #      print(f"Excel File {i+1}: {path}")

    def process_files(self):
        if self.input_entry_green:
            if len(self.selected_files)!=0:
                print("List of selected files:")
                for i, path in enumerate(self.selected_files):
                    print(f"Excel File {i+1}: {path}")
            else:
                messagebox.showerror("Error", "No file selected.")

        else:
            messagebox.showerror("Error", "Please press 'Add Key' at least once before processing files.")

  
    def add_input(self):
        input_str = self.input_text.get()
        if input_str:
            #self.listbox.insert(tk.END, input_str)
            if not self.input_entry_green:
                self.input_entry.config(bg="#90ee90")
                self.input_entry_green = True


    def reset_data(self):
        # Reset the data
        self.selected_files = []
        self.input_text.set("")  # Clear the input text
        self.input_entry.config(bg="white")  # Reset input entry background color
        self.input_entry_green = False
        self.listbox.delete(0, tk.END)




class DoAThing:
    def __init__(self, root):
        self.root = root


        self.pagemastrini = tk.Frame(self.root, bg='#182a3d')
        self.pagemastrini.place(relwidth=1, relheight=1) 


        label1 = tk.Label(self.pagemastrini, text="Do the thing", font=("Times New Roman", 40), bg='#182a3d', fg='white')
        label1.place(relx=0.5, rely=0.1, anchor=tk.CENTER) 
        # Initialize variables to store input strings
        self.file_to_operate_on_string = tk.StringVar()
        self.number_text = tk.StringVar()
        self.key_text = tk.StringVar()

        # Initialize background color flags for each Entry widget
        self.bg_color_set_file_to_operate_on = False
        self.bg_color_set_number_column = False
        self.bg_color_set_key = False

        # Label and Entry for file mastrino
        key_label = tk.Label(self.pagemastrini, text="File",bg='#182a3d', fg='white', highlightbackground='#182a3d', anchor=tk.CENTER)
        key_label.place(relx=0.05, rely=0.3, anchor="w")

        self.directory_entry = tk.Entry(self.pagemastrini, textvariable=self.file_to_operate_on_string, font=("Arial", 12), width=60 ,bg='white', fg='black', highlightbackground='#182a3d')
        self.directory_entry.place(relx=0.18, rely=0.3, anchor="w")

        browse_button = tk.Button(self.pagemastrini, text="Browse", command=self.browse_file,bg='#182a3d', fg='#182a3d', highlightbackground='#182a3d', anchor=tk.CENTER)
        browse_button.place(relx=0.18, rely=0.35, anchor="w")

        # Label and Entry for number_column
        key_label = tk.Label(self.pagemastrini, text="Column1",bg='#182a3d', fg='white', highlightbackground='#182a3d', anchor=tk.CENTER)
        key_label.place(relx=0.05, rely=0.45, anchor="w")

        self.key_entry_number_column = tk.Entry(self.pagemastrini, textvariable=self.number_text,bg='white', fg='black', highlightbackground='#182a3d')
        self.key_entry_number_column.insert(0, "Number Column Name")  # Default text
        self.key_entry_number_column.place(relx=0.18, rely=0.45, anchor="w")

        # Label and Entry for Key
        key_label = tk.Label(self.pagemastrini, text="Key",bg='#182a3d', fg='white', highlightbackground='#182a3d', anchor=tk.CENTER)
        key_label.place(relx=0.05, rely=0.55, anchor="w")

        self.key_entry_key = tk.Entry(self.pagemastrini, textvariable=self.key_text,bg='white', fg='black', highlightbackground='#182a3d')
        self.key_entry_key.insert(0, "Key Text")  # Default text
        self.key_entry_key.place(relx=0.18, rely=0.55, anchor="w")


        output_button = tk.Button(self.pagemastrini, text="Output", command=self.submit_strings,bg='#182a3d', fg='#182a3d', highlightbackground='#182a3d', anchor=tk.CENTER)
        output_button.place(relx=0.2, rely=0.9, anchor="w")

        refresh_button = tk.Button(self.pagemastrini, text="Refresh", command=self.refresh_entries,bg='#182a3d', fg='#182a3d', highlightbackground='#182a3d', anchor=tk.CENTER)
        refresh_button.place(relx=0.4, rely=0.9, anchor="w")




    def browse_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Excel Files", "*.xlsx")])
        if file_path:
            self.file_to_operate_on_string.set(file_path)

    def submit_strings(self):
        file_to_operate_on = self.file_to_operate_on_string.get()
        number_column = self.number_text.get()
        key = self.key_text.get()

        # Check if the strings are non-empty
        if file_to_operate_on and number_column and key:
            # Strings are submitted, change the background color for all Entry widgets
            self.directory_entry.config(bg="#90ee90")
            self.key_entry_number_column.config(bg="#90ee90")
            self.key_entry_key.config(bg="#90ee90")

            # Check if all the background colors are set
            if (
                self.bg_color_set_file_to_operate_on and
                self.bg_color_set_number_column and
                self.bg_color_set_key
            ):
                print("All entries are set and colored.")
            else:
                print("Some entries are set and colored.")
            
            data = [file_to_operate_on, number_column, key]
            print("Submitted Data:", data)
        else:
            messagebox.showerror("Error", "Please fill in all fields.")



    def refresh_entries(self):
        # Reset all entry fields and their background colors
        self.file_to_operate_on_string.set("")
        self.number_text.set("Number Column Name")
        self.key_text.set("Suggested Key Text")

        # Reset background color flags
        self.bg_color_set_file_to_operate_on = False
        self.bg_color_set_number_column = False
        self.bg_color_set_key = False

        # Reset background colors
        self.directory_entry.config(bg="white")
        self.key_entry_number_column.config(bg="white")
        self.key_entry_key.config(bg="white")





class JustifiedTextFrame:
    def __init__(self, root):
        self.root = root


        self.page = tk.Frame(self.root, bg='#182a3d')  # Background color
        self.page.place(relwidth=1, relheight=1)  # Take the entire window

        self.text_widget = tk.Text(self.page, wrap='char', bg='#182a3d', font=("Arial", 12), bd=0, highlightbackground='#182a3d')
        self.text_widget.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)
        self.text_widget.tag_configure('tag-center', justify='left')


        tex = "This is just a sample text."

        self.text_widget.insert('1.0', tex, 'tag-center')
        self.text_widget.config(state='disabled')  # Make the text non-editable
        self.text_widget.bind("<1>", lambda event: "break")  # Disable text selection






class SimpleApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Aide Analyst")

        # Create Page 1
        self.page1 = tk.Frame(self.root, bg='#182a3d')
        self.page1.place(relwidth=1, relheight=1)  # Take the entire window
        label1 = tk.Label(self.page1, text="Aide Analyst", font=("Times New Roman", 70), bg='#182a3d', fg='white')
        label1.place(relx=0.5, rely=0.2, anchor=tk.CENTER)  # Position the label
        label1p1 = tk.Label(self.page1, text="Menu", font=("Times New Roman", 25), bg='#182a3d', fg='white')
        label1p1.place(relx=0.5, rely=0.32, anchor=tk.CENTER)  # Position the label
        
        label1p1 = tk.Label(self.page1, text="by Andrea Landini", font=("Times New Roman", 25), bg='#182a3d', fg='white')
        label1p1.place(relx=0.5, rely=.9, anchor=tk.CENTER)  # Position the label


        button1 = tk.Button(self.page1, text="Do a Thing", command=self.show_page2, bg='#182a3d', fg='#182a3d', highlightbackground='#182a3d',width=10)
        button1.place(relx=0.25, rely=0.40, anchor=tk.W)  # Position the button
        button3 = tk.Button(self.page1, text="About me", command=self.show_page3, bg='#182a3d', fg='#182a3d', highlightbackground='#182a3d',width=10)
        button3.place(relx=0.75, rely=0.40, anchor=tk.E)  # Position the button
        button4 = tk.Button(self.page1, text="To another thing", command=self.show_page4, bg='#182a3d', fg='#182a3d', highlightbackground='#182a3d',width=10)
        button4.place(relx=0.25, rely=0.50, anchor=tk.W)  # Position the button

        # Create Page 2
        self.page2 = tk.Frame(self.root)
        label2 = tk.Label(self.page2, text="Page 2", font=("Arial", 16))
        label2.place(relx=0.5, rely=0.5, anchor=tk.CENTER)  # Position the label
        self.df_app_frame = tk.Frame(self.page2)
        self.df_app_frame.place(relwidth=1, relheight=1)
        self.df_app = ExcelFileSelector(self.df_app_frame)



        # Create Page 3
        self.page3 = tk.Frame(self.root)
        label3 = tk.Label(self.page3, font=("Arial", 16))
        label3.place(relx=0.5, rely=0.5, anchor=tk.CENTER)  # Position the label
        self.df_app_frame3 = tk.Frame(self.page3)
        self.df_app_frame3.place(relwidth=1, relheight=1)
        self.df_app = JustifiedTextFrame(self.df_app_frame3)




        # Create Page 4
        self.page4 = tk.Frame(self.root)
        label4 = tk.Label(self.page4, font=("Arial", 16))
        label4.place(relx=0.5, rely=0.5, anchor=tk.CENTER)  # Position the label
        self.df_app_frame2 = tk.Frame(self.page4)
        self.df_app_frame2.place(relwidth=1, relheight=1)
        self.df_app = DoAThing(self.df_app_frame2)

        # Set minimum and maximum window sizes
        self.root.minsize(600, 500)
        self.root.maxsize(800, 800)

        # Start with Page 1
        self.current_page = "page1"
        self.show_page(self.current_page)

    def show_page1(self):
        self.show_page("page1")


    def show_page2(self):
        self.show_page("page2")

    def show_page3(self):
        self.show_page("page3")

    def show_page4(self):
        self.show_page("page4")


    def show_page(self, page_name):
        # Hide all pages
        self.page1.place_forget()
        self.page2.place_forget()
        self.page3.place_forget()
        self.page4.place_forget()

        if page_name == "page1":
            self.page1.place(relwidth=1, relheight=1)  # Show Page 1
            self.current_page = "page1"
        elif page_name == "page2":
            self.page2.place(relwidth=1, relheight=1)  # Show Page 2
            self.current_page = "page2"
            # Add a "Menu" button in Page 2
            back_to_menu_button = tk.Button(self.page2, text="Menu", command=self.show_page1, bg='#182a3d', fg='#182a3d', highlightbackground='#182a3d')
            back_to_menu_button.place(relx=0.1, rely=0.1, anchor=tk.W)  # Position the button
        elif page_name == "page3":
            self.page3.place(relwidth=1, relheight=1)  # Show Page 3
            self.current_page = "page3"
            back_to_menu_button = tk.Button(self.page3, text="Menu", command=self.show_page1, bg='#182a3d', fg='#182a3d', highlightbackground='#182a3d')
            back_to_menu_button.place(relx=0.5, rely=0.8, anchor=tk.CENTER)  # Position the button




        elif page_name == "page4":
            self.page4.place(relwidth=1, relheight=1)  # Show Page 4
            self.current_page = "page4"
            back_to_menu_button = tk.Button(self.page4, text="Menu", command=self.show_page1, bg='#182a3d', fg='#182a3d', highlightbackground='#182a3d')
            back_to_menu_button.place(relx=0.1, rely=0.1, anchor=tk.W)  # Position the button


if __name__ == "__main__":
    root = tk.Tk()
    app = SimpleApp(root)
    root.geometry("800x600")  # Set the initial window size
    root.mainloop()

