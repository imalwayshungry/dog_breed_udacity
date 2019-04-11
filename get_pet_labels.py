#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                             
# PROGRAMMER: 
# DATE CREATED:                                  
# REVISED DATE: 
# PURPOSE: Create the function get_pet_labels that creates the pet labels from 
#          the image's filename. This function inputs: 
#           - The Image Folder as image_dir within get_pet_labels function and 
#             as in_arg.dir for the function call within the main function. 
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main. 
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0 : pet image label (string).
#
##
# Imports python modules
from os import listdir

# TODO 2: Define get_pet_labels function below please be certain to replace None
#       in the return statement with results_dic dictionary that you create 
#       with this function
# 
def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames 
    of the image files. These pet image labels are used to check the accuracy 
    of the labels that are returned by the classifier function, since the 
    filenames of the images contain the true identity of the pet in the image.
    Be sure to format the pet labels so that they are in all lower case letters
    and with leading and trailing whitespace characters stripped from them.
    (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by the classifier function (string)
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
      List. The list contains for following item:
         index 0 = pet image label (string)
    """
    # Replace None with the results_dic dictionary that you created with this
    # function
    import os
    image_list = listdir(image_dir)
    full_labelz = []
    local_list_inner = []
    for i in image_list:
        ii = os.path.basename(i)
        local_list = ii.split("_")
        keep_adding = True
        list_throttle = 0
        while keep_adding:
            try:
                temp_s = local_list[list_throttle]
                int(temp_s[0]) #***does it start with a string or not?
                keep_adding = False
            except:
                local_list_inner.append(temp_s)
                list_throttle += 1  # ***iterate through file name!
        s = ""
        for j in local_list_inner:
            s +=  j + " "
        del local_list_inner[:]
        s = s.strip()
        file_name = i
        image_label = s
        breed_name = image_label.lower() #**just make them lower case
        name = ii.split(".")
        image_label = name[0]
        full_labelz.append((file_name, breed_name, image_label))

    return full_labelz
