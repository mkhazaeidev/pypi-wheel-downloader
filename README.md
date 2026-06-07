# PyPI Wheel Downloader

Download all available wheel (`.whl`) files of the latest release of a package directly from PyPI.

دانلود تمام فایل‌های Wheel مربوط به آخرین نسخه منتشرشده یک پکیج از PyPI.

---

## Features / امکانات

### English

* Download all available wheel files from PyPI
* Automatic discovery of existing wheels
* No unnecessary failed attempts
* Real-time download progress
* Success and failure reports
* No third-party dependencies
* Works on Linux, macOS, and Windows

### فارسی

* دانلود تمام فایل‌های Wheel موجود از PyPI
* تشخیص خودکار Wheelهای واقعی
* جلوگیری از تلاش‌های ناموفق غیرضروری
* نمایش پیشرفت دانلود به‌صورت زنده
* گزارش فایل‌های موفق و ناموفق
* بدون وابستگی به کتابخانه‌های جانبی
* قابل اجرا روی لینوکس، مک و ویندوز

---

## Requirements / پیش‌نیازها

* Python 3.8+

Check Python version:

بررسی نسخه پایتون:

```bash
python3 --version
```

---

## Installation / نصب

Clone the repository:

کلون کردن ریپازیتوری:

```bash
git clone https://github.com/mkhazaeidev/pypi-wheel-downloader.git
cd pypi-wheel-downloader
```

No additional dependencies are required.

نیازی به نصب کتابخانه اضافی نیست.

---

## Usage / نحوه استفاده

Syntax:

ساختار دستور:

```bash
python3 download_all_wheels.py <package_name> <output_directory>
```

Example:

مثال:

```bash
python3 download_all_wheels.py numpy ./downloads
```

Another example:

مثال دیگر:

```bash
python3 download_all_wheels.py requests ./downloads
```

---

## Output Structure / ساختار خروجی

Example:

نمونه:

```
downloads/
└── numpy/
    ├── *.whl
    ├── success.txt
    └── failed.txt
```

### success.txt

Contains successfully downloaded files.

فهرست فایل‌هایی که با موفقیت دانلود شده‌اند.

### failed.txt

Contains files that failed to download.

فهرست فایل‌هایی که دانلود آن‌ها ناموفق بوده است.

---

## How It Works / نحوه عملکرد

### English

The script uses the official PyPI JSON API to retrieve metadata about the latest package release. It automatically discovers all available wheel files and downloads them.

### فارسی

این اسکریپت از API رسمی PyPI برای دریافت اطلاعات آخرین نسخه پکیج استفاده می‌کند و تمام Wheelهای موجود را به‌صورت خودکار پیدا و دانلود می‌کند.

---

## Use Cases / موارد استفاده

### English

* Offline package repositories
* Air-gapped environments
* Backup of package wheels
* CI/CD caching
* Research and package analysis

### فارسی

* ساخت مخزن آفلاین پکیج‌ها
* محیط‌های بدون دسترسی به اینترنت
* تهیه نسخه پشتیبان از Wheelها
* کش کردن وابستگی‌ها در CI/CD
* تحلیل و بررسی پکیج‌ها

---

## License / مجوز

MIT License

