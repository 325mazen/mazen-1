import tweepy
import random

# الصق مفاتيحك الجديدة هنا بدقة
bearer_token = 'ضع_هنا_الـ_Bearer_Token'
consumer_key = 'ضع_هنا_الـ_API_Key'
consumer_secret = 'ضع_هنا_الـ_API_Key_Secret'
access_token = 'ضع_هنا_الـ_Access_Token'
access_token_secret = 'ضع_هنا_الـ_Access_Token_Secret'

# قائمة الأذكار
azkar = ["سُبْحَانَ اللَّهِ وَبِحَمْدِهِ", "سُبْحَانَ اللَّهِ الْعَظِيمِ", "أَسْتَغْفِرُ اللَّهَ", "لَا إِلَهَ إِلَّا اللَّهُ"]

def tweet():
    try:
        # الاتصال باستخدام OAuth 1.0a (الأضمن للنشر)
        auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_token_secret)
        api = tweepy.API(auth)
        
        # اختيار ذكر عشوائي
        zikr = random.choice(azkar)
        
        # محاولة النشر
        api.update_status(status=zikr)
        print(f"✅ Success: {zikr}")
        
    except Exception as e:
        print(f"❌ Error Detail: {e}")

if __name__ == "__main__":
    tweet()
