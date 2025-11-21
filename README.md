# 1) Executive Summary
## Problem
Humor plays a massive roll in human interaction for everyone. It can be amazing if comedy is pulled off well, but that task is difficult to master.
## Solution 
Few things are funnier than a well-timed sound effect. With my soundboard app, anyone can easily click on a sound that is perfect for any scenario. Is your friend taking too long to answer your question? Click on the Jeopardy sound effect and let them know in a humorous way! Your coworker completes a task they've been stressing about. Click on the Applause sound effect and make them smile! It can be used by anyone and is sure to brighten the day of everyone around you.

# 2) System Overview


# 3) How to Run (Local)
## Build
docker build -t soundboard .
## Run
docker run --rm -p 8080:8080 --env-file .env soundboard

# 4) Design Decisions
## Why this concept?
- I considered having a visible play button on each sound tile, but decided that clicking on the tile itself was intuitive enough and made it visually look more like a soundboard.
- I also considered creating the app so that only one sound could play at once, but decided that that limited the abilities of the user.
- I also played around with different colored tiles and different tile annimations, but ultimately decided that black text with large white tiles on the off-whtie background was the easiest to read and the least overwhelming.
## Tradeoffs
- The choice to have one "Stop All Sounds" button sacraficed the ability of the user to have the control to stop some sounds and not others for the sake of positive simplicity for both the user and the visual appearance of the app.
- The choice to add emojis to the sound tiles may make some feel that the app looks childish, but I decided it was worth it in order to increase clarify and add a much-needed pop of color to the app.

# 5) Results and Evaluation
## Performance/Test Notes
- While testing this product I was able to make my girlfriend, my TA, and a couple of my classmates laugh.   
- I was easily able to find ways to use the product in conversation during testing.
- The sounds have never failed to play when their respective tiles have been clicked on during testing, nor has the "Stop All Sounds" button failed to stop all sounds from playing.
