### Libraries import
import streamlit as st
from PIL import Image
import pandas as pd
import random
st.set_page_config(page_title="👦🏽 Celebrity Faces")

### Side bar
st.sidebar.write("Welcome to my project in which I will show off my compiuter vision skills")
st.sidebar.write("I would like to show what I can do along with image processing hence several tabs such as 'Celebrity finder', 'Bounding box', 'Face landmarks', 'AI about your face', 'Face generator'.")
st.sidebar.write("Each one shows a different part of my skills and what the tab shows can be found inside it")
st.sidebar.write("Have fun with my computer vision models")

### Defining tabs
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(["Main tab 👦🏽","Celebrity finder :mag:", "Bounding box :man-pouting:", "Face landmarks :eyes:", "AI about your face :crystal_ball:", "Face generator :alien:" ])

##### Main tab ##########
tab1.title("Main tab 👦🏽")

tab1.write("In this sub-site I would like to present my skills which are based on computer vision. In it I would like to present:")
tab1.write(":large_blue_circle: Searching for faces using their characteristics")
tab1.write(":large_blue_circle: Searching by AI model of bounding boxes")
tab1.write(":large_blue_circle: AI model's search for face landmarks")
tab1.write(":large_blue_circle: Determination of the characteristics of your face by the AI model")
tab1.write(":large_blue_circle: Creating new faces based on a few selected ones + yours using the GAN network")

tab1.header("About models", divider='rainbow')
tab1.write("Each artificial intelligence model was created based on the CNN or GAN network. All models were created in-house, and access to them is included in the link at the bottom of this tab.")

tab1.header("Glossary", divider='rainbow')
tab1.subheader(":blue[GAN]")
tab1.write("""GAN stands for "Generative Adversarial Network." It is a class of machine learning models used in unsupervised learning to generate new data that is similar to a given dataset. GANs were introduced by Ian Goodfellow and his colleagues in 2014 and have since become a popular and influential approach in the field of deep learning.""")

tab1.subheader(":blue[CNN]")
tab1.write("""CNN stands for "Convolutional Neural Network." It is a type of artificial neural network that is particularly well-suited for tasks related to computer vision, image recognition, and image analysis. CNNs have been instrumental in advancing the field of deep learning and achieving state-of-the-art performance in various image-related tasks.""")

tab1.subheader(":blue[Bounding box]")
tab1.write("A bounding box is a rectangular or square-shaped region that is used to enclose or define the spatial extent of an object within an image or a two-dimensional space. Bounding boxes are commonly used in computer vision, object detection, image annotation, and various machine learning tasks to locate and delineate objects of interest within images or video frames.")

tab1.header("Foundations of the project", divider='rainbow')
tab1.write("The entire project was built on a dataset that is available on the Kaggle.com platform and is called CelebFaces Attributes (CelebA) Dataset. Below is the entire documentation of the project.")

tab1.subheader(":blue[Context]")
tab1.write("A popular component of computer vision and deep learning revolves around identifying faces for various applications from logging into your phone with your face or searching through surveillance images for a particular suspect. This dataset is great for training and testing models for face detection, particularly for recognising facial attributes such as finding people with brown hair, are smiling, or wearing glasses. Images cover large pose variations, background clutter, diverse people, supported by a large quantity of images and rich annotations. This data was originally collected by researchers at MMLAB, The Chinese University of Hong Kong (specific reference in Acknowledgment section).")

tab1.subheader(":blue[Overall]")
tab1.write(":large_blue_circle: 202,599 number of face images of various celebrities")
tab1.write(":large_blue_circle: 10,177 unique identities, but names of identities are not given")
tab1.write(":large_blue_circle: 40 binary attribute annotations per image")
tab1.write(":large_blue_circle: 5 landmark locations")

tab1.subheader(":blue[Data Files]")
tab1.write(":large_blue_circle: img_align_celeba.zip: All the face images, cropped and aligned")
tab1.write(":large_blue_circle: list_eval_partition.csv: Recommended partitioning of images into training, validation, testing sets. Images 1-162770 are training, 162771-182637 are validation, 182638-202599 are testing")
tab1.write(""":large_blue_circle: list_bbox_celeba.csv: Bounding box information for each image. "x_1" and "y_1" represent the upper left point coordinate of bounding box. "width" and "height" represent the width and height of bounding box""")
tab1.write(":large_blue_circle: list_landmarks_align_celeba.csv: Image landmarks and their respective coordinates. There are 5 landmarks: left eye, right eye, nose, left mouth, right mouth")
tab1.write(""":large_blue_circle: list_attr_celeba.csv: Attribute labels for each image. There are 40 attributes. "1" represents positive while "-1" represents negative""")

