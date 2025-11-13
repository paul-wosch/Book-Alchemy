# Book‑Alchemy 📚✨

![Python](https://img.shields.io/badge/python-3.10%2B-blue)
![Flask](https://img.shields.io/badge/flask-3.x-lightgrey)
![Code style: PEP8](https://img.shields.io/badge/code%20style-PEP8-yellow)
![Status](https://img.shields.io/badge/status-learning--project-orange)
![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)
[![Quick Start](https://img.shields.io/badge/⚡-Quick%20Start-orange)](#-quick-start)

*A public learning artifact on building a modular Flask app with SQLAlchemy, Jinja2 templates, and styled UI themes.*

---

## 📑 Table of Contents  

- [⚠️ Disclaimer](#-disclaimer)  
- [📝 Description](#-description)  
- [✨ Features](#-features)  
- [🛠️ Tech Stack & Dependencies](#-tech-stack--dependencies)  
- [📦 Key Dependencies](#-key-dependencies)  
- [📁 Project Structure](#-project-structure)  
- [🛠️ Development Setup](#-development-setup)  
  - [🚀 Quick Start](#-quick-start)  
  - [📖 Step‑by‑Step Guide](#-step-by-step-guide)  
- [👥 Contributing](#-contributing)  
- [🏷️ Badges](#-badges)  
- [📄 License](#-license)  

---

## ⚠️ Disclaimer
This repository is a **learning project** created as part of my journey in software engineering. It represents a work in progress where I applied my best effort and current knowledge.  

* The focus has been on practicing **object‑oriented programming** with Python and **SQLAlchemy**, building a **Flask application** backed by an SQLite database, and modularizing **Jinja2 templates** for a maintainable UI.
* Along the way, I also explored **AI‑assisted programming** — initially motivated by time constraints, later reframed as an exercise in experimentation. AI support was mainly used for **UI styling** and for quickly generating **code snippets** that I would otherwise have written manually, while all **architectural decisions** remained deliberate and accountable.
* Finally, this project gave me the chance to practice **project development and documentation** with Git/GitHub.  

This project is not intended for production use and will not be actively maintained, but it reflects my growth, curiosity, and dedication to learning modern development principles.


---

## 📝 Description  
**Book‑Alchemy** is a small web application for managing a personal library of books and authors.  

- Provides full CRUD functionality for authors and books.  
- Uses SQLAlchemy with SQLite for data persistence.  
- Built with modular Jinja2 templates for maintainable UI.  
- Offers a styled interface with theming and user feedback.  

---

## ✨ Features  
- 📚 **Library overview**: list all books with author details and cover images (via OpenLibrary ISBN).  
- ➕ **Create**: add new authors and books through forms.  
- ✏️ **Update**: edit existing authors and books with pre‑filled forms.  
- ❌ **Delete**: remove books directly from their detail view.  
- 🔍 **Search**: filter books by title.  
- ↕️ **Sort**: order books by title or author.  
- 🎨 **Themes**: toggle between dark, pastel, and high contrast styles.  
- 🔔 **Flash messages**: success messages implemented; info, warning, and error styles prepared.  
- 🧩 **Modular templates**: reusable base layout and form components.  

---

## 🛠️ Tech Stack & Dependencies  

- ![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python) **Python** – core language  
- ![Flask](https://img.shields.io/badge/Flask-3.x-lightgrey?logo=flask) **Flask** – web framework  
- ![Flask-SQLAlchemy](https://img.shields.io/badge/Flask--SQLAlchemy-3.x-red?logo=python) **Flask‑SQLAlchemy** – ORM integration with Flask  
- ![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.x-red?logo=python) **SQLAlchemy** – database toolkit for SQLite  
- ![Jinja2](https://img.shields.io/badge/Jinja2-templates-orange) **Jinja2** – templating engine  
- ![CSS](https://img.shields.io/badge/CSS-Themes-green?logo=css3) **CSS** – multiple themes (dark, pastel, high contrast)  
- ![dotenv](https://img.shields.io/badge/python--dotenv-envvars-yellow) **python‑dotenv** – environment variable management  

---

## 📁 Project Structure  

```
.
├── .env                        # env vars (untracked)
├── LICENSE                     # MIT license
├── README.md                   # project documentation
├── requirements.txt            # Python dependencies
├── app.py                      # Flask app with routes
├── config.py                   # config + secret key handling
├── data/
│   ├── .gitkeep                # keep folder in VCS
│   └── library.sqlite          # SQLite DB (untracked)
├── data_models.py              # SQLAlchemy models
├── static/
│   ├── .gitkeep                # keep folder in VCS
│   ├── common.css              # shared styles
│   ├── style-dark.css          # dark theme
│   ├── style-highcontrast.css  # high contrast theme
│   └── style-pastel.css        # pastel theme
└── templates/
    ├── base.html               # base layout
    ├── home.html               # home page
    ├── single_book.html        # single book view
    ├── book.html               # book entry partial
    ├── add_author.html         # add author page
    ├── add_book.html           # add book page
    ├── update_author.html      # update author page
    ├── update_book.html        # update book page
    ├── author_form.html        # reusable author form
    └── book_form.html          # reusable book form
```

---

## 🛠️ Development Setup  

### 🚀 Quick Start  
```bash
git clone https://github.com/paul-wosch/Book-Alchemy.git \
&& cd Book-Alchemy \
&& pip install -r requirements.txt
```

Run the Flask app:  
```bash
python app.py
```

Open [http://127.0.0.1:5002](http://127.0.0.1:5002) in your browser.

---

### 📖 Step‑by‑Step Guide  

1. **Clone the repository**  
   ```bash
   git clone https://github.com/paul-wosch/Book-Alchemy.git
   cd Book-Alchemy
   ```

2. **Create virtual environment** (optional)  
   ```bash
   python -m venv .venv
   source .venv/bin/activate   # Mac/Linux
   .venv\Scripts\activate      # Windows
   ```

3. **Install dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the app**  
   ```bash
   python app.py
   ```

5. **Access the app**  
   - UI: [http://127.0.0.1:5002](http://127.0.0.1:5002)  

---

## 👥 Contributing  
This project is primarily a **learning exercise**. It is not intended for long‑term maintenance.  

You are welcome to:  
- Explore the codebase and learn from it.  
- Use it as a reference for your own experiments.  
- Share feedback or ideas — even if they won’t be acted upon, they’re valuable for reflection.  

Think of this project less as a collaborative product and more as a **public learning artifact**.  

---

## 🏷️ Badges  

- **Python** – minimum supported Python version  
- **Flask** – framework used  
- **Code style** – follows PEP8 guidelines  
- **Status** – indicates this is a learning project  
- **License** – MIT license  
- **Quick Start** – link to setup instructions  

---

## 📄 License  
This project is licensed under the terms of the [MIT License](./LICENSE).  
See the LICENSE file for full details.