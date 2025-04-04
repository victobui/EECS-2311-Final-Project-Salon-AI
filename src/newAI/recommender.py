import requests
from PIL import Image, ImageDraw,ImageFont
import face_recognition
import pandas as pd
import numpy as np
from os.path import basename
import math
import pathlib
from pathlib import Path
import os
import random
import matplotlib.pyplot as plt
import uuid
from hairstyle_descriptions import get_hairstyle_description

image_dir = "data/pics"

style_df = pd.DataFrame()
style_df = pd.DataFrame(columns = ['face_shape','hair_length','location','filename','score'])

def process_rec_pics(style_df,image_dir = "data/pics"):
    image_root = "data/rec_pics" 
    dir_list = ['heart','long','oval','square','round']
    filenum = 0   
    for dd in dir_list: 
            image_dir = image_root + '/' + dd
            sub_dir = [q for q in pathlib.Path(image_dir).iterdir() if q.is_dir()]
            #print(sub_dir)
            start_j = 0
            end_j = len(sub_dir)

            for j in range(start_j, end_j):
                    #images_dir = [p for p in pathlib.Path(sub_dir[j]).iterdir() if p.is_file()]

                    for p in pathlib.Path(sub_dir[j]).iterdir():
                        shape_array= []

                        face_shape = os.path.basename(os.path.dirname(os.path.dirname(p)))
                        hair_length = os.path.basename(os.path.dirname(p)) 
                        sub_dir_file = p
                        face_file_name = os.path.basename(p)

                        shape_array.append(face_shape)
                        shape_array.append(hair_length)
                        shape_array.append(sub_dir_file)
                        shape_array.append(face_file_name)  
                        
                        random.seed(filenum)  # this keeps the score the same each time I run it
                        rand = random.randint(25,75)  # make a random score to start the rec. engine
                        shape_array.append(rand)

                        style_df.loc[filenum] = np.array(shape_array)

                        filenum += 1
    return(filenum)

process_rec_pics(style_df)

style_df

def run_recommender(test_shape):
    name = input("What is your name? ")
    print("Hello, %s." % name)
    face_shape_input = test_shape
    if face_shape_input not in ['heart','long','oval','round','square']:
        face_shape_input = input("What is your face shape?")
    updo_input = input("Would you like to see up-dos? (Y/N)")
    if updo_input in ['n','no','N','No','NO']:
            hair_length_input = input("Is your hair short (shoulder-length shorter) or long?")
            if hair_length_input in ['short','Short','s','S']:
                hair_length_input = 'Short'
            if hair_length_input in ['long','longer','l','L']:
                hair_length_input = 'Long'
    else: hair_length_input = 'Updo'
    
    print(hair_length_input)
    print(face_shape_input)
    r = 6
    
    n_col = 3
    n_row = 2
    recommended_df = style_df.loc[(style_df['face_shape'] ==face_shape_input) & (style_df['hair_length']==       hair_length_input)].sort_values('score', ascending = 0).reset_index(drop=True)
    recommended_df = recommended_df.head(r)
    
    plt.figure(figsize=(5 * n_col, 4 * n_row))
    plt.subplots_adjust(bottom=0, left=.01, right=.99, top=.90, hspace=.35)    
    font = ImageFont.truetype("fonts/Arial.ttf", 60)
    for p in range(0,r):
        idea = str(recommended_df.iloc[p]['location'] )
        idea = idea.replace('\\', '/')
        img = Image.open(idea)
        plt.subplot(n_row, n_col, p+1 )
        draw = ImageDraw.Draw(img)
        plt.title(p+1,fontsize = 40)
        plt.xlabel(recommended_df.iloc[p]['score'],fontsize = 20)
        plt.xticks([])
        plt.yticks([])
        plt.imshow(img)
        img.close()

    plt.show()
    
    fav = input("Which style is your favorite? ")
    yuck = input("Which style is your least favorite? ")
    # update scores based on fav/least fav

    for row in range(0,r):
        fn = recommended_df.at[row,'filename']
        srow = style_df.index[style_df['filename'] == fn].tolist()
        srow = srow[0]
        #print('Srow %s' %srow)
        row += 1
        if str(row) == str(fav):
            style_df.at[srow,'score'] =  style_df.at[srow,'score'] + 5
        if str(row) == str(yuck):
            style_df.at[srow,'score'] =  style_df.at[srow,'score'] - 5

def run_recommender_face_shape(test_shape, style_df, hair_length_input):
    face_shape_input = test_shape
    r = 1  # Number of recommendations
    
    # Get recommended hairstyles sorted by score
    recommended_df = style_df.loc[(style_df['face_shape'] == face_shape_input) & 
                                  (style_df['hair_length'] == hair_length_input)].sort_values('score', ascending=0).reset_index(drop=True)
    recommended_df = recommended_df.head(r)
    
    # Create a new figure with more space for descriptions
    fig = plt.figure(figsize=(15, 12))
    
    # Create a directory for output images if it doesn't exist
    os.makedirs("output", exist_ok=True)
    
    # Set up the grid layout
    n_col = 2
    n_row = 3
    
    # Loop through each recommended style and add to plot with description
    for p in range(0, r):
        # Get image path
        idea = str(recommended_df.iloc[p]['location'])
        idea = idea.replace('\\', '/')
        filename = os.path.basename(idea)
        
        # Get description for this hairstyle
        description = get_hairstyle_description(face_shape_input, hair_length_input, filename)
        
        # Create subplot
        ax = plt.subplot(n_row, n_col, p+1)
        
        # Display image
        img = Image.open(idea)
        ax.imshow(img)
        
        # Create title with hairstyle name
        ax.set_title(f"{description['name']}", fontsize=14, fontweight='bold')
        
        # Add description text below image
        desc_text = f"Description: {description['description']}\n\nBarber Instructions: {description['barber_instructions']}"
        
        # Remove axis ticks
        ax.set_xticks([])
        ax.set_yticks([])
        
        # Add description as text below image
        plt.figtext(ax.get_position().x0, ax.get_position().y0 - 0.07, 
                   desc_text, fontsize=10, wrap=True, 
                   bbox=dict(facecolor='white', alpha=0.8, boxstyle='round,pad=0.5'))
    
    # Set the overall title
    plt.suptitle(f"Recommended Hairstyles for {face_shape_input.title()} Face Shape", 
                fontsize=18, fontweight='bold', y=0.98)
    
    # Add some space between subplots
    plt.subplots_adjust(hspace=0.4, wspace=0.3)
    
    # Save the figure
    img_id = uuid.uuid4()
    img_filename = f"output/output_{img_id}.png"
    plt.savefig(img_filename, bbox_inches='tight', dpi=150)
    plt.close(fig)
    
    return img_filename

