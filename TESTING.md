# Testing and Deployment

[Visit site here]()

# Contents

1. [Development and Problem Solving](#development-and-Problem-Solving)
2. [Testing for User Stories](#Testing-for-User-Stories)
3. [Responsiveness](#Responsiveness)
4. [Code Validators and Lighthouse](#Code-Validators-and-Lighthouse)
5. [Deployment](#Deployment)
6. [Browser Tests](#Browser-Tests)

# Development and Problem Solving

The first test I ran at the start of the project was to check the data I had entered when setting up MongoDB was being pulled across successfully from the Mongo database. 
I checked this using a Jinja for loop to iterate through the 'recipe' data. This was successful. 

<img alt=data-test-app.png src="testing-images/data-test-app.png" width=25%>
<img alt=data-test-html.png src="testing-images/data-test-html.png" width=30%>
<img alt=data-test.png src="testing-images/data-test.png" width=35%>

After adding Materialize and the static CSS/Script files, I added a background template to style.css to test the files were connected. 
At this point Werkzeug pointed out a typo, I had not added a comma into the my script.js tag. Upon fixing this, the background colour worked. 

<img alt=css-test-error.png src="testing-images/css-test-error.png" width=35%>
<br>
<img alt=css-test-jinja.png src="testing-images/css-test-jinja.png" width=35%>
<img alt=css-test-success.png src="testing-images/css-test-success.png" width=35%>

## Issues in development

# Testing for User Stories

User Stories can be found in [The README.md UX](insert readme.md)

# Responsiveness

## Code Validators and Lighthouse

I used the code validators below and Lighthouse (Chrome Dev Tools):
- [Javascript Beautify Tools Validator](https://beautifytools.com/javascript-validator.php)
- [HTML W3 Validator](https://validator.w3.org/)
- [CSS W3 Validator](http://www.css-validator.org/)

## HTML Validator:

## CSS Validator:

## Javascript Validator:

## Lighthouse:

# Deployment 

I started the project by creating a repository in GitHub and used the Gitpod IDE to write the code. I deployed the app to Heroku early on in the production of the app. I 
There were no issues or problems during the heroku deployment process. 
To deploy the Nutri-smooth web application, I used Heroku. Here is a step-by-step account of the process. 
1. I started by creating a requirements.txt to list all of apps and dependencies required to run the site. 
2. In the Gitpod terminal I used the command 'echo web: python app.py > Procfile' to create a Procfile for Heroku to to read the app.py file.
3. I logged into Heroku and created a new app, calling it 'nutri-smooth' to match the GitHub repository and the title/logo of the site.
4. I then chose automatic deployment from my GitHub repository, specifying the 'nutri-smooth' repo-name.
5. Once found, I connected it to my app. 
6. Before enabling the automatic deployment, I entered the configuration variables (hidden from Heroku inside the env.py file). This included the IP address, port, the secret key (generated using randomkeygenerator.com) a link to MongoDB and the 'nutri_smooth' database. 
7. Before deploying the site, I went back to Gitpod and committed the Procfile and requirements.txt.
8. Going back to Heroku, I enabled the automatic deployment and deploy branch. Heroku then built the app and successfully deployed it.

## Bugs discovered after deployment

## 1. 
## 2. 

# Browser Tests

After deployment, I tested the site on Safari, Firefox and Microsoft Edge...