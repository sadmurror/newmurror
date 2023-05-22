import os
from PIL import Image

end_dir = "end_photo"
os.makedirs(end_dir, exist_ok=True)

first_dir = "first_photo"

for filename in os.listdir(first_dir):
    if filename.endswith(".png") or filename.endswith(".jpg") or filename.endswith(".jpeg"):
        with Image.open(os.path.join(first_dir, filename)) as image:
            image = image.rotate(90)
            end_file = os.path.join(end_dir, filename)
            image.save(end_file)