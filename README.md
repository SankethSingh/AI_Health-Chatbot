
# Healthcare Assistant Chatbot 
The Healthcare Assistant Chatbot is an AI-powered chatbot designed to assist users with healthcare-related queries. Built using Streamlit and Google's Gemini AI, this chatbot provides users with information on symptoms, medications, and appointments while ensuring a sleek and interactive user experience.

This project focuses on delivering quick and reliable health-related responses with a modern, elegant UI that includes smooth transitions, animations, and interactive elements. In case of critical health concerns, the chatbot displays a special warning urging users to seek immediate medical assistance.

## Features 🚀

 - 🤖 AI-powered chatbot using Gemini AI

 - 🏥 Provides responses to health queries, symptoms, and medication information

 - ⚠️ Displays critical case warnings for severe conditions

 - 🎨 Sleek dark-themed UI with elegant animations and transitions

 - 🖥️ Built with Streamlit for fast and responsive interactions

## How It Works

    1. Enter a health-related query in the text input box
    2. The chatbot analyzes the input and generates an appropriate response
    3. If a severe condition is detected (e.g., "chest pain"), a red warning is displayed
    4. The chatbot continuously improves by leveraging AI-driven responses
## Technologies Used
 - 	Programming Language: Python
 - Libraries & Frameworks:
 - 	NLP: Google Gemini API
 - 	Web Development: Streamlit
 - 	Data Processing: Pandas, NumPy
 - 	Visualization: Matplotlib, Seaborn

## Installation ⬇️

Clone the repository:
```bash 
git clone https://github.com/yourusername/AI_Health-Chatbot.git
cd AI_Health-Chatbot
```
 - Install dependencies:
Ensure you have Python installed, then install the required libraries:
```bash
pip install streamlit google-generativeai nltk
```
Create a virtual environment to isolate the project dependencies:
```bash
python -m venv healthcare-chatbot-env
```
Activate the virtual environment:

On Windows:
```bash 
healthcare-chatbot-env\Scripts\activate
```
On macOS/Linux:
```bash 
source healthcare-chatbot-env/bin/activate
```

Run the application:

```bash     
streamlit run healthcare_chatbot.py
```

Gemini API Key:

Ensure you have a valid Gemini API key from Google AI Studio.

    Replace "your-gemini-api-key" in the code with your actual API key.
    
## Prediction
Let's give a sample prompt:
    
    How to treat common cold at home 
               (or) 
    How to treat Chest Pain (Critical Case)
## Screenshots
- Dashboard UI

![Dashboard](https://github.com/SankethSingh/AI_Health-Chatbot/blob/master/images/dashboard-bot.png?raw=true)

- Processing Query
![Processing Query](https://github.com/SankethSingh/AI_Health-Chatbot/blob/master/images/query-bot.png?raw=true)

- Display Output
![Output](https://github.com/SankethSingh/AI_Health-Chatbot/blob/master/images/result-bot.png?raw=true)

- Critical case input
![Critical-input](https://github.com/SankethSingh/AI_Health-Chatbot/blob/master/images/critical-input.png?raw=true)


## Future Enhancements
 - Future improvements can focus on integrating voice recognition and synthesis to enhance accessibility, allowing users to interact with the chatbot using voice commands.
- Expanding the chatbot's capabilities to support multiple languages will make it more inclusive and accessible to a diverse user base worldwide.
- Integrating real-time medical databases and AI-driven anomaly detection can improve the accuracy of responses and provide users with the latest healthcare insights.
- Deploying the chatbot on cloud platforms like AWS or Google Cloud will enhance scalability and accessibility for a broader audience.
- Incorporating telemedicine services to connect users with healthcare professionals for virtual consultations can further enhance the chatbot’s impact.

## Contributing
Contributions are welcome! If you find any issues or have suggestions for improvement, feel free to open an issue or submit a pull request.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments
 - [Attention-Transformer] - Vaswani, A. (2017). Attention is all you need. Advances in Neural Information Processing Systems.

 - [Using health chatbots for behavior change] - Pereira, J., & Díaz, Ó. (2019). Using health chatbots for behavior change: a mapping study. Journal of medical systems, 43, 1-13.