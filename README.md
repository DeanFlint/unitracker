# Unitracker - Project 4

[![Build Status](https://travis-ci.org/DeanFlint/unitracker.svg?branch=master)](https://travis-ci.org/DeanFlint/unitracker)

## Getting Started

Unitracker is a web application that allow users to report bugs, request features and view the details of each ticket.
The user can create an account, login, logout and view their profile. There is functionality to allow users to reset their password if needed. 

There are two types of tickets a user can submit. Bugs are available for any user to create and they also have the option to upvote other bug tickets. The developers are Unitracker will spend 50% of their time each working on the highest voted tickets. As developers are working on each ticket, they have the ability to change the status of the ticket (which include; 'to do', 'in progress' and 'done') which users can then see. 

The other type of ticket is a feature ticket. All users can view feature tickets however, only users that have donated £30 or more can post new feature tickets and upvote current feature tickets. The developers will spend the other 50% of their time each week working on feature tickets. Users have the functionality to donate however, it's not required if they only need to create bug tickets.

Users can order the view of both of the ticket types by name of ticket or status but by default, they are ordered by newest ticket submitted.

This app is written using Django, HTML, CSS and Javascript. It used Stripe as a means of allowing the user to donate and uses a sqlite and postgres database (depending on which environment is being used.)



## Prerequisites

Some the tech used includes:

- [Django](https://www.djangoproject.com/)
    - I used **Django** to handle page routing and manage the majority of the functionality on the app.
- [Bootstrap](http://getbootstrap.com/)
    - I used **Bootstrap** to give my project a simple, responsive layout
- [npm](https://www.npmjs.com/)
    - I used **npm** to help manage some of the dependencies in our application
- [gulp](https://gulpjs.com/)
    - **Gulp** is used to manage the tasks of running the scss and moving files from Node Modules to my project folders.
- [font-awesome](http://fontawesome.io/)
    - I used **font-awesome** to include images for icons.
- [Google Fonts](https://fonts.google.com/) 
    - **Google Fonts** is used to style the text in my site.
- [Stripe](https://stripe.com/gb) 
    - **Stripe** is used to manage the user donations.


## WireFrame

Click [here](wireframe.pdf) to view the wireframe of this project.

## To initilise and edit

1. Download Python 3: (http://www.python.org/download/)

2. Clone the repository 

``` $ git clone https://github.com/DeanFlint/unitracker.git```

3. Move into the folder

``` cd unitracker ```

4. After you've that you'll need to make sure that you have **npm** installed. You can get **npm** by installing Node from [here](https://nodejs.org/en/)

``` $ npm install ```

``` $ npm start ```


5. Create and activate your virtual env:

``` $ python -m venv env ```

``` $ source env/Scripts/activate ```

6. Install requirements with pip:

``` (env)$ pip install -r requirements.txt ```


7. Open unitracker, settings.py and amend the following:

``` SECRET_KEY = "whatever password you like" ```

8. Amend the ALLOWED_HOSTS to whatever IP you're using. For example, if localhost, use 127.0.0.1

``` ALLOWED_HOSTS = [os.environ.get('C9_HOSTNAME'), 'unitracker.herokuapp.com', '127.0.0.1'] ```

``` app.run(host=os.getenv('IP'), port=5005, debug=True) ```

9. Migrate the database settings:

``` python manage.py migrate ```

10. Finally, run the following:

``` python manage.py runserver ```



End with an example of getting some data out of the system or using it for a little demo

## Running the tests

### Break down into end to end tests

Explain what these tests test and why

```
TO DO
```

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Authors

* **Dean Flint** - *Initial work* - [Dean Flint](https://github.com/DeanFlint)


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* The good people at CodeInstitute!

* Derek Hyland