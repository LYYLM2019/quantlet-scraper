<a href = "http://quantlet.de/">
    <img src = "https://github.com/alextruesdale/quantlet-scraper/blob/master/repository_media/Q.png" alt = "Q logo" title = "Quantlet" align = "right" height = "120" /></a>

# Quantlet Scraping Tool
This is a small Python script for scraping the raw .R code of ~1500 GitHub repositories to then be used as a structured language training set for a LSTM Neural Network.

# Motivation
The QuantNet is a network of standalone tools for data science and statistical purposes at the Humboldt-Universität zu Berlin. Each of these tools is called a Qauntlet (like an Applet). For the Digital Economy and Decision Analytics course at the HU statistics chair, a friend of mine worked on a LSTM Neural Network to be trained on and dynamically reproduce structured, natural language.

One such example of structured language can be programming code (indeed highly structured). This tool was developed to fetch the .R code from ~1500 unique repositories as a training set for this NN.
