import argparse
import yaml
from video_capture import run_camera

def get_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--hyp', type=str, default='./utils/hyp.hc.sr04.yaml', help='Ultrasound sensor [HC-SR04] hyperparameters path')
    parser.add_argument('--cpu', type=str, default='True', help='if cpu is None, use CUDA')
    parser.add_argument('--per_frames', type=int, default=10,  help='num frames to predict at each thread for reducing device burden')
    opt = parser.parse_args()
    return opt

if __name__ == '__main__':
    opt = get_parser()
    with open(opt.hyp, errors='ignore') as f:
        hyp = yaml.safe_load(f)
    run_camera(opt, hyp)
