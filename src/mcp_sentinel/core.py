from dataclasses import dataclass,field
from hashlib import sha256
@dataclass(frozen=True)
class ToolPolicy: allowed_tools:frozenset[str]=frozenset(); max_arguments:int=32
@dataclass
class SecurityGateway:
 policy:ToolPolicy; audit:list[dict[str,str]]=field(default_factory=list)
 def authorize(self,tool,arguments):
  ok=tool in self.policy.allowed_tools and len(arguments)<=self.policy.max_arguments
  self.audit.append({"tool":tool,"decision":"allow" if ok else "deny","fingerprint":self.fingerprint(tool,arguments)})
  return ok
 @staticmethod
 def fingerprint(tool,arguments):return sha256((tool+repr(sorted(arguments.items()))).encode()).hexdigest()
