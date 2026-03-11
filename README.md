import tweepy
import random

# المفاتيح اللي في صورك
consumer_key = '8YVRhaWnXsUYpeHXFHXrfEFK3'
consumer_secret = 'C05oFIV3yWTLcDw3YUiru1Hx6jWgutYiVnEUqYPkPwRyc2EpCi'
access_token = '2030833849136025601-vQTothKZh1vRxC3NjpgDn3vjn06vKP'
access_token_secret = 'QNHzhcMZDTVtZJZWR1UCkMAXSyEwm6ocjpRFywIImRyn7'

azkar = ["سُبْحَانَ اللَّهِ وَبِحَمْدِهِ", "الْحَمْدُ لِلَّهِ", "لَا إِلَهَ إِلَّا اللَّهُ"]

def tweet():
    try:
        # استخدام الطريقة التقليدية (OAuth 1.0a) وهي الأقوى في الصلاحيات
        auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_token_secret)
        api = tweepy.API(auth)
        
        zikr = random.choice(azkar)
        # محاولة النشر عبر الطريقة القديمة (تلقائياً يحولها تويتر لـ V2 إذا لزم الأمر)
        api.update_status(status=zikr)
        print("✅ Success!")
    except Exception as e:
        print(f"❌ Error Detail: {e}")

if __name__ == "__main__":
    tweet()
