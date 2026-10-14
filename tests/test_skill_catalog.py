import unittest
def chain(previous,is_chain,valid,applied,capability=True,active=True):
 if not active or not capability or not valid or not is_chain:return 0
 return min(3,previous+1) if applied else 0
def dot_tick(effect):
 if effect["remaining"]<=0:return 0,None
 damage=effect["damage"]; effect["remaining"]-=1
 return damage,effect if effect["remaining"]>0 else None
def overflow(before,after,threshold,locked=False,already=False):
 return int(not locked and not already and before<threshold<=after)
def finisher(targets,threshold=.8):
 outcomes=[{"id":t["id"],"success":t["eligible"] and t["permitted"] and t["strain"]>=threshold,"persists":t["eligible"] and t["permitted"] and t["strain"]>=threshold} for t in targets]
 return outcomes,bool(outcomes) and all(x["success"] for x in outcomes)
def tentacle_order(snapshot,enabled):
 order={"Enemy":0,"Ally":1,"Self":2}
 return [x for x in sorted(snapshot,key=lambda x:(order[x["side"]],x["id"])) if x["side"] in enabled]
def p_growth(actor,has_capability):return actor=="ALYA" and has_capability
class Tests(unittest.TestCase):
 def test_chain(self):
  self.assertEqual(chain(1,True,True,True),2); self.assertEqual(chain(1,True,True,False),0); self.assertEqual(chain(2,False,True,True),0); self.assertEqual(chain(2,True,False,True),0); self.assertEqual(chain(2,True,True,True,False),0); self.assertEqual(chain(3,True,True,True),3)
 def test_dot(self):
  e={"damage":5,"remaining":2}; a,e=dot_tick(e); self.assertEqual(a,5); self.assertEqual(e["remaining"],1); b,e=dot_tick(e); self.assertEqual(b,5); self.assertIsNone(e)
 def test_overflow_once_and_lock(self):
  self.assertEqual(overflow(79,80,80),1); self.assertEqual(overflow(80,90,80),0); self.assertEqual(overflow(79,90,80,already=True),0); self.assertEqual(overflow(79,90,80,locked=True),0); self.assertEqual(overflow(79,90,80),1)
 def test_partial_finisher(self):
  out,v=finisher([{"id":"A","eligible":True,"permitted":True,"strain":.9},{"id":"B","eligible":False,"permitted":True,"strain":1.0}]); self.assertTrue(out[0]["persists"]); self.assertFalse(out[1]["success"]); self.assertFalse(v)
 def test_friendly_fire(self):
  s=[{"id":"Z","side":"Self"},{"id":"B","side":"Ally"},{"id":"A","side":"Enemy"}]; self.assertEqual([x["id"] for x in tentacle_order(s,{"Enemy","Ally","Self"})],["A","B","Z"]); self.assertEqual([x["id"] for x in tentacle_order(s,{"Enemy"})],["A"])
 def test_p_growth(self):
  self.assertTrue(p_growth("ALYA",True)); self.assertFalse(p_growth("ALLY-001",True)); self.assertFalse(p_growth("ALYA",False))
if __name__=="__main__":unittest.main()
