#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/classify_images.py
#                                                                             
# PROGRAMMER: 
# DATE CREATED:                                 
# REVISED DATE: 
# PURPOSE: Create a function classify_images that uses the classifier function 
#          to create the classifier labels and then compares the classifier 
#          labels to the pet image labels. This function inputs:
#            -The Image Folder as image_dir within classify_images and function 
#             and as in_arg.dir for function call within main. 
#            -The results dictionary as results_dic within classify_images 
#             function and results for the functin call within main.
#            -The CNN model architecture as model within classify_images function
#             and in_arg.arch for the function call within main. 
#           This function uses the extend function to add items to the list 
#           that's the 'value' of the results dictionary. You will be adding the
#           classifier label as the item at index 1 of the list and the comparison 
#           of the pet and classifier labels as the item at index 2 of the list.
#
##
# Imports classifier function for using CNN to classify images 
from classifier import classifier 
from get_pet_labels import get_pet_labels
from get_input_args import get_input_args
from decimal import getcontext, Decimal
import time
from calculates_results_stats import calculates_results_stats
# TODO 3: Define classify_images function below, specifically replace the None
#       below by the function definition of the classify_images function. 
#       Notice that this function doesn't return anything because the 
#       results_dic dictionary that is passed into the function is a mutable 
#       data type so no return is needed.
#


def classify_images(images_dir, results_dic, model):
    """
    Creates classifier labels with classifier function, compares pet labels to 
    the classifier labels, and adds the classifier label and the comparison of 
    the labels to the results dictionary using the extend function. Be sure to
    format the classifier labels so that they will match your pet image labels.
    The format will include putting the classifier labels in all lower case 
    letters and strip the leading and trailing whitespace characters from them.
    For example, the Classifier function returns = 'Maltese dog, Maltese terrier, Maltese' 
    so the classifier label = 'maltese dog, maltese terrier, maltese'.
    Recall that dog names from the classifier function can be a string of dog 
    names separated by commas when a particular breed of dog has multiple dog 
    names associated with that breed. For example, you will find pet images of
    a 'dalmatian'(pet label) and it will match to the classifier label 
    'dalmatian, coach dog, carriage dog' if the classifier function correctly 
    classified the pet images of dalmatians.
     PLEASE NOTE: This function uses the classifier() function defined in 
     classifier.py within this function. The proper use of this function is
     in test_classifier.py Please refer to this program prior to using the 
     classifier() function to classify images within this function 
     Parameters: 
      images_dir - The (full) path to the folder of images that are to be
                   classified by the classifier function (string)
      results_dic - Results Dictionary with 'key' as image filename and 'value'
                    as a List. Where the list will contain the following items: 
                  index 0 = pet image label (string)
                --- where index 1 & index 2 are added by this function ---
                  NEW - index 1 = classifier label (string)
                  NEW - index 2 = 1/0 (int)  where 1 = match between pet image
                    and classifer labels and 0 = no match between labels
      model - Indicates which CNN model architecture will be used by the 
              classifier function to classify the pet images,
              values must be either: resnet alexnet vgg (string)
     Returns:
           None - results_dic is mutable data type so no return needed.         
    """

def contains_word(s, w):
    return (' ' + w + ' ') in (' ' + s + ' ')

