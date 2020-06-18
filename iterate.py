import address_book

# Here's a small dictionary of favorite books, each keyed to a different person.
favorite_books = {
  "diana": "Crime and Punishment",
  "sophie": "The Secret History",
  "cory": "Fahrenheit 451",
  "gabe": "The Hobbit",
  "danny": "Lonesome Dove",
  "dan": "Don Quixote",
  "katie": "10:04",
  "zara": "Rebecca",
  "david": "The Sun Also Rises",
  "alexandra": "Hyperbole and a Half",
  "martin": "The House on Mango Street",
  "jeff": "The Hitchhiker's Guide to the Galaxy"
}

# 1. Print out Martin's favorite book.



# 2. Print out Alexandra's favorite book.




# 3. Before we get started, let's adjust a few things. First off, Jeff just read a new book called "The Martian" and loved it. With just one line of code, change Jeff's favorite book to "The Martian"



# 4. Print out Jeff's favorite book to confirm that the change was successful.




# 5. We should also add Ronald to the list. His favorite book is "Lies my History Teacher Told Me."
#    Add that info to the dictionary as a new key-value pair.



# 6. Confirm that Ronald's book was added by printing it out.




# 7. Now let's start iterating. For each person in the dictionary, print out a statement that says "___'s favorite book is ____" and fill in the blanks with that person's name and that person's favorite book.





# LEVEL 2: In the address_book.py file, there's a list called "contacts" with 100 dictionaries inside of it. Each dictionary representes a person, and has that person's name, phone number, email, the company they work for, and their address.
#    That means you could print the 7th person's email using this line of code:
#    print(address_book.contacts[6]["email"]) # Uncomment this to see if it works. (Remember, list indexing starts at zero, so we use the number 6 to access the 7th name).

# 8. Print the address book.




# 9. Print out the fifth person from the the address book.




# 10. Print out the email of the 10th person from the address book.



# 11 Print out the name of the first person from the address book.



# 12. Print out the name and phone number of the first person in the address book in the following format:
#    "_____ can be reached at ______" filling in the blanks with the person's name and phone number.






# 13. Print out the same information "_____ can be reached at ______" with names and phone numbers for all 100 of our contacts.






# 14. We're going to send a mass text to all our contacts, so we need everyone's phone number. Our texting program can do it in an instant if we put all the numbers into a list.
#    Create a list called phone_numbers, iterate over our contacts, and add each person's number to that list. Print out the list when you're done to check your work.






# 15. If we wanted to send an email that was only useful for college students and their professors, we could send that email ONLY to folks in our contacts whose email addresses end in ".edu".
#    Create a list called edu_emails and put every .edu email address from our contacts into that list. Print the list when you're done to check your work.
