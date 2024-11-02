mood = ""
x = 0  # X coordinate for moving shapes
size_factor = 1  # Initial size factor for the breathing circle
breathing_in = True  # Direction of breathing
max_size = 200  # Maximum size of the circle
min_size = 50  # Minimum size of the circle
speed = 2  # Speed of the breathing effect
wave_duration = 300  # Duration for the waves to show

# Variables for sun position and rotation
sun_x = 400  # Initial X position of the sun
sun_y = 300  # Initial Y position of the sun
rotation_angle = 0  # Initial rotation angle
spinning = False  # Check if the sun should spin

# List of positions of happy circles
happy_circles = []
smiley_faces = []  # List to store smiley face positions
circle_speed = 2  # Speed of moving circles
num_happy_circles = 8  # Number of happy circles

# Timer variables
timer_duration = 15  # Duration of the timer loop in seconds (15 seconds)
timer_start = 0  # When the timer starts
timer_running = False  # Whether the timer is active

# Score variable
score = 0  # Initialize score

def setup():
    size(800, 600)
    textSize(24)
    textAlign(CENTER)
    noStroke()
    
    # Random positions for circles
    for _ in range(num_happy_circles):
        happy_circles.append((random(width), random(height)))

def draw():
    global x, sun_x, sun_y, rotation_angle, spinning, mood, score, timer_running, timer_start

    background(225, 246, 255)  # Sky blue background

    # Display mood prompt only if mood is not set
    if mood == "":
        fill(0) #Black text
        text("How are you feeling? (Type and press Enter)", width / 2, height / 2 - 80)

    # Display the current mood input
    fill(0)
    text(mood, width / 2, height / 2)  # Display the current mood

    # Display score only if mood is "happy"
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
            
    # Timer display and features
    if timer_running:
        remaining_time = timer_duration - (frameCount - timer_start) / 60  # Calculate remaining time
        if remaining_time > 0:
            fill(255, 0, 0)  # Red colour for the timer
            text("Time left: {:.1f}s".format(remaining_time), width - 100, 30)
        else:
            timer_running = False  # Stop the timer when it reaches 0
            mood = ""  # Reset mood after timer ends
            score = 0  # Reset score

    # Only draw waves if mood is not entered
    if mood == "":
        drawLines(x)
        x += 2
        if x > width:
            x = -100  # Reset position
    else:
        displayMood(mood)  # Display the corresponding mood art

        # Update sun position to follow the mouse
        sun_x = mouseX
        sun_y = mouseY

        # Spin the sun if mouse is clicked
        if spinning:
            rotation_angle += 10  # Increment rotation angle by 10 degrees

        # Start timer when mood is entered
        if not timer_running:
            timer_start = frameCount  # Set the start frame for the timer
            timer_running = True  # Activate the timer

def keyPressed():
    global mood

    if key == ENTER:  #Effective when 'Enter' is entered
        mood = mood.strip()  # Remove unnecessary characters
        
    elif key != CODED:  # Only add keys that aren't special
        mood += key  # Add new character to mood

def mousePressed():
    global spinning, score
    # Check if the mouse is within the sun's area to start spinning
    if dist(mouseX, mouseY, sun_x, sun_y) < 100:  # Adjust the radius as needed
        spinning = not spinning  # Toggle spinning

    # Check if any happy circle is clicked
    for circle in happy_circles[:]:  # Iterate over a copy of the list
        if dist(mouseX, mouseY, circle[0], circle[1]) < 25:  # Radius is 25
            happy_circles.remove(circle)  # Remove the clicked circle
            smiley_faces.append(circle)  # Add a smiley face at the same position
            score += 1  # Increment the score
            # Add a new circle at a random position
            happy_circles.append((random(width), random(height)))

def drawLines(x):
    stroke(300, 150, 250, 150)  # Light pink color with transparency
    strokeWeight(42)  # Line thickness
    for i in range(0, width, 30):  # Vertical spacing of lines
        y_offset = 35 * sin(radians(i + x))  # Display dynamic wave based on time
        line(i, height / 2 + y_offset, i, height / 2 + height * 0.2)  # Draw line height

def displayMood(mood):
    if mood.lower() == "happy":
        drawHappyArt()
    elif mood.lower() == "sad":
        drawSadArt()
    elif mood.lower() == "angry":
        drawCalmingArt()
    else:
        fill(0)
        text("Thanks for contributing! Every mood is important!", width / 2, height / 2 + 160) #Neutral text for unrecognised input

def drawHappyArt():
    global happy_circles
    fill(255, 128, 0)  # Orange for happiness
    
    # Move and draw each circle
    for i in range(len(happy_circles)):
        x, y = happy_circles[i]
        
        # Update position with slight random movement
        x += random(-circle_speed * 0.5, circle_speed * 0.5)
        y += random(-circle_speed * 0.5, circle_speed * 0.5)

        # Keep circles within bounds
        x = constrain(x, 0, width)
        y = constrain(y, 0, height)

        happy_circles[i] = (x, y)  # Update the position

        ellipse(x, y, 50, 50)  # Draw each circle
    
    # Draw smiley faces for those that burst
    for face in smiley_faces:
        drawSmileyFace(face[0], face[1])  # Draw smiley face at the position

    # Display score
    fill(0) # Black colour for text
    text("Score: " + str(score), width / 2, height / 2 - 40)  # Display score above mood prompt

    text("That's great to hear! Click the circles for a happy surprise! :)", width / 2, height / 2 + 160) #Happy text for happy input

def drawSmileyFace(x, y):
    fill(255, 255, 0)  # Yellow for the smiley face
    ellipse(x, y, 50, 50)  # Face
    fill(0)  # Black for facial features
    ellipse(x - 15, y - 10, 10, 10)  # Left eye
    ellipse(x + 15, y - 10, 10, 10)  # Right eye
    arc(x, y + 5, 30, 20, 0, PI)  # Smile

def drawSadArt():
    pushMatrix()  # Save the current coordinates
    translate(sun_x, sun_y)  # Move to the sun's position
    rotate(radians(rotation_angle))  # Rotate the sun 

    fill(255, 204, 0)  # Yellow colour for the sun
    ellipse(0, 0, 200, 200)  # Sun body

    # Draw rays around the sun
    ray_length = 75  # Length of the rays
    for angle in range(0, 360, 30):  # Quantity of sun Rays
        x1 = cos(radians(angle)) * 100  # Start point for rays
        y1 = sin(radians(angle)) * 100
        x2 = cos(radians(angle)) * (100 + ray_length)  # End point for rays
        y2 = sin(radians(angle)) * (100 + ray_length)
        line(x1, y1, x2, y2)  # Draw the ray

    # Draw face on the sun
    fill(0)  # Black color for sun's face
    ellipse(-30, -20, 20, 20)  # Left eye
    ellipse(30, -20, 20, 20)  # Right eye
    arc(0, 20, 60, 40, 0, PI)  # Happy mouth

    popMatrix()  # Restore the coordinates

    text("Cheer up by clicking this silly sun! Hope you feel better.", sun_x, sun_y + 100) #Happy text for sad input

def drawCalmingArt():
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

    fill(0)  # Darker color for the text
    text("Let's do some calming breathing exercises! Breathe in and out with the circle.", width / 2, height / 2 + 160) #Calming text for angry input
