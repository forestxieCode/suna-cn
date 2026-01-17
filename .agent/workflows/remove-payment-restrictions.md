---
description: 移除Kortix项目的收费限制和账户验证功能
---

# Kortix 二次开发 - 移除收费限制和账户验证

## 目标
移除Kortix项目中的以下限制：
- ✅ Stripe支付集成
- ✅ 订阅管理和验证
- ✅ 使用限制检查
- ✅ 账户验证要求
- ✅ 收费相关的API端点
- ⚠️ 保留核心功能代码

## 项目结构分析

### 收费相关模块
- `backend/core/billing/` - 完整的计费系统
  - `subscriptions/` - 订阅管理
  - `payments/` - 支付处理
  - `credits/` - 积分系统
  - `external/` - 外部支付集成（Stripe, RevenueCat）
- `backend/core/auth/` - 认证系统
- `backend/core/utils/limits_checker.py` - 使用限制检查

### 前端收费相关
- `apps/frontend/` - Next.js前端
- `apps/mobile/lib/billing/` - 移动端计费

## 实施步骤

### 第一阶段：后端核心修改

#### 1. 移除Billing模块依赖
**文件**: `backend/api.py`
- [ ] 移除 `from core.billing.api import router as billing_router`
- [ ] 移除 `api_router.include_router(billing_router)`
- [ ] 移除 `from core.admin.billing_admin_api import router as billing_admin_router`

#### 2. 禁用订阅验证
**文件**: `backend/core/utils/limits_checker.py`
- [ ] 修改所有限制检查函数，直接返回允许访问
- [ ] 移除 `subscription_service` 的调用
- [ ] 示例修改：
```python
# 原代码
async def check_user_limits(account_id: str):
    tier = await subscription_service.get_user_subscription_tier(account_id)
    if tier == 'free':
        raise LimitExceededError()
    
# 修改后
async def check_user_limits(account_id: str):
    # 移除所有限制检查
    return True
```

#### 3. 简化认证系统
**文件**: `backend/core/auth/auth.py`
- [ ] 保留基本的用户身份验证
- [ ] 移除订阅状态检查
- [ ] 移除支付方式验证

#### 4. 修改环境配置
**文件**: `backend/.env`
- [ ] 移除或注释掉所有Stripe相关配置：
  - `STRIPE_SECRET_KEY`
  - `STRIPE_WEBHOOK_SECRET`
  - 所有 `STRIPE_TIER_*` 配置

**文件**: `backend/core/utils/config.py`
- [ ] 将所有Stripe配置设为Optional且默认为None
- [ ] 移除Stripe配置的必需验证

#### 5. 修改数据库初始化
**文件**: `backend/supabase/migrations/`
- [ ] 创建新的迁移文件，移除订阅相关的表约束
- [ ] 或者修改账户初始化逻辑，自动给予最高权限

### 第二阶段：前端修改

#### 6. 移除前端计费UI
**目录**: `apps/frontend/`
- [ ] 查找并移除所有计费相关的页面和组件
- [ ] 搜索关键词：`billing`, `subscription`, `payment`, `stripe`
- [ ] 移除升级提示、付费墙等UI元素

#### 7. 移除移动端计费
**目录**: `apps/mobile/lib/billing/`
- [ ] 修改 `provider.ts` 中的 `shouldUseStripe` 返回 `false`
- [ ] 移除所有计费检查逻辑

#### 8. 更新前端环境配置
**文件**: `apps/frontend/.env.local`
- [ ] 移除所有Stripe相关的公开密钥

### 第三阶段：Setup脚本修改

#### 9. 简化安装向导
**文件**: `setup.py`
- [ ] 移除Stripe API密钥的收集步骤（第382-384行）
- [ ] 跳过订阅相关的配置步骤
- [ ] 修改账户初始化，默认给予完整权限

### 第四阶段：核心功能保留

#### 10. 确保核心功能正常
- [ ] Agent创建和管理
- [ ] 对话线程管理
- [ ] 工具集成（浏览器自动化、文件管理等）
- [ ] API密钥管理
- [ ] 知识库功能

#### 11. 修改默认配置
创建一个配置覆盖文件，设置无限制的默认值：
```python
# backend/core/utils/no_limits_config.py
DEFAULT_USER_TIER = "unlimited"
MAX_AGENTS = 999999
MAX_THREADS = 999999
MAX_MESSAGES = 999999
ENABLE_ALL_FEATURES = True
```

### 第五阶段：测试和验证

#### 12. 功能测试
- [ ] 测试用户注册（无需支付信息）
- [ ] 测试Agent创建（无数量限制）
- [ ] 测试所有核心功能是否正常工作
- [ ] 验证没有付费墙提示

#### 13. 清理代码
- [ ] 删除未使用的billing模块文件
- [ ] 更新README，移除付费相关说明
- [ ] 清理导入语句中的billing引用

## 快速实施方案（最小改动）

如果你想快速实现，可以采用以下最小改动方案：

### 方案A：配置覆盖法
1. 修改 `backend/core/utils/limits_checker.py`，让所有检查都返回通过
2. 在 `backend/api.py` 中注释掉billing router
3. 修改前端，隐藏所有付费相关UI

### 方案B：数据库默认值法
1. 修改用户初始化脚本，自动给所有用户最高tier
2. 在数据库层面设置默认订阅为"unlimited"
3. 前端隐藏计费UI

## 关键文件清单

### 必须修改的文件
```
backend/api.py                          # 移除billing router
backend/core/utils/limits_checker.py    # 禁用限制检查
backend/core/auth/auth.py               # 简化认证
backend/.env                            # 移除Stripe配置
setup.py                                # 简化安装流程
```

### 可选修改的文件
```
backend/core/billing/                   # 整个目录可以删除或忽略
apps/frontend/                          # 搜索并移除计费UI
apps/mobile/lib/billing/                # 移除移动端计费
```

## 注意事项

⚠️ **重要提醒**：
1. 备份原始项目代码
2. 使用Git创建新分支进行修改
3. 某些功能可能依赖订阅系统，需要仔细测试
4. Supabase的RLS（行级安全）策略可能需要调整
5. 保留基本的用户认证，只移除付费验证

## 下一步

选择你想要的实施方案：
1. **完全移除** - 删除所有billing相关代码（需要较多时间）
2. **最小改动** - 只修改关键检查点，让限制失效（快速）
3. **配置覆盖** - 通过配置文件覆盖，不修改核心代码（最安全）

你想从哪个方案开始？
