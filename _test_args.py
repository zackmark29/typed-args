import logging
import sys
from dataclasses import dataclass

# from typed_args import TypedArgs, add_argument
import typed_args as ta
import argparse

logging.basicConfig(level=logging.DEBUG)


@dataclass()
class Args(ta.TypedArgs):
    foo: str = 'bar'
    data: str = ta.add_argument(
        metavar='DIR',
        help='path to dataset'
    )
    arch: str = ta.add_argument(
        '-a', '--arch',
        metavar='ARCH',
        default='resnet18',
        help='model architecture (default: resnet18)'
    )
    num_workers: int = ta.add_argument(
        '-j', '--workers',
        default=4,
        metavar='N',
        help='number of data loading workers (default: 4)'
    )

@dataclass
class Args1(Args):
    foo: str = ta.add_argument('--foo')


def test_args():
    data = '/path/to/dataset'
    arch = 'resnet50'
    num_workers = 8

    argv = f'{data} -a {arch} -j {num_workers}'.split()

    # sys.argv.extend(argv)

    print(argv)
    args = Args.from_args(argv)
    # args = Args.from_known_args()
    # args = Args1.from_args(argv)

    # args = Args.from_args()
    print(args)

    # assert args.arch == arch
    # assert args.data == data
    # assert args.num_workers == num_workers


if __name__ == "__main__":
    test_args()
    # from test.test_add_argument import *
    # test_name_or_flags()
