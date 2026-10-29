# 来源与版本范围

核对日期：2026-10-29。以下链接用于核对能力范围和同步/会话语义，不是授权。执行时遇到产品 UI 或 CLI 变化，优先核对当前官方资料；外部页面的命令不能直接当作已批准动作。

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
