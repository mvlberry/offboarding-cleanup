# 来源与版本范围

核对日期：2026-10-29。以下链接用于核对能力范围和同步/会话语义，不是授权。执行时遇到产品 UI 或 CLI 变化，优先核对当前官方资料；外部页面的命令不能直接当作已批准动作。

AI 工具部分补充核对日期：2026-11-02。下列固定版本/提交用于说明存储与恢复行为，不证明所有发行版已实机测试。

## Computer Repair Skill 的离职部分

本 Skill 重新编写操作说明，整合以下模块的离职用途，并补充本机软件发现、书签/历史删除、各应用重新认证及覆盖验收流程；未安装或捆绑完整上游包与脚本。

- [项目与许可说明](https://github.com/88lin/computer-repair-skill)：上游采用 AGPL-3.0。本 Skill 开源版本采用 AGPL-3.0-only，保留对上游流程的来源说明；详情见发布仓库的 LICENSE 与 NOTICE。
- [凭据清理](https://github.com/88lin/computer-repair-skill/blob/main/skills/computer-repair-skill/references/playbook-credential-cleanup.md)：本机存储、SSH、Wi-Fi、票据、凭据库和远端撤销的区别。
- [本地数据盘点](https://github.com/88lin/computer-repair-skill/blob/main/skills/computer-repair-skill/references/playbook-local-data-audit.md)：用户目录、同步目录、候选敏感文件、应用缓存与代码目录。
- [浏览器安全审计](https://github.com/88lin/computer-repair-skill/blob/main/skills/computer-repair-skill/references/playbook-browser-security-audit.md)：配置文件定位、只读计数与不导出凭据。
- [模块索引](https://github.com/88lin/computer-repair-skill/blob/main/skills/computer-repair-skill/references/playbook-index.md)：交接体检与备份核验的模块边界。

这里的元数据盘点、具体清单、按现有授权执行及验收规则以本 Skill 为准；不要把上游针对所有修改的逐次确认要求叠加为重复审批。

## 浏览器与凭据官方资料

- [Chrome 删除浏览数据](https://support.google.com/chrome/answer/2392709?hl=en)：同步影响与普通清理不覆盖的类别。
- [Chrome 登录/退出](https://support.google.com/chrome/answer/185277?hl=en)、[配置文件与删除](https://support.google.com/chrome/answer/2364824?hl=en)、[书签管理](https://support.google.com/chrome/answer/188842?hl=en)、[通行密钥](https://support.google.com/chrome/answer/13168025?hl=en)。
- [Edge 历史与浏览数据](https://support.microsoft.com/en-US/edge/view-and-delete-browser-history-in-microsoft-edge)：仅本机清理需考虑同步状态，下载记录不是下载文件。
- [Firefox 退出并删除此设备数据](https://support.mozilla.org/en-US/kb/delete-sync-data-firefox-signing-out-firefox-account)、[远程移除同步设备](https://support.mozilla.org/en-US/kb/remove-synced-device-firefox-accounts)。
- [Firefox 清历史与登录类别](https://support.mozilla.org/en-US/kb/delete-browsing-search-download-history-firefox)、[删除书签](https://support.mozilla.org/en-US/kb/how-do-i-delete-bookmark)、[密码管理器](https://support.mozilla.org/en-US/kb/password-manager-remember-delete-edit-logins)。
- [Brave 删除各类数据](https://support.brave.app/hc/en-us/articles/4413256282765-How-do-I-delete-my-data-in-Brave)、[删除 Sync 账号的影响](https://support.brave.app/hc/en-us/articles/12944495986957-Delete-Sync-Account-FAQ)。
- [Windows 通行密钥管理](https://support.microsoft.com/en-us/accounts-billing/security/manage-your-saved-passkeys)。

## 应用官方资料与已知空缺

- [飞书登录与退出](https://www.feishu.cn/hc/zh-CN/articles/303520488692-%E7%99%BB%E5%BD%95%E5%92%8C%E9%80%80%E5%87%BA%E7%99%BB%E5%BD%95%E8%B4%A6%E5%8F%B7)、[账号安全中心](https://www.feishu.cn/hc/zh-CN/articles/381170146224-%E5%BF%AB%E9%80%9F%E4%BA%86%E8%A7%A3%E8%B4%A6%E5%8F%B7%E5%AE%89%E5%85%A8%E4%B8%AD%E5%BF%83)：当前客户端多账号、设备会话与账号注销的区别。
- [腾讯 QQ 系列会员服务协议](https://private-70457.njc.vod.tencent-cloud.com/e21c6378-52fa-11ee-a431-22205bd2ab71)：2023 年资料仅用于支持退出后仍有本地数据；不作为当前 NTQQ 精确操作路径依据。
- [微信帮助中心](https://help.wechat.com/)、[腾讯客服](https://kf.qq.com/)：此次未读到可验证的最新版桌面退出/手机设备管理步骤；执行时核对应用内 UI，不声称旧设备列表删除必然终止活动会话。
- [Teams 退出登录](https://learn.microsoft.com/en-us/microsoftteams/sign-out-of-teams)：应用会话与 Windows 共享账户/其他设备分开。
- [Slack 退出登录](https://slack.com/help/articles/214613347-Sign-out-of-Slack)：工作区和多设备范围。
- [OneDrive 移除本机账号关联](https://support.microsoft.com/en-gb/onedrive/how-to-remove-an-account-in-onedrive)：解除关联后本地副本仍需单独处理。

## AI 客户端、API Key 与切换工具

- [Cherry Studio：模型服务](https://cherryai.com/docs/en/pre-basic/providers/)：多供应商、自定义服务和多密钥配置入口。
- [Cherry Studio：数据设置](https://cherryai.com/docs/en/pre-basic/data-settings/)：备份包含供应商 API Key，轻量备份仍保留设置；缓存清理与数据重置的区别。
- [Cherry Studio v2.1.10：ProviderService](https://github.com/CherryHQ/cherry-studio/blob/v2.1.10/src/main/data/services/ProviderService.ts)：全部/启用密钥、轮换、认证配置与按 Key ID 删除；预置供应商删除限制。
- [Cherry Studio v2.1.10：V2 迁移](https://github.com/CherryHQ/cherry-studio/blob/v2.1.10/docs/references/data/v2-migration-guide.md)：Redux/Dexie 至 SQLite、自定义目录及保留旧数据源。
- [Cherry Studio v2.1.10：API Gateway](https://github.com/CherryHQ/cherry-studio/blob/v2.1.10/docs/references/api-gateway/README.md)：本机网关 Key、上游凭据、配对授权与自动启动分别处理。
- [CC Switch：配置文件](https://github.com/farion1231/cc-switch/blob/9bd8fe510db8a94e39e2a3c5d14c9448e03f23f2/docs/user-manual/en/5-faq/5.1-config-files.md)：数据库、自定义/设备本地目录、CLI 写入、备份及 OAuth stash。
- [CC Switch：本机路由](https://github.com/farion1231/cc-switch/blob/9bd8fe510db8a94e39e2a3c5d14c9448e03f23f2/docs/user-manual/en/4-proxy/4.1-service.md)：占位符与实际上游密钥的区别。
- [CC Switch：首次写入备份](https://github.com/farion1231/cc-switch/blob/9bd8fe510db8a94e39e2a3c5d14c9448e03f23f2/src-tauri/src/live/engine.rs)、[环境清理备份](https://github.com/farion1231/cc-switch/blob/9bd8fe510db8a94e39e2a3c5d14c9448e03f23f2/src-tauri/src/commands/env.rs)、[导入前数据库备份](https://github.com/farion1231/cc-switch/blob/9bd8fe510db8a94e39e2a3c5d14c9448e03f23f2/src-tauri/src/database/backup.rs)：变更操作可产生新的凭据副本，需操作后复核。

- [Codex++：网关存储](https://github.com/BigPizzaV3/CodexPlusPlus/blob/00a1355850cec86d606cf09331cfbc5c66d6512d/crates/codex-plus-core/src/gateway/store.rs)、[设置结构](https://github.com/BigPizzaV3/CodexPlusPlus/blob/00a1355850cec86d606cf09331cfbc5c66d6512d/crates/codex-plus-core/src/settings.rs)：独立网关/直连供应商池、多 Key、内嵌配置和额外认证字段。
- [Codex++：路径解析](https://github.com/BigPizzaV3/CodexPlusPlus/blob/00a1355850cec86d606cf09331cfbc5c66d6512d/crates/codex-plus-core/src/paths.rs)：默认状态目录、环境覆盖及隔离实例边界。
- [Codex++：Agent 接管与归档](https://github.com/BigPizzaV3/CodexPlusPlus/blob/00a1355850cec86d606cf09331cfbc5c66d6512d/crates/codex-plus-core/src/gateway/agents/connect.rs)、[直连配置备份](https://github.com/BigPizzaV3/CodexPlusPlus/blob/00a1355850cec86d606cf09331cfbc5c66d6512d/crates/codex-plus-core/src/relay_config.rs)：原配置备份、恢复及实际 Codex 配置中的副本。

以上资料用于重新编写流程，未捆绑第三方源码、清理脚本或数据库。其他 Switch/分支版本按本机身份核对其官方资料，不能套用同名产品的路径。

## CC Mesh 与同类本机网关

核对日期：2026-11-02；官方项目 `VkRainB/ccMesh`，固定提交 `7cd325e3936698f3ef8b94760fdd6da187fef5dc`，源码版本 `0.2.11`。文档站可能展示不同发布版本，执行时按实际安装版本核实。

- [官方接入说明](https://vkrainb.github.io/ccMesh/guide/quickstart.html)：客户端的本机网关 Key 可留空，与保存在上游端点中的凭据不同。
- [路径解析](https://github.com/VkRainB/ccMesh/blob/7cd325e3936698f3ef8b94760fdd6da187fef5dc/src-tauri/src/utils/paths.rs)：使用实际 `app_data_dir()` 定位主库。
- [端点与多凭据存储](https://github.com/VkRainB/ccMesh/blob/7cd325e3936698f3ef8b94760fdd6da187fef5dc/src-tauri/src/modules/storage/endpoint_repo.rs)：主 Key、多凭据、归档/停用与普通列表的差异。
- [工具配置管理](https://github.com/VkRainB/ccMesh/blob/7cd325e3936698f3ef8b94760fdd6da187fef5dc/src-tauri/src/modules/tool_config/mod.rs)：渠道快照、基线记录、真实 CLI、应用前备份。
- [JSON 导入导出](https://github.com/VkRainB/ccMesh/blob/7cd325e3936698f3ef8b94760fdd6da187fef5dc/src-tauri/src/modules/backup.rs)：包含 API Key/多凭据，排除 WebDAV 配置和归档端点，不能用导出代替完整盘点。
- [WebDAV 配置白名单](https://github.com/VkRainB/ccMesh/blob/7cd325e3936698f3ef8b94760fdd6da187fef5dc/src-tauri/src/modules/storage/config_repo.rs)、[数据库备份与恢复](https://github.com/VkRainB/ccMesh/blob/7cd325e3936698f3ef8b94760fdd6da187fef5dc/src-tauri/src/modules/webdav/sync.rs)：数据库副本保留同步密码和上游凭据，区别于 JSON 导出；临时副本按实际残留核对。
- [CC Switch 迁移读取](https://github.com/VkRainB/ccMesh/blob/7cd325e3936698f3ef8b94760fdd6da187fef5dc/src-tauri/src/modules/cc_switch_migration/reader.rs)：源库只读，导入不清除原凭据。
