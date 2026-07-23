# Simple Gmail API — Vercel Free

এটি আগের project-এর সহজ, ready-made সংস্করণ। Google Cloud, OAuth, Redis, Telegram, Pub/Sub বা database লাগবে না। শুধু দুইটি Vercel Environment Variable দিলেই কাজ করবে:

```dotenv
GMAIL_ADDRESS=yourname@gmail.com
GMAIL_APP_PASSWORD=your-16-character-app-password
```

## ৫ মিনিটে deploy

1. এই folder GitHub-এ upload করুন (private repository রাখাই ভালো)। `.env` file upload করবেন না।
2. [Vercel](https://vercel.com) → **Add New → Project** → GitHub repository import → Deploy। Free Hobby plan-ই যথেষ্ট।
3. Google account-এ **2-Step Verification** চালু করুন। তারপর [App Passwords](https://myaccount.google.com/apppasswords) খুলে একটি 16-character password তৈরি করুন। Google-এর নিয়ম অনুযায়ী App Password ব্যবহার করতে 2-Step Verification দরকার; Google password বদলালে app password revoke হয়। [Official Gmail help](https://support.google.com/mail/answer/185833)
4. Vercel → Project → **Settings → Environment Variables**-এ এই দুইটি variable add করুন:

   - `GMAIL_ADDRESS`: আপনার সম্পূর্ণ Gmail address
   - `GMAIL_APP_PASSWORD`: Google-এর দেওয়া 16-character App Password

5. Deployments → সর্বশেষ deployment → **Redeploy** করুন।

Gmail personal account-এ IMAP এখন default-ভাবে enabled থাকে; আলাদা করে IMAP enable করার দরকার নেই। [Gmail help](https://support.google.com/mail/answer/75726)

## পুরনো API একইভাবে ব্যবহার

Vercel URL যদি `https://my-api.vercel.app` হয়, তবে:

| কাজ | URL |
|---|---|
| Random dot alias | `/api/generate/dot` |
| Random plus alias | `/api/generate/dotplus` |
| Random dot/plus | `/api/generate/mixed` |
| Alias-এর message দেখা | `/api/read/your.alias@gmail.com` |
| Text দিয়ে খোঁজা | `/api/readby/your.alias@gmail.com/verification` |
| Message Trash-এ পাঠানো | `/api/delete/MESSAGE_UID` |

সব inbox endpoint নিরাপদ রাখার জন্য একই Gmail App Password header-এ দিতে হবে। এটি কোনো নতুন secret নয়। উদাহরণ:

```sh
curl -H 'Authorization: Bearer YOUR_16_CHARACTER_APP_PASSWORD' \
  'https://my-api.vercel.app/api/generate/mixed'
```

`/read/...` response-এ প্রতিটি message-এর `uid` পাওয়া যায়। সেটি `/delete/{uid}`-এ ব্যবহার করবেন।

## কী আছে, কী নেই

আছে: Gmail dot/plus generator, inbox check, sender/date/subject/body দেখা, text search, এবং message Trash-এ পাঠানো।

নেই: instant Telegram notification, multiple Gmail account, browser dashboard, continuous background checking। Vercel Free serverless function সব সময় চালু থাকে না; প্রতিটি API call-এর সময় Gmail-এ connect করে, কাজ করে, তারপর বন্ধ হয়। এই কারণেই এটি কেবল Gmail ও App Password দিয়েই চলে।

## নিরাপত্তা

- App Password কাউকে দেবেন না এবং URL query parameter-এ লিখবেন না। শুধু Vercel Environment Variable ও `Authorization` header-এ ব্যবহার করুন।
- Vercel project public হলেও header ছাড়া কেউ inbox পড়তে পারবে না।
- Google account password বদলালে নতুন App Password বানিয়ে Vercel-এর `GMAIL_APP_PASSWORD` update করে Redeploy দিন।
- এটি শুধু নিজের, অথবা যাঁদের স্পষ্ট অনুমতি আছে, তাঁদের inbox-এর জন্য ব্যবহার করুন।

## Local test

```sh
python3 -m unittest discover -s tests -v
```
