# from typed_args import TypedArgs, add_argument, dataclass
import typed_args as ta
import pickle
from typing import List, Optional
from dataclasses import dataclass


@dataclass()
class Args(ta.TypedArgs):
    foo: Optional[str] = ta.add_argument('--foo')
    bar: List[int] = ta.add_argument(nargs='*', default=[1, 2, 3])


def test_pickle():
    args, _ = Args.from_known_args([])
    _pickled_args = pickle.dumps(args)
    assert _pickled_args


if __name__ == "__main__":
    test_pickle()