tab1.subheader(":blue[Acknowledgements]")
tab1.write("Original data and banner image source came from http://mmlab.ie.cuhk.edu.hk/projects/CelebA.html")
tab1.write("As mentioned on the website, the CelebA dataset is available for non-commercial research purposes only. For specifics please refer to the website.")
tab1.write("""The creators of this dataset wrote the following paper employing CelebA for face detection:""")
tab1.write("""S. Yang, P. Luo, C. C. Loy, and X. Tang, "From Facial Parts Responses to Face Detection: A Deep Learning Approach", in IEEE International Conference on Computer Vision (ICCV), 2015""")

tab1.subheader(":blue[Inspiration]")
tab1.write("Can you train a model that can detect particular facial attributes?")
tab1.write("Which images contain people that are smiling?")
tab1.write("Does someone have straight or wavy hair?")

tab1.header(" ", divider='rainbow')
tab1.write("Created by: Igor Winek | Last update: 28.10.2023")

##### Celebrity finder tab ##########
tab2.title("Celebrity finder :mag:")

### Explanation of how the search engine works
tab2.header("How it works?", divider='rainbow')
tab2.subheader("Context")
tab2.write("""The data that was used in the project comes from the Kaggle dataset, which is called the "CelebFaces Attributes (CelebA) Dataset." As author Jessica Li mentions, this is a popular dataset used in mobile app login authentication. You can read more about it at the source: https://www.kaggle.com/datasets/jessicali9530/celeba-dataset. The entire dataset has 202,599 images of a face and 40 attributes that define its appearance. In the attributes section, I will present all the attributes that you can use in searching for an image.""")
tab2.subheader("Attributes")
tab2.write(""" The following is a list of all the attributes you can use in the image search. Remember not to select attributes that are mutually exclusive, i.e. 'Black hair' and 'Blond hair'. In this case, the wysdzukiwarka results may be falsified and the program will not return any image""")

col1,col2,col3 = tab2.columns(3)

col1.write(":large_blue_circle: Arched eyebrows ")
col1.write(":large_blue_circle: Attractive")
col1.write(":large_blue_circle: Bags under eyes")
col1.write(":large_blue_circle: Bald")
col1.write(":large_blue_circle: With bangs")
col1.write(":large_blue_circle: Big lips")
col1.write(":large_blue_circle: Big nose")
col1.write(":large_blue_circle: Black hair")
col1.write(":large_blue_circle: Straight hair")
col1.write(":large_blue_circle: Narrow eyes")
col1.write(":large_blue_circle: Wavy hair")
col1.write(":large_blue_circle: Gray hair")
col1.write(":large_blue_circle: Male")

col2.write(":large_blue_circle: Blond hair")
col2.write(":large_blue_circle: Blurry")
col2.write(":large_blue_circle: Brown hair")
col2.write(":large_blue_circle: Sideburns")
col2.write(":large_blue_circle: Smiling")
col2.write(":large_blue_circle: Wearing hat")
col2.write(":large_blue_circle: Wearing lipstick")
col2.write(":large_blue_circle: Young")
col2.write(":large_blue_circle: Pale skin")
col2.write(":large_blue_circle: No beard")
col2.write(":large_blue_circle: High cheekbones")
col2.write(":large_blue_circle: Bushy eyebrows")
col2.write(":large_blue_circle: Wearing necklace")

col3.write(":large_blue_circle: Pointyn nose")
col3.write(":large_blue_circle: Receding hairline")
col3.write(":large_blue_circle: Chubby")
col3.write(":large_blue_circle: Goatee")
col3.write(":large_blue_circle: Eyeglasses")
col3.write(":large_blue_circle: Mustache")
col3.write(":large_blue_circle: Oval face")
col3.write(":large_blue_circle: Rosy cheeks")
col3.write(":large_blue_circle: Wearing earrings")
col3.write(":large_blue_circle: Double chin")
col3.write(":large_blue_circle: Mouth slightly open")
col3.write(":large_blue_circle: Heavy makeup")
col3.write(":large_blue_circle: Wearing necktie")

