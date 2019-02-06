# importing scripts
import melNET_augData
import melNET_train
import melNET_test

# importing libs
from tkinter import *


#######################################################################################################################
# Main >>>
def main():
    # Window  Creation: Welcome to melNET
    root = Tk()
    root.title("melNET")  # Title
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

    # Check Box variables
    _aug_data = BooleanVar()
    _train = BooleanVar()
    _test = BooleanVar()

    # UI Creation
    Label(root, text="Welcome to melNET!").grid(row=0, column=2)

    Checkbutton(root, text="Augment Data", variable=_aug_data).grid(row=2, sticky=W)
    Checkbutton(root, text="TRAIN with melNET", variable=_train).grid(row=4, sticky=W)
    Checkbutton(root, text="TEST with melNET", variable=_test).grid(row=6, sticky=W)

    Label(root, text="It is required to keep class-folders in the [Data] directory").grid(row=8)

    Button(root, text="Quit", command=quit_button_applied, width=15).grid(row=11, column=1, sticky=W)
    Button(root, text="Apply", command=apply_button_applied, width=15).grid(row=11, column=2, sticky=W)

    root.mainloop()

    if applied:
        aug_data = _aug_data.get()
        train = _train.get()
        test = _test.get()

        if aug_data is False and train is False and test is False:
            print("Nothing is Selected!")
            exit()
    else:
        print("melNET has not been Used!")
        exit()

    # Data Augmentation:
    if aug_data:
        print("Augmentation Started...")
        melNET_augData.main()
        print("Augmentation Done!\n")

    # TRAIN with melNET
    if train:
        print("Training Started...")
        melNET_train.main()
        print("Training Done!\n")

    # TEST with melNET
    if test:
        print("Testing Started...")
        melNET_test.main()
        print("Testing Done!\n")
#######################################################################################################################


# Main Call Func. >>>
if __name__ == "__main__":
    main()
