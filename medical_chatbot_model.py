import pandas as pd

class MedicalChatbot:
    def __init__(self, data_path='data/gale_medical_data.csv'):
        try:
            self.medical_data = pd.read_csv(data_path)
        except FileNotFoundError:
            print(f"Error: File not found at {data_path}. Make sure the CSV exists.")
            self.medical_data = pd.DataFrame()

    def suggest_medicine(self, user_input):
        if self.medical_data.empty:
            return "Error: Medical data not loaded."

        # Clean user input: lowercase and remove leading/trailing whitespace
        cleaned_input = user_input.lower().strip()

        # Basic matching: Check if the cleaned user input is in the disease/condition column (case-insensitive)
        matches = self.medical_data[self.medical_data['disease_or_condition'].str.lower().str.contains(cleaned_input)]

        if not matches.empty:
            # For simplicity, let's take the first match and its medicines
            suggested_medicines = matches.iloc[0]['possible_medicines']
            return f"Based on your input, possible medicines might include: {suggested_medicines}"
        else:
            return "Sorry, I couldn't find information related to that. Please check your spelling or try a different phrasing."
if __name__ == '__main__':
    chatbot = MedicalChatbot()
    print(chatbot.suggest_medicine("common cold"))
    print(chatbot.suggest_medicine("headache"))
    print(chatbot.suggest_medicine("unknown condition"))