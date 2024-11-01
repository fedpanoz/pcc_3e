class Macchina:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        
    def visualizza_info(self):
        return f"{self.year} {self.make} {self.model}"
    
    def start_engine(self):
        return f"Fai partire il mototre della {self.model}"
    
    
    
mia_macchina = Macchina('Tesla', 'Modello X', 2024)

print(type(mia_macchina))

print(mia_macchina.visualizza_info())
print(mia_macchina.start_engine())