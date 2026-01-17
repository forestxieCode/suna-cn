# Kortix - 无限制版本

> 基于原始Kortix项目的二次开发版本，移除了所有收费限制和账户验证

## 🎯 主要修改

这个版本移除了以下限制：
- ❌ Stripe支付集成
- ❌ 订阅验证
- ❌ 使用限制（Agent数量、线程数量、项目数量等）
- ❌ 付费墙和升级提示

## ✅ 保留功能

所有核心功能完全保留：
- ✅ AI Agent创建和管理
- ✅ 对话线程管理
- ✅ 浏览器自动化
- ✅ 文件管理
- ✅ 知识库
- ✅ 工具集成
- ✅ API访问

## 🚀 快速开始

```bash
# 1. 克隆或使用现有项目
cd d:\project\suna

# 2. 运行setup（如果还没运行过）
python setup.py

# 3. 启动项目
python start.py
# 或使用 Docker
docker-compose up -d
```

## 📖 详细文档

- **[二次开发完成.md](./二次开发完成.md)** - 完整的使用指南和说明
- **[UNRESTRICTED_MODIFICATIONS.md](./UNRESTRICTED_MODIFICATIONS.md)** - 技术细节和修改记录
- **[.agent/workflows/remove-payment-restrictions.md](./.agent/workflows/remove-payment-restrictions.md)** - 详细的实施步骤

## 🔧 核心修改

### 1. 移除限制检查
**文件**: `backend/core/utils/limits_checker.py`
```python
# 所有用户自动获得unlimited tier
return {
    'name': 'unlimited',
    'concurrent_runs': 999999,
    'thread_limit': 999999,
    'project_limit': 999999,
    # ... 所有限制都是999999
}
```

### 2. 禁用Billing模块
**文件**: `backend/api.py`
```python
# 注释掉billing相关的导入和路由
# from core.billing.api import router as billing_router
# api_router.include_router(billing_router)
```

## ⚠️ 重要提示

1. 这是基于原始Kortix项目的修改版本
2. 仅用于个人学习和开发
3. 所有修改都是最小化的，易于理解和维护
4. 可以随时通过Git恢复到原始版本

## 📝 版本信息

- **原始项目**: [Kortix/Suna](https://github.com/kortix-ai/suna)
- **修改版本**: v1.0 - 无限制版
- **修改日期**: 2026-01-17
- **修改方式**: 最小改动方案

## 🤝 贡献

这是一个二次开发版本，主要用于移除商业限制。如果你发现问题或有改进建议，欢迎提出。

## 📄 许可

遵循原始项目的许可协议。

---

**开始使用你的无限制AI Agent平台吧！🚀**
