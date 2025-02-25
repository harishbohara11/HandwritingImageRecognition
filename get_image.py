import idx2numpy
import json

# Load training images from local file
train_images = idx2numpy.convert_from_file('dataset/train-images-idx3-ubyte')

# Select one image (for example, the first image)
image = train_images[1]  # shape is (28, 28)

# Convert the image to a nested list
image_list = image.tolist()

# Manually print the JSON payload with one row per line
print("{")
print('  "images": [')
print("    [")
for row in image_list:
    # Each row is dumped as a JSON array and printed on one line
    print("      " + json.dumps(row) + ",")
print("    ]")
print("  ]")
print("}")
