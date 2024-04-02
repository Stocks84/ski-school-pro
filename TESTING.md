# Testing

> [!NOTE]  
> Return back to the [README.md](README.md) file.

## Code Validation

### HTML

I have used the recommended [HTML W3C Validator](https://validator.w3.org) to validate all of my HTML files.

| Directory | File | Screenshot | Notes |
| --- | --- | --- | --- |
| booking | booking_form.html | ![screenshot](documentation/validation/booking_form.png) | |
| booking | home.html | ![screenshot](documentation/validation/home.html.png) | |
| booking | instructor_list.html | ![screenshot](documentation/validation/instructor_list.png) | |
| booking | instructor_profile.html | ![screenshot](documentation/validation/instructor_profile.png) | |
| booking | lesson_list.html | ![screenshot](documentation/validation/lesson_list.png) | |
| booking | login_form.html | ![screenshot](documentation/validation/login_form.png) | |
| booking | registration_form.html | ![screenshot](documentation/validation/registration_form.png) | |

### CSS

I have used the recommended [CSS Jigsaw Validator](https://jigsaw.w3.org/css-validator) to validate all of my CSS files.

| Directory | File | Screenshot | Notes |
| --- | --- | --- | --- |
| static | styles.css | ![screenshot](documentation/validation/css_styles.png) | |

### JavaScript

I have used the recommended [JShint Validator](https://jshint.com) to validate all of my JS files.

| Directory | File | Screenshot | Notes |
| --- | --- | --- | --- |
| static | script.js | ![screenshot](documentation/validation/script_js.png) | |

### Python

I have used the recommended [PEP8 CI Python Linter](https://pep8ci.herokuapp.com) to validate all of my Python files.

| Directory | File | CI URL | Screenshot | Notes |
| --- | --- | --- | --- | --- |
| booking | admin.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Stocks84/ski-school-pro/main/booking/admin.py) | ![screenshot](documentation/validation/admin.png) | |
| booking | context_processors.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Stocks84/ski-school-pro/main/booking/context_processors.py) | ![screenshot](documentation/validation/context.png) | |
| booking | forms.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Stocks84/ski-school-pro/main/booking/forms.py) | ![screenshot](documentation/validation/forms.png) | |
| booking | models.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Stocks84/ski-school-pro/main/booking/models.py) | ![screenshot](documentation/validation/models.png) | |
| booking | urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Stocks84/ski-school-pro/main/booking/urls.py) | ![screenshot](documentation/validation/urls.png) | |
| booking | views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Stocks84/ski-school-pro/main/booking/views.py) | ![screenshot](documentation/validation/views.png) | |
|  | manage.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Stocks84/ski-school-pro/main/manage.py) | ![screenshot](documentation/validation/manage.png) | |
| ski_school | settings.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Stocks84/ski-school-pro/main/ski_school/settings.py) | ![screenshot](documentation/validation/settings.png) | |
| ski_school | urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Stocks84/ski-school-pro/main/ski_school/urls.py) | ![screenshot](documentation/validation/ski_urls.png) | |

## Browser Compatibility

I've tested my deployed project on multiple browsers to check for compatibility issues.

| Browser | Home | About | Contact | etc | Notes |
| --- | --- | --- | --- | --- | --- |
| Chrome | ![screenshot](documentation/browsers/browser-chrome-home.png) | - | Works as expected |
| Firefox | ![screenshot](documentation/browsers/browser-firefox-home.png) | - | Works as expected |
| Safari | ![screenshot](documentation/browsers/browser-safari-home.png) | - | Works as expected |

## Responsiveness

I've tested my deployed project on multiple devices to check for responsiveness issues.

| Device | Home | Notes |
| --- | --- | --- |
| Mobile (DevTools) | ![screenshot](documentation/responsiveness/responsive-mobile-home.png) | Works as expected |
| Tablet (DevTools) | ![screenshot](documentation/responsiveness/responsive-tablet-home.png) | Works as expected |
| Desktop | ![screenshot](documentation/responsiveness/responsive-desktop-home.png) | Works as expected |

