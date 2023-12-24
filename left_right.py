import csv
import os
import shutil
import math


def find():

    ##########################
    # Read the labels file
    ##########################

    file_path = ('C:\\Users\\oisin\\Documents\\University\\3rd Year\\Final Year Project\\Retinal Imaging FYP Shared '
            'Folder\\Datasets\\Brazilian\\labels.csv')

    rows = []

    with open(file_path, 'r') as file:
        csvreader = csv.reader(file)
        header = next(csvreader)
        for row in csvreader:
            rows.append(row)

    column = header.index('exam_eye')
    # 1 = right, 2 = left
    #print(column)

    right = []
    left = []
    for row in rows:
        if row[column] == '1':
            right.append(row[0])
        elif row[column] == '2':
            left.append(row[0])

    print(len(right))
    print(len(left))

    file.close()


    #######################
    # Find the images
    #######################

    folder_path = ('C:\\Users\\oisin\\Documents\\University\\3rd Year\\Final Year Project\\Retinal Imaging FYP Shared '
            'Folder\\Datasets\\Brazilian\\full_data_set\\fundus_photos')

    data = '\\small_dataset'
    class1 = '\\right'
    class2 = '\\left'

    data_folder = ('C:\\Users\\oisin\\Documents\\University\\3rd Year\\Final Year Project\\'
            'Retinal Imaging FYP Shared Folder\\Datasets\\Brazilian' + data)

    # 80% training, 10% test, 10% validation
    training_folder = data_folder + '\\training'
    test_folder = data_folder + '\\test'
    validation_folder = data_folder + '\\validation'

    files = os.listdir(folder_path)

    if os.path.isdir(data_folder):
        print('Folder already exists')
        exit()
    else:
        os.mkdir(data_folder)
        os.mkdir(training_folder)
        os.mkdir(test_folder)
        os.mkdir(validation_folder)

    for folder in os.listdir(data_folder):
        os.mkdir(data_folder + '\\' + folder + class1)
        os.mkdir(data_folder + '\\' + folder + class2)

    #############################
    # Organise data
    ##############################

    # for small dataset
    training_number = 40
    test_number = training_number + 20
    validation_number = test_number + 20

    #training_number = math.ceil((len(files)/100)*80) #80%
    #test_number = math.floor((len(files) - training_number) / 2) + training_number
    #validation_number = len(files)

    current_number = 0

    for file in files:
        full_file_path = os.path.join(folder_path, file)
        file_name = file.removesuffix('.jpg')

        if current_number <= training_number:
            if os.path.isfile(full_file_path) and file_name in right:
                shutil.copy(full_file_path, training_folder + class1)
            elif os.path.isfile(full_file_path) and file_name in left:
                shutil.copy(full_file_path, training_folder + class2)

        elif training_number < current_number <= test_number:
            if os.path.isfile(full_file_path) and file_name in right:
                shutil.copy(full_file_path, test_folder + class1)
            elif os.path.isfile(full_file_path) and file_name in left:
                shutil.copy(full_file_path, test_folder + class2)

        elif test_number < current_number <= validation_number:
            if os.path.isfile(full_file_path) and file_name in right:
                shutil.copy(full_file_path, validation_folder + class1)
            elif os.path.isfile(full_file_path) and file_name in left:
                shutil.copy(full_file_path, validation_folder + class2)

        current_number = current_number + 1


    #
    # destination_size = len(os.listdir(destination_folder))
    # if destination_size > 1:
    #     print(f'Successfully added {destination_size} to destination folder')

    #print(os.listdir(folder_path))


