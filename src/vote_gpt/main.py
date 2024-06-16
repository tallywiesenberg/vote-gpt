from vote_gpt.forms import get_google_sheets_data
from vote_gpt.prompt import call_gpt

def main():
    # Get data from Google Sheets
    rows = get_google_sheets_data()
    
    for row in rows:
        if len(row) < 2:
            # If there are less than 2 columns, skip this row (assume first column is question, second column is the response)
            continue
        
        timestamp = row[0]
        state = row[1]
        zip_code = row[2]
        applicable_questions = row[3].split(",")
        print(f"Question: {applicable_questions}")
        
        # Call OpenAI with the question
        answer = call_gpt(question)
        print(f"OpenAI Answer: {answer}")

if __name__ == '__main__':
    main()