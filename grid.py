import cv2
import imutils

# Read the image
img = cv2.imread('board.png')

# Define the grid size (number of rows and columns)
grid_size = (20,20)

# Define the grid line color and thickness
line_color = (0,0,0) # black
line_thickness = 1

# Get the image height and width
temp = img.shape
height,width = temp[0],temp[1]

# Calculate the cell width and height
cell_width = width // grid_size[0]
cell_height = height // grid_size[1]

# Iterate through the rows and columns and draw lines to form the grid
for i in range(1, grid_size[0]):
    x = i * cell_width
    y = 0
    x_end = i * cell_width
    y_end = height
    cv2.line(img, (x, y), (x_end, y_end), line_color, line_thickness)

for j in range(1, grid_size[1]):
    x = 0
    y = j * cell_height
    x_end = width
    y_end = j * cell_height
    cv2.line(img, (x, y), (x_end, y_end), line_color, line_thickness)

# Show the image with the grid overlay
cv2.imshow("Image with grid", img)
cv2.waitKey()
