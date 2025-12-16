from dataclasses import dataclass

@dataclass(frozen=True)
class SafetyConfig:
    allow_network_io: bool = False  # hard kill-switch
    allow_real_users: bool = False  # must remain False
    audit_log_enabled: bool = True

CONFIG = SafetyConfig()
