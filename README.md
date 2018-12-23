# Dictionary Iteration Practice

### The goal

In this lab, you'll start to deal with dictionaries that organize data more and more clearly. We'll start with a list of favorite books, but each book is keyed to a person's name.

For example, to print Zara's favorite book, you'd use the code `print(favorite_books["zara"])`.

Open up iterate.py, code out solutions to the challenges, and enter the command `python iterate.py` in the console when you're ready to run it.

### Tips, examples, & answers

Iteration for a dictionary is really similar to iteration for a list. Here's an example:

```Python

  treatments = {
    "sunburn": "apply some aloe vera",
    "dehydration": "drink some water",
    "headache": "drink some water and consider taking a pain-reliever"
  }

  # Whatever you put first in the pipes will be the name we use to refer to the keys. The second will refer to the values.
  treatments.each do |issue, remedy| # You're naming these internal variables. You can call them whatever you want, but the more descriptive your internal variables, the easier they are to use.
    puts "If you're suffering from #{issue}, you should probably #{remedy}."
  end

```

If you need a boost, you can see answers to challenge 1 and challenge 3.

<details>
  <summary> Click to see a solution to challenge 1 </summary>

  ```Ruby

    # Reassign values for a key in a hash the same way we replace items in an array:
    favorite_books[:jeff] = "The Martian"
    # You can print it out to check whether it works by also including this line of debugging code:
    puts favorite_books[:jeff]

  ```

</details>
<br>

<details>
  <summary> Click to see a solution to challenge 3 </summary>

  ```Ruby

  favorite_books.each do |person, book|
    person_as_string = person.to_s.capitalize # You can still print the information without this line of code, but it looks much prettier as a string and capitalized.
    puts "#{person_as_string}'s favorite book is#{book}"
  end


  ```

</details>
<br>
