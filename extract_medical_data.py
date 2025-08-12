import re
import pandas as pd

def extract_condition_treatment(text_file_path, output_csv_path):
    condition = None
    data = []
    try:
        with open(text_file_path, 'r', encoding='utf-8') as infile:
            text = infile.read()
            # Split the text into sections based on potential condition headings (uppercase lines)
            sections = re.split(r'(\n[A-Z][a-zA-Z\s]+?\n)', text)

            for i in range(1, len(sections), 2):
                potential_condition = sections[i].strip()
                if len(potential_condition.split()) < 15 and not potential_condition.lower().startswith(('resources', 'organizations', 'other', 'key terms', 'prognosis', 'prevention', 'diagnosis', 'books', 'periodicals')):
                    condition = potential_condition.replace(',', '')
                    treatment_text = ""
                    if i + 1 < len(sections):
                        treatment_section = sections[i + 1].strip()
                        # Look for treatment-related keywords in the following section
                        if re.search(r'\b(treatment|medication|drug|prescribe)\b', treatment_section, re.IGNORECASE):
                            treatment_text = treatment_section

                    if condition and treatment_text:
                        medicines = re.findall(r'\b(aspirin|ibuprofen|naproxen|acetaminophen|paracetamol|antibiotics|antivirals|antifungals|corticosteroids|prednisone|insulin)\b', treatment_text, re.IGNORECASE)
                        if medicines:
                            unique_medicines = ', '.join(sorted(list(set(medicines))))
                            data.append({'disease_or_condition': condition, 'possible_medicines': unique_medicines})
                            condition = None # Reset condition

    except FileNotFoundError:
        print(f"Error: File not found at '{text_file_path}'")
        return
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return
    
    df = pd.DataFrame(data)
    df.to_csv(output_csv_path, index=False)
    print(f"Successfully created '{output_csv_path}'")

if __name__ == "__main__":
    input_file = r"C:\Users\umari\Downloads\Medical Book.txt" # Use raw string for path
    output_file = "data/gale_medical_data.csv"
    extract_condition_treatment(input_file, output_file)