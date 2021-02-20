### Arduino Sentiment Analysis for AstonHack 2021

This project is a submission for AstonHack.

**Please do not mark this as cheating - I know it may be sketchy that I uploaded everything at once, but I had not put google-cloud-sdk in my .gitignore so it wouldn't push and by the time I noticed, I tried just deleting all of the git history, but it caused an error so I had to just redo the GitHub repo**

The concept is to use Google Cloud for Sentiment Analysis and then create a connection to an Arduino board to show a colored light based on the sentiment analysis. If time permits, I'll also be making a web app version.

This is also my first time using Arduino on my own and second time using Arduino ever!

Followed [this tutorial](https://cloud.google.com/natural-language/docs/sentiment-tutorial) for Google Cloud Sentiment Analysis.
Followed [this tutorial](https://realpython.com/arduino-python/) to learn how to set up my Arduino with Python
Followed [this tutorial](https://www.digitalocean.com/community/tutorials/how-to-make-a-web-application-using-flask-in-python-3) for setting up a Flask App

This is also my first time trying my own project with Google Cloud Machine Learning for a hackathon!

General Flow:
User types something in the chat
Chat gets analyzed
Based on analysis, light turns green (pos), red (neg), white (neutral)

## Inspiration
Oftentimes reading tone from text can be confusing. There's so much that can be led up to interpretation, especially if English is not your first language or you don't understand the connotations behind each word, only their definitions.

This semester is the first time I'm taking a hardware class and I knew I wanted to try something out with hardware. As a newbie, I really only know how to use the LEDs and was brainstorming to see what I could learn in a weekend, but would also benefit my audience. Knowing LEDs have different lighting, I started thinking about what each of the lights could correspond to, maybe red is bad and good is good. This reminded me of sentiment analysis -- something I've heard a lot about, but know little of. 

## What it does
Users can take a test file and based off of that score, the LED on the Arduino will light up. Red for negative, green for positive, and blue for neutral.

## How we built it
I followed documentation on Google Cloud's website on how to set up sentiment analysis using their natural language processing. I also looked up how to connect Arduino to Python so make the transition a little easier.
I also created a Flask app to allow for a software implementation of this app.

## Challenges we ran into
I had trouble connecting the Arduino to the Python as the recommend library required 3.7 and I had 3.8. I also am not familiar with setting up apps; I often work on them, but they're set up first and then I help out, so that was a learning curve. I'm pretty new to Flask and haven't done my own Flask project before.
## Accomplishments that we're proud of
This is my first time working on a hardware hack as well as my first time working on machine learning by myself. I don't believe I've used Google Cloud before, aside from Google Maps and Google Calendar.

## What we learned
I learned more about how to put a breadboard together to create a working circuit! I also had the chance to learn more about sentiment analysis and how to analyze the numbers outputted.

## What's next for Sentiment Analysis with Arduino Lights
In the future, I want to get more hardware so I can connect my Arduino with APIs and make the transition more seamless. I'd also love to design a clean box for the Arduino to sit in so users can put it either next to or on their laptop for easy reference. Then the web app (registered at whatdotheymean.online) could connect with Arduino hardware.