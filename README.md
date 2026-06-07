# PyPI Wheel Downloader

Download wheel (`.whl`) files directly from the official PyPI API.

دانلود فایل‌های Wheel (`.whl`) مستقیماً از API رسمی PyPI.

---

## Features / امکانات

### English

* Download all available wheel files for the latest release of a PyPI package.
* Automatic discovery of published wheels.
* Real-time download progress.
* Success and failure reports.
* No external dependencies.
* Cross-platform support.
* Dedicated Windows-only downloader.

### فارسی

* دانلود تمام فایل‌های Wheel مربوط به آخرین نسخه یک پکیج.
* شناسایی خودکار Wheelهای منتشرشده.
* نمایش زنده پیشرفت دانلود.
* گزارش فایل‌های موفق و ناموفق.
* بدون وابستگی به کتابخانه‌های جانبی.
* پشتیبانی از پلتفرم‌های مختلف.
* اسکریپت اختصاصی برای دانلود Wheelهای ویندوز.

---

## Requirements / پیش‌نیازها

* Python 3.8 or newer

Check your Python version:

بررسی نسخه پایتون:

```bash
python3 --version
```

---

# Available Scripts / اسکریپت‌های موجود

## 1. download_pypi_all.py

### English

Downloads **all available wheel files** for the latest release of a package, regardless of operating system or architecture.

### فارسی

تمام Wheelهای موجود مربوط به آخرین نسخه منتشرشده یک پکیج را دانلود می‌کند؛ بدون توجه به سیستم‌عامل یا معماری.

---

## Usage / نحوه استفاده

```bash
python3 download_pypi_all.py <package_name> <output_directory>
```

Example:

```bash
python3 download_pypi_all.py numpy ./downloads
```

Another example:

```bash
python3 download_pypi_all.py requests ./downloads
```

---

## Example Output / نمونه خروجی

```text
downloads/
└── numpy/
    ├── numpy-*.whl
    ├── success.txt
    └── failed.txt
```

---

# 2. download_pypi_win.py

### English

Downloads only **Windows wheel files** (`win_amd64` and `win32`) for the latest release of a package.

This is useful if you only need packages for Windows environments.

### فارسی

فقط Wheelهای ویندوز (`win_amd64` و `win32`) مربوط به آخرین نسخه منتشرشده یک پکیج را دانلود می‌کند.

اگر فقط به فایل‌های ویندوز نیاز دارید، استفاده از این اسکریپت سریع‌تر و کم‌حجم‌تر خواهد بود.

---

## Usage / نحوه استفاده

```bash
python3 download_pypi_win.py <package_name> <output_directory>
```

Example:

```bash
python3 download_pypi_win.py numpy ./downloads
```

Another example:

```bash
python3 download_pypi_win.py pyqt6 ./downloads
```

---

## Example Output / نمونه خروجی

```text
downloads/
└── numpy/
    ├── numpy-2.x.x-cp311-cp311-win_amd64.whl
    ├── numpy-2.x.x-cp312-cp312-win_amd64.whl
    ├── success.txt
    └── failed.txt
```

---

# How It Works / نحوه عملکرد

### English

The scripts use the official PyPI JSON API to retrieve metadata about the latest release of a package. They automatically discover available wheel files and download them with real-time progress reporting.

### فارسی

این اسکریپت‌ها از API رسمی PyPI برای دریافت اطلاعات آخرین نسخه پکیج استفاده می‌کنند. سپس Wheelهای موجود را به‌صورت خودکار پیدا کرده و همراه با نمایش پیشرفت دانلود می‌کنند.

---

# Use Cases / موارد استفاده

### English

* Offline package repositories
* Air-gapped environments
* CI/CD cache preparation
* Wheel backups
* Package analysis
* Windows deployment preparation

### فارسی

* ساخت مخزن آفلاین پکیج‌ها
* محیط‌های بدون اینترنت
* آماده‌سازی کش برای CI/CD
* تهیه نسخه پشتیبان از Wheelها
* تحلیل پکیج‌ها
* آماده‌سازی استقرار روی ویندوز

---

# Project Structure / ساختار پروژه

```text
pypi-wheel-downloader/
├── download_pypi_all.py
├── download_pypi_win.py
├── README.md
├── LICENSE
├── requirements.txt
└── .gitignore
```

---

# License / مجوز

This project is licensed under the MIT License.

این پروژه تحت مجوز MIT منتشر شده است.

See the LICENSE file for details.

برای جزئیات بیشتر، فایل LICENSE را مطالعه کنید.

---

# Version

Current stable release: **v1.0.0**

