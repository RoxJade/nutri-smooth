<img alt=responsive-1.png src="testing-images/responsive-1.png" width=100%>

# Nutri-Smooth

[Visit site Nutri-Smooth](http://nutri-smooth.herokuapp.com/index)

The aim of the Nutri-Smooth site is to encourage users to share a range of healthy, nutritious and tasty smoothie recipes. The site showcases a selection of smoothie recipe's, breaking down ingredients and macro-nutrients for each. 
Nutri-Smooth is a web application allowing users to create, read, update and delete their own smoothie recipes. It also allows users to search for recipes.
Nutri-Smooth has been created using a variety of languages including HTML, CSS and Python and uses MongoDB to store data.

# Contents
1. [UX](#UX)
2. [Wireframes and Mockups](#Wireframes-and-Mockups)
3. [Features](#Features)
4. [Technologies Used](#Technologies-used)
5. [Credits](#Credits)

Testing and Deployment can be found in a separate file:
[Testing & Deployment](https://github.com/RoxJade/nutri-smooth/blob/master/TESTING.md)

# UX

## User
Target Audeience/User Profile
- The site could be aimed at a wide range of ages, from 16 and above depending on the audience's interest in smoothies. 
- As the site will be designed to enable the user to store smoothie recipes as a digital recipe book, it's functionality is most likely to be utilised by people aged 28+.
- The audience is likely to lead a family lifestyle and maybe male or female with an interest in using mobile technology such as tablets and phones. They will appreciate the ability to store, save and revisit their digital recipe book. 
- They will have an invested interest in their health, food and nutrition and an active lifestyle.
- As the site will include a wide variety of smoothie types, including protein-based, some users may have an interest in an active lifestyle, sports or regularly attending the gym.

## User stories/User goals

1. As a user I want to be able to add and store my own smoothie recipes.
2. As a user I want to be able to read through my own smoothie recipes, share them with the community and read recipes added by others to gain inspiration and recreate them.
3. As a user I may wish to change a recipe or update it's ingredients.
4. As a user, I may wish to delete recipes I am no longer like.
5. As a user, I would like to be able to search for different smoothie recipes or ingredients for inspiration.
6. As a user, I want to be able to mark my favourite recipes and access these quickly.
7. As a user, I want the design of the site to be aesthetically appealing with clear navigation and a sense of calm and colour.
8. As a user I would like to know the breakdown of the nutrition or health benefits in the recipes so I can make informed, healthy choices.
9. As a returning user, I would like to access all of my added smoothies on my own personal profile.
10. As a user, I want the option to add minimal information to my smoothie recipes if I wish.
11. As a user, I want the option to add lots of information and imagery to my smoothie recipes if I wish.
12. As a simple recipe book, I would like the site to be easy and quick to navigate around. 
13. As a user, I want the site to be responsive, especially for mobile and tablet as I will probably be creating smoothie recipes from a mobile device in the kitchen.

## Scope
- The site will contain a page or individual pages listing all smoothies, these will be available for all site viewers.
- Users will be able to register their details and regularly return to their own profile, add their recipes and view their recipes. 
- Users will be able to add ingredients and nutritional information about the smoothies.
- Users will have the option to add images of their smoothies to go with their recipes.
- Users will be able amend and delete their added smoothie recipe information.
- Unless users are registered and signed in, they will not have the option to create, edit or delete smoothies.
- All users will be able to search for smoothies, via ingredients.
- Admin will be able to view all smoothies, delete all smoothies (if necessary), create and delete smoothie categories.
- Depending if time allows within development, there may be a feature to allow users to rate smoothies.

## Structure & Skeleton
**Data structure**

In MongoDB, I will create a 3 collections to capture and contain **user data, smoothie recipe data and smoothie category data**. Below is a an outline of how the data will be structured and where it links together. 
<br>
<img alt=data-structure.png src="testing-images/data-structure.png" width=70%>
<br>

**Site structure**

Below is a basic structure of the main site navigation
<br>
<img alt=site-structure.png src="testing-images/site-structure.png" width=90%>
<br>

## Surface design

**Inspiration and Research**
I drew inspiration for the site from research on [pinterest](https://pinterest.com), [current website trends](https://99designs.co.uk/blog/trends/web-design-trends/) and [dribbble](https://dribbble.com/shots/6492236-Balosto?utm_source=Pinterest_Shot&utm_campaign=Podavalkin&utm_content=Balosto&utm_medium=Social_Share).
I was inspired by the impact of a 'parallax' feature and the 'comfortable colours' in the website trends article on 99 designs. 
**Colour Theme**
I developed a calm colour theme, inspired by a web-trend article and blended-smoothie colours. I decided to use colours mainly from the Materialize colour sets for ease of design and consistency throughout the site.
<br>
<img alt=colour-palette.png src="testing-images/colour-palette.png" width=50%>
<br>

**Logo Development**
I initially designed a basic logo on Adobe Illustrator and saved as an SVG file (for great resolution and low file size). Further on down the line of developing the site, I decided to edit this to a more eye-catching design that tied in with my chosen fonts.
<br>
<img alt=logo-dev.png src="testing-images/logo-dev.png" width=50%>
<img alt=two-logos.png src="testing-images/two-logos.png" width=25%>
<br>

# Wireframes and Mockups
Below is a selection of wireframe designs for desktop, mobile and tablet. All pages primarily with forms will not be altered dramatically for different screen sizes unless necessary. The main pages that will display differently include the index page and the smoothie recipe page.
<br>
<img alt=wire-1.png src="testing-images/wire-1.png" width=50%>
<img alt=wire-2.png src="testing-images/wire-2.png" width=50%>
<img alt=wire-3.png src="testing-images/wire-3.png" width=50%>
<img alt=wire-4.png src="testing-images/wire-4.png" width=50%>

# Features
<img alt=responsive-1.png src="testing-images/responsive-1.png" width=50%>


## Home/Index page

-Navbar
    - Navbar displays the Nutri-Smooth logo (which contains a home page link)
    - Links in navbar displayed to site visitor include: Home, Smoothies, Sign In and Register. Links in navbar displayed to registered/returning user include: Add Smoothie and Profile (but remove)
    - Sign In is an icon, a tooltip will occur when hovered over 'Sign in?'
    - On mobile and tablet screens, the navbar converts a side nav and a 'hamburger' icon menu appears on the left side dropdown with the same links.



## Additional considerations and features to implement in the future

1. Adding a private profile feature
2. Adding a 'suggested search' function or recommendenations based on user preferences
    - Increase interactivity by Add a star rating / likes counter and community engagement by requesting mini-smoothie reviews from users trying out shared smoothie recipes.
    - Turn the admin user into a 'superuser' by using the database
    - Give detailed instructions on how to add images url's for users who may not know how to do this

# Technologies Used

- [Adobe Illustrator](https://www.adobe.com/uk/products/illustrator.html) Used the deisgn and mockups.
- [Gitpod and Github](https://github.com/RoxJade/) All code and files created in Gitpod, repository in Github.
- [Heroku](https://www.heroku.com/home)Site deployed on Heroku.
- [MongoDB]() Document oriented database used to store data
- Flask()
- HTML
- CSS
- [JQuery]().
- [Google fonts]() . 
- [Font Awesome](https://fontawesome.com/) Used to add the 'star' icons for the rating system.
- [Weukzeug]() Used to add security to user passwords and debug code whlst in production.

# Credits
## Content
The design of the site was created by myself, including logo design.
A list of the resources are below:

## Javascript resources and research
- [Code Institute - Back End Development Module]()

## Additional resources and research
- [Stack Overflow](https://stackoverflow.com/)
- [W3 Schools](https://www.w3schools.com/)
- [CDNJS](https://cdnjs.com/)
- [Slack](https://app.slack.com/)

## Media

- [Unsplash](https://unsplash.com/)

## Acknowledgements
I received inspiration for ideas, colour palette and design of this project from: 
- [My Protein](https://www.myprotein.com/)
- []()
- []()
- [](https://dribbble.com/shots/6492236-Balosto?utm_source=Pinterest_Shot&utm_campaign=Podavalkin&utm_content=Balosto&utm_medium=Social_Share)
[pinterest](https://pinterest.com), [current website trends](https://99designs.co.uk/blog/trends/web-design-trends/) and [dribbble](https://dribbble.com/shots/6492236-Balosto?utm_source=Pinterest_Shot&utm_campaign=Podavalkin&utm_content=Balosto&utm_medium=Social_Share).