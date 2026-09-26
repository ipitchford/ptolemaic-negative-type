#!/usr/bin/env python3
"""Build the paper (pdfLaTeX) and optionally the response (XeLaTeX), without downloads.

Only explicit output paths outside the immutable bundle are written. Existing
installed TeX packages/fonts are used; no font files are distributed.
"""
from __future__ import annotations
import argparse,os,shutil,subprocess,tempfile
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--output',type=Path,required=True)
    p.add_argument('--response',action='store_true');a=p.parse_args();out=a.output.resolve()
    if out.is_relative_to(ROOT):p.error('Choose an output outside the bundle.')
    out.mkdir(parents=True,exist_ok=True)
    jobs=[(ROOT/'paper/ptolemaic.tex','pdflatex')]
    if a.response:jobs.append((ROOT/'review/RESPONSE_TO_REVIEW.tex','xelatex'))
    for source,engine in jobs:
        if not shutil.which(engine):raise RuntimeError(engine+' is not installed')
        with tempfile.TemporaryDirectory(prefix='ptolemaic-typeset-') as tmp:
            env=dict(os.environ,SOURCE_DATE_EPOCH='1790294400',FORCE_SOURCE_DATE='1',TZ='UTC')
            for _ in range(3):
                run=subprocess.run([engine,'-interaction=nonstopmode','-halt-on-error',f'-output-directory={tmp}',source.name],cwd=source.parent,env=env,capture_output=True,text=True,timeout=180)
                if run.returncode:
                    (out/(source.stem+'.failed.log')).write_text(run.stdout+'\n'+run.stderr);raise RuntimeError(source.name+' failed to compile')
            log=(Path(tmp)/(source.stem+'.log')).read_text(errors='replace')
            for token in ('undefined references','undefined citations','Overfull \\hbox','Overfull \\vbox','Missing character:'):
                if token in log:
                    (out/(source.stem+'.failed.log')).write_text(log);raise RuntimeError(source.name+': '+token)
            shutil.copy2(Path(tmp)/(source.stem+'.pdf'),out/(source.stem+'.pdf'))
            (out/(source.stem+'.log')).write_text(log)
            shutil.copy2(Path(tmp)/(source.stem+'.aux'),out/(source.stem+'.aux'))
    print('Build complete. Inspect rendering when rebuilding with different TeX/font versions.')
if __name__=='__main__':main()
