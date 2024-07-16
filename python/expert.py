class ExpertSystem:
    def __init__(self):
        self.symptoms = []
        self.diagnosis = None

    def add_symptom(self, symptom):
        self.symptoms.append(symptom)

    def diagnose(self):
        # Rule-based diagnosis
        if 'fever' in self.symptoms and 'cough' in self.symptoms:
            self.diagnosis = "Flu"
        elif 'headache' in self.symptoms and 'nausea' in self.symptoms:
            self.diagnosis = "Migraine"
        else:
            self.diagnosis = "Unknown"

    def get_diagnosis(self):
        return self.diagnosis


def main():
    print("Welcome to the Medical Diagnosis Expert System")
    print("Please enter the symptoms you are experiencing (separated by commas):")
    user_input = input().lower().split(',')

    expert_system = ExpertSystem()
    for symptom in user_input:
        expert_system.add_symptom(symptom.strip())

    expert_system.diagnose()
    print("Diagnosis:", expert_system.get_diagnosis())


if __name__ == "__main__":
    main()
