# Dictionary Iteration Practice

[![Run on Repl.it](https://repl.it/badge/github/upperlinecode/dictionary-iteration-mini-lab-python)](https://repl.it/github/upperlinecode/dictionary-iteration-mini-lab-python)

### The goal

In this lab, you'll start to deal with dictionaries that organize data more and more clearly. We'll start with a list of favorite books, but each book is keyed to a person's name.

For example, to print Zara's favorite book, you'd use the code `print(address_book.favorite_books["zara"])`.

Open up iterate.py, code out solutions to the challenges, and enter the command `python iterate.py` in the console when you're ready to run it.

### Tips, examples, & answers

Iteration for a dictionary is really similar to iteration for a list. Here's an example:

```Python

  treatments = {
    "sunburn": "apply some aloe vera",
    "dehydration": "drink some water",
    "headache": "drink some water and consider taking a pain-reliever"
  }
  
  for issue in treatments: # You're naming this internal variable (issue in this case). You can call it whatever you want, but the more descriptive your variable names, the easier they are to use.
    print("If you're suffering from " + issue + ", you should probably " + treatments[issue] + ".") # Since the issue variable is only taking on the value of keys from the tratements dictionary, we need to use bracket notation to get the matching remedy for each issue.

```

If you need a boost, you can see answers to challenge 1 and challenge 3.

<details>
  <summary> Click to see a solution to challenge 1 </summary>

  ```Python

    # Reassign values for a key in a dictionary the same way we replace items in a list:
    favorite_books["jeff"] = "The Martian"
    # You can print it out to check whether it works by also including this line of debugging code:
    print(favorite_books["jeff"])

  ```

</details>
<br>

<details>
  <summary> Click to see a solution to challenge 3 </summary>

  ```Python
  for person in favorite_books:
    capitalizedPerson = person.capitalize()
    print(capitalizedPerson + "'s favorite book is " + favorite_books[person])


  ```

</details>
<br>