tab2.subheader("How to handle?")
tab2.write("Select the features you want the photo to meet and then click the search button")
tab2.subheader("Enjoy :smile:")

### Search engine
options = tab2.multiselect(
    'Choose the features of appearance to be fulfilled by the celebrity',
    [
        "Arched eyebrows",
        "Attractive",
        "Bags under eyes",
        "Bald",
        "With bangs",
        "Big lips",
        "Big nose",
        "Black hair",
        "Blond hair",
        "Blurry",
        "Brown hair",
        "Bushy eyebrows",
        "Chubby",
        "Double chin",
        "Eyeglasses",
        "Goatee",
        "Gray hair",
        "Heavy makeup",
        "High cheekbones",
        "Male",
        "Mouth slightly open",
        "Mustache",
        "Narrow eyes",
        "No beard",
        "Oval face",
        "Pale skin",
        "Pointyn nose",
        "Receding hairline",
        "Rosy cheeks",
        "Sideburns",
        "Smiling",
        "Straight hair",
        "Wavy hair",
        "Wearing earrings",
        "Wearing hat",
        "Wearing lipstick",
        "Wearing necklace",
        "Wearing necktie",
        "Young"],
    ['Attractive', 'Young'])

### Uploading appearance features data
map = pd.read_excel("data/CelebFinderData/map.xlsx")
df = pd.read_csv("data/CelebFinderData/list_attr_celeba.csv")
df = df.replace(-1, 0)
df = df.drop('5_o_Clock_Shadow', axis=1)
for i, row in map.iterrows():
        df.rename(columns={row['original_name']: row['gui_name']}, inplace=True)
### Defining the action of the search button
if tab2.button('Search'):
        
        if "image_id" in options:
            pass
        else:
            options.append("image_id")

        ### Data filtering
        diss_df = df[options]
        diss_df = diss_df[(diss_df.iloc[:, :-1] != 0).any(axis=1)]
        diss_df = diss_df[(diss_df   != 0).all(axis=1)]
        diss_df.reset_index(drop=True, inplace=True)
        diss_df = diss_df.iloc[:, -1:]
        diss_df = diss_df['image_id'].to_list()
        val = len(diss_df)
        
        ### More than 5 images were retrieved
        if val > 5:
            diss_df = random.sample(diss_df, 5)
            tab2.subheader("There are " +str(val)+ " faces with your atributes!")
            tab2.subheader("Here are 5 examples")

            col4,col5,col6,col7,col8 = tab2.columns(5)

            col4.image(Image.open("data/CelebFinderData/img_align_celeba/"  +diss_df[0]))
            col5.image(Image.open("data/CelebFinderData/img_align_celeba/"  +diss_df[1]))
            col6.image(Image.open("data/CelebFinderData/img_align_celeba/"  +diss_df[2]))
            col7.image(Image.open("data/CelebFinderData/img_align_celeba/"  +diss_df[3]))
            col8.image(Image.open("data/CelebFinderData/img_align_celeba/"  +diss_df[4]))

        ### 4 images were retrieved
        elif val == 4:
            tab2.subheader("There are 4 face with your atributes!")

            col9,col10,col11,col12 = tab2.columns(4)

            col9.image(Image.open("data/CelebFinderData/img_align_celeba/"  +diss_df[0]))
            col10.image(Image.open("data/CelebFinderData/img_align_celeba/"  +diss_df[1]))
            col11.image(Image.open("data/CelebFinderData/img_align_celeba/"  +diss_df[2]))
            col12.image(Image.open("data/CelebFinderData/img_align_celeba/"  +diss_df[3]))
        
        ### 3 images were retrieved
        elif val == 3:
            tab2.subheader("There are 3 face with your atributes!")
            col13,col14,col15 = tab2.columns(3)
            col13.image(Image.open("data/CelebFinderData/img_align_celeba/"  +diss_df[0]))
            col14.image(Image.open("data/CelebFinderData/img_align_celeba/"  +diss_df[1]))
            col15.image(Image.open("data/CelebFinderData/img_align_celeba/"  +diss_df[2]))

        ### 2 images were retrieved
        elif val == 2:
            tab2.subheader("There are 2 face with your atributes!")
            col16,col17 = tab2.columns(2)
            col16.image(Image.open("data/CelebFinderData/img_align_celeba/"  +diss_df[0]))
            col17.image(Image.open("data/CelebFinderData/img_align_celeba/"  +diss_df[1]))

        ### 1 image was retrieved
        elif val == 1:
            tab2.subheader("There is 1 face with your atributes!")
            tab2.image(Image.open("data/CelebFinderData/img_align_celeba/"  +diss_df[0]))
        
        ### no image found
        elif val == 0:
                tab2.subheader(("I could not find a face with such attributes. Try again"))
