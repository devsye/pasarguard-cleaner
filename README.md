# pasarguard-cleaner

[English](#english) | [فارسی](#فارسی)

---

## English

A small Python script that deletes **expired** and **data-limited** users from a PasarGuard panel through its REST API.

- Lists every user with status `expired` or `limited`
- Asks for confirmation before deleting anything
- Throttled (1 request per second) and auto-retries if the panel drops the connection
- Credentials are read from environment variables, never stored in code

### Requirements

- Python 3
- `requests` library
- A panel admin account that is allowed to delete users

### Android (Termux)

Install Termux from F-Droid (not the Play Store version), then:

    pkg update -y
    pkg install python git -y
    git clone https://github.com/devsye/pasarguard-cleaner
    cd pasarguard-cleaner
    pip install -r requirements.txt

    export PANEL_URL='https://your-panel.example.com:8000'
    export PANEL_USER='your-admin-username'
    export PANEL_PASS='your-admin-password'
    python clean_expired.py

### Windows (PowerShell)

Install Python from python.org (tick "Add Python to PATH"), then:

    git clone https://github.com/devsye/pasarguard-cleaner
    cd pasarguard-cleaner
    pip install -r requirements.txt

    $env:PANEL_URL='https://your-panel.example.com:8000'
    $env:PANEL_USER='your-admin-username'
    $env:PANEL_PASS='your-admin-password'
    python clean_expired.py

### Linux / macOS

    git clone https://github.com/devsye/pasarguard-cleaner
    cd pasarguard-cleaner
    pip3 install -r requirements.txt

    export PANEL_URL='https://your-panel.example.com:8000'
    export PANEL_USER='your-admin-username'
    export PANEL_PASS='your-admin-password'
    python3 clean_expired.py

No git? Download the ZIP from the green **Code** button on GitHub instead.

### How it works

1. Logs in and gets a token (`POST /api/admin/token`)
2. Lists users with status `expired` and `limited` (`GET /api/users`)
3. Prints the count and waits for you to type `yes`
4. Deletes users one by one (`DELETE /api/user/{username}`)

### Troubleshooting

| Error | Meaning |
|-------|---------|
| `401` | Wrong username or password |
| `403` | Your account is not allowed to do this (common on reseller panels) |
| `404` on login | Wrong `PANEL_URL`, or a different panel version |
| `Connection aborted` | Panel is rate limiting; the script waits and retries |

### Notes

- Written for PasarGuard API paths. Marzban-style panels may work too, but this is untested.
- Deleting users is **permanent**. Check the printed count first.
- Put single quotes around values so special characters in passwords do not break the command.
- Use only on panels you own or are authorized to manage.

---

<div dir="rtl">

## فارسی

یک اسکریپت ساده‌ی پایتون که کاربران **منقضی‌شده** و **حجم‌تمام‌شده** رو از پنل پاسارگارد از طریق API حذف می‌کنه.

- همه‌ی کاربران با وضعیت `expired` و `limited` رو لیست می‌کنه
- قبل از حذف تأیید می‌گیره
- آروم کار می‌کنه (هر ثانیه یک درخواست) و اگه پنل ارتباط رو قطع کرد، خودش دوباره تلاش می‌کنه
- یوزر و پسوورد از متغیر محیطی خونده می‌شه و توی کد ذخیره نیست

### پیش‌نیازها

- پایتون ۳
- کتابخانه‌ی `requests`
- اکانت ادمین پنل که اجازه‌ی حذف کاربر داشته باشه

### اندروید (Termux)

Termux رو از F-Droid نصب کن (نسخه‌ی پلی‌استور خراب کار می‌کنه) و بعد:

    pkg update -y
    pkg install python git -y
    git clone https://github.com/devsye/pasarguard-cleaner
    cd pasarguard-cleaner
    pip install -r requirements.txt

    export PANEL_URL='https://your-panel.example.com:8000'
    export PANEL_USER='your-admin-username'
    export PANEL_PASS='your-admin-password'
    python clean_expired.py

### ویندوز (PowerShell)

پایتون رو از python.org نصب کن (تیک «Add Python to PATH» رو بزن) و بعد:

    git clone https://github.com/devsye/pasarguard-cleaner
    cd pasarguard-cleaner
    pip install -r requirements.txt

    $env:PANEL_URL='https://your-panel.example.com:8000'
    $env:PANEL_USER='your-admin-username'
    $env:PANEL_PASS='your-admin-password'
    python clean_expired.py

### لینوکس / مک

    git clone https://github.com/devsye/pasarguard-cleaner
    cd pasarguard-cleaner
    pip3 install -r requirements.txt

    export PANEL_URL='https://your-panel.example.com:8000'
    export PANEL_USER='your-admin-username'
    export PANEL_PASS='your-admin-password'
    python3 clean_expired.py

گیت نداری؟ از دکمه‌ی سبز **Code** توی گیت‌هاب فایل ZIP رو دانلود کن.

### نحوه‌ی کار

۱. لاگین می‌کنه و توکن می‌گیره
۲. لیست کاربران `expired` و `limited` رو می‌گیره
۳. تعدادشون رو چاپ می‌کنه و منتظر می‌مونه تا `yes` بنویسی
۴. کاربرها رو یکی‌یکی حذف می‌کنه

### رفع خطا

| خطا | معنی |
|-----|------|
| `401` | یوزر یا پسوورد اشتباهه |
| `403` | اکانتت اجازه‌ی این کار رو نداره (توی پنل‌های نمایندگی رایجه) |
| `404` موقع لاگین | آدرس `PANEL_URL` اشتباهه یا نسخه‌ی پنل فرق داره |
| `Connection aborted` | پنل جلوی درخواست‌ها رو گرفته؛ اسکریپت صبر می‌کنه و دوباره تلاش می‌کنه |

### نکته‌ها

- برای مسیرهای API پاسارگارد نوشته شده. پنل‌های مرزبان‌مانند ممکنه کار کنن، ولی تست نشده.
- حذف کاربر **دائمیه**. قبل از تأیید، تعداد چاپ‌شده رو چک کن.
- مقادیر رو داخل تک‌کوتیشن بنویس تا کاراکترهای خاص پسوورد مشکل ایجاد نکنه.
- فقط روی پنل‌هایی استفاده کن که مال خودته یا اجازه‌ی مدیریتشون رو داری.

</div>

---

## License

MIT
