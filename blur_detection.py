import cv2


def variance_of_laplacian(image):
    return cv2.Laplacian(image, cv2.CV_64F).var()


def main():
    image = cv2.imread("sharp.jpg")
    cv2.imshow("Image", image)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    fm = variance_of_laplacian(gray)

    print(fm)
    cv2.waitKey(0)


# Main Call Func. >>>
if __name__ == "__main__":
    main()
