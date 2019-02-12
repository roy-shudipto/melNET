# importing libs
from tkinter import *
import os


#######################################################################################################################
# Main >>>
def main(classes=['cat', 'dog']):
    # Window  Creation: Train to melNET
    root = Tk()
    root.title("Save Confusion Matrix")  # Title
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
    _add_conf_mat = BooleanVar()
    _class_1 = BooleanVar()
    _class_2 = BooleanVar()
    _five_fold = BooleanVar()

    # UI
    Label(root, text="Only 2 classes have been DETECTED!").grid(row=1, column=1)
    Checkbutton(root, text="Create CONFUSION MATRIX", variable=_add_conf_mat).grid(row=2, column=1, sticky=W)
    Label(root, text="Choose the POSITIVE class:").grid(row=3, column=1)
    Checkbutton(root, text=classes[0], variable=_class_1).grid(row=4, column=1, sticky=W)
    Checkbutton(root, text=classes[1], variable=_class_2).grid(row=5, column=1, sticky=W)
    Checkbutton(root, text="Five-Fold (Default: Single-Fold)", variable=_five_fold).grid(row=6, column=1, sticky=W)

    Button(root, text="Quit", command=quit_button_applied, width=7).grid(row=7, column=2, sticky=W)
    Button(root, text="Apply", command=apply_button_applied, width=7).grid(row=7, column=3, sticky=W)

    root.mainloop()

    if applied:
        add_conf_mat = _add_conf_mat.get()
        class_1 = _class_1.get()
        class_2 = _class_2.get()
        five_fold = _five_fold.get()

        if add_conf_mat is False:
            print("Confusion Matrix is not being SAVED!")
            exit()
        if class_1 == class_2:
            print("POSITIVE class has not been chosen correctly!")
            exit()

        if class_1:
            pos_class = classes[0]
        else:
            pos_class = classes[1]

        if five_fold:

        else:
            res_root = os.getcwd() + "/aug_Data/Single_Fold_(Aug)/Test"


    else:
        print("Confusion Matrix is not being SAVED!")
        exit()


#######################################################################################################################
# Main Call Func. >>>
if __name__ == "__main__":
    main()
