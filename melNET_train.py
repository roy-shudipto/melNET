# importing scripts
import melNET_train_src

# importing libs
import os
from tkinter import *
import tensorflow as tf
from tensorflow.python.platform import gfile

#######################################################################################################################
# Main >>>
def main():
    # Window  Creation: Train to melNET
    root = Tk()
    root.title("TRAIN with melNET")  # Title
    global applied
    applied = False

    def apply_button_applied():
        root.destroy()
        global applied
        applied = True

    def quit_button_applied():
        root.destroy()
        global applied
        applied = False

    # Variables
    _five_fold = BooleanVar()
    _learning_rate1 = BooleanVar()
    _learning_rate2 = BooleanVar()
    _learning_rate3 = BooleanVar()
    _learning_rate4 = BooleanVar()
    _batch_size = IntVar(0)
    _iteration = IntVar(0)

    # UI
    Checkbutton(root, text="Five-Fold (Default: Single-Fold)", variable=_five_fold).grid(row=1, column=3, sticky=W)

    Label(root, text="Batch Size: ").grid(row=4, column=0)
    Label(root, text="(Default: 100)").grid(row=5, column=0)
    Entry(root, textvariable=_batch_size).grid(row=4, column=1)

    Label(root, text="Number of Iteration: ").grid(row=6, column=0)
    Label(root, text="(Default: 4000)").grid(row=7, column=0)
    Entry(root, textvariable=_iteration).grid(row=6, column=1)

    Checkbutton(root, text="Learning Rate: 0.005", variable=_learning_rate1).grid(row=8, column=0, sticky=W)
    Checkbutton(root, text="Learning Rate: 0.001", variable=_learning_rate2).grid(row=9, column=0, sticky=W)
    Checkbutton(root, text="Learning Rate: 0.01", variable=_learning_rate3).grid(row=10, column=0, sticky=W)
    Checkbutton(root, text="Learning Rate: 0.015", variable=_learning_rate4).grid(row=11, column=0, sticky=W)
    Label(root, text="If NONE or more than one is chosen, default Learning Rate is 0.01").grid(row=12, column=0)

    Button(root, text="Quit", command=quit_button_applied, width=15).grid(row=14, column=2, sticky=W)
    Button(root, text="Apply", command=apply_button_applied, width=15).grid(row=14, column=3, sticky=W)

    root.mainloop()

    if applied:
        five_fold = _five_fold.get()

        learning_rate1 = _learning_rate1.get()
        learning_rate2 = _learning_rate2.get()
        learning_rate3 = _learning_rate3.get()
        learning_rate4 = _learning_rate4.get()

        batch_size = _batch_size.get()
        iteration = _iteration.get()

        # Default Values
        if batch_size is 0:
            batch_size = 100
        if iteration is 0:
            iteration = 4000

        if learning_rate1:
            learning_rate = 0.005
        elif learning_rate2:
            learning_rate = 0.001
        elif learning_rate3:
            learning_rate = 0.01
        elif learning_rate4:
            learning_rate = 0.015

        learning_rate_sum = int(learning_rate1) + int(learning_rate2) + int(learning_rate3) + int(learning_rate4)

        if learning_rate_sum > 1 or learning_rate_sum == 0:
            learning_rate = 0.01

        # Managing directories
        accessories_path = os.getcwd() + "/Accessories"   # same name in malNET_train_src
        if tf.gfile.Exists(accessories_path):
            tf.gfile.DeleteRecursively(accessories_path)

        tf.gfile.MakeDirs(accessories_path)

        # Save hyper-parameters
        hyper_path = accessories_path + "/hyper_parameters.csv"
        hyper = open(hyper_path, 'w')
        hyper.write('Learning Rate, Iterations, Batch Size, Five-Fold\n' + str(learning_rate) + ',' + str(iteration) +
                    ',' + str(batch_size) + ',' + str(five_fold))
        hyper.close()

        # Getting Train-data directory
        aug_data_path = os.getcwd() + "/aug_Data"
        if tf.gfile.Exists(aug_data_path):
            if five_fold:
                fold_num = 5  # Five-Fold
                root = aug_data_path + "/Five_Fold_(Aug)"
                for num in range(fold_num):
                    train_path = root + "/Fold_" + str(num+1) + "/Train"
                    weight_path = accessories_path + "/Five_Fold_Trained/Trained_Fold_" + str(num+1)
                    tf.gfile.MakeDirs(weight_path)
                    if tf.gfile.Exists(train_path):
                        melNET_train_src.main(train_path, weight_path, float(learning_rate), int(batch_size),
                                              int(iteration))
                    else:
                        print("Training Data is NOT available!")
            else:  # Single-Fold
                root = aug_data_path + "/Single_Fold_(Aug)"
                train_path = root + "/Train/"
                weight_path = accessories_path + "/Single_Fold_Trained"
                tf.gfile.MakeDirs(weight_path)
                if tf.gfile.Exists(train_path):
                    melNET_train_src.main(train_path, weight_path, float(learning_rate), int(batch_size), int(iteration))
                else:
                    print("Training Data is NOT available!")
        else:
            print("Augmented Data is NOT found!")
            exit()

    else:
        print("melNET has not been TRAINED!")
        exit()
#######################################################################################################################


# Main Call Func. >>>
if __name__ == "__main__":
    main()