## Lighthouse Audit

I've tested my deployed project using the Lighthouse Audit tool to check for any major issues.

| Page | Mobile | Desktop | Notes |
| --- | --- | --- | --- |
| Home | ![screenshot](documentation/lighthouse/lighthouse-home-mobile.png) | ![screenshot](documentation/lighthouse/lighthouse-home-desktop.png) | Some minor warnings |
| Instructors | ![screenshot](documentation/lighthouse/lighthouse-instructors-mobile.png) | ![screenshot](documentation/lighthouse/lighthouse-instructors-desktop.png) | Some minor warnings |

## Defensive Programming

Defensive programming was manually tested with the below user acceptance testing:

| Page | Expectation | Test | Result | Fix | Screenshot |
| --- | --- | --- | --- | --- | --- |
| All Pages | | | | | |
| | Social Icons in the footer is expected to open a new window to the social media site when the user clicks on the icon | Tested the feature by clicking the icons | The feature behaved as expected. | Test concluded and passed | ![screenshot](documentation/testing/testing01.png) |
| | Navigation bars is expected to have line appear underneath when the cursor hovers and then take the user to the designated page on the site when the user clicks on the page they want | Tested the feature by hovering the cursor and then clicking on the links | The feature worked as expected | Test concluded and passed | ![screenshot](documentation/testing/testing02.png) |
| | Search bar is expected to have a list of instructors and once chosen click search to head to the bio page | Tested the feature by using the drop down menu and then clicking search | The feature worked as expected | Test concluded and passed | ![screenshot](documentation/testing/testing03.png) |
| Lessons page & Booking page without login | | | | | |
| | User login screen is expected to appear and restrict the user from accessing the page when the user tries to view the page without logging in | Tested the feature by trying to access the page without a logging in | The feature behaved as expected | Test concluded and passed | ![screenshot](documentation/testing/testing04.png) |
| Register page | | | | | |
| | Register for login is expected to redirect to the home page with a success confirmation message when the user puts all the correct information into the fields | Tested the feature by doing registering the correct details | The feature behaved as expected | Test concluded and passed | ![screenshot](documentation/testing/testing05.png) |
| | If the required field is missing or not filled in correctly it is expected to come up with a message to fill or enter the correct information when the user does not fill the required fields properly | Tested the feature by entering the wrong data | The feature behaved as expected | Test concluded and passed | ![screenshot](documentation/testing/testing06.png) |
| Login page | | | | | |
| | Login is expected to redirect to the home page with a welcome back message when the user logins correctly | Tested the feature by logging in as a student | The feature behaved as expected | Test concluded and passed | ![screenshot](documentation/testing/testing07.png) |
| Instructor profile page | | | | | |
| | Restricted access for student is expected to redirect to the home page with a ‘you are not allowed access’ message when the user puts the correct url in| Tested the feature by putting the private url in, signed in as a student | The feature behaved as expected | Test concluded and passed | ![screenshot](documentation/testing/testing08.png) |
| | Gain access as Instructor & be able to edit or delete their profile by logging in with the correct instructor log in | Tested the feature by entering the correct instructor log in| The feature behaved as expected | Test concluded and passed | ![screenshot](documentation/testing/testing10.png) |
| | Instructor allowed to edit their bio is expected to have a success message when the instructor saves the new edit | Tested the feature by saving the edited bio | The feature behaved as expected | Test concluded and passed | ![screenshot](documentation/testing/testing11.png) |
| | Delete profile is expected to have alert message pop up to confirm in the instructor want to delete the profile when they click the delete button | Tested the feature by putting the private url in, singed in as a student | The feature behaved as expected | Test concluded and passed | ![screenshot](documentation/testing/testing12.png) |
