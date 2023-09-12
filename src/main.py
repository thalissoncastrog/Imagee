from rembg import remove
from PIL import Image
import sys

def RemoveBackgroundPicture(inputPath, outputPath):
    originalImg = Image.open(inputPath)
    noBackgroundImg = remove(originalImg)
    noBackgroundImg.save(outputPath)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python main.py <inputPath> <outputPath>")
        sys.exit(1)

    inputPath = sys.argv[1]
    outputPath = sys.argv[2]

RemoveBackgroundPicture(inputPath, outputPath)