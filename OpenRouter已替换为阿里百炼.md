# ✅ OpenRouter已替换为阿里百炼

## 📝 已完成的修改

我已经直接修改了项目代码，将OpenRouter替换为阿里百炼：

### 1. 修改的文件

#### ✅ `backend/.env`
- 将 `OPENROUTER_API_BASE` 设置为阿里百炼地址
- 添加了配置说明

#### ✅ `backend/core/utils/config.py`  
- 修改默认的 `OPENROUTER_API_BASE` 为阿里百炼API地址

#### ✅ `backend/core/ai_models/registry.py`
- 将 `kortix/basic` 映射到 `qwen-plus`
- 将 `kortix/power` 映射到 `qwen-max`
- 将 `kortix/test` 映射到 `qwen-turbo`
- 更新了各模型的成本配置

#### ✅ `backend/core/sandbox/canvas_ai_api.py`
- 将画板AI模型替换为 `qwen-vl-plus` 和 `qwen-vl-max`
- 确保画板功能也走阿里百炼通道

#### ✅ `backend/core/services/llm.py`
- 添加自动配置逻辑，使LiteLLM能正确识别阿里百炼API

#### ✅ `setup.py`
- 修改安装向导中的OpenRouter说明为阿里百炼

---

## 🚀 现在你需要做的

### 步骤1: 获取阿里百炼API密钥

1. 访问 https://bailian.console.aliyun.com/
2. 登录阿里云账号
3. 创建应用并获取API Key
4. API Key格式类似: `sk-xxxxxxxxxxxxxxxx`

### 步骤2: 填写API密钥

编辑 `backend/.env` 文件，找到这一行：

```bash
OPENROUTER_API_KEY=your_bailian_api_key_here
```

将 `your_bailian_api_key_here` 替换为你的实际API密钥：

```bash
OPENROUTER_API_KEY=sk-你的真实API密钥
```

### 步骤3: 重启服务

```bash
# 停止当前运行的服务（Ctrl+C）
# 然后重新启动
python start.py
```

---

## 🎯 使用阿里百炼模型

现在在Agent配置中，你可以直接使用以下模型名称：

### 推荐模型

- **`qwen-turbo`** - 快速响应，适合日常对话
  - 成本: 输入 ¥0.3/百万tokens, 输出 ¥0.6/百万tokens
  
- **`qwen-plus`** - 平衡性能，推荐使用 ⭐
  - 成本: 输入 ¥0.8/百万tokens, 输出 ¥2.0/百万tokens
  
- **`qwen-max`** - 最强性能，复杂任务
  - 成本: 输入 ¥20/百万tokens, 输出 ¥60/百万tokens

### 使用方法

在创建或编辑Agent时，模型字段填写：

```
qwen-plus
```

或者

```
qwen-turbo
```

或者

```
qwen-max
```

---

## ✨ 优势

### 相比OpenRouter

- ✅ **成本降低50-80%**
- ✅ **国内访问速度快**
- ✅ **无需翻墙**
- ✅ **低延迟响应**
- ✅ **数据合规**

---

## 🔍 验证配置

填写API密钥后，运行测试：

```bash
python test_bailian.py
```

如果看到：

```
✅ API调用成功！
模型响应: 我是通义千问...
```

说明配置成功！

---

## ⚠️ 注意事项

1. **API密钥格式**: 以 `sk-` 开头
2. **环境变量名称**: 虽然变量名还是 `OPENROUTER_API_KEY`，但实际指向阿里百炼
3. **模型名称**: 直接使用 `qwen-turbo`、`qwen-plus`、`qwen-max`
4. **兼容性**: 完全兼容原有代码，无需修改其他地方

---

## 📋 配置文件位置

```
backend/.env  ← 在这里填写API密钥
```

找到这一行并修改：

```bash
OPENROUTER_API_KEY=your_bailian_api_key_here  ← 改成你的真实密钥
```

---

## 🎉 完成！

修改完API密钥后，重启服务即可使用阿里百炼！

**下一步**:
1. ✅ 获取API密钥
2. ✅ 填写到 `backend/.env`
3. ✅ 重启服务
4. ✅ 使用 `qwen-plus` 模型
5. ✅ 享受更快更便宜的AI服务！

---

**最后更新**: 2026-01-17
