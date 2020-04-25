# Virtual Economics

## Welcome

`virtual-econ.info` is intended to store various virtual conferences, seminars, talks, and resources while many of us are sequestered at home. Hat tip to [Luke Stein](https://twitter.com/lukestein) for the initial resources and the suggestion to build the website.

## How to add your calendar

If you have a Google calendar or iCal link, you can add your calendar to the master list. A Python script runs every night at midnight and retrieves all calendars from the file `calendar_sources.txt`. 

Steps: 

1. Get a URL that points to your calendar -- the URL should end with `.ics`. If you are using Google Calendars, you can look at [this picture](calendar-example.png) to see where to click. Search on how to get this link for your calendar provider if you are not using a Google calendar. As an example, the URL for the website's calendar is

    ```
    https://raw.githubusercontent.com/cpfiffer/virtual-econ.info/master/virtual-econ-calendar.ics
    ```

2. Edit the file `calendar_sources.txt` in this repo, and stick your URL at the bottom of the list. Here's a [handy link](https://github.com/cpfiffer/virtual-econ.info/edit/master/calendar_sources.txt) to do so.

3. Click the "Propose file change" button at the bottom of the page.

4. Wait for someone to accept your changes.

## How to contribute

You can contribute information to this website by opening a pull request on GitHub repository for [this page](https://github.com/cpfiffer/virtual-econ.info) to edit any of the various webpages you see here. Each page has its own handy "Edit me" button if you want to quickly add something to a list.

## Support or Contact

Contact the maintainer of this page by emailing [cpfiffer@gmail.com](mailto:cpfiffer@gmail.com) or by tweeting [@cameron_pfiffer](https://twitter.com/cameron_pfiffer).
