import csv
import os
import shutil
import math


def find():

    ##########################
    # Read the labels file
    ##########################

    label_path = ('C:\\Users\\oisin\\Documents\\University\\3rd Year\\Final Year Project\\Retinal Imaging FYP Shared '
            'Folder\\Datasets\\Brazilian\\labels.csv')

    rows = []

    with open(label_path, 'r') as file:
        csvreader = csv.reader(file)
        header = next(csvreader)
        for row in csvreader:
            rows.append(row)

    column1 = header.index('diabetic_retinopathy')
    # 1 = yes, 0 = no

    # This is the last disease listed in the labels file
    column2 = header.index('other')

    dr = []
    healthy = []

    for row in rows:
        if row[column1] == '1':
            dr.append(row[0])
        elif all(element == '0' for element in row[column1:column2]):
            healthy.append(row[0])

    file.close()

    #######################
    # Find the images and make new folder structure
    #######################

    folder_path = ('C:\\Users\\oisin\\Documents\\University\\3rd Year\\Final Year Project\\Retinal Imaging FYP Shared '
            'Folder\\Datasets\\Brazilian\\full_data_set\\fundus_photos')

    data = 'DR_vs_healthy\\'
    class1 = '\\DR'
    class2 = '\\healthy'

    # destination_folder = ('C:\\Users\\oisin\\Documents\\University\\3rd Year\\Final Year Project\\'
    #         'Retinal Imaging FYP Shared Folder\\Datasets\\Brazilian\\' + data)

    # for small dataset
    destination_folder = ('C:\\Users\\oisin\\Documents\\University\\3rd Year\\Final Year Project\\'
                          'Retinal Imaging FYP Shared Folder\\Datasets\\Brazilian\\smaller_datasets\\' + data)

    # 80% training, 10% test, 10% validation
    training_folder = destination_folder + 'training'
    test_folder = destination_folder + 'test'
    validation_folder = destination_folder + 'validation'

    files = os.listdir(folder_path)

    if os.path.isdir(destination_folder):
        print('Folder already exists')
        exit()
    else:
        os.mkdir(destination_folder)
        os.mkdir(training_folder)
        os.mkdir(test_folder)
        os.mkdir(validation_folder)

    for folder in os.listdir(destination_folder):
        os.mkdir(destination_folder + folder + class1)
        os.mkdir(destination_folder + folder + class2)

    #############################
    # Organise data
    ##############################

    # for small dataset
    training_number = 40
    test_number = training_number + 20
    validation_number = test_number + 20

    #
    # training_number = math.ceil((len(files)*0.6)) #80%
    # test_number = math.floor((len(files) - training_number) / 2) + training_number
    # validation_number = len(files)

    current_number = 0

    for file in files:
        full_file_path = os.path.join(folder_path, file)
        file_name = file.removesuffix('.jpg')

        if dr.count(file_name) != 0 or healthy.count(file_name) != 0:
            continue

        if current_number <= training_number:
            if os.path.isfile(full_file_path) and file_name in dr:
                shutil.copy(full_file_path, training_folder + class1)
            elif os.path.isfile(full_file_path) and file_name in healthy:
                shutil.copy(full_file_path, training_folder + class2)

        elif training_number < current_number <= test_number:
            if os.path.isfile(full_file_path) and file_name in dr:
                shutil.copy(full_file_path, test_folder + class1)
            elif os.path.isfile(full_file_path) and file_name in healthy:
                shutil.copy(full_file_path, test_folder + class2)

        elif test_number < current_number <= validation_number:
            if os.path.isfile(full_file_path) and file_name in dr:
                shutil.copy(full_file_path, validation_folder + class1)
            elif os.path.isfile(full_file_path) and file_name in healthy:
                shutil.copy(full_file_path, validation_folder + class2)

        current_number = current_number + 1


    #
    # destination_size = len(os.listdir(destination_folder))
    # if destination_size > 1:
    #     print(f'Successfully added {destination_size} to destination folder')

    #print(os.listdir(folder_path))


