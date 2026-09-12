# 本地配置

插件提供一个 COMPUTE 服务器键的示例 SSH 别名和密码变量名，位于 `assets/server-aliases.env`。该文件不包含地址、密码、私钥或令牌。

需要覆盖别名时，使用 `~/.config/lab-codex-ops/servers.env`，或通过 `LAB_CODEX_OPS_CONFIG_FILE` 指定其他文件。覆盖文件只需填写需要变化的字段，不要求设置为 `600`。

管理员密码保存在 `~/.config/lab-codex-ops/secrets.env`，也可通过 `LAB_CODEX_OPS_SECRETS_FILE` 指定。密码文件必须设置为 `600`。如果新密码文件不存在，脚本兼容读取 `~/.config/server-ops/local-secrets.env`。

脚本优先使用 SSH 密钥；只有密钥认证失败或远程 `sudo` 需要密码时，才读取受保护密码文件。
