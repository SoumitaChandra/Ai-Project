import random
import re

class RuleAiBot:
    
# Responses

    negative_res = {"no", "nope", "nah", "naw", "not a chance","nothing", "sorry"}
    exit_commands = {"quit", "pause", "exit", "goodbye", "bye", "later"}

    def __init__(self):
        self.support_responses = {
            'ask_about_product': r'.*\s*product.*',
            'technical_support': r'.*technical.*support.*',
            'about_returns': r'.*return.*policy.*',
            'general_query': r'.*how.*help.*'
        }

    
    def greet(self):
        self.name = input("Hii! Welcome to our Customer Support and Service. What's your name?\n Your name: ")
        will_help = input(f"Hi {self.name}, how can I assist you today?\n").lower()
        if will_help in self.negative_res:
            print("Okay, have a nice day!")
            return
        self.chat()


    def create_exit(self,reply):
        for command in self.exit_commands:
            if command in reply:
                print("Thanks for reaching out. Have a great day!")   
                return True
        return False
        
    
    def chat(self):
        reply = input("Please tell me your Query:").lower()
        while not self.create_exit(reply):
            reply = input(self.same_reply(reply)).lower()


    def same_reply(self, reply):
        for intent, regex_pattern in self.support_responses.items():
            found_match = re.search(regex_pattern, reply)
            if found_match:
                if intent == 'ask_about_product':
                    return self.ask_about_product()
            elif intent == 'technical_support':
                    return self.technical_support()
            elif intent == 'about_returns':
                    return self.about_returns()
            elif intent == 'general_query':
                    return self.general_query()
        return self.no_match_intent()
    

    def ask_about_product(self):
        responses = ("Our product has high demand and reviews are excellent!\n",
                     "You can find all details about the product on our website.\n")
        return random.choice(responses)
    
    def technical_support(self):
        responses = ("You can call our tech support helpline for any kind of help.\n",
                     "Please visit our technical support page for proper assistance.\n")
        return random.choice(responses)
    
    def about_returns(self):
        responses = (" We have a 30 days return policy.\n",
                     "Please confirm that the product is in it's initial condition while returning.\n")
        return random.choice(responses)
    
    def general_query(self):
        responses = ("How can I assist you further?\n"
                     "Do you have any other questions about the product?\n")
        return random.choice(responses)
    
    def no_match_intent(self):
        responses = ("Sorry! I can't understand that. Can you please repharse?\n",
                     "Pardon me, Can you provide more details?\n")
        return random.choice(responses)
    
bot = RuleAiBot()
bot.greet()

            
            