class MassHandler:

    def __init__(self, mass, unit):
        self.mass = mass
        self.unit = unit

    def unit_convert(self):
        if self.unit == 'kg':
            pass
        elif self.unit == 'pound':
            self.mass *= 0.453592


class HeightHandler:

    def __init__(self, height, unit):
        self.height = height
        self.unit = unit

    def unit_converter(self):
        if self.unit == 'm':
            pass
        if self.unit == 'cm':
            self.height *= 0.01
        if self.unit == 'feet':
            self.height *= 0.3048
        if self.unit == 'inch':
            self.height *= 0.0254


class BmiHandler:

    def __init__(self, mass, height):
        self.mass = mass
        self.height = height
        self.bmi = "Uncalculated"

    def bmi_value(self):
        return self.mass/(self.height**2)

    def check_range(self):
        self.bmi = self.bmi_value()

        if self.bmi < 18.5:
            return('''You are under weight
            Take more protein and carbs''')
        elif 18.5 <= self.bmi <= 24.9:
            return '''You are normal
            Do exercises regularly to maintain your health'''
        elif 25 <= self.bmi <= 29.9:
            return '''You seem to be over-weight
            You must limit carbs intake and do exercises '''
        elif self.bmi >= 30:
            return '''You are obese
            You must do exercises daily.
            You must develop a healthy eating habit.
            You must be seriously concerned to your health now'''
