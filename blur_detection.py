import cv2
import os


def main(blur_thresh=7):
    folder_list = []
    if len(os.listdir("Data")) == 0:
        print("[Data] folder is empty!\n")
        exit()
    else:
        for entry_name in os.listdir("Data"):
            folder_list.append(entry_name)

    counter = 0
    for folder in folder_list:
        folder_path = "Data/" + folder
        for file_name in os.listdir(folder_path):
            img = cv2.imread(os.path.join(folder_path, file_name), cv2.IMREAD_COLOR)

            img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            var = variance_of_laplacian(img_gray)

            if var < blur_thresh:
                counter += 1
                '''cv2.imshow("Image", img)
                cv2.waitKey(0)
                cv2.destroyAllWindows()'''
                os.remove(os.path.join(folder_path, file_name))
                print("File Name: " + str(file_name) + " >> Blur detected >> Removed!")
                print("Original Var: " + str(var))
                print('--------------------------------')
    print("Total " + str(counter) + " files removed because of BLUR!")


def variance_of_laplacian(image):
    return cv2.Laplacian(image, cv2.CV_64F).var()


# Main Call Func. >>>
if __name__ == "__main__":
    main()
