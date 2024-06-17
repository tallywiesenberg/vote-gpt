from src.vote_gpt.forms import get_google_sheets_data
from src.vote_gpt.prompt import create_search_query, process_search_results
from src.vote_gpt.search import fetch_search_results, search_tavily

def main():
    # Get data from Google Sheets
    rows = get_google_sheets_data()
    
    for row in rows:
        if len(row) < 2:
            # If there are less than 2 columns, skip this row (assume first column is question, second column is the response)
            continue
        
        state = row[1]
        zip_code = row[2]
        applicable_questions = row[3].split(",") + [row[4]]

        
        for question in applicable_questions:
            user_question = f"I live in {state} in zip code {zip_code}. For the upcoming election, {question}"

            search_results = search_tavily(user_question)

            summarized_content = process_search_results(search_results, user_question)

            print("Q:", question)
            print("A:", summarized_content)
            print("\n")
if __name__ == '__main__':
    main()