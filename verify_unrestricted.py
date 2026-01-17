#!/usr/bin/env python3
"""
验证Kortix无限制修改是否生效

运行此脚本来检查限制是否已被移除
"""
import sys
import os

# 添加backend到路径
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'backend'))

def test_limits_checker():
    """测试limits_checker是否返回无限制配置"""
    print("=" * 60)
    print("测试 1: 检查limits_checker配置")
    print("=" * 60)
    
    try:
        import asyncio
        from core.utils.limits_checker import _get_tier_info_if_needed
        
        async def check():
            tier_info = await _get_tier_info_if_needed("test_account_id")
            print(f"\n✅ Tier信息获取成功:")
            print(f"   - Tier名称: {tier_info.get('name')}")
            print(f"   - 并发运行限制: {tier_info.get('concurrent_runs')}")
            print(f"   - 线程限制: {tier_info.get('thread_limit')}")
            print(f"   - 项目限制: {tier_info.get('project_limit')}")
            print(f"   - 自定义Worker限制: {tier_info.get('custom_workers_limit')}")
            print(f"   - 定时触发器限制: {tier_info.get('scheduled_triggers_limit')}")
            print(f"   - 应用触发器限制: {tier_info.get('app_triggers_limit')}")
            
            if tier_info.get('name') == 'unlimited':
                print("\n✅ 成功！所有限制已移除，tier为'unlimited'")
                return True
            else:
                print(f"\n❌ 警告！Tier仍为 '{tier_info.get('name')}'，不是'unlimited'")
                return False
        
        result = asyncio.run(check())
        return result
        
    except Exception as e:
        print(f"\n❌ 错误: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_api_imports():
    """测试API是否正确禁用了billing模块"""
    print("\n" + "=" * 60)
    print("测试 2: 检查API配置")
    print("=" * 60)
    
    try:
        with open('backend/api.py', 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 检查billing router是否被注释
        billing_import_commented = '# from core.billing.api import router as billing_router' in content
        billing_router_commented = '# api_router.include_router(billing_router)' in content
        billing_admin_commented = '# from core.admin.billing_admin_api import router as billing_admin_router' in content
        
        print("\n检查结果:")
        print(f"   - Billing导入已注释: {'✅' if billing_import_commented else '❌'}")
        print(f"   - Billing路由已注释: {'✅' if billing_router_commented else '❌'}")
        print(f"   - Billing管理已注释: {'✅' if billing_admin_commented else '❌'}")
        
        if billing_import_commented and billing_router_commented and billing_admin_commented:
            print("\n✅ 成功！Billing模块已完全禁用")
            return True
        else:
            print("\n❌ 警告！部分billing代码未被注释")
            return False
            
    except Exception as e:
        print(f"\n❌ 错误: {e}")
        return False

def test_env_config():
    """检查环境配置"""
    print("\n" + "=" * 60)
    print("测试 3: 检查环境配置")
    print("=" * 60)
    
    env_file = 'backend/.env'
    if not os.path.exists(env_file):
        print(f"\n⚠️  环境文件 {env_file} 不存在")
        print("   这是正常的，如果你还没运行setup.py")
        return True
    
    try:
        with open(env_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        has_stripe = 'STRIPE_SECRET_KEY' in content and not content.startswith('#STRIPE_SECRET_KEY')
        
        if has_stripe:
            print("\n⚠️  注意: 环境文件中仍包含STRIPE配置")
            print("   这不会影响功能，因为billing模块已被禁用")
            print("   你可以选择删除或注释这些配置")
        else:
            print("\n✅ 环境文件中没有活动的Stripe配置")
        
        return True
        
    except Exception as e:
        print(f"\n❌ 错误: {e}")
        return False

def main():
    """运行所有测试"""
    print("\n" + "🚀" * 30)
    print("Kortix 无限制修改验证脚本")
    print("🚀" * 30 + "\n")
    
    results = []
    
    # 运行测试
    results.append(("Limits Checker", test_limits_checker()))
    results.append(("API配置", test_api_imports()))
    results.append(("环境配置", test_env_config()))
    
    # 总结
    print("\n" + "=" * 60)
    print("测试总结")
    print("=" * 60)
    
    for name, passed in results:
        status = "✅ 通过" if passed else "❌ 失败"
        print(f"{name}: {status}")
    
    all_passed = all(result[1] for result in results)
    
    if all_passed:
        print("\n" + "🎉" * 30)
        print("所有测试通过！你的Kortix项目已成功移除限制！")
        print("🎉" * 30)
        print("\n下一步:")
        print("1. 运行 'python setup.py' 完成初始配置（如果还没运行）")
        print("2. 启动项目: 'python start.py' 或 'docker-compose up'")
        print("3. 创建账户并开始使用，没有任何限制！")
    else:
        print("\n⚠️  部分测试未通过，请检查上述错误信息")
        print("查看 UNRESTRICTED_MODIFICATIONS.md 了解详细信息")
    
    print("\n")

if __name__ == "__main__":
    main()
