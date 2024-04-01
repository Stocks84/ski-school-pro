# [SKI SCHOOL PRO](https://ski-school-pro-2-4db020aae0bc.herokuapp.com)

The Ski School Pro (SKP) is a simple booking online project. It is based on a fictional small ski school that could be based anywhere in Europe! It is designed for instructors and customers alike. For the customers they can move around the site fluidly and see who the instructors are and book a ski lesson safely. For the instructors they can see which lessons they have, they also be able to alter their own bio’s. Please see the UX section for more details.

[![GitHub commit activity](https://img.shields.io/github/commit-activity/t/Stocks84/ski-school-pro)](https://github.com/Stocks84/ski-school-pro/commits/main)
[![GitHub last commit](https://img.shields.io/github/last-commit/Stocks84/ski-school-pro)](https://github.com/Stocks84/ski-school-pro/commits/main)
[![GitHub repo size](https://img.shields.io/github/repo-size/Stocks84/ski-school-pro)](https://github.com/Stocks84/ski-school-pro)

![screenshot](documentation/mockup.png)

source: [amiresponsive](https://ui.dev/amiresponsive?url=https://ski-school-pro-2-4db020aae0bc.herokuapp.com)

## UX

For the SKP design I had to consider the USER’S needs:
-	Website to be simple,
-	Easily fluid to get around the site,
-	Keep their data secure,
-	Option for the owner to have an administration section private only for the owner,
-	Implement CRUD design features & where needed defensive programming.


### Colour Scheme

With the colour scheme I used a combination of soft greys and blues to enhance the feeling of the cool winter season.

### Typography

I used the default Font from Bootstraps, as it stands out quite nicely. (Subject to change due time constrictions). I used the Font Awesome icons for the social media icons and altered the colours to reflect the colour scheme throughout the site. 

- [Font Awesome](https://fontawesome.com) icons were used throughout the site, such as the social media icons in the footer.

## User Stories


### Ski Instructor

-	As a ski school instructor, I can be able to view my teaching schedule and see details of upcoming lessons, including student information and skill levels so that I am able to cater to my client.

### Student

-	As a ski school student, I can be able to book a lesson by providing my personal details and preferences so that so that I can get the lesson I need.
-	As a ski school student, I can be able to browse available lessons and view details so that I can make informed decision.
-	As a ski school student, I can be able to view my upcoming lessons and any relevant information, or updates related to them. Additionally, I want to have the ability to cancel my appointment if needed so that I can have some flexibility

### Site Admin

-	As a ski school administrator, I can be able to manage lesson availability, including adding new lessons, modifying existing ones, and cancelling lessons if necessary so that have a overview on what is going on in the ski school

## Wireframes

To follow best practice, wireframes were developed for desktop sizes.
I've used [Balsamiq](https://balsamiq.com/wireframes) to design my site wireframes.

### Desktop Wireframes

Home
  - ![screenshot](documentation/wireframes/desktop-home.png)


## Features

### Existing Features

- **Social Icons-#1**

    - Once clicked on opens a new window for the user to visit SKP social media sites which improves interactivity and promotion.

![screenshot](documentation/features/feature01.png)

- **User Registration-#2**

    - The user is allowed to register so that they can eventually be able to login and potentially book a lesson and access membership areas of the website.

![screenshot](documentation/features/feature02.png)

- **Registration Successful-#3**

    - Gives the User acknowledgement that their registration was a success. Allows them to proceed to login.

![screenshot](documentation/features/feature03.png)

- **Restricted Access to Lesson or Booking Page-#4/5**

    - If the User is not logged on that User can not view the lessons or Booking page and is invited to register and then login.

![screenshot](documentation/features/feature04.png)
![screenshot](documentation/features/feature05.png)


- **Welcome Back-#6**

    - The user is given a welcome back message to confirm the success of the login. Also for added clarity their user name is now in the navigation bar in the top right corner and a logout button has been introduced.

![screenshot](documentation/features/feature06.png)

- **Restricted access to the instructor Bio’s-#7**

    - If a non-instructor manages to gain access to the instructor/profile page a message will appear on the redirected home page and ask them to book a lesson instead.

![screenshot](documentation/features/feature07.png)

- **Access to lesson list-#8**

    - Now the user has access to the lesson list, and see what lessons are available to them and with instructor.

![screenshot](documentation/features/feature08.png)

- **Access to booking form-#9**

    - The user can now select a lesson from the dropdown menu. Also, they are required to put their username to complete the booking.

![screenshot](documentation/features/feature09.png)

- **Booking confirmation-#10**

    - Once a lesson is submitted the User is redirected to the home page with a message confirming their booking.

![screenshot](documentation/features/feature10.png)
- **Access to lesson list-#11**

    - In the navbar in the Top right-hand corner there is a search ski instructor that will only display instructors. Once selected will take the user to the instructor bio.

![screenshot](documentation/features/feature11.png)

- **Access to booking form-#12**

    - The website works on a mobile/tablet device and the navigation bar transforms into a drop-down menu for convenience.

![screenshot](documentation/features/feature12.png)

- **Instructor Profile-#13**

    - The instructor can update their ‘bio’ or if they no longer want to be part of the ski school have the option of deleting their whole profile.

![screenshot](documentation/features/feature13.png)

- **Change Bio-#14**

    - Once bio is updated a success message is supplied to confirm the changes. 

![screenshot](documentation/features/feature14.png)

- **Delete Bio-#15**

    - The instructor can delete their whole profile as well but using defensive programming a message pops asking the instructor if they are sure they want to delete their profile.

![screenshot](documentation/features/feature15.png)

