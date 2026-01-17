# Kortix 二次开发 - 无限制配置

## 已完成的修改

### ✅ 1. 移除使用限制检查 (limits_checker.py)
**文件**: `backend/core/utils/limits_checker.py`

**修改内容**:
- 修改 `_get_tier_info_if_needed()` 函数
- 移除了对 `subscription_service` 的调用
- 直接返回无限制的tier配置：
  - concurrent_runs: 999999
  - thread_limit: 999999
  - project_limit: 999999
  - custom_workers_limit: 999999
  - scheduled_triggers_limit: 999999
  - app_triggers_limit: 999999

**效果**: 所有用户自动获得无限制权限，无需订阅验证

---

### ✅ 2. 禁用Billing API路由 (api.py)
**文件**: `backend/api.py`

**修改内容**:
- 注释掉 `from core.billing.api import router as billing_router`
- 注释掉 `from core.admin.billing_admin_api import router as billing_admin_router`
- 注释掉 `api_router.include_router(billing_router)`
- 注释掉 `api_router.include_router(billing_admin_router)`

**效果**: 
- 避免加载整个billing模块
- 减少启动时间和内存占用
- 移除所有支付相关的API端点

---

## 核心功能保留

以下功能完全保留且正常工作：

✅ **用户认证** - 基本的登录/注册功能保留  
✅ **Agent管理** - 创建、编辑、删除AI Agent  
✅ **对话线程** - 无限制创建和管理对话  
✅ **工具集成** - 浏览器自动化、文件管理等所有工具  
✅ **项目管理** - 无限制创建项目  
✅ **知识库** - 文档上传和管理  
✅ **触发器** - 定时任务和应用触发器  
✅ **MCP集成** - 自定义MCP服务器  
✅ **API密钥** - API访问管理  

---

## 使用说明

### 启动项目

1. **使用Docker Compose** (推荐):
```bash
docker-compose up -d
```

2. **手动启动**:
```bash
# 启动后端
cd backend
python api.py

# 启动前端
cd apps/frontend
npm run dev
```

### 验证修改

1. 创建账户后，检查账户状态应显示 `tier: unlimited`
2. 尝试创建多个Agent、Thread、Project，应该没有任何限制
3. 所有功能应该可以正常使用，不会出现"升级提示"

---

## 注意事项

⚠️ **重要提醒**:

1. **环境变量**: 不需要配置Stripe相关的环境变量
2. **数据库**: 订阅相关的表仍然存在，但不会被查询
3. **前端UI**: 前端可能仍显示一些计费相关的UI，需要单独处理
4. **备份**: 建议保留原始代码的备份

---

## 可选的进一步优化

如果你想彻底清理项目，可以考虑：

### 前端修改
- 移除 `apps/frontend/` 中的计费相关页面
- 搜索并移除 "upgrade"、"billing"、"subscription" 相关的UI组件

### 环境配置
- 清理 `backend/.env` 中的Stripe配置
- 简化 `setup.py`，跳过支付配置步骤

### 数据库清理
- 可选：删除订阅相关的数据库表（不推荐，可能影响其他功能）

---

## 恢复原始功能

如果需要恢复原始的付费功能：

1. 使用Git恢复修改：
```bash
git checkout backend/core/utils/limits_checker.py
git checkout backend/api.py
```

2. 或者手动取消注释被注释的代码

---

## 技术支持

如果遇到问题：

1. 检查日志中是否有 "payment restrictions removed" 的提示
2. 确认 `limits_checker.py` 返回的是 `unlimited` tier
3. 验证API中没有加载billing router

---

**最后更新**: 2026-01-17  
**修改版本**: v1.0 - 最小改动方案
