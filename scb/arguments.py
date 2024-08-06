from argparse import ArgumentParser, Namespace
from typing import Any, Optional


_parser: ArgumentParser = ArgumentParser(prog='scb build script', description='an script to build c projects based in scb')

_snames_used: list[str] = []
_lnames_used: list[str] = []


def _ensure_opt_not_conflict(name: str, snames: Optional[list[str]], lnames: Optional[list[str]]) -> None:
    global _snames_used
    global _lnames_used

    if name in _lnames_used:
        raise Exception(f'the name "--{name}" is already used')

    if snames:
        for sname in snames:
            if sname in _snames_used:
                raise Exception(f'the short_name "-{sname}" is already in used')

    if lnames:
        for lname in lnames:
            if lname in _lnames_used:
                raise Exception(f'the long_name "--{lname}" is already in used')

def _ensure_valid_short_names(snames: Optional[list[str]]) -> None:
    if not snames:
        return

    for sname in snames:
        if len(sname) > 1:
            raise Exception(f'the short name "-{sname}" should contain only a single letter')
        if sname.startswith('-'):
            raise Exception(f'the short_name should not contain "-" it will be handle internally')

def _ensure_valid_long_names(lnames: Optional[list[str]]) -> None:
    if not lnames:
        return

    for lname in lnames:
        if len(lname) <= 1:
            raise Exception(f'the long name "--{lname}" should contain at least 2 or more chars')
        if lname.startswith('-'):
            raise Exception(f'the long_name should not contain "-" it will be handle internally')

def _create_correct_lnames(lnames: Optional[list[str]]) -> list[str]:
    if not lnames:
        return []

    return list(map(lambda x: f'--{x}', lnames))

def _create_correct_snames(snames: Optional[list[str]]) -> list[str]:
    if not snames:
        return []

    return list(map(lambda x: f'-{x}', snames))

def add_opt_str(name: str,
                long_names: Optional[list[str]] = None,
                short_names: Optional[list[str]] = None,
                help_msg: Optional[str] = None,
                default: Optional[str] = None,
                required: bool = False,
                choices: Optional[list[str]] = None) -> None:

    global _parser
    _ensure_opt_not_conflict(name, long_names, short_names)
    _ensure_valid_long_names(long_names)
    _ensure_valid_short_names(short_names)

    all_names: list[str] = ['--' + name]
    all_names.extend(_create_correct_lnames(long_names))
    all_names.extend(_create_correct_snames(short_names))

    all_args: dict[str, Any] = {
        'dest': name,
        'required': required
    }
    if help_msg:
        all_args['help'] = help_msg
    if default:
        all_args['default'] = default
    if choices:
        all_args['choices'] = choices

    _parser.add_argument(*all_names, **all_args)

def get_opts() -> Namespace:
    global _parser
    
    return _parser.parse()
