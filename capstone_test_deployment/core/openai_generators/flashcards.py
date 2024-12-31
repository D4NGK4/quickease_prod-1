from openai import OpenAI
from dotenv import load_dotenv
import os
import json

load_dotenv()

client = OpenAI(api_key=os.environ.get('OPENAI_API_KEY'))

def generate_flashcards(paragraph):
    prompt =(
        '''
            Convert the following summary content into flashcards based on all possible key terms and their definitions.
	    The total flashcards should only be maximum of 40.

            ### Important Instruction:
	    - Generate flashcards with the following structure: Each flashcard should have a 'Term' on the front and a 'Definition' on the back.
            - The format should be in JSON format: Id:# Front: Term \n Back: Definition "
	    - Begin each definition with an appropriate phrase (e.g., 'It is', 'This refers to', 'An example of', 'Known as', 'Defined as') to create a complete sentence. Vary the starting phrases to make the definitions more engaging.
	    - DON'T INCLUDE (INTRODUCTION SECTION) AND (OVERVIEW SUMMARY SECTION) IN THE BASIS OF MAKING THE FLASHCARDS
            - Use the exact words and phrases from the input text as much as possible, but minor rephrasing is acceptable for clarity.
            - Only JSON data is required. No other decorators like ``` are needed.
            - The terms should be related to [specific subject or topic]. Provide concise and accurate definitions for each term.
	    - Ensure that the content of the definition is accurate and closely reflects the terminology from the text while making grammatical sense.

	    Here is an example format of the JSON output:
		[
    			{
        			"Front": "Least Privilege",
        			"Back": "It is the principle that users should have the minimum level of access necessary to perform their tasks, reducing the risk of accidental or intentional damage.",
   	 		},
		]

        '''
             )
    

    response = client.chat.completions.create(
        model='gpt-4o',
        messages=[
            {"role": "system", "content": prompt },
            {"role": "user", "content": paragraph},
        ],
        max_tokens=4000,  
        temperature=0.7,
    )
    
    flashcards_text = response.choices[0].message.content
    
        
    print(flashcards_text)

    return flashcards_text
