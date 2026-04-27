import argparse
import sys
import json
from src.engine import MockForgeEngine

def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="mockforge", description="Declarative HTTP mock and API simulator")
    p.add_argument("--version", action="store_true", help="Print version")
    p.add_argument("--port", type=int, default=8000, help="Listen port")
    p.add_argument("--latency", type=float, default=0.0, help="Fixed latency ms")
    return p

def main(args=None):
    parser = build_parser()
    opts = parser.parse_args(args)
    if opts.version:
        print("mockforge v0.1.0")
        return 0
    return 0
