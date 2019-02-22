# importing libs
import os
import shutil
import csv


def main():
    # removing old data and creating new directories
    if os.path.exists(os.getcwd() + "/Data"):
        shutil.rmtree(os.getcwd() + "/Data")
    os.makedirs(os.getcwd() + "/Data")
    os.makedirs(os.getcwd() + "/Data/melanoma")
    os.makedirs(os.getcwd() + "/Data/nevus")

    # reading from .csv file
    class_path = os.getcwd() + "/PH2_dataset.csv"
    with open(class_path) as classification:
        classification_reader = csv.reader(classification, delimiter=',')
        line_count = 0
        mel_count = 0
        nev_count = 0
        for row in classification_reader:
            # Skipping 1st 13 lines
            if line_count < 13:
                line_count += 1
                continue

            else:
                print(">>> " + row[0])
                type = row[4]
                if type is "X":
                    dst = os.getcwd() + "/Data/melanoma"
                    print("Melanoma Entry")
                    mel_count += 1
                else:
                    dst = os.getcwd() + "/Data/nevus"
                    print("Nevus Entry")
                    nev_count += 1

                src = os.getcwd() + "/PH2 Dataset images/" + row[0] + "/" + row[0] + "_Dermoscopic_Image/" \
                      + row[0] + ".bmp"

                shutil.copy(src, dst)
                line_count += 1

                print("Melanoma Count: " + str(mel_count))
                print("Nevus Count: " + str(nev_count))
                print("------------------------------------")


#######################################################################################################################
# Main Call Func. >>>
if __name__ == "__main__":
    main()
