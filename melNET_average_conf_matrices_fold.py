# importing libs
import os
import csv
import numpy as np


#######################################################################################################################
# Main >>>
def main():
    avg_conf = open(os.getcwd() + "/avg_conf.csv", 'w')
    avg_conf.write('Threshold, Specificity, FPR, TPR, AUC, Accuracy\n')

    specificity = np.zeros((1, 21))
    TPR = np.zeros((1, 21))
    accuracy = np.zeros((1, 21))

    for fold in range(5):
        temp_specificity = []
        temp_TPR = []
        temp_accuracy = []
        with open(os.getcwd() + "/Fold_0" + str(fold+1) + "/conf_mat.csv") as conf:
            conf_reader = csv.reader(conf, delimiter=',')
            line_count = 0
            for row in conf_reader:
                if line_count == 0:  # skipping 1st row
                    line_count += 1
                else:
                    temp_specificity.append(float(row[6]))
                    temp_TPR.append(float(row[5]))
                    temp_accuracy.append(float(row[7]))

        np.reshape(temp_specificity, (1, -1))
        np.reshape(temp_TPR, (1, -1))
        np.reshape(temp_accuracy, (1, -1))

        specificity += temp_specificity
        TPR += temp_TPR
        accuracy += temp_accuracy

    specificity /= 5.0
    TPR /= 5.0
    accuracy /= 5.0

    np.reshape(specificity, (1, -1))
    np.reshape(TPR, (1, -1))
    np.reshape(accuracy, (1, -1))

    x = 0
    for thresh in range(0, 105, 5):
        avg_conf.write(str(thresh/100.0) + ',' + str(specificity[0][x]) + ',' + str(1-specificity[0][x]) +
                       ',' + str(TPR[0][x]) + ',' + 'AUC' + ',' + str(accuracy[0][x]) + '\n')
        x += 1

    avg_conf.close()


#######################################################################################################################
# Main Call Func. >>>
if __name__ == "__main__":
    main()
