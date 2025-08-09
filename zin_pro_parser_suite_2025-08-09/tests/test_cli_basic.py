import os, sys, subprocess, json, platform

def run(cmd):
    return subprocess.run(cmd, shell=False, capture_output=True, text=True)

def test_version():
    p = run([sys.executable, "-m", "compiler.cli", "-v"])
    assert p.returncode == 0
    assert "0.0.1" in p.stdout

def test_gen_and_parse():
    # generate
    if platform.system() == "Windows":
        p = run(["powershell", "-ExecutionPolicy", "Bypass", "-File", "scripts/gen_parser.ps1"])
    else:
        p = run(["bash", "scripts/gen_parser.sh"])
    assert p.returncode == 0, p.stderr

    # parse hello
    p2 = run([sys.executable, "-m", "compiler.cli", "parse", "tests/grammar/hello.zin"])
    assert p2.returncode == 0, p2.stderr
    assert "PARSE OK" in p2.stdout
