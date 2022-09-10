
#%%
import pandas
import os

#%% getting list of image files
image_filenames = []

os.system("ls ./images | grep -Ev '\.(txt|pdf|py|csv)$' > images_list.txt")
with open("images_list.txt", "r") as image_list:
    for i, line in enumerate(image_list):
        image_filenames.append(line[0:-1])
print(len(image_filenames), ' images found in folder:\n', image_filenames)

#%% extracting text from images
text = []

for i in range(len(image_filenames)):
    os.system(f'tesseract ./images/{image_filenames[i]} temp')
    with open('temp.txt', 'r') as temp:
        text.append(temp.read().replace('\n', '')) # stripping new lines

print('text extraction: complete')

#%% storing extracted text in csv format
text_dataframe = pandas.DataFrame(data={'raw_text': text})
text_dataframe.to_csv('raw_data.csv', index=False)
print('data imported to raw_data.csv')
