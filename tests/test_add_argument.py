import typed_args as ta
import pytest
from dataclasses import dataclass


def test_name_or_flags():
    @dataclass
    class Args(ta.TypedArgs):
        foo: str = ta.add_argument('-f', '--foo')
        bar: str = ta.add_argument()

    args1 = Args.from_args(['BAR'])
    assert args1 == Args(bar='BAR')

    args2 = Args.from_args(['BAR', '--foo', 'FOO'])
    assert args2 == Args(foo='FOO', bar='BAR')

    # with pytest.raises()
    with pytest.raises(SystemExit) as e:
        args3 = Args.from_args(['--foo', 'FOO'])
    assert e.value.code == 2


def test_store_action():
    @dataclass
    class Args(ta.TypedArgs):
        foo: str = ta.add_argument('--foo')

    args = Args.from_args('--foo 1'.split())
    assert args == Args(foo='1')


def test_store_const_action():
    @dataclass
    class Args(ta.TypedArgs):
        foo: int = ta.add_argument('--foo', action='store_const', const=42)

    args = Args.from_args(['--foo'])
    assert args == Args(foo=42)



