#!/usr/bin/env python3
"""Build both CVs from repository sources; publish only after both succeed."""
from pathlib import Path
import shutil
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parents[1]
outputs = []
# Retain build diagnostics outside the published website.
build = Path(tempfile.mkdtemp(prefix='wanxing-cv-'))
for language, engine, output in [('EN', 'xelatex', 'cv.pdf'), ('CN', 'xelatex', 'cv_cn.pdf')]:
    binary = shutil.which(engine)
    if not binary and Path('/Library/TeX/texbin', engine).exists():
        binary = str(Path('/Library/TeX/texbin', engine))
    if not binary:
        raise SystemExit(f'{engine} is required. Install MacTeX. Existing PDFs were not changed.')
    name = f'Wanxing_Wu_CV_{language}'
    for _ in range(2):
        result = subprocess.run([binary, '-no-shell-escape', '-interaction=nonstopmode',
            '-halt-on-error', f'-output-directory={build}', f'{name}.tex'],
            cwd=ROOT / 'cv', stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        if result.returncode:
            raise SystemExit(f'{name} failed. See {build / (name + ".log")}\n{result.stdout[-2500:]}')
    outputs.append((build / f'{name}.pdf', ROOT / output))
for source, destination in outputs:
    shutil.copyfile(source, destination)
print(f'Built cv.pdf and cv_cn.pdf. Build logs: {build}')
