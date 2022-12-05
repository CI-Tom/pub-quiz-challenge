
# Pub Quiz Challenge

## Overview
A Python terminal game for uesers to test their knowledge in 5 areas: -

- Science
- Sports
- Movies & TV
- Music
- History

Game developed by Tom Manahan for Code Institute Project Portfolio 3 using Python.

[Live Game Link](https://pub-quiz-challenge.herokuapp.com/)

![Home Screen](assets/images/Quiz%20Start%20Screen.PNG)

## Table of contents

1.  [How to play](#how-to-play)

2.  [Project Goals](#project-goals)
    - [Main Goals](#main-goals)
    - [Target Audience](#target-audience)

3.  [Features](#features)
    - [Start Screen](#welcome-screen) 
    - [Bet Input](#bet-input)
    - [Main Game Screen](#main-game-screen)

4.  [Future Features](#possible-future-features)

5.  [Technologies](#technologies)
    - [Platforms](#platforms)
    - [Python Modules](#python-modules)

6.  [Flow Chart](#flow-chart)

7.  [Testing](#testing)
    - [Validator Testing](#validator-testing) 
    - [Testing User Stories](#testing-user-stories)
    - [Function And Bug Testing](#function-and-bug-testing)

8.  [Deployment](#deployment)   

9. [Credits](#credits)

10. [Acknowledgements](#acknowledgements)

## How to play 
The Pub Quiz Challenge is a basic terminal game designed to test user's knowledge in the style of a pub quiz.

There are five ares of expertise to choose from. 

At the the start of the game the user is presented with the welcome screen and asked to enter their name.

Once a name is entered, the user must then select form the list of five topics to start the game.

The game presents the user with a question and three options to choose from for the answer.

The user must select an answer from the options by entering A, B or C.

A message is the displayed to let the user know if they are correct or not, and the score increments by 1.

When all questions are answered, the total score is displayed as a percentage of correct answers and the user may select to play again or quit.

If play again is chosen, the quiz restarts and the user enters their name again and has the option to pick the same or another topic.


[Top of page](#pub-quiz-challenge)


## Project Goals

 This project was created for Code Institute's full stack software development course for Portfolio Project 3

 - ### Main goals
  
   - Create a functional terminal game using the Python language.

   - Make the game user friendly and easy to understand while still presenting a challenge

   - Implement technologies learned from the Python module such as Lists, Dictionaries, functions etc.

 - ### Target audience

   - Users with an interest in quizzes

   - Users who want to test their general knowledge

   [Top of page](#pub-quiz-challenge)


## Features

 ### Welcome screen

  When the 'Run Program' button is clicked on the Heroku mock terminal, the user is presented with the start screen.
  The start screen features a "Welcome To Blackjack" ASCII text message and a message prompting the user to either press S to start the game or I for the instruction screen.

  - If the user presses the S key they are shown a prompt to enter their username.
  If the username is valid the user is shown a welcome message and the game starts.
 
 ![Start Screen](assets/images/Quiz%20Start%20Screen.PNG)

 ![Username](docs/README-images/Home-screen.png)

  - If the user presses the I key they are brought to the instructions page where text is typed out in a typewriter effect and the user is given a prompt to enter any key to return to the main menu

  ![Instruction Page](docs/README-images/ins-page.png)

 ### Bet Input

  ![Bet Input](docs/README-images/Chip-input.png)

  After the user enters a valid username, they are brought to the bet input screen which asks them how many chips they would like to bet

   - If the user tries to bet more chips than they currently have they are shown an error message telling them they don't have enough chips to place the bet.

   ![Invalid Bet](docs/README-images/invalid-bet.png)

   - If the user tries to type in a bet amount that is not a number or zero they are shown an error message that asks them to type in a valid bet amount.

   ![Invalid Bet 2](docs/README-images/nan.png)

   - If the user enters a valid bet amount they are shown an ASCII message telling them the cards are being dealt before moving on to the next screen.

   ![Dealing Cards](docs/README-images/deal-cards.png)

   [Top of page](#pub-quiz-challenge)

 ### Main Game Screen

  ![Main Game Screen](docs/README-images/game-screen.png) 

  After the user enters a valid bet amount the cards are dealt and the user is brought to the main game screen. The user is shown their two cards and total, 1 dealer card and total and is given the option of whether to hit or stand.

   - If the user selects hit they are dealt another card and asked to hit or stand again until they bust or choose to stand.

   ![Player Hit](docs/README-images/hit-screen.png)

   - If the user selects stand it is the dealer's turn. The dealer's 2 cards and the total are now revealed to the player and the dealer takes another card if they are not already on a total of 17.

   ![Player Stand](docs/README-images/stand-screen.png)

   - After both the player has chosen to stand and the dealer has taken its go the 2 hands are compared and the user is told if they either won or lost the hand. If the user won the hand the text is green and if the user lost the hand the text is red.
   The user is then given an updated chip count and asked if they want to play again.

   ![Hand Compare](docs/README-images/hand-compare.png)

   - If the user selects no on playing again they are brought back to the start screen and their chips reset.

   - If the user selects yes on playing again they are brought back to the bet input screen and their current chip count stays the same.

   ![Play Again](docs/README-images/play-again.png)

   - If the user runs out of chips they are told that they have run out of chips, shown an ASCII text game over message and are brought back to the start screen. Their chips are also reset.

   ![Out Of Chips](docs/README-images/out-of-chips.png)

   ![Game Over](docs/README-images/game-over.png)

   [Top of page](#pub-quiz-challenge)

## Possible Future Features

 Some possible features that could be implemented into the game in the future are

   - Leaderboard betting system

     - While there is currently a chip betting system already in the game I would like to expand on it for game replayability.

   - ASCII card art

     - While there are currently Unicode suits for cards I would like to have the cards generated in ASCII art in the future, including different colors to match card suits.

   - Sound effects

     - Card shuffling sound effects is a feature I would eventually like to add to the game. 

     [Top of page](#pub-quiz-challenge) 

## Technologies

 ### Platforms

   - Python was the programming language used to create this project.

   - [Heroku](https://www.heroku.com/) was the platform used to deploy the project.

   - [GitHub](https://github.com/) and Git were used for version control on the project.

   - Gitpod was the I.D.E used to create the project.

   - [Code Institute](https://www.googleadservices.com/pagead/aclk?sa=L&ai=DChcSEwihmpOZxdT7AhUY7O0KHQfoCQoYABAAGgJkZw&ohost=www.google.com&cid=CAESbOD23lTrQj-qdni7kiJrbFGiE6foYCdCBlBfPjQiteL7YMJQfW4m6Wq768MU5PttgLc80SMqCtz2JIXMrLRwvBZnNHF48SVSK7-f6l2qO2XaL1vj4yBiBt3ZFE9Zd3_sMo8_VpVo0G1C0DeN0A&sig=AOD64_0o-rshCZ_TWMJtTwfpl71-w7W3GA&q&adurl&ved=2ahUKEwiC6ouZxdT7AhUPXMAKHXZJARkQ0Qx6BAgHEAE) template was used on Gitpod for this project.

 ### Python Modules

   - [os](https://docs.python.org/3/library/os.html) was imported to make the clear function to clear the terminal

   - [random](https://docs.python.org/3/library/random.html) was imported for the card shuffle function.

   - [time](https://docs.python.org/3/library/time.html) was imported for the sleep function.

   - [pyfiglet](https://pypi.org/project/pyfiglet/0.7/) was imported for custom ASCII messages.

   - [colorama](https://pypi.org/project/colorama/) was imported for custom coloured messages. 

   [Top of page](#pub-quiz-challenge)

## Flow Chart

 The below flow chart was used in the design of the game and shows how the game loop works from start to finish.

 ![Flowchart](docs/README-images/flowchart.png)

 [Top of page](#pub-quiz-challenge)

## Testing

 ### Validator Testing

  - No errors or warnings were found when putting the code through the CI Python Linter
  ![Linter](docs/README-images/linter.png)
  
 ### Testing User Stories

  - As a user, I want clear instructions on how to start the game.

     - The start screen has a very simple layout and only gives the user two clearly labelled options. Either S to start the game or I to read the instructions.

  -  As a user, I want Instructions on how to play the game.

     - On the start screen if the user wishes to they can select to view the instructions page which gives a full rundown on how the game works.

  -  As a user, I want an option to play the game again when finished.

     - After every hand, the user is given the choice to play again by typing Y for yes or N for no. If the user wants to continue with their current chips they can select yes, otherwise they can select no. 

  - As a user, I want to be able to enter a username.

     - At the start of every game, the user must enter a username to continue.

  - As a user, I want game feedback if I have an incorrect input.

     - The user is given clear instructions in game on every input needed and is unable to continue until they input correctly.

 ### Function and bug testing

  - All other testing for this project including Function testing and bugs are on a separate file found here [Function Testing](docs/TESTING.md)  

  [Top of page](#pub-quiz-challenge)


## Deployment

  The following steps were used to deploy this project to [Heroku](https://www.heroku.com/) 

   - Go to Heroku and click on the new button in the top right corner of the page. Then select create new app from the dropdown menu.

   - Choose an app name, select the region and click create app.

   - Go to settings and select Config Vars

   - Add a new Config Var with a keyword of PORT and a value of 8000

   - Next in settings find Buildpacks and add Buildpacks Python and NodeJS in that order.

   - Exit settings and click Deploy. Select GitHub from the deploy options.

   - Find your repository and connect it to Heroku.

   - Select Manual Deploy from the options, make sure main branch is selected and click Deploy Branch.

   - The live version of the app can be found here [Live Game Link](https://python-blackjack.herokuapp.com/)

   [Top of page](#pub-quiz-challenge)

## Credits

  - [fun quizzes](https://www.funquizzes.uk//pub-quiz-questions) used to get questions for different topics

  - Card suit Unicode symbols were found on Wikipedia [Here](https://en.wikipedia.org/wiki/Playing_cards_in_Unicode)

  - The clear display function was found on geek for geeks [Here](https://www.geeksforgeeks.org/clear-screen-python/#:~:text=You%20can%20simply%20%E2%80%9Ccls%E2%80%9D%20to%20clear%20the%20screen%20in%20windows.)

  - The template used for this project was the Code Institute python essentials template found [Here](https://github.com/Code-Institute-Org/python-essentials-template)

  - The flowchart created for this project was made on [Lucidchart](https://www.googleadservices.com/pagead/aclk?sa=L&ai=DChcSEwjm0IXtxdv7AhUm7-0KHRVNDHwYABAAGgJkZw&ohost=www.google.com&cid=CAESbOD2FmT0TtByzzkK620v_t26vgxZBwp1SyXz5cFeI64MHuAO2lqZGDOZZBd9ZTH5BuNL_bcb_Nr1Z5HKl_aYY9dOpjvjSG3PcPU27A1FbQ5b2_Us-gOYsRmxM1SH0BUrkbAYjVAiG8hA6ifQ2A&sig=AOD64_2FaTT_YSoGZDvf3kC_eU4DD5hjRw&q&adurl&ved=2ahUKEwiA0P7sxdv7AhUCYcAKHQmCCdQQ0Qx6BAgJEAE)

  - The linter used for code validation was the CI Python Linter found [Here](https://pep8ci.herokuapp.com/)

  - The idea of how to set up the deck and dictionary values for cards were Found on Dave Crabbes youtube video [Here](https://www.youtube.com/watch?v=SHz5cUeljZw)

  - [Stack Overflow](https://stackoverflow.com/) was used for solutions for various bug fixes.

  - [W3Schools](https://www.w3schools.com/) was used for research on various syntaxes.

  - [Grammarly](https://www.googleadservices.com/pagead/aclk?sa=L&ai=DChcSEwjGsafOh9_7AhUJl-0KHQmxCicYABAAGgJkZw&ohost=www.google.com&cid=CAESbOD2Xcxc5xKr6RvUm7TpPwpbCU10LjQrGKOUpXrGNnyNWmaO2Zk_y3dAnW0mpTc0x3-DbRTeK6OH9zUg9xamXSqmNqv6wX1BoWxsXzUdK4K_UGDr0UcXNmNKVLXoTN8VKvjK_8V0CSW2WZ2Chg&sig=AOD64_2EL-jS1jY_9um_H6eqlNDcftFF3Q&q&adurl&ved=2ahUKEwjs2qHOh9_7AhWGI8AKHbzkBSwQ0Qx6BAgHEAE) was used for the README spell and grammar checks.

  [Top of page](#pub-quiz-challenge)

## Acknowledgements

 - To my classmates Sean Finn and Victoria Traynor who helped review my project along the way and discussions about various issues and bugs.

 - To the slack community as a whole for help and support throughout the whole project.

 - To my friends, family and in particular my fiancee Sinead for support throughout the project.

 [Top of page](#pub-quiz-challenge)
