import google.generativeai as ai

#API Key
API_Key = 'AIzaSyC-T-xYmXcqibj_hKERObtjKVk33_7-fZE'

#Configure the API
ai.Configure(api_key=API_Key)

#Create a new model 
model = ai.GenerativeModel("gemini-pro")
Chat = model start_chat()

#Start a Conversation 
While True:
Message = Input ('You: ')
if message.lower() =='bye':
  print('Chatbot: Goodbye:')
  break
  response = chat.send_message(message)
  print('Chatbot:' response.text)
