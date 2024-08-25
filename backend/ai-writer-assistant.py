import openai
import os

openai.api_key = "你的API密鑰"

class SmartWritingAssistant:
    def __init__(self):
        self.conversation_history = []

    def generate_text(self, prompt):
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful writing assistant."},
                    {"role": "user", "content": prompt}
                ]
            )
            return response.choices[0].message['content'].strip()
        except Exception as e:
            return f"Error: {str(e)}"

    def improve_text(self, text):
        prompt = f"Please improve the following text:\n\n{text}\n\nImproved version:"
        return self.generate_text(prompt)

    def summarize_text(self, text):
        prompt = f"Please summarize the following text:\n\n{text}\n\nSummary:"
        return self.generate_text(prompt)

    def translate_text(self, text, target_language):
        prompt = f"Translate the following text to {target_language}:\n\n{text}\n\nTranslation:"
        return self.generate_text(prompt)

def main():
    assistant = SmartWritingAssistant()
    
    while True:
        print("\n1. Generate Text")
        print("2. Improve Text")
        print("3. Summarize Text")
        print("4. Translate Text")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            prompt = input("Enter a prompt for text generation: ")
            result = assistant.generate_text(prompt)
        elif choice == '2':
            text = input("Enter the text to improve: ")
            result = assistant.improve_text(text)
        elif choice == '3':
            text = input("Enter the text to summarize: ")
            result = assistant.summarize_text(text)
        elif choice == '4':
            text = input("Enter the text to translate: ")
            language = input("Enter the target language: ")
            result = assistant.translate_text(text, language)
        elif choice == '5':
            print("Thank you for using the Smart Writing Assistant!")
            break
        else:
            print("Invalid choice. Please try again.")
            continue
        
        print("\nResult:")
        print(result)

if __name__ == "__main__":
    main()