import json
import datetime
import random

# مواضيع متجددة وذكية يختار منها الروبوت لإنشاء محتوى حصري
ai_topics = [
    {
        "title": "The Evolution of Autonomous AI Agents in Software Engineering",
        "category": "Artificial Intelligence",
        "description": "How self-coding systems and autonomous software agents are radically transforming application architecture, debugging, and deployment workflows globally."
    },
    {
        "title": "Next-Gen Web Architecture: Zero-Maintenance Static Hubs",
        "category": "Web Development",
        "description": "Exploring how combining static hosting platforms with automated CI/CD pipelines creates infinitely scalable, self-updating digital ecosystems."
    },
    {
        "title": "Quantum Computing Milestones and Their Impact on Cryptography",
        "category": "Future Tech",
        "description": "A deep dive into recent hardware breakthroughs in quantum processors and what they mean for global digital security protocols."
    },
    {
        "title": "The Rise of Edge AI: Processing Intelligence on Local Devices",
        "category": "Hardware & AI",
        "description": "Why shifting machine learning workloads from massive cloud servers to edge devices is lowering latency and redefining user privacy."
    }
]

# اختيار موضوع عشوائي أو توليد محتوى متجدد
selected_topic = random.choice(ai_topics)
current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')

new_article = {
    "title": f"{selected_topic['title']} ({current_time})",
    "description": f"[{selected_topic['category']}] {selected_topic['description']} Autonomous systems have verified this trend as high-impact for 2026.",
    "url": "https://github.com/trending"
}

# قراءة الملف القديم أو إنشاء قائمة جديدة
try:
    with open("news.json", "r", encoding="utf-8") as f:
        news_list = json.load(f)
except Exception:
    news_list = []

# إضافة المقال الجديد في أول القائمة ليظهر دائماً في أعلى الموقع
news_list.insert(0, new_article)

# الاحتفاظ بأخر 10 مقالات فقط ليبقى الموقع خفيفاً ومنظماً
news_list = news_list[:10]

# حفظ البيانات المحدثة
with open("news.json", "w", encoding="utf-8") as f:
    json.dump(news_list, f, ensure_ascii=False, indent=4)

print("AI Autonomous Content Generated Successfully!")
