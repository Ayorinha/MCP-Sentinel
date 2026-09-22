from dataclasses import dataclass
@dataclass(frozen=True)
class ToolCall: name:str; arguments:dict[str,object]
@dataclass(frozen=True)
class Rule: tool:str; allowed:bool=True
class Policy:
 def __init__(self,rules:list[Rule]): self.rules={r.tool:r for r in rules}
 def authorize(self,call:ToolCall)->bool:
  rule=self.rules.get(call.name)
  return bool(rule and rule.allowed)
