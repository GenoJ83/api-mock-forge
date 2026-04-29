from src.cli.main import build_parser, main

def test_cli_flags():
    p = build_parser()
    opts = p.parse_args(["--port", "9090", "--latency", "25.5"])
    assert opts.port == 9090
    assert opts.latency == 25.5
    assert main(["--version"]) == 0
