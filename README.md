# Twitter-Emotion-Analysis-COVID19
## Twitter Emotion Analysis during the COVID 19 Pandemic
Made by- <br />
Gaurav Singh,<br />
Abhinav Dugar, <br />
Sidharth Lanka, <br />
Navyasree B <br /><br />
The visualisation of the project was done where we can see the dominant emotion of each country when we hover the mouse over the country and can be accessed here: https://gaurav2699.github.io/Twitter-Emotion-Analysis-COVID19/map.html
### IT254 Web Technologies Project
This work describes the emotion analysis of tweets regarding the COVID-19 pandemic with respect to the country of origin of the tweet. It attempts to identify the dominant emotion - joy, sadness, fear, anger or neutral - of that country which in turn hints at the degree of seriousness of the pandemic in that region.

11,209 tweets were web-scraped along with their locations after which they were categorized into different countries

We used multiple models to test the emotion analysis and achieved the following results. The BERT model gave an F1 score of 0.83, the BiLSTM gave 0.74 and the LSTM model achieved an F1 score of 0.73. We concluded that the BERT model was the best fit for the task. We further implemented a front-end for the application to provide a user interface using HTML, CSS and javascript and D3.js was used for the visualisation of the data. A map made using D3.js with each country as an element is displayed and when the user hovers over one, the sentiment of that country is shown.

To run:

In your Terminal, go to root directory of project and type ```http-server``` (if not installed, install with npm)

Go to ```localhost:8080```.

Open map.html. 
