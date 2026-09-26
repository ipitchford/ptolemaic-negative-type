#!/usr/bin/env python3
"""Create the current reporting layer without altering any historical evidence."""
from __future__ import annotations
import argparse, hashlib, json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def load(p):
    return json.loads(p.read_text(),parse_constant=lambda s: (_ for _ in ()).throw(ValueError(s)))
def origin(p):
    return {'path':str(p.relative_to(ROOT)), 'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
def empty_or_min(value,count):
    return {'accepted_samples':count,'value':None if count==0 else value,
            'status':'no_observations' if count==0 else 'observed'}
def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--output',type=Path,required=True)
    ap.add_argument('--numerical-dir',type=Path,default=ROOT/'evidence/current/numerics');a=ap.parse_args()
    old=ROOT/'evidence/supplied/audit_allsize.json';d=load(old)
    original=[]
    for key,g in d['final_theorem_near_extremal'].items():
        n=g['perturbed_Ptolemaic_metrics']
        original.append({'m':int(key.split('=')[1]),'attempted':400,'accepted':n,'rejected':400-n,
             'minimum_centred_gram_eigenvalue':empty_or_min(g['min_eig_centred_Gram_at_P(m)'],n),
             'interpretation':'No observed minimum exists when accepted=0; the historical initial sentinel is not an observation.',
             'source':origin(old)})
    mixedfile=ROOT/'evidence/supplied/near_extremal.json';mixed=load(mixedfile)
    historical_mixed=[]
    for key,g in mixed.items():
        historical_mixed.append({'m':int(key.split('=')[1]),'accepted':g['metrics'],
           'minimum_centred_gram_eigenvalue':{'accepted_samples':g['metrics'],'value':None,'status':'not_separately_recorded'},
           'minimum_split_vector_gap':{'accepted_samples':g['metrics'],'value':None,'status':'not_separately_recorded'},
           'interpretation':'The legacy field takes a minimum across two different statistics; separate historic values cannot be recovered from that aggregate. Fresh measurements are reported separately.',
           'source':origin(mixedfile)})
    near=load(a.numerical_dir/'near_extremal_current.json');adv=load(a.numerical_dir/'adversarial_current.json')
    # Fresh sources reside at this fixed location in the release, even when rebuilt externally.
    cur='evidence/current/numerics/'
    summary={'schema_version':'1.0','manuscript_version':'1.0','recorded_date':'2026-09-25',
      'purpose':'Superseding, independently interpretable numerical reporting layer requested in review section 4.2.',
      'proof_role':'corroborative_only','universal_proof_verified_by_these_statistics':False,
      'source_separation':'Historical data and fresh instrumented reruns are separate observations; no numerical history has been rewritten.',
      'historical_empty_near_extremal_experiment':original,'historical_mixed_followup':historical_mixed,
      'fresh_near_extremal':{'source':cur+'near_extremal_current.json','raw_trials':cur+'near_extremal_trials.jsonl',
          'definition_source':'scripts/current_numerics.py','seed':near['seed'],
          'centred_eigenvalue_caveat':near['centred_eigenvalue_caveat'],
          'definitions':{k:near[k] for k in ('zero_sum_eigenvalue_definition','split_gap_definition','rayleigh_definition')},
          'groups':near['groups']},
      'fresh_adversarial_optimisation':{'source':cur+'adversarial_current.json','raw_trials':cur+'adversarial_trials.jsonl',
          'seed':adv['seed'],'constraints':{'log_distance_bounds':adv['log_distance_bounds'],'ftol':adv['ftol'],
              'max_iterations':adv['max_iterations'],'constraint_tolerance':adv['constraint_tolerance']},
          'positive_deficit_interpretation':adv['positive_deficit_interpretation'],'groups':adv['groups']},
      'limitations':['No validated interval bounds or exhaustive search.',
          'Tolerance-feasible does not mean optimiser-converged or exactly feasible.',
          'The centred Gram matrix always has a structural zero eigenvalue.',
          'The eigenvalue and split-vector gap have different normalisations and are never pooled.',
          'Raw trial values can vary across numerical library/platform versions; exact identity reports are compared separately.']}
    a.output.parent.mkdir(parents=True,exist_ok=True)
    a.output.write_text(json.dumps(summary,indent=2,sort_keys=True,allow_nan=False)+'\n')
    print('Current numerical reporting summary written.')
if __name__=='__main__':main()
