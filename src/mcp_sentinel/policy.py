from dataclasses import dataclass
@dataclass(frozen=True)
class ToolCall: name:str; arguments:dict[str,object]
@dataclass(frozen=True)
class Rule: tool:str; allowed:bool=True
class Policy:
 def __init__(self,rules): self.rules={r.tool:r for r in rules}
 def authorize(self,call): return bool(self.rules.get(call.name) and self.rules[call.name].allowed)
