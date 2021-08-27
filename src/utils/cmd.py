import argparse


def register_launch_arguments():
    parser = argparse.ArgumentParser(description='App for utilize some operations with files')

    parser.add_argument('-i', '--input_dir', help='specify directory with images')
    parser.add_argument('-o', '--output_dir', help='specify directory for results', default='../out/')
    parser.add_argument('-p', '--parameters', help='parameters of application', default='./assets/config.json')
    parser.add_argument('-t', '--test', help='flag for testing', action="store_true")
    parser.add_argument('-n', '--network', help='flag for using of neural network', action="store_true")

    return parser.parse_args()
