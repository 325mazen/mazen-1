import tweepy
import random

# مفاتيح مازن (مستخرجة من صورك)
c_k = '8YVRhaWnXsUYpeHXFHXrfEFK3'
c_s = 'C05oFIV3yWTLcDw3YUiru1Hx6jWgutYiVnEUqYPkPwRyc2EpCi'
a_t = '2030833849136025601-vQTothKZh1vRxC3NjpgDn3vjn06vKP'
a_ts = 'QNHzhcMZDTVtZJZWR1UCkMAXSyEwm6ocjpRFywIImRyn7'

# قائمة الأذكار مرتبة
azkar = [
    "سُبْحَانَ اللَّهِ وَبِحَمْدِهِ",
    "سُبْحَانَ اللَّهِ الْعَظِيمِ",
    "لَا حَوْلَ وَلَا قُوَّةَ إِلَّا بِاللَّهِ",
    "اللَّهُ أَكْبَرُ",
    "الْحَمْدُ لِلَّهِ",
    "لَا إِلَهَ إِلَّا اللَّهُ"
]

def tweet():
    try:
        # الربط الرسمي
        client = tweepy.Client(
            consumer_key=c_k.strip(),
            consumer_secret=c_s.strip(),
            access_token=a_t.strip(),
            access_token_secret=a_ts.strip()
        )
        zikr = random.choice(azkar)
        client.create_tweet(text=zikr)
        print("✅ Success!")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    tweet()
