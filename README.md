# WWDC-A2 : 'Mood Simulator'

This project includes a repository including the history of my code, proejct process and other general information contriubuting towards the finalisation of my prototype. Through the use of Python, I was able to code an interactive 'quiz style' visual output that offers varying visuals and games according to the user's mood. This data is collected through a simple quiz asked at the beginning and the visual representation is suited towards the answer. This prototype is aimed towards younger individuals who have difficulties expresing their emotions verbally, therefore the interactive and visual aspect of this project will enable them to engage whilst understanding the complexities of human emotion. 

**PROJECT AIM:**
This prototype aims to allow (mainly) children to express their emotions through a visual output. The information is collected through the user's responses and output through a visual feature coded in Processing.Org. This is due to children often finding difficulty in expressing themselves only verbally, therefore this prototype offers an alternate method of doing this. Furthermore, it can help stimulate positive feelings through the features- which are evidenced in the 'Calming' and 'Sad' functions. 

**TECHNOLOGIES USED:**
This prototype is a beginner level coding project that has been executd through Processing.Org and Python , as it is the most appropriate software and language for achieving my creative and realistic goals. The use of Processing.org libraries have also been incorporated throughout the development of my project, offering straightforward methods of visual output. 

**FEATURES:**
The 'Mood Simulator' serves as a creative visual prototype aimed for kids struggling to express their emotions verbally. Through the 'quiz' based question: 'What is your mood?,' they are able to type in their answer to generate an artistic feature corresponding to their answer. The 3 recognised moods are: sad, happy and angry- with each having their own distinct features. If another mood is input, a default message: 'Thanks for contributing! Every mood is important!' is displayed onto the screen, with the option of inputting a different mood after 15 seconds, re routing back to the home page. 

**SCREENSHOTS/FEATURES:**

HOME PAGE - Input mood answer 

<img width="596" alt="image" src="https://github.com/user-attachments/assets/d6c48660-bce8-4309-aa41-54f184bf9071"> 

'ANGRY' INPUT - Breathing exercise to calm down: inhale/exhale with the pulsating circle
<img width="589" alt="image" src="https://github.com/user-attachments/assets/0e7db11d-1229-4a76-8361-a745f92e6a5c">

'SAD' INPUT - To cheer up feeling of sadness: interactive spinning sun with a smiley face
<img width="583" alt="image" src="https://github.com/user-attachments/assets/44ff9b5b-3c29-4f4d-b90e-8b69edbb0fac">

'HAPPY' INPUT - Interactive game where circles are popped into smiley faces, with a scoreboard included
<img width="583" alt="image" src="https://github.com/user-attachments/assets/672d20d5-f446-4b6a-b7bd-911801f947b2">

'ELSE' INPUT - Message 'Thanks for contributing! Every mood is important!' (Neutral positive message to correspond with what answer is given.)

<img width="584" alt="image" src="https://github.com/user-attachments/assets/744ce5ef-7d23-4a28-9e4f-c269ace0920a">

**SETUP:**
1. Ensure that the Processing.Org software has been installed onto your device, and is able to run seamlessly. You are able to do this from a google chrome browser- and download the appropriate Processing.Org platform according to what device you are using. E.g. for Macbook, Windows....
2. Make sure it is saved in a folder which you can easily access within your device.
3. Run the code by clicking the navy blue 'play' icon on the top left.
4. A new tab should pop up, with a pink 'wave like' animation moving.
5. Type in a mood. Recognised moods with a visual output" happy, sad and angry.
6. If 'happy': a popping circle game will appear, when these circles are popped, they turn into a smiley face. A scoreboard is also included to keep track. You are given 15 seconds before you return to the home page.
7. If 'sad': an animated sun will appear. To interact, click on the sun with your mouse to make it start spinning clockwise. To stop, click on it again. The sun will follow your mouse. You are given 15 seconds before you return to the home page.
8. If 'angry': a series of circles will appear in pastel shades, slowly increasing and decreasing. This a breathing exercise to follow to stimualte calmness. When the circle decreases, breathe in. When the circle increases, breathe out accordingly. You are given 15 seconds before you return to the home page. 

**USAGE OF CODE:**
This code can be altered to one's preferences by changing certain variables to suit them. There are endless possibilities that are able to cater towards different needs through visual stimulation, engaging audiences. It may serve as a way to express emotions without direct communication with a person, as well as regulate negative thoughts. 

**ROOM FOR IMPROVEMENT/ PROJECT STATUS**
Although this project is finished for now, there is definitely room for development to add more features such as:
- further recognised mood options
- extensive features that have higher levels of interaction
- further development of the outputs of each mood

**USE OF AI**
https://chatgpt.com/

EXAMPLE 1: Developing the 'CalmingArt' Feature

