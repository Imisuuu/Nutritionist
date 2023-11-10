import tkinter as tk
from helper import Helper
import datetime


def gui():
    helper = Helper()
    root = tk.Tk()
    root.geometry("1100x450")
    root.title("NutritionApp")


    date = datetime.datetime.today().strftime("%Y-%m-%d")
    text = tk.Label(root, text=f"Calorie intake for {date}.", font=("Fira Code", 20))
    text.pack(padx=20, pady=20)

    def space_in_between(frame, row):
        bridge = tk.Label(frame,text="-----------------------------------------------------------------------------------------------------------------------------------------")
        bridge.grid(row=row, column=0, columnspan=4)

    def create_frame():
        frame = tk.Frame(root)
        canvas = tk.Frame(root)
        for i in range(5):
            canvas.columnconfigure(i, weight=1)
            frame.columnconfigure(i, weight=1)


        wanted = ["name", "calories", "protein", "carbohydrates"]
        col=0
        for j in wanted:
            title = tk.Label(frame, text=j.capitalize(), font=("Fira Code", 18))
            title.grid(row=0, column=col, padx=20)
            col+=1

        nutrition = helper.read_file()
        dict = {}
        row = 1 # Important element, used further for all the labels

        for key in wanted:
            if key == 'name':
                dict[key] = ""
            else:
                dict[key] = 0

        for item in nutrition:
            column = 0
            for val, key in zip(item, wanted):
                if isinstance(val, str):
                    dict[key] = str(dict[key]) + val + " "
                else:
                    dict[key] += float(val)

                lbl = tk.Label(frame, text=val, font=("Arial", 12))
                lbl.grid(row=row, column=column, padx=20)
                column += 1
            row +=1

        space_in_between(frame, row=row)


        licznik = 1
        all_in_all = tk.Label(frame, text="Sum:")
        all_in_all.grid(row=row+1, column=0)
        for key,val in dict.items():
            if isinstance(val, str):
                continue
            final = tk.Label(frame, text=int(val))
            final.grid(row= row+1,column = licznik)
            licznik+=1
    
    
        def add_to_list():
            data = input_widget.get()
            instance = Helper(data)

            try:
                instance.edit_file(data)
            except:
                print("An error has occured with the GUI!")
            frame.destroy()
            canvas.destroy()
            create_frame()
        
        new_row = 0
        space_in_between(canvas, row=new_row)

        input_widget = tk.Entry(canvas)
        input_widget.grid(row=new_row+1, column=0, columnspan=2, sticky=tk.W+tk.E)
        input_btn = tk.Button(canvas, text="Add", command=add_to_list).grid(row=new_row+1, column=3, sticky=tk.W+tk.E)

        frame.pack()
        canvas.pack()

        

    create_frame()
    root.mainloop()
