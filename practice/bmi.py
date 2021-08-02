import math as m


class BMI:
    def __init__(self, w_kg, h_cm):
        self.w_kg = w_kg
        self.h_cm = h_cm

    def bmi(self):
        return self.w_kg / (self.h_cm/100) ** 2

    def category(self):
        diag = ""
        bmi_value = self.bmi()
        if bmi_value < 18.5:
            diag = "Underweight"
        elif 18.5 <= bmi_value <= 25:
            diag = "Healthy Weight"
        elif 25 < bmi_value <= 30:
            diag = "Overweight"
        elif bmi_value > 30:
            diag = "Obese"
        return diag

    # def __str__(self):
    #     return "BMI = {:.2f} ({})".format(self.bmi(),self.category())

    def __repr__(self) -> str:
        return repr((self.w_kg,self.h_cm,self.bmi()))