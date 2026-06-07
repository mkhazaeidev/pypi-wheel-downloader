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
* Dedicated downloaders for Windows, Linux, and macOS.

### فارسی

* دانلود تمام فایل‌های Wheel مربوط به آخرین نسخه یک پکیج.
* شناسایی خودکار Wheelهای منتشرشده.
* نمایش زنده پیشرفت دانلود.
* گزارش فایل‌های موفق و ناموفق.
* بدون وابستگی به کتابخانه‌های جانبی.
* پشتیبانی از پلتفرم‌های مختلف.
* اسکریپت‌های اختصاصی برای ویندوز، لینوکس و macOS.

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

| Script                   | English                            | فارسی                      |
| ------------------------ | ---------------------------------- | -------------------------- |
| `download_pypi_all.py`   | Download all available wheel files | دانلود تمام Wheelهای موجود |
| `download_pypi_win.py`   | Download Windows wheels only       | دانلود فقط Wheelهای ویندوز |
| `download_pypi_linux.py` | Download Linux wheels only         | دانلود فقط Wheelهای لینوکس |
| `download_pypi_macOS.py` | Download macOS wheels only         | دانلود فقط Wheelهای macOS  |

---

# 1. download_pypi_all.py

## English

Downloads **all available wheel files** for the latest release of a package, regardless of operating system or architecture.

## فارسی

تمام Wheelهای موجود مربوط به آخرین نسخه منتشرشده یک پکیج را دانلود می‌کند؛ بدون توجه به سیستم‌عامل یا معماری.

### Usage / نحوه استفاده

```bash
python3 download_pypi_all.py <package_name> <output_directory>
```

### Examples / مثال‌ها

```bash
python3 download_pypi_all.py numpy ./downloads
```

```bash
python3 download_pypi_all.py requests ./downloads
```

### Example Output / نمونه خروجی

```text
downloads/
└── numpy/
    ├── *.whl
    ├── success.txt
    └── failed.txt
```

---

# 2. download_pypi_win.py

## English

Downloads only Windows wheel files (`win_amd64` and `win32`) for the latest release of a package.

Useful when you only need packages for Windows systems.

## فارسی

فقط Wheelهای ویندوز (`win_amd64` و `win32`) مربوط به آخرین نسخه منتشرشده یک پکیج را دانلود می‌کند.

برای زمانی مناسب است که فقط به فایل‌های ویندوز نیاز دارید.

### Usage / نحوه استفاده

```bash
python3 download_pypi_win.py <package_name> <output_directory>
```

### Examples / مثال‌ها

```bash
python3 download_pypi_win.py numpy ./downloads
```

```bash
python3 download_pypi_win.py pyqt6 ./downloads
```

### Example Output / نمونه خروجی

```text
downloads/
└── numpy/
    ├── numpy-*-win_amd64.whl
    ├── success.txt
    └── failed.txt
```

---

# 3. download_pypi_linux.py

## English

Downloads only Linux wheel files.

Supports all Linux distributions published on PyPI, including:

* manylinux
* manylinux2014
* manylinux_2_x
* musllinux

Useful for Ubuntu servers, Docker images, offline repositories, and Linux deployments.

## فارسی

فقط Wheelهای لینوکسی را دانلود می‌کند.

از تمام توزیع‌های لینوکسی منتشرشده در PyPI پشتیبانی می‌کند، از جمله:

* manylinux
* manylinux2014
* manylinux_2_x
* musllinux

برای سرورهای Ubuntu، داکر، مخازن آفلاین و استقرار روی لینوکس بسیار مناسب است.

### Usage / نحوه استفاده

```bash
python3 download_pypi_linux.py <package_name> <output_directory>
```

### Examples / مثال‌ها

```bash
python3 download_pypi_linux.py numpy ./downloads
```

```bash
python3 download_pypi_linux.py torch ./downloads
```

### Example Output / نمونه خروجی

```text
downloads/
└── numpy/
    ├── numpy-*-manylinux*.whl
    ├── numpy-*-musllinux*.whl
    ├── success.txt
    └── failed.txt
```

---

# 4. download_pypi_macOS.py

## English

Downloads only macOS wheel files.

Supports:

* Intel (`x86_64`)
* Apple Silicon (`arm64`)
* Universal builds (`universal2`)

Useful for preparing offline installations on macOS devices.

## فارسی

فقط Wheelهای macOS را دانلود می‌کند.

پشتیبانی می‌کند از:

* پردازنده‌های Intel (`x86_64`)
* پردازنده‌های Apple Silicon (`arm64`)
* نسخه‌های Universal (`universal2`)

برای نصب آفلاین روی دستگاه‌های macOS بسیار کاربردی است.

### Usage / نحوه استفاده

```bash
python3 download_pypi_macOS.py <package_name> <output_directory>
```

### Examples / مثال‌ها

```bash
python3 download_pypi_macOS.py numpy ./downloads
```

```bash
python3 download_pypi_macOS.py pyqt6 ./downloads
```

### Example Output / نمونه خروجی

```text
downloads/
└── numpy/
    ├── numpy-*-macosx_*_x86_64.whl
    ├── numpy-*-macosx_*_arm64.whl
    ├── numpy-*-macosx_*_universal2.whl
    ├── success.txt
    └── failed.txt
```

---

# How It Works / نحوه عملکرد

## English

The scripts use the official PyPI JSON API to retrieve metadata about the latest release of a package. They automatically discover available wheel files and download them while displaying real-time progress.

## فارسی

این اسکریپت‌ها از API رسمی PyPI برای دریافت اطلاعات آخرین نسخه پکیج استفاده می‌کنند. سپس Wheelهای موجود را به‌صورت خودکار پیدا کرده و همراه با نمایش زنده پیشرفت دانلود می‌کنند.

---

# Use Cases / موارد استفاده

## English

* Offline package repositories
* Air-gapped environments
* CI/CD cache preparation
* Wheel backups
* Package analysis
* Windows deployments
* Linux deployments
* macOS deployments

## فارسی

* ساخت مخزن آفلاین پکیج‌ها
* محیط‌های بدون اینترنت
* آماده‌سازی کش برای CI/CD
* تهیه نسخه پشتیبان از Wheelها
* تحلیل پکیج‌ها
* استقرار روی ویندوز
* استقرار روی لینوکس
* استقرار روی macOS

---

# Project Structure / ساختار پروژه

```text
pypi-wheel-downloader/
├── download_pypi_all.py
├── download_pypi_win.py
├── download_pypi_linux.py
├── download_pypi_macOS.py
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

Current stable release: **v1.3.0**