INPUT: 'please code me a rough outline of a pulsating circle in python in processing'

OUTPUT: # Global variable to control the size of the circle
circle_size = 100
growth_speed = 1  # Speed at which the circle grows and shrinks
max_size = 150    # Maximum size of the circle
min_size = 50     # Minimum size of the circle

def setup():
    size(400, 400)  # Set the canvas size
    noStroke()      # Remove outline from the circle

def draw():
    global circle_size  # Use the global variable
    
    background(255)  # Clear the background each frame
    
    # Draw the pulsating circle
    ellipse(width / 2, height / 2, circle_size, circle_size)
    
    # Update the circle size to create the pulsating effect
    circle_size += growth_speed
    
    # Reverse the growth direction if the size exceeds the limits
    if circle_size > max_size or circle_size < min_size:
        growth_speed *= -1  # Reverse the direction of growth

RESULT: def drawCalmingArt():
    global size_factor, breathing_in

    # Calculate the size of the breathing circle
    circle_size = size_factor * 120
    small_circle_size = circle_size * 0.5  # Smaller circle size (half of bigger circle)

    # Center the main circle on the canvas 
    fill(173, 216, 230) # Light blue for the main circle
    ellipse(width / 2, height / 2 + 50, circle_size, circle_size) #Circle coordinates half of canvas 

    # Draw additional smaller circles within the main circle for engagement
    colors = [(255, 224, 204), (255, 204, 204), (255, 178, 204)]  # Soft pastel shades
    offsets = [0, 30, 60]  # Offsets for smaller circles

    for i in range(3):  # Draw 3 smaller circles
        fill(*colors[i])  # Set color for each smaller circle
        ellipse(width / 2, height / 2 + 50, small_circle_size + offsets[i], small_circle_size + offsets[i]) #Smaller circles

    # Inner circle for breathing effect
    fill(255, 182, 193, 200)  # Light pink for the inner circle with transparency
    ellipse(width / 2, height / 2 + 40, small_circle_size, small_circle_size)  # Smaller circle inside the biggest one

    if breathing_in:
        size_factor += speed * 0.01  # Increase circle size SLOWLY 
        if size_factor >= max_size / 30:  # Check if max size is reached
            breathing_in = False  # Alternate to shrinking circle
    else:
        size_factor -= speed * 0.01  # Decrease circle size SLOWLY
        if size_factor <= min_size / 20:  # Check if min size is reached
            breathing_in = True  # Switch to growing circle 

  EXAMPLE 2: Incorporating a Timer Feature

  INPUT: 'Please also code a timer feature to incorporate'

  OUTPUT:
 ** # Timer Logic**
    if timer_running:
        # Calculate remaining time based on the time elapsed
        elapsed_time = (millis() - timer_start) / 1000  # Convert to seconds
        remaining_time = timer_duration - elapsed_time  # Calculate remaining time
        
        if remaining_time > 0:
            # Display the remaining time
            fill(255, 0, 0)  # Red color for the timer
            text("Time left: {:.1f}s".format(remaining_time), width - 20, 30)
        else:
            # Stop the timer when it reaches 0
            timer_running = False
            remaining_time = 0  # Ensure remaining time does not go negative
            fill(0, 255, 0)  # Green color to show timer has ended
            text("Time's Up!", width / 2, height / 2)  # Display message

  RESULT:
    # Timer Display and Features
    if timer_running:
        remaining_time = timer_duration - (frameCount - timer_start) / 60  # Calculate remaining time
        if remaining_time > 0:
            fill(255, 0, 0)  # Red colour for the timer
            text("Time left: {:.1f}s".format(remaining_time), width - 100, 30)
        else:
            timer_running = False  # Stop the timer when it reaches 0
            mood = ""  # Reset mood after timer ends
            score = 0  # Reset score

  EXAMPLE 3: Debugging Boolean Result

  INPUT: 'Please help me debug this processing' : # Adjust background color based on mood
        if mood.lower() = "happy":
            background(255, 255, 204)  # Light yellow for happiness

  OUTPUT: Corrected Code:
  python
**  # Adjust background colour based on mood**
  if mood.lower() == "happy":
      background(255, 255, 204)  # Light yellow for happiness

  RESULT:
 ** # Display score only if mood is "happy"**
    if mood.lower() == "happy": #'==' Is a true statement 
        fill(0)
        text("Score: " + str(score), width / 2, height / 2 - 40)  # Display score above mood prompt
        
        # Adjust background color based on mood
        if mood.lower() == "happy":
            background(255, 255, 204)  # Light yellow for happiness
        elif mood.lower() == "sad":
            background(204, 204, 255)  # Light blue for sadness
        elif mood.lower() == "angry":
            background(173, 216, 230)  # Light blue for calming
        else:
            background(225, 246, 255)  # Default sky blue background
