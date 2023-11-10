from request import get_data
import json
import datetime

class Helper():
    date = datetime.datetime.today().strftime("%d-%m-%Y")
    default = ''

    def __init__(self, input="chicken"):
        self.input = input

    def process_data(self, input):
        wanted = ["name", "calories", "protein_g", "carbohydrates_total_g"]
        data = ""
        try:
            data = get_data(input)
            data = json.loads(data)
        except:
            print("Error has occured!")
            data = self.default
        if len(data["items"]) == 0:
            return 0

        tab = []

        for i in data["items"]:
            for key,val in i.items():
                if key in wanted:
                    tab.append(val)

        return tab

    def create_file(self):
        text = self.default
        with open(f"./Data/{self.date}.txt", "w+") as f:
            f.write(text)

    def read_file(self):
        with open(f"./Data/{self.date}.txt", "r") as f:
            output = f.read().splitlines()
            tab_dimentional = []
            for x in range(len(output)):
                tab_dimentional.append([])

            timer = 0
            for i in output:
                data = i.split(",")
                for j in data:
                    try:
                        tab_dimentional[timer].append(float(j))
                    except:
                        tab_dimentional[timer].append(j)
                timer+=1
            
            return tab_dimentional
        
    def file_length(self, input):
        with open(f"./Data/{input}.txt", "r") as f:
            return len(f.read())

    
    def edit_file(self, input):
        output = self.process_data(input)
        with open(f"./Data/{self.date}.txt", "a") as f:
            if self.file_length(self.date) == 0:
                f.write(",".join(str(x) for x in output))
            else:
                f.write("\n" + ",".join(str(x) for x in output))

        


    
