# importing scripts
import melNET_test_src

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
    root.title("TEST with melNET")  # Title
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
    _save_performance = BooleanVar()
    _show_detection = BooleanVar()

    # UI
    Checkbutton(root, text="Five-Fold (Default: Single-Fold)", variable=_five_fold).grid(row=1, column=1, sticky=W)
    Label(root, text="For Single-Fold, keep class folders in: aug_Data/Single_Fold_(Aug)/Test ").grid(row=2, column=1)
    Checkbutton(root, text="Save Performance Report", variable=_save_performance).grid(row=4, column=1, sticky=W)
    Checkbutton(root, text="View Detection", variable=_show_detection).grid(row=5, column=1, sticky=W)

    Button(root, text="Quit", command=quit_button_applied, width=15).grid(row=7, column=2, sticky=W)
    Button(root, text="Apply", command=apply_button_applied, width=15).grid(row=7, column=3, sticky=W)

    root.mainloop()

    if applied:
        five_fold = _five_fold.get()
        save_performance = _save_performance.get()
        show_detection = _show_detection.get()

        # Managing directories
        accessories_path = os.getcwd() + "/Accessories"   # same name in malNET_train_src
        aug_data_path = os.getcwd() + "/aug_Data"

        if tf.gfile.Exists(accessories_path) and tf.gfile.Exists(aug_data_path):
            if five_fold:
                fold_num = 5  # Five-Fold
                root = aug_data_path + "/Five_Fold_(Aug)"
                for num in range(fold_num):
                    test_path = root + "/Fold_" + str(num+1) + "/Test/mountain_bikes"
                    weight_path = accessories_path + "/Five_Fold_Trained/Trained_Fold_" + str(num+1)
                    if tf.gfile.Exists(test_path) and tf.gfile.Exists(weight_path):
                        melNET_test_src.main(test_path, weight_path, save_performance, show_detection)
                    else:
                        print("Either [Test Data] or [Weight] is NOT available!")
                        exit()
            else:  # Single-Fold
                root = aug_data_path + "/Single_Fold_(Aug)"
                test_path = root + "/Test"
                weight_path = accessories_path + "/Single_Fold_Trained"
                if tf.gfile.Exists(test_path) and tf.gfile.Exists(weight_path):
                    melNET_test_src.main(test_path, weight_path, save_performance, show_detection)
                else:
                    print("Either [Test Data] or [Weight] is NOT available!")
                    print("For Single-Fold, keep class folders in: aug_Data/Single_Fold_(Aug)/Test ")
                    exit()
        else:
            print("Necessary Files are NOT found!")
            exit()

    else:
        print("melNET has not been TESTED!")
        exit()
#######################################################################################################################


# Main Call Func. >>>
if __name__ == "__main__":
    main()
