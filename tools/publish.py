#!/usr/bin/env python3
"""Build, check, and publish the static site to the existing gh-pages branch."""
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
def run(*args, cwd=ROOT):
    return subprocess.run(args, cwd=cwd, check=True)

run(sys.executable, 'build.py')
run(sys.executable, 'tools/check_site.py')
remote = subprocess.check_output(['git', 'remote', 'get-url', 'origin'], cwd=ROOT, text=True).strip()
with tempfile.TemporaryDirectory(prefix='jenna-publish-') as folder:
    target = Path(folder)
    run('git', 'clone', '--branch', 'gh-pages', '--single-branch', remote, folder)
    for path in target.iterdir():
        if path.name == '.git':
            continue
        if path.is_dir():
            shutil.rmtree(path)
        else:
            path.unlink()
    shutil.copytree(ROOT / 'dist', target, dirs_exist_ok=True)
    run('git', 'add', '-A', cwd=target)
    changed = subprocess.run(['git', 'diff', '--cached', '--quiet'], cwd=target)
    if changed.returncode == 1:
        run('git', 'commit', '-m', 'Update published portfolio', cwd=target)
        run('git', 'push', 'origin', 'gh-pages', cwd=target)
    elif changed.returncode != 0:
        raise SystemExit(changed.returncode)
    else:
        print('Published site is already up to date.')
