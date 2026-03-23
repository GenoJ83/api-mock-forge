import re
from typing import Dict, Optional, Tuple
from src.core.types import MockResponse, MockRequest

class Route:
    def __init__(self, method: str, path_pattern: str, response: MockResponse):
        self.method = method.upper()
        self.raw_path = path_pattern
        self.regex, self.param_names = self._compile_pattern(path_pattern)
        self.response = response
        
    def _compile_pattern(self, pattern: str) -> Tuple[re.Pattern, list]:
        param_names = []
        regex_parts = []
        for segment in pattern.strip("/").split("/"):
            if segment.startswith(":"):
                pname = segment[1:]
                param_names.append(pname)
                regex_parts.append(f"(?P<{pname}>[^/]+)")
            elif segment.startswith("{") and segment.endswith("}"):
                pname = segment[1:-1]
                param_names.append(pname)
                regex_parts.append(f"(?P<{pname}>[^/]+)")
            else:
                regex_parts.append(re.escape(segment))
        regex_str = "^/" + "/".join(regex_parts) + "$" if regex_parts and pattern != "/" else "^/?$"
        return re.compile(regex_str), param_names

    def match(self, method: str, path: str) -> Optional[Dict[str, str]]:
        if self.method != method.upper():
            return None
        m = self.regex.match(path)
        if m:
            return m.groupdict()
        return None
