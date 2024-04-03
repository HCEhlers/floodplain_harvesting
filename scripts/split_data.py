# Split data into train and validation folder 
import shutil 
import os
from sklearn.model_selection import train_test_split

#Use only this method if running directly from scripts folder otherwise comment out the 
os.chdir('..')

cwd = os.getcwd()
data_path = cwd

# Define path to image data
path = f"{cwd}/labeled_data/images"
bb_path = f"{cwd}/labeled_data/labels"
data = os.listdir(path)

# Split to training and validation
train, test = train_test_split(data, test_size=0.2, random_state=1)

# Create test and train directory
train_path = cwd + "/training_data/train/"
test_path = cwd + "/training_data/test/"
img_path = cwd + "/training_data/images/"

train_box = train_path + "/boundingboxes"
train_images = train_path + "/images"
test_box = test_path + "/boundingboxes"
test_images = test_path + "/images"


try:
   os.mkdir(train_path)
   os.mkdir(test_path)
   os.mkdir(train_box)
   os.mkdir(train_images)
   os.mkdir(test_box)
   os.mkdir(test_images)
except FileExistsError:
   pass


# Move train files to train folder
for file_name in train:
   #Boundingboxes folder:
   shutil.copy(os.path.join(path, file_name), train_box)
   #Images folder:
   print(f"{path}/{file_name}")
   shutil.copy(os.path.join(path, file_name[:-4] + '.jpg'), train_images)


# Move test files to test folder
#for file_name in test:
#   shutil.copy(os.path.join(data_path + bb_path, file_name), test_box)
#   shutil.copy(os.path.join(img_path, file_name[:-4] + '.jpg'), test_frames)

#print("Size train data: ", len(train), "\n","Size test data: ", len(test))
#print(len(data))
