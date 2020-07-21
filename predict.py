from tflite_runtime.interpreter import Interpreter
import argparse
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt # plt 用于显示图片
import matplotlib.image as mpimg # mpimg 用于读取图片
def set_input_tensor(interpreter, image):
    """Sets the input tensor."""
    tensor_index = interpreter.get_input_details()[0]['index']
    input_tensor = interpreter.tensor(tensor_index)()[0]
    input_tensor[:,:]= image
def get_output_tensor(interpreter, index):
    """Returns the output tensor at the given index."""
    output_details = interpreter.get_output_details()[index]
    tensor = np.squeeze(interpreter.get_tensor(output_details['index']))
    return tensor


def prediect(interpreter, image):
    set_input_tensor(interpreter, image)
    interpreter.invoke()
    classes = get_output_tensor(interpreter, 0)


    print("classes:", classes)


def main():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument(
        '--model', help='File path of .tflite file.', required=True)
    parser.add_argument(
        '--threshold',
        help='Score threshold for detected objects.',
        required=False,
        type=float,
        default=0.4)
    args = parser.parse_args()
    interpreter = Interpreter(args.model)
    interpreter.allocate_tensors()
    print("input_details", interpreter.get_input_details())
    _, input_height, input_width, _ = interpreter.get_input_details()[0]['shape']
    print("output_details:", interpreter.get_output_details())

    test_image = "./yellow.png"
    image = Image.open(test_image).convert('RGB').resize(
        (input_width, input_height), Image.ANTIALIAS)
    print("input_width",input_width)
    print("input_height",input_height)
    prediect(interpreter, image)
    # plt.imshow(image) # 显示图片
    # plt.show()
if __name__ == '__main__':
    main()
