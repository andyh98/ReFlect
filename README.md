**Name**: Andy Hameed

**Online Demo**: https://murmuring-forest-00201.herokuapp.com/

**Project Title**: ReFlect

**License**: [MIT Licence](LICENSE.md)

# ReFlect
Have you ever struggled with organizing a daily journal? Got stuck thinking of a topic to write about? ReFlect is a web app built to make the habit of journaling less daunting to pick up. With ReFlect, you'll be able to create journal entries anytime and anywhere. This app was created using the Flask microframework on top of a PostgreSQL database, all of which is built and hosted on Heroku. 

# Features

## ReFlect Account

Users can register for an account to gain access to journal entry and modification features. One registration is successful, the user can log on to their dashboard and view, enter and delete journal entries as they wish.

## Dashboard

Once logged in, you will be presented with a Dashboard containing all your existing entries in table row format. Each row contains information about the entry as well buttons for Edit and Delete operations that can be executed on that specific entry. It also allows for creation of new journal entries.

## Entry Creation

The most prominent feature of the dashboard is the journal entry creation feature. Use the green "New Entry" button found at the top of the page to create a new journal entry. The app uses the ckeditor API for flexible text entry fields with a wide range of text tools including font and formatting options.

### Using a Journal Prompt

If you choose to recieve a prompt for you entry, click the "prompt me" button to unviel a thought-provoking prompt that'll get you going on your daily reflection. 

Once you have written your journal entry, a checkbox can be used to indicate whether or not you used the prompt that was provided. Checking this checkbox will allow the app to use JQuery to display the prompt along with your entry when viewing the journal entry.

## Entry Modification & Deletion

You can modify your entries on the Dashboard by clicking the "Edit" button on one of the displayed journal entry rows. The deletion process is just as simple with the "Delete" button.

## Viewing Journal Entries 

You can view entries using the "Journal Entries" tab at the top of the page. This will display your entries by title and date, which you can click through to view on a separate page in full detail.

# [Video Demo](https://drive.google.com/file/d/1lNjVF0-yb_n7EoQkf6Vq1HnPhB4ICUrJ/view?usp=sharing){:target="_blank"}

# Credit 

This project was made possible with the help of [Brad Traversy](https://github.com/bradtraversy)'s myflaskapp tutorial as well as [Kirsten Hunter](https://www.linkedin.com/in/synedra)'s "Learning Flask" course offered through LinkedIn Learning.

# License
This code is licensed under the MIT license, approved by Open Source Initiative. For more information, visit [opensource.org](https://opensource.org/licenses/MIT)
