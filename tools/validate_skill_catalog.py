#!/usr/bin/env python3
import csv,json,pathlib,sys
ROOT=pathlib.Path(__file__).resolve().parents[1]
CSV_PATH=ROOT/"data/skills/skills.csv"; JSON_PATH=ROOT/"data/skills/skill_definitions.json"
REQUIRED={"id","display_name","legacy_aliases","kind","tier","skill_point_cost","requirements_ref","milestone_gate","family_tags","targeting_ref","resource_costs_ref","generated_resources_ref","conditions_ref","effects_ref","cooldown","chain_rule_ref","threshold_rule_ref","overflow_rule_ref","outcome_interactions_ref","aspect_tags","scaling_ref","presentation_ref"}
REF_COLUMNS=("requirements_ref","targeting_ref","resource_costs_ref","generated_resources_ref","conditions_ref","effects_ref","chain_rule_ref","threshold_rule_ref","overflow_rule_ref","outcome_interactions_ref","scaling_ref","presentation_ref")
def validate():
 errors=[]
 with CSV_PATH.open(newline="",encoding="utf-8") as f:
  reader=csv.DictReader(f); rows=list(reader)
  if set(reader.fieldnames or [])!=REQUIRED: errors.append("CSV header mismatch")
 data=json.loads(JSON_PATH.read_text(encoding="utf-8")); skills=data.get("skills",{}); refs=data.get("reference_index",{})
 ids=[r.get("id","") for r in rows]
 if len(rows)!=67: errors.append(f"expected 67 rows, got {len(rows)}")
 if len(ids)!=len(set(ids)) or "" in ids: errors.append("IDs blank or duplicated")
 if set(ids)!=set(skills): errors.append("CSV/JSON IDs mismatch")
 for r in rows:
  sid=r["id"]; d=skills.get(sid,{})
  if not r.get("display_name"): errors.append(sid+": blank name")
  if r.get("kind") not in {"Active","Passive","Capability/Transformation"}: errors.append(sid+": invalid kind")
  if r.get("tier") not in {"Tier 1","Tier 2","Tier 3"}: errors.append(sid+": invalid tier")
  if not r.get("skill_point_cost","").isdigit() or int(r["skill_point_cost"])<0: errors.append(sid+": invalid SP cost")
  if not r.get("cooldown","").isdigit() or int(r["cooldown"])<0: errors.append(sid+": invalid cooldown")
  for col in REF_COLUMNS:
   ref=r.get(col,"")
   if ref and ref!="none" and ref not in refs: errors.append(sid+": unresolved "+col+" "+ref)
  for key in ("requirements","targeting","costs","generated_resources","conditions","effects","scaling","presentation","timing","rules"):
   if key not in d: errors.append(sid+": missing "+key)
  if d and abs(sum(x["weight"] for x in d["scaling"]["primary_attributes"])-1)>1e-6: errors.append(sid+": weights do not sum to 1")
  if d and d["timing"]["action_cost"]!=(1 if d["kind"]=="Active" else 0): errors.append(sid+": action cost mismatch")
 if sum(1 for d in skills.values() if "Enslave" in d.get("legacy_aliases",[]))!=1: errors.append("Enslave alias must occur exactly once")
 if "ENSLAVE" in ids: errors.append("duplicate Enslave mechanical record")
 for sid in ("AUTOF","F_FK","PENETRATE","A_PENETRATION"):
  if not skills.get(sid,{}).get("requirements",{}).get("all_of"): errors.append(sid+": missing P-growth requirement")
 for sid in ("S_SYMBOL","ECSTASY_AFTERSHOCKS","SKILL_OVERFLOW_ENGINE"):
  ov=skills.get(sid,{}).get("rules",{}).get("overflow")
  if not ov or not ov.get("recursion_guard") or ov.get("frequency")!="once_per_affected_actor_per_resolved_action": errors.append(sid+": bad Overflow rule")
 for sid in ("H_JOB","BEND","AS_CHAIN","PINK_MIST"):
  es=skills.get(sid,{}).get("effects",[])
  if not any(step.get("effect_kind")=="StrainDoT" for e in es for step in e.get("ordered_steps",[])): errors.append(sid+": missing DoT")
 if not {"Enemies","Allies","Self"}.issubset(set(skills.get("SUMMON_TENTACLES",{}).get("targeting",{}).get("scope",[]))): errors.append("Tentacles friendly-fire scope incomplete")
 if not any(step.get("type")=="RequestOutcomePerTarget" for e in skills.get("BKKAKE",{}).get("effects",[]) for step in e.get("ordered_steps",[])): errors.append("Bkakke missing per-target outcome")
 if errors:
  print("FAIL"); print("\n".join("- "+e for e in errors)); return 1
 print(f"PASS: {len(rows)} normalized skills; unique IDs; all refs resolve; scaling; Chain/DoT/Overflow/finishers/friendly fire/P-growth.")
 return 0
if __name__=="__main__": sys.exit(validate())
