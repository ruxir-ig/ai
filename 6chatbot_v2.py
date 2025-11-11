import gradio as gr

chatbot_name = "Flux"

responses = {
    "Shipping": "We offer free shipping on orders over $50. Standard delivery takes 3-5 business days. For faster options, check our website.",
    "Returns": "You can return items within 30 days for a full refund. Please visit our returns page or provide your order number for assistance.",
    "Products": "We sell electronics, clothing, and home goods.(e.g., 'Laptops' or 'Shirts')",
    "Laptops": "Our laptops range from $500 to $1500.For more enquiry visit our store.",
    "Shirts": "We have casual shirts starting at $20. Sizes from S to XXL available in various colors.",
    "Orders": "To check an order, please visit our website(www.web2store.com)",
    "Support Hours": "We're available 9 AM to 6 PM EST, Monday to Friday. For urgent issues, email w2s.support@gmail.com.",
    "Quit": f"Thank you for visiting! Have a great day!"
}

def respond(button_choice):
    return f"{chatbot_name}: {responses[button_choice]}"

demo = gr.Interface(
    fn=respond,
    inputs=gr.Radio(list(responses.keys()), label="Choose a question"),
    outputs=gr.Textbox(label="Chatbot Response", lines=3),
    title=f"{chatbot_name} - Customer Support",
    description=f"Hello! I'm {chatbot_name}. Click a question to get a response."
)

if name == "main":
    demo.launch()

# --- 

# ANOTHER APPROACH SIMPLE PYTHON

# Simple dictionary-based responses
responses = {
    "hi": "Hello! Welcome to ABC Store. How can I help you today?",
    "hello": "Hi there! How can I assist you?",
    "price": "Our products range from $10 to $500 depending on the category.",
    "delivery": "We offer standard delivery in 3-5 business days and express delivery in 1-2 days.",
    "return": "You can return any product within 30 days of purchase.",
    "thanks": "You’re welcome! Have a great day!",
    "bye": "Goodbye! Thanks for visiting ABC Store."
}

def chatbot():
    print("Chatbot: Hello! I am your assistant. Type 'bye' to exit.\n")
    
    # Print possible questions
    print("You can ask me questions like:")
    for key in responses:
        if key != "bye":  # exclude exit
            print("-", key)
    print("\nLet's chat!\n")
    
    while True:
        user_input = input("You: ").strip().lower()  # normalize input
        if user_input == "bye":
            print("Chatbot: Goodbye! Have a nice day.")
            break
        # respond based on dictionary
        response = responses.get(user_input, "I'm sorry, I didn't understand that. Can you rephrase?")
        print("Chatbot:", response)

# Run the chatbot
chatbot()
