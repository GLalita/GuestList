# GuestList
From a JSON formated file listing customer data, including names, user IDs, and location coordinates, this program determines a "guest list" of customers within a certain distance of the target coordinates.

## Run

Download repository as a zip file. Save to computer in the desired directory. Open terminal and change to the appropriate directory. Run the script by entering 'python3 CustomerParse.py' (if Python version 3.0 or later)

## Overview

The program target coordiantes are set to be (37.788802,-122.4025067), the GPS coordinates of the Intercom SF Office. Customers will be included on the guest list (output to InviteList.txt) if they are within 100km from the Office. InviteList.txt is sorted in ascending order of UserID.

## Testing

Unit testing run with 
'python3 testInvites.py'

