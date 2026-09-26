#!/usr/bin/env python3
"""Check the added seven-point example and required editorial changes."""
from __future__ import annotations
import argparse,json
from pathlib import Path
import sympy as s
ROOT=Path(__file__).resolve().parents[1]
def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--output',type=Path,required=True);a=p.parse_args()
    text=(ROOT/'paper/ptolemaic.tex').read_text();checks=[]
    fragments={'dependency_sentence':'so its strictness hypothesis comes entirely from the outer induction',
      'new_cardinalities':'newly determined values begin at $P(7)$',
      'methodological_comparison':'replace the need for separate higher-cardinality sign-pattern analyses',
      'snowflake_definition':r'\emph{snowflake}',
      'split_graph_definition':'a clique of size $a$ and an independent set of size $r$',
      'introductory_values':r'P(7)=\log_2(16/9),\qquad P(8)=\log_2(5/3)',
      'adjacent_sharpness_regime':r'When $R_n(T)\ge2$, this bound is attained for equal lengths.',
      'worked_seven_point_example':r'\paragraph{Seven-point example.}',
      'dependency_appendix_retained':r'\section{Where the strictness hypotheses enter}',
      'missingness_and_separate_statistics':r'\texttt{null}',
      'unrefereed_status':'Unrefereed.'}
    for name,frag in fragments.items():
        if frag not in text:raise AssertionError(name)
        checks.append(name)
    loc=text.index(r'\label{thm:inverse-bound}');proof=text.index(r'\begin{proof}',loc)
    assert fragments['dependency_sentence'] in text[loc:proof]
    checks.append('dependency_sentence_immediately_after_theorem_before_proof')
    loc=text.index(r'\label{thm:packing}');end=text.index(r'\end{theorem}',loc)
    assert fragments['adjacent_sharpness_regime'] in text[loc:end]
    checks.append('sharpness_regime_in_packing_statement')
    T=s.symbols('T');E=s.ones(7)-s.eye(7)
    for i in range(3,7):
        for j in range(3,7):
            if i!=j:E[i,j]=T
    z=s.Matrix([s.Rational(1,3)]*3+[-s.Rational(1,4)]*4)
    form=(z.T*E*z)[0];assert s.expand(form-(s.Rational(2,3)+s.Rational(3,4)*T-2))==0
    assert form.subs(T,s.Rational(16,9))==0 and s.diff(form,T)>0
    J=s.eye(7)-s.ones(7)/7;G=-J*E.subs(T,s.Rational(16,9))*J/2
    eig=G.eigenvals();assert eig=={s.Rational(1,2):2,s.Rational(8,9):3,s.Integer(0):2}
    checks.extend(['seven_point_quadratic_form_and_sharp_endpoint','seven_point_centred_gram_exact_spectrum'])
    assert 1+s.Rational(8,((8-1)**2//4))==s.Rational(5,3)
    checks.append('eight_point_introductory_threshold')
    report={'status':'PASS','scope':'editorial requirements and exact added examples; not proof-assistant verification',
      'check_count':len(checks),'checks':checks,'seven_point_form':str(form),
      'seven_point_centred_gram_eigenvalues':{str(k):v for k,v in eig.items()}}
    a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(json.dumps(report,indent=2,sort_keys=True)+'\n');print(json.dumps(report,indent=2))
if __name__=='__main__':main()
