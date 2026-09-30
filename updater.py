import json
import datetime

# بيانات تجريبية يتم جلبها وتحديثها أوتوماتيكياً
updated_news = [
    {
        "title": f"AI Breakthroughs Update - {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}",
        "description": "Autonomous agents are reshaping software development, automation, and global digital infrastructure today.",
        "url": "https://news.google.com/search?q=Artificial+Intelligence"
    },
    {
        "title": "The Rise of Autonomous Web Hubs",
        "description": "Static hosting platforms combined with automated workflows enable zero-maintenance content distribution.",
        "url": "https://github.com"
    }
]

with open("news.json", "w", encoding="utf-8") as f:
    json.dump(updated_news, f, ensure_ascii=False, indent=4)

print("News updated successfully!")
