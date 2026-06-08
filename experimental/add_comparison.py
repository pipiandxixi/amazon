import os

def add_comparison_section():
    file_path = "/Users/zhoufan/Public/workspace/amazon/recommended_niches_metrics.md"
    artifact_path = "/Users/zhoufan/.gemini/antigravity-cli/brain/9984e585-9795-4a86-9aa8-aeb0a61ba197/recommended_niches_metrics.md"
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    comparison_text = """### 2. 物流仓储限制前后的变化对比（过滤掉 20 个，新增 20 个）

在 Sellersprite 默认的列表提取中，原本**不加物流限制**时也同样返回了 **30 个**符合新手指标的子类目。但由于我们这次加入了严格的重量（$\\le 2.0$ lbs）与体积（$\\le 500$ in³）限制，**其中 20 个（占比 66.7%）偏大或偏重的子类目被成功过滤**，并被 **20 个更轻小的蓝海子类目**所替代。

具体变动如下：

*   ❌ **被过滤掉的 20 个超重/超大子类目**：
    1.  `Treadmills (跑步机)` (约 43.9 lbs)
    2.  `Raised Beds (花箱)` (约 22.5 lbs)
    3.  `Seat Covers (宠物汽车座椅套)` (约 4.5 lbs)
    4.  `Bug Zappers (灭虫器)` (约 2.3 lbs)
    5.  `Neck & Cervical Pillows (颈项枕)` (约 2.6 lbs)
    6.  `Formal (礼服)` (体积约 2548 in³)
    7.  `Floor Lamps (落地灯)` (超长件)
    8.  `Ceiling Fans (吊扇)` (超重/超大)
    9.  `Chairs (椅子)` (大件家具)
    10. `Outdoor Rugs (户外地毯)` (大体积)
    11. `Table Lamps (桌灯)`
    12. `Back Massagers (全身按摩垫)`
    13. `Foot Massagers (腿部按摩仪)`
    14. `Cushions (坐垫)`
    15. `Spotlights (聚光灯)`
    16. `Sun Shelters (海滩遮阳篷)`
    17. `Wall-Mounted Mirrors (墙镜)` (易碎/重)
    18. `Shade Cloth (遮光布)`
    19. `Weed Barrier Fabric (防草布)`
    20. `Reels (卷盘)`
*   ✨ **新晋并符合物流限制的 20 个轻小子类目**：
    1.  `Preserved Flowers (保鲜花)` (1.08 lbs) —— **🟢 终极推荐**
    2.  `Grill Brushes (烤炉刷)` (0.94 lbs) —— **🟢 终极推荐**
    3.  `Hand Fuel Pumps (手动燃油泵)` (1.58 lbs) —— **🟢 终极推荐**
    4.  `Wrinkle & Anti-Aging Devices (皱纹和抗衰老设备)` (0.93 lbs) —— **🟢 终极推荐**
    5.  `Electrical System Tools (电气系统工具)` (0.99 lbs) —— **🟢 终极推荐**
    6.  `Headlights (自行车车头灯)` (0.47 lbs) —— **🟢 终极推荐**
    7.  `GPS Trackers (GPS 追踪器)` (0.25 lbs) —— 🟡 谨慎
    8.  `Bladder Control Devices (膀胱控制设备)` (0.56 lbs) —— 🟡 谨慎
    9.  `Motion Detectors (生命探测器)` (0.71 lbs) —— 🟡 谨慎
    10. `Clutches (手拿包)` (0.58 lbs) —— 🟡 谨慎
    11. `Livestock Health Supplies (牲畜健康用品)` (1.19 lbs) —— 🔴 避坑
    12. `Battery Chargers (电池充电器)` (0.51 lbs) —— 🔴 避坑
    13. `Active Pants (运动裤)` (0.83 lbs) —— 🔴 避坑
    14. `Costumes (女士装扮服饰)` (0.99 lbs) —— 🔴 避坑
    15. `Costumes (男士装扮服饰)` (1.27 lbs) —— 🔴 避坑
    16. `Beneficial Insects (益虫)` (1.88 lbs) —— 🔴 避坑
    17. `Remote & App Controlled Vehicle Batteries (遥控模型电池)` (0.37 lbs) —— 🔴 避坑
    18. `Casual Jackets (休闲夹克)` (0.77 lbs) —— 🔴 避坑
    19. `Vests (女士单马甲)` (0.59 lbs) —— 🔴 避坑
    20. `Vests (男士单马甲)` (0.99 lbs) —— 🔴 避坑
*   🔄 **在限制前后均保留在 Top 30 的 10 个原本就轻小的子类目**：
    `Club & Night Out (俱乐部装)`, `Dresses (连衣裙)`, `Testosterone Boosters (睾酮助推器)`, `Handheld Massagers (手持按摩器)`, `Battery Packs (电池组)`, `Special Occasion (特殊场合)`, `Shoulder Bags (单肩包)`, `Suits (套装)`等。

---"""
    
    # We will insert it right before "## 一、 全 30 个符合条件细分市场关键数据汇总表"
    target = "## 一、 全 30 个符合条件细分市场关键数据汇总表"
    if target in content:
        updated_content = content.replace(target, comparison_text + "\n\n" + target)
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(updated_content)
            
        with open(artifact_path, 'w', encoding='utf-8') as f:
            f.write(updated_content)
            
        print("Comparison section successfully added to the report files.")
    else:
        print("Target header not found in the file.")

if __name__ == "__main__":
    add_comparison_section()
