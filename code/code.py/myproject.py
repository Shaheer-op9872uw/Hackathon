import os
import pygame
import sys

# Check the current working directory
print("Current working directory:", os.getcwd())

# Initialize pygame
pygame.init()

# Set up the display
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Deep Sea Discovery")

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 102, 204)

# Load images from the images folder
fish_image = pygame.image.load('images/fish.png')
shipwreck_image = pygame.image.load('images/shipwreck.png')
volcano_image = pygame.image.load('images/volcano.png')

# Scale images
fish_image = pygame.transform.scale(fish_image, (300, 200))  # Scale fish to 300x200
shipwreck_image = pygame.transform.scale(shipwreck_image, (300, 200))  # Scale shipwreck to 300x200
volcano_image = pygame.transform.scale(volcano_image, (800, 400))  # Scale volcano to 800x400

# Set the position for each image
fish_pos = (0, 0)                    # Top left corner for fish
shipwreck_pos = (screen_width - 300, 0)  # Top right corner for shipwreck
volcano_pos = (0, 200)                # Bottom half for volcano

# Fonts for text
font = pygame.font.Font(None, 36)

# Function to display info text
def show_info(image_name):
    screen.fill(BLUE)  # Clear the screen with blue background

    if image_name == "fish":
        text = "Ships have been vital to human exploration and trade. Did you know there are about 50,000 merchant ships globally?"
    elif image_name == "shipwreck":
        text = "Shipwrecks tell stories of maritime history. Over 3 million shipwrecks are believed to be scattered across the world's oceans."
    elif image_name == "volcano":
        text = "Volcanoes are openings in the Earth's crust. There are about 1,500 active volcanoes worldwide, with approximately 50-70 erupting each year."
    
    # Split the text into lines with a maximum of 5 words per line
    words = text.split()
    lines = []
    current_line = ""

    for word in words:
        if len(current_line.split()) < 5:
            current_line += word + " "
        else:
            lines.append(current_line.strip())
            current_line = word + " "
    if current_line:
        lines.append(current_line.strip())

    # Render each line and display it
    y_offset = 20
    for line in lines:
        info_surface = font.render(line, True, WHITE)
        screen.blit(info_surface, (20, y_offset))
        y_offset += 40  # Adjust the vertical spacing

    pygame.display.update()
    pygame.time.delay(5000)  # Show the text for 5 seconds

# Main loop
running = True
while running:
    screen.fill(BLUE)  # Fill the screen with blue background

    # Draw images on the screen
    screen.blit(fish_image, fish_pos)
    screen.blit(shipwreck_image, shipwreck_pos)
    screen.blit(volcano_image, volcano_pos)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            # Check which image was clicked and show corresponding information
            if fish_image.get_rect(topleft=fish_pos).collidepoint(mouse_pos):
                show_info("fish")
            elif shipwreck_image.get_rect(topleft=shipwreck_pos).collidepoint(mouse_pos):
                show_info("shipwreck")
            elif volcano_image.get_rect(topleft=volcano_pos).collidepoint(mouse_pos):
                show_info("volcano")

    # Update the display
    pygame.display.update()

# Quit pygame
pygame.quit()
sys.exit()
