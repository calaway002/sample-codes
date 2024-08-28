import cv2
import numpy as np

def main():
    print("Hello, World!")

    image = np.zeros((512, 512, 3), np.uint8)
    print("Black image created.")

    cv2.imshow('Black Image', image)
    print("Image displayed.")

    cv2.waitKey(5000)  # Wait indefinitely for a key event.
    print("Key pressed, closing window.")

    cv2.destroyAllWindows()
    print("All windows closed.")

if __name__ == "__main__":
    main()