### Last update
tab2.header(" ", divider='rainbow')
tab2.write("Created by: Igor Winek | Last update: 28.10.2023")

########## Bounding Box Tab ##########

### Content
tab3.title("Bounding box finder :man-pouting:")
tab3.write("""Okay from the main tab we can already find out what a bounding box is. But what is it used for? Bounding boxes are widely used in various fields and applications, primarily in computer vision and image processing, but they also have applications in other domains. The main purpose of a bounding box is to enclose and represent the spatial extent or location of an object or region of interest in an image or a two-dimensional space. Here are some common uses of bounding boxes:""")
tab3.write("""1. Object Detection: Bounding boxes are used to identify and locate objects within images or video frames. In object detection tasks, algorithms draw bounding boxes around objects of interest, providing information about the object's position, size, and orientation.""")
tab3.write("""2. Object Localization: Bounding boxes are used for object localization tasks, where the goal is to determine not only the presence of an object but also its precise location within the image. This is commonly used in applications like self-driving cars and robotics.""")
tab3.write("""3. Image Annotation: Bounding boxes are often used for annotating images, making it easier for machine learning models to recognize and classify objects within the images. These annotations can be used for training data for object detection or segmentation tasks.""")
tab3.write("""4. Object Tracking: In computer vision and video analysis, bounding boxes can be used to track the movement of objects across frames in a video sequence. Object tracking algorithms use bounding boxes to keep tabs on the objects of interest.""")
tab3.write("""5. Region of Interest (ROI) Selection: Bounding boxes are used to define regions of interest in an image. For example, in medical imaging, a bounding box can be drawn around a specific area of interest, such as a tumor, to focus on further analysis.""")

tab3.write("""I don't want to bore you with what bounding boxes are used for, just to show how I used them in this model. Let me just say that I used them for the first application mentioned above, which is 'Object Detection'.""")
tab3.subheader("About this model")
tab3.write("""My model uses CNN's popular VGG16 network to detect the position of a face in an image. In short, after the image is processed through the prepared model, a bounding box appears that indicates the most popular place where the face is located. Note the model does not take into account for these moments the situation in which the face is not in the image. With more time I will be able to solve this problem, and what is more, the model will not only search for faces in the images, but will also look for them while the user's camera is turned on.""")
tab3.write("""If you would like to see how I prepared the model you can access it using the button below.""")
tab3.link_button("Go to the model repository", "https://github.com/IgorWinek/Model_BBox_CelebA")

### Model using
tab3.subheader("Using the model")
tab3.write("""In the container below, you can upload a photo with your face on it""")
uploaded_files = tab3.file_uploader("Choose a IMG file", accept_multiple_files=False)

col18,col19 = tab3.columns(2)
col20,col21,col23= tab3.columns(3)

col21.link_button("Generate bounding box", "https://github.com/IgorWinek/Model_BBox_CelebA")

if uploaded_files is not None:
    image = Image.open(uploaded_files)
    col18.image(image, caption='Your image')

if uploaded_files is not None:
    image = Image.open(uploaded_files)
    col19.image(image, caption='Your image')



tab3.header(" ", divider='rainbow')
tab3.write("Created by: Igor Winek | Last update: 29.10.2023")
### Face landmarks
tab4.title("Face landmarks finder :eyes:")
tab4.title("Work in progress :smile:")
tab4.write("Created by: Igor Winek | Last update: 28.10.2023")
### AI about yor face
tab5.title("AI about your face :crystal_ball:")
tab5.title("Work in progress :smile:")
tab5.write("Created by: Igor Winek | Last update: 28.10.2023")
###Face generator by GAN
tab6.title("Face generator :alien:")
tab6.title("Work in progress :smile:")
tab6.write("Created by: Igor Winek | Last update: 28.10.2023")



    