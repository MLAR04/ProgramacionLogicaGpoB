diseases = {"Gripe", "Covid", "Migraña", "Resfriado"}
symptoms_per_disease = {
    "Gripe": {"tos", "dolor de cabeza"},
    "Covid": {"fiebre", "tos", "cansansio", "perdida del olfato"},
    "Migraña": {"dolor de cabeza", "nauseas"},
    "Resfriado": {"congestion nasal", "fiebre", "tos"},
}
all_symptoms = set().union(*symptoms_per_disease.values())  # ex: tos, fiebre, etc.

def is_disease(n: str) -> bool:
    return n in diseases  # is on disease list? true/false

def is_symptom(n: str) -> bool:
    return n in all_symptoms  # is on all symptoms list? true/false

def required_symptoms(disease: str) -> set:
    return symptoms_per_disease.get(disease, set())  # returns a list of symptoms per disease

def exact_match(disease: str, symptoms: set) -> bool:
    if not is_disease(disease):
        return False
    return symptoms == symptoms_per_disease[disease]

# returns the disease(s) that match exactly
def match(user_symptoms) -> set:
    symptoms = set(user_symptoms)
    matches = {d for d in diseases if exact_match(d, symptoms)}
    return matches

def diagnose(*symptoms):  # ex: diagnose("tos", "fiebre")
    user_symptoms = set(symptoms)
    matches = match(user_symptoms)

    print(f"\nSíntomas ingresados: {list(symptoms)}")
    if not matches:
        print(f"No coincide con ninguna enfermedad en la base de conocimiento.")
    elif len(matches) == 1:
        disease = next(iter(matches))
        print(f"Diagnóstico:  {disease}")
    else:  # if for some reason its more than one
        print(f"Diagnósticos posibles: {','.join(sorted(matches))}")

# use examples
diagnose("tos", "fiebre")
diagnose("tos", "fiebre", "congestion nasal")
