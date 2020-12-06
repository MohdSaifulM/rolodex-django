# ROLODEX - Contacts Management w/ Django

# Task from homework god
Develop a boomer-friendly contacts management app. Decided to put in a bit more effort cause some of us still using ROLODEX(whatever that is)

# Deliverables
1. User should be able to create a contact via a form
1. A page listing all of your contacts
1. A page to show one contact (crap I forgot about this)
1. Edit and Delete a contact

**A lonely start**
<img src="https://i.ibb.co/crywqmx/2020-12-06-16-30.png" width="400">
  - This is where users will land. It'll show the above message if users have yet to add any contacts. Clicking the <i class="material-icons">add</i> icon on the message will bring users directly to the add a new contact page

**Add a new contact**
<img src="https://i.ibb.co/zrYhQ0x/2020-12-06-16-32.png" width="400">
  - My first time using materializecss cause I thought the form was cool. Not the best idea but I wanted to please the homework god.
  - Realized to activate the form you have to either click on the line of the input OR to the left of the label

**Dashboard**
<img src="https://i.ibb.co/gd1LFxH/2020-12-06-16-35.png" width="400">
<img src="https://i.ibb.co/hRwdnZS/2020-12-06-16-37.png" width="400">
  - Users will have a default photo for their contact which they could upload when they feel like editing the contact
  - Actually wanted to have the option to add photo while adding contact but I kept getting a 302 error however just like in our phones, we usually don't add our contact's photo while exchaning numbers so I guess this is making the app abit more realistic
  - Users can edit/add photo by clicking the button on the contact's car
  - Hovering on the card, will give users the option to delete the contact

<img src="https://i.ibb.co/c3D1J2h/2020-12-06-17-09.png" width="400">
<img src="https://i.ibb.co/XkJLcz4/2020-12-06-17-09-1.png" width="400">
  - From the dashboard, users can also start a search, where it'll filter the people on the app according to their name, email and contact number
  - However, if there is no matching results, it'll return an error message

<img src="https://i.ibb.co/ypvfpmq/2020-12-06-16-41.png" width="400">


**Technologies used:** <br>
- django, python
- psycopg2-binary
- django-widget-tweaks (for the forms)
- pillow
- django-filter
- materializecss

<img src="https://i.pinimg.com/originals/e7/e7/02/e7e7021ea20cfc722b8e4d8cea343361.jpg">

<h1><a href="https://www.starwars.com/databank/darth-vader">JOIN THE DARK SIDE</a></h1> 













