# DARE Lab Starter — Make Content Bilingual with i18n

Starter project for the DARE Labs lab **[Make Content Bilingual with i18n](https://darelabs.tech/labs/make-content-bilingual-with-i18n)**.

Pick your stack, then complete the lab by making the failing tests pass. The goal is the
same in every language: make a content model (`Article`) **translatable per locale**
(`en`, `pt-BR`) with **fallback** (never blank) and a **stable slug** (not translated).
The tests define the target behavior — they start red; make them green.

| Stack | Folder | Run |
|-------|--------|-----|
| Ruby / Rails | [`rails/`](rails/) | `bundle install && RAILS_ENV=test bin/rails db:prepare && bundle exec rspec` |
| Python / FastAPI | [`python/`](python/) | `pip install -r requirements.txt && pytest` |
| TypeScript / Node | [`typescript/`](typescript/) | `npm install && npm test` |

Each folder has its own README with details. You only need to complete **one** stack.

---
Part of [DARE Labs](https://darelabs.tech) — learn AI-assisted engineering with the DARE method.
