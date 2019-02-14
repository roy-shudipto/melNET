# importing libs
from tkinter import *
import os
import csv


#######################################################################################################################
# Main >>>
def main(classes):
    # Window  Creation: Create Confusion Matrix
    root = Tk()
    root.title("Confusion Matrix Creation")  # Title
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
            pos_class = classes[0].upper()
            neg_class = classes[1].upper()
        else:
            pos_class = classes[1].upper()
            neg_class = classes[0].upper()

        fold_num = 5
        if five_fold:
            for fold in range(fold_num):
                root = os.getcwd() + "/aug_Data/Five_Fold_(Aug)/Fold_"+str(fold+1)+"/Test"
                result_path = root + "/_result.csv"
                conf_mat_path = root + "/conf_mat.csv"
                error_path = root + "/error_analysis.csv"
                err_thresh = 70
                conf_mat_make(result_path, conf_mat_path, error_path, err_thresh, pos_class, neg_class)

        else:
            result_path = os.getcwd() + "/aug_Data/Single_Fold_(Aug)/Test/_result.csv"
            conf_mat_path = os.getcwd() + "/aug_Data/Single_Fold_(Aug)/Test/conf_mat.csv"
            error_path = os.getcwd() + "/aug_Data/Single_Fold_(Aug)/Test/error_analysis.csv"
            err_thresh = 70
            conf_mat_make(result_path, conf_mat_path, error_path, err_thresh, pos_class, neg_class)

    else:
        print("Confusion Matrix is not being SAVED!")
        exit()


def conf_mat_make(result_path, conf_mat_path, error_path, err_thresh, pos_class, neg_class):
    # Result Evaluation
    conf_mat = open(conf_mat_path, 'w')
    error = open(error_path, 'w')

    for thresh in range(0, 105, 5):
        tp = fp = tn = fn = 0
        pos_idx = 1

        with open(result_path) as result:
            result_reader = csv.reader(result, delimiter=',')
            line_count = 0

            for row in result_reader:
                # Setting Headers and positive class
                if line_count == 0:
                    if thresh == 0:
                        conf_mat.write('Threshold, TP, FP, TN, FN, Sensitivity, Specificity, Accuracy\n')
                        error.write(f'{", ".join(row)}' + '\n')
                        if pos_class == str(row[2]):
                            pos_idx = 2
                    line_count += 1

                # Going through every row (starting from 2nd one) and evaluate
                else:
                    truth = row[4].upper()
                    if (float(row[pos_idx]) * 100) >= thresh:
                        decision = pos_class
                        if decision == truth:
                            tp += 1
                        else:
                            fp += 1
                            if thresh == err_thresh:
                                error.write(f'{", ".join(row)}' + '\n')
                    else:
                        decision = neg_class
                        if decision == truth:
                            tn += 1
                        else:
                            fn += 1
                            if thresh == 50:
                                error.write(f'{", ".join(row)}' + '\n')

        # Calculation
        acc = (tp + tn) / (tp + fp + tn + fn)
        sen = tp / (tp + fn)
        spe = tn / (tn + fp)
        # pre = tp / (tp+fp)

        '''print(">>> Threshold: " + str(thresh))
        print('TP: ' + str(tp) + ', FP: ' + str(fp) + ', TN: ' + str(tn) + ', FN: ' + str(fn))
        print('Accuracy: ' + str(acc))
        print('Sensitivity: ' + str(sen))
        print('Specificity: ' + str(spe))
        # print('Precision: ' + str(pre))'''

        # Storing calculations in a file
        conf_mat.write(str(thresh*0.01) + ',' + str(tp) + ',' + str(fp) + ',' + str(tn) + ',' + str(fn) + ',' + str(sen)
                       + ',' + str(spe) + ',' + str(acc) + '\n')


#######################################################################################################################
# Main Call Func. >>>
if __name__ == "__main__":
    main()
