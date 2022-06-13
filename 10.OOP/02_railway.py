class RailWayForm:
    formType = "RailWayForm"
    def printData(self):
        print(f"Name is {self.name}")
        print(f"Train is {self.train}")

binodApplication = RailWayForm()
binodApplication.name = "Binod"
binodApplication.train = "Gulmi Express"
binodApplication.printData()
