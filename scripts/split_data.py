import shutil
import os
from sklearn.model_selection import train_test_split

WORK_DIR = os.getcwd()
DATA_DIR = os.path.join(WORK_DIR, "annotated_data")

# Define paths to image and label data
images_path = os.path.join(WORK_DIR, "labeled_data", "images")
labels_path = os.path.join(WORK_DIR, "labeled_data", "labels")
data = os.listdir(images_path)

# Split to training and test
train, test = train_test_split(data, test_size=0.2, random_state=1)

# Create test and train directories
train_path = os.path.join(DATA_DIR, "train")
test_path = os.path.join(DATA_DIR, "test")

train_labels = os.path.join(train_path, "labels")
train_images = os.path.join(train_path, "images")
test_labels = os.path.join(test_path, "labels")
test_images = os.path.join(test_path, "images")

# Create directories if they do not exist
os.makedirs(train_labels, exist_ok=True)
os.makedirs(train_images, exist_ok=True)
os.makedirs(test_labels, exist_ok=True)
os.makedirs(test_images, exist_ok=True)

# Move train files to train folder
for file_name in train:
    # Copy bounding box (label) files
    label_name = file_name[:-4] + '.txt'
    label_source_path = os.path.join(labels_path, label_name)
    label_dest_path = os.path.join(train_labels, label_name)
    if os.path.exists(label_source_path):
        shutil.copy(label_source_path, label_dest_path)
    else:
        print(f"Label file not found: {label_source_path}")
    
    # Copy image files
    img_source_path = os.path.join(images_path, file_name)
    img_dest_path = os.path.join(train_images, file_name)
    shutil.copy(img_source_path, img_dest_path)

# Move test files to test folder
for file_name in test:
    # Copy bounding box (label) files
    label_name = file_name[:-4] + '.txt'
    label_source_path = os.path.join(labels_path, label_name)
    label_dest_path = os.path.join(test_labels, label_name)
    if os.path.exists(label_source_path):
        shutil.copy(label_source_path, label_dest_path)
    else:
        print(f"Label file not found: {label_source_path}")
    
    # Copy image files
    img_source_path = os.path.join(images_path, file_name)
    img_dest_path = os.path.join(test_images, file_name)
    shutil.copy(img_source_path, img_dest_path)

print("Size train data:", len(train))
print("Size test data:", len(test))
