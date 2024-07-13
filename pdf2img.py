from pdf2image import convert_from_path # module used to convert pdf to image
import os                               # to intract with os

# Define the input path for pdf and output path for the images to be saved
pdf_path= r'D:\Datasets\SHIVA\PIPE & FITTINGS\CS PIPE\Buhlman Singapore - CS Pipes - BPC-TWH-CRR-PIP-005.pdf'
output_directory= r'D:\Py\pythonProject\pdf2img_copy'

# To create output directory if it doesnt exist
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Convert all pdf page to image and store it as a list
images= convert_from_path(pdf_path, poppler_path=r"C:\Program Files\poppler-24.02.0\Library\bin")

# save all the images in th output directory
for i,image in enumerate(images):
    image_path= os.path.join(output_directory,f'Image_{i+1}.jpeg')
    image.save(image_path,"jpeg")

# To check whether image was create and its format
image.show()
print(image.format)


print("all page converted to image.jpeg")