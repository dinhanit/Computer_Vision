import cv2

# List of image paths to be stitched together
image_paths = ['Images_Q1/Q1_3.jpg','Images_Q1/Q1_4.jpg','Images_Q1/Q1_5.jpg','Images_Q1/Q1_2.jpg','Images_Q1/Q1_1.jpg']

# Read the first image to initialize the panorama
panorama = cv2.imread(image_paths[0])

# Iterate over the remaining images
for i in range(1, len(image_paths)):
    # Read the current image
    image = cv2.imread(image_paths[i])

    # Create a stitcher object
    stitcher = cv2.Stitcher_create()

    # Stitch the current image with the panorama
    status, panorama = stitcher.stitch([panorama, image])

    # Check if the stitching was successful
    if status == cv2.Stitcher_OK:
        print(f"Image {i+1} stitched successfully.")
    else:
        print(f"Image {i+1} stitching failed.")

# Display the final panorama
print(panorama.shape)
cv2.imshow("Panorama", panorama[80:500,20:])
cv2.waitKey(0)
cv2.destroyAllWindows()
