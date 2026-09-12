#!/usr/bin/env python3
import pathlib
import sys

import yaml


path = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "examples/mihomo.template.yaml")
config = yaml.safe_load(path.read_text()) or {}

expected_groups = {
    "第二来源智能自动",
    "第二来源通用自动",
    "人工智能自动",
    "谷歌自动",
    "GitHub核心自动",
    "GitHub内容自动",
    "GitHub归档自动",
    "学术外网自动",
    "默认外网自动",
}
groups = {item.get("name"): item for item in config.get("proxy-groups", [])}
providers = config.get("proxy-providers", {})

assert config.get("tun", {}).get("enable") is False
assert set(groups) == expected_groups
assert len(providers) == 2
assert all(item.get("type") == "http" for item in providers.values())
assert all(item.get("interval") == 86400 for item in providers.values())
assert all(item.get("type") == "url-test" for item in groups.values())
source_groups = {
    name: item for name, item in groups.items() if name.startswith("第二来源")
}
business_groups = {
    name: item for name, item in groups.items() if name not in source_groups
}
assert all(item.get("interval") == 600 for item in business_groups.values())
assert all(item.get("interval") == 1800 for item in source_groups.values())
assert all(item.get("lazy") is False for item in groups.values())
assert all(item.get("timeout") == 10000 for item in business_groups.values())
assert all(item.get("timeout") == 3000 for item in source_groups.values())
assert all("max-failed-times" not in item for item in groups.values())
assert all(item.get("tolerance") == 200 for item in groups.values())
assert all(item.get("use") == ["第一订阅"] for item in business_groups.values())
assert all(item.get("use") == ["第二订阅"] for item in source_groups.values())
assert all("health-check" not in item for item in providers.values())
assert groups["人工智能自动"].get("proxies") == ["第二来源智能自动"]
for name, item in business_groups.items():
    if name != "人工智能自动":
        assert "第二来源通用自动" in item.get("proxies", [])

direct_groups = {
    name for name, item in business_groups.items() if "DIRECT" in item.get("proxies", [])
}
assert direct_groups == {
    "谷歌自动",
    "GitHub核心自动",
    "GitHub内容自动",
    "GitHub归档自动",
    "学术外网自动",
}

print(f"模板结构检查通过：{len(providers)} 个提供器，{len(groups)} 个自动组")
