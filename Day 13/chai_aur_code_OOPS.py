class hospital:
    def __init__(self,name):
        self.__name = name
    @property
    def name(self):
        print(f"hospital name is {self.__name}")
    

class ayurvedicHospital(hospital):
    def __init__(self,name,department):
        super().__init__(name)
        self.departmemt = department
kd = hospital('KD hospital')
kd.name

ayurvedic = ayurvedicHospital("chikitsalaya","ayurvedic")

ayurvedic.name

