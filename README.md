# ChessAssistant

## Context  

The Chess Assistant will help you know if there's a killer move you can make in your turn, with the current status of the board. Although this function might be too slow or not practical to use during a real match, it was fun to code it and achieve the expected result.  

In order to use the Assistant, you have to set the board first: you will give the name and location of the white piece you are interested in (e.g. pawn a2). Then, you can set as many black pieces in the board as you want (hey! no more than 16, don't go crazy). Whenever you are done setting the board, you must write the word "Done".  

With this, the program will find your killer move, if any, and tell you which black pieces can be eaten by the white piece you placed.  

For now, you can only use two different white pieces: rook and pawn. More pieces coming soon!

## Process

This Python program was fully written in VS Code, my favorite IDE. It was a task for a course I was taking, and it was very interesting to jump into programming and be able to code a program that works, the way it has to.  

My first step was to 'brainstorm' step by step what was neede from the program. After having this line by line, I jumped into coding and started defining the main section with functions that don't exist just yet. With this structure set, I started defining all the functions I will need: first setting up the board, and teaching the program some Chess rules (basically, piece names and locations). With this working in the background I was ready to prompt the user for the chosen White piece, and then for the Black pieces that will be sitting on the board. In both cases, lots of rules and limitations had to be set: location must be valid, there's a limit for each piece (1x, 2x, 8x) and a limit for the total amount of them, pieces can't have the same location.  

After all this is set, the program can start reviewing the board and analyze if the selected White piece is able to eat one or more Black pieces. At this moment, I've taught the program how does each piece move (again, only 2 White pieces available for the moment). After this processing is done, the program will return the results to the user in a readable and clear way. Here, I chose not to print the board to keep the interface clean though I might chnge this in the future to improve visibility of the board.
