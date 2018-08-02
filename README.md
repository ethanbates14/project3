# Project 3

Django - Pinnochios Pizza Restaurant

0) Some base resources across whole project
-- main.css - used for base html template and extending style project wide
-- mainly bootstrap grids with some google fonts, custom CS, and custom JavaScript

1) Users Application
-- Utilizes built in authentication and login from Django
-- Login and Logout Pages Passing Message to templates
-- Registration Page has logic to check if user already exists - creates if passes checks
-- Routes to user home page - with data about previous orders, and information about Pinnochios
-- Registration and Login have Jinja logic if user is already logged in

2) Orders Application
-- Two main views - index and checkout - index is the base menu that contains most of the data models, checkout controls submitted orders
-- Data Array send dictionary to front end - Catgory -> Items -> query strings of prices and topping options
-- Index template uses Jinja to Loop through key value pairs - building items with Modals for ordering options
-- The driver here is Prices Model - as it is the most granular/ unique element from the menu
-- Users can only see their orders unless admin
-- menuorders.JS -is the main driver on the index page - Logic -> grab the modal for the element that is being selcted, and grab what is checked
-- pass that data to the checkout cart - append to cart and add to total
-- Form sends data to Checkout Page, then added to DB
-- [admin|cs50superuser] -- for Django Admin Page