def do_predictions(models, target_tuple, is_dog, results_class, doggie_namez):
    for model_name in models:
        correct_preds = 0
        false_preds = 0
        for xx in target_tuple:
            results_list = []  #***new list struct for each image!
            predict_from_model = classifier(img_path + "/" + xx[0], model_name)
            temper = xx[1].split(" ")
            results_list.append(xx[1]) #***record actual image label
            prediction_truth = "False"
            is_dog_predict = False
            for local_xx in temper:
                if local_xx in predict_from_model:
                    prediction_truth = "True"
            for local_xx in temper:
                if local_xx.capitalize() in predict_from_model:
                    prediction_truth = "True"
            if prediction_truth == "True":
                results_list.append(1) #***a prediction match!
            else:
                results_list.append(0) #***NOT A prediction match!

            temper2 = predict_from_model.split(" ")
            for local_xx in temper2:
                for dog_name_ind in doggie_namez:
                    if contains_word(dog_name_ind, local_xx.lower()):
                        is_dog_predict = True

            results_list.append(is_dog) #***IS PICTURE an actual doggie?
            if is_dog_predict:
                results_list.append(1)
            else:
                results_list.append(0)

            if is_dog:
                report_s = "Identified Dog Pic: "
            else:
                report_s = "Identified Non Dog Pic: "
            print (report_s + xx[
                0] + " Prediction: " + predict_from_model + " Predic Success: " + prediction_truth)
            if prediction_truth == "False":
                false_preds += 1
                results_list.append(0) #***record bad prediction
            if prediction_truth == "True":
                correct_preds += 1
                results_list.append(1) #***record good prediction
            results_class.add_stats(xx[0], results_list)  # ***RECORD OUR STATS in dict per project requirements!
            if is_dog_predict:
                print ("Classifier Predicted A Doggie: " + predict_from_model)
            else:
                print ("Classifier Predicted Not A Doggie: " + predict_from_model)
        print ("\n")
        print ("Model: " + model_name + " Correct Predictions: " + str(correct_preds) + " False Predictions: " + str(
            false_preds))
        print ("Percentage of Accuracy: ")
        image_count = len(target_tuple)
        percent = Decimal(correct_preds) / Decimal(image_count)
        print ("Total Images: " + str(image_count) + " Accuracy of Prediction Percentage: " + "{:.2%}".format(percent))

argz_present = False

argz = get_input_args()

if len(argz):
    argz_present = True

if argz_present: #***default actions if no command line args provided!

    try:
        dogfile = argz["dogfile"]
    except:
        pass

    try:
        arch = argz["arch"]
    except:
        pass

    try:
        pet_images = argz["pet_images"]
    except:
        pass

if argz_present == False:  #***default configurations
    fh = open('dognames.txt', 'r')
    dog_namez = fh.read()
    fh.close()

    image_dir = "pet_images"
    model_name = "alexnet"
    img_path = image_dir

if argz_present:
    try:
        fh = open(dogfile, 'r')
        dog_namez = fh.read()
        fh.close()

        image_dir = pet_images
        model_name = arch
        img_path = image_dir
        print ("Command Line Args: " + "image dir: " + image_dir + " model name: " + model_name + " file: " + dogfile)

    except Exception as e:
        import sys
        print ("ERROR: Problem With Command Line Arguments")
        sys.exit(1)

my_dog_images_dict = {}

type_tuple = get_pet_labels(image_dir)  #***type tuple contains actual image labels

doggie_tuple = []
not_doggie_tuple = []

dog_namez = dog_namez.replace(",", "")  #contains list with broken up dog names!
dog_namez = dog_namez.split("\n")

for x in type_tuple:
    if x not in doggie_tuple:
            if x[1] in dog_namez:
                print ("Dog Name Label Found: " + x[2])
                doggie_tuple.append(x)      #identified dog names in file dir

print "\n"

for x in type_tuple:
    if x not in doggie_tuple:
        print ("Non Dog Label: " + x[2])
        not_doggie_tuple.append(x)  #identified not dog names in file dir

print ("\n")

print ("SUCCESS: Dog Names Identified")

for xx in doggie_tuple:
    print ("Identified Dog Pic: " + xx[0])

print ("-------")
print ("PREDICTIONS OF DOG LABELS")
print ("-------")

print ("Number of Images: " + str(len(doggie_tuple)))

models = []

if argz_present == False:  #***IF no CL args just scan with all models!
    models.append("resnet")
    models.append("alexnet")
    models.append("vgg")

if argz_present:
    models.append(model_name)

results_class = calculates_results_stats()

start = time.time()
print ("Predictions with Dog Images: " + "\n")
do_predictions(models, doggie_tuple, 1, results_class, dog_namez)
end = time.time()
print ("Time Taken for Prediction of Dog Images: " + str(end - start))

start = time.time()
print ("Predictions with Non Dog Images: " + "\n")
do_predictions(models, not_doggie_tuple,0, results_class, dog_namez)
end = time.time()
print ("Time Taken for Prediction of Non Dog Images: " + str(end - start))