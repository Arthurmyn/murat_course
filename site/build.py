#!/usr/bin/env python3
# Generates static index.html from the design content (mirrors landing-design/Main.dc.html)
import html

ACCENT = "#a20202"

audience = [
    {"k1": "Новая", "k2": "профессия", "text": "Если вы хотите освоить новую профессию — обучение проходит с нуля, без опыта в учёте."},
    {"k1": "Уже", "k2": "калькулятор", "text": "Если вы уже работаете калькулятором — систематизируете знания и повысите квалификацию."},
    {"k1": "Работаете", "k2": "в ресторане", "text": "Если вы работаете в ресторане — разберётесь в себестоимости, производстве и складском учёте."},
]

skills = [
    "рассчитывать себестоимость блюд",
    "создавать и проверять технологические карты",
    "работать с сырьём и полуфабрикатами",
    "вести производственный учёт",
    "контролировать склад",
    "проводить инвентаризации",
    "находить расхождения и потери",
    "работать в iiko",
    "понимать реальные цифры ресторана",
]

modules = [
    {"num": "01", "title": "Профессия бухгалтера-калькулятора"},
    {"num": "02", "title": "Технологические карты"},
    {"num": "03", "title": "Себестоимость"},
    {"num": "04", "title": "Сырьё и полуфабрикаты"},
    {"num": "05", "title": "Производство"},
    {"num": "06", "title": "Складской учёт"},
    {"num": "07", "title": "Инвентаризация"},
    {"num": "08", "title": "Работа в iiko"},
    {"num": "09", "title": "Практические задания"},
]

lecturer_facts = [
    "Практический опыт: кухня, склад, производство, калькуляция, учёт, ресторанные системы",
    "Обучаю профессии бухгалтера-калькулятора на практике — от себестоимости и техкарт до склада и производства",
    "Учредитель Resto Calculator — производственный учёт и аудит в общепите",
]

support_items = [
    "Ответы на вопросы по iiko",
    "Проверка выполненной работы",
    "Помощь с настройкой учёта",
    "Консультации по себестоимости и финансам",
    "Поддержка в WhatsApp",
]

career_points = [
    "Сертификат о прохождении курса",
    "Рекомендации работодателям",
    "Помощь в трудоустройстве при наличии вакансий",
]

reviews = [
    {"role": "[ роль / должность ]", "text": "[ Текст отзыва — контент предоставит заказчик после первого потока ]", "name": "[ Имя ]"},
    {"role": "[ роль / должность ]", "text": "[ Текст отзыва — контент предоставит заказчик после первого потока ]", "name": "[ Имя ]"},
    {"role": "[ роль / должность ]", "text": "[ Текст отзыва — контент предоставит заказчик после первого потока ]", "name": "[ Имя ]"},
]

def e(s):
    return html.escape(str(s), quote=False)

skills_html = "\n".join(
    f'<span style="background:#fff;border:1px solid #e0dede;border-radius:26px;padding:18px 28px;font:600 18px/1 \'Onest\',sans-serif;color:#14171c">{e(s)}</span>'
    for s in skills
)

audience_html = "\n".join(f'''<div>
  <h3 style="font:800 22px/1.25 'Onest',sans-serif;letter-spacing:-.005em;text-transform:uppercase;margin:0 0 16px">
    <span style="color:#14171c">{e(a["k1"])}</span> <span style="color:{ACCENT}">{e(a["k2"])}</span>
  </h3>
  <div style="display:flex;gap:12px;align-items:flex-start">
    <span class="dash">—</span>
    <p style="font:500 15.5px/1.55 'Onest',sans-serif;margin:0;color:#4a4a4a">{e(a["text"])}</p>
  </div>
</div>''' for a in audience)

modules_html = "\n".join(f'''<div style="border:1px solid #e0dede;border-radius:16px;padding:30px 26px;display:flex;flex-direction:column;gap:18px">
  <div style="width:52px;height:52px;background:{ACCENT};border-radius:10px;display:flex;align-items:center;justify-content:center">
    <span style="font:800 21px/1 'Onest',sans-serif;color:#fff">{e(m["num"])}</span>
  </div>
  <h3 style="font:800 19px/1.3 'Onest',sans-serif;letter-spacing:-.005em;color:#14171c;margin:0">{e(m["title"])}</h3>
</div>''' for m in modules)

lecturer_facts_html = "\n".join(f'''<div style="display:flex;gap:14px;align-items:flex-start">
  <span class="dash" style="color:#14171c">—</span>
  <p style="font:500 16px/1.55 'Onest',sans-serif;margin:0;color:rgba(255,255,255,.92)">{e(f)}</p>
</div>''' for f in lecturer_facts)

support_items_html = "\n".join(f'''<div style="display:flex;gap:10px;align-items:flex-start">
  <span class="dash">—</span>
  <p style="font:500 15px/1.5 'Onest',sans-serif;margin:0;color:#333333">{e(s)}</p>
</div>''' for s in support_items)

career_points_html = "\n".join(f'''<div style="display:flex;gap:14px;align-items:flex-start">
  <span class="dash">—</span>
  <p style="font:500 16px/1.55 'Onest',sans-serif;margin:0;color:#333333">{e(c)}</p>
</div>''' for c in career_points)

reviews_html = "\n".join(f'''<div style="background:#fff;border:1.5px dashed #c6c6c6;border-radius:16px;padding:28px">
  <div style="display:flex;align-items:center;gap:14px;margin:0 0 22px">
    <span style="width:48px;height:48px;border-radius:50%;background:#e9eaed;flex:none"></span>
    <div>
      <p style="font:700 15px/1.25 'Onest',sans-serif;margin:0 0 3px;color:{ACCENT}">{e(r["name"])}</p>
      <p style="font:500 12.5px/1.2 'Onest',sans-serif;margin:0;color:#8a8a8a">{e(r["role"])}</p>
    </div>
  </div>
  <p style="font:500 15px/1.55 'Onest',sans-serif;margin:0;color:#8a8a8a">{e(r["text"])}</p>
</div>''' for r in reviews)

TEMPLATE = """<!doctype html>
<html lang="ru">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Бухгалтер-калькулятор — практическое обучение | Resto Calculator</title>
<meta name="description" content="Практическое обучение профессии бухгалтера-калькулятора для ресторанного бизнеса. Себестоимость, технологические карты, склад, производство, iiko.">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Onest:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
<style>
  body{{margin:0;background:#ffffff;color:#14171c;font-family:'Onest',system-ui,sans-serif;text-wrap:pretty;-webkit-font-smoothing:antialiased}}
  a{{color:inherit;text-decoration:none}}
  a.link:hover{{opacity:.7}}
  ::selection{{background:rgba(162,2,2,.22)}}
  input::placeholder{{color:rgba(20,23,28,.4)}}
  .btn{{display:inline-flex;align-items:center;justify-content:center;gap:8px;border-radius:10px;font:700 14px/1 'Onest',sans-serif;letter-spacing:.01em;cursor:pointer;transition:filter .15s ease,opacity .15s ease}}
  .btn:hover{{filter:brightness(1.14)}}
  .btn-outline:hover{{background:rgba(255,255,255,.1)}}
  .dash{{color:{ACCENT};font:800 15px/1.6 'Onest',sans-serif;flex:none}}
  @keyframes driftA{{0%,100%{{transform:translate(0,0) scale(1)}}50%{{transform:translate(70px,50px) scale(1.15)}}}}
  @keyframes driftB{{0%,100%{{transform:translate(0,0) scale(1)}}50%{{transform:translate(-60px,-40px) scale(1.1)}}}}
  @keyframes driftC{{0%,100%{{transform:translate(0,0) scale(1)}}50%{{transform:translate(-40px,60px) scale(1.18)}}}}
  @keyframes bob1{{0%,100%{{transform:translate(0,0) rotate(-10deg)}}50%{{transform:translate(4px,-20px) rotate(-2deg)}}}}
  @keyframes bob2{{0%,100%{{transform:translate(0,0) rotate(8deg)}}50%{{transform:translate(-6px,18px) rotate(14deg)}}}}
  @keyframes bob3{{0%,100%{{transform:translate(0,0) rotate(-4deg) scale(1)}}50%{{transform:translate(10px,-14px) rotate(6deg) scale(1.06)}}}}
  @keyframes bob4{{0%,100%{{transform:translate(0,0) rotate(6deg)}}50%{{transform:translate(-10px,-12px) rotate(-4deg)}}}}
  .blob{{position:absolute;border-radius:50%;filter:blur(50px);mix-blend-mode:screen;pointer-events:none}}
  .blob-a{{background:radial-gradient(circle,#ff7452 0%,#ff5a3c 38%,rgba(255,90,60,0) 74%);animation:driftA 20s ease-in-out infinite}}
  .blob-b{{background:radial-gradient(circle,#8c0202 0%,#5c0101 38%,rgba(92,1,1,0) 74%);animation:driftB 24s ease-in-out infinite}}
  .blob-c{{background:radial-gradient(circle,rgba(255,171,92,.5) 0%,rgba(255,138,60,.28) 40%,rgba(255,138,60,0) 74%);animation:driftC 18s ease-in-out infinite}}
  .blob-soft{{position:absolute;border-radius:50%;filter:blur(55px);mix-blend-mode:multiply;pointer-events:none}}
  .blob-soft-a{{background:radial-gradient(circle,rgba(255,110,80,.4) 0%,rgba(255,110,80,0) 72%);animation:driftA 24s ease-in-out infinite}}
  .blob-soft-b{{background:radial-gradient(circle,rgba(162,2,2,.3) 0%,rgba(162,2,2,0) 72%);animation:driftB 28s ease-in-out infinite}}
  @keyframes sweepline{{0%{{transform:translateX(0)}}100%{{transform:translateX(1440px)}}}}
  .sweep-line{{position:fixed;top:0;left:0;width:240px;height:100vh;background:linear-gradient(90deg,rgba(255,255,255,0) 0%,rgba(255,255,255,.16) 50%,rgba(255,255,255,0) 100%);filter:blur(18px);pointer-events:none;z-index:50;animation:sweepline 12s linear infinite}}
  .logo-chip{{display:inline-flex;align-items:center;background:#fff;border-radius:9px;padding:7px 11px;box-shadow:0 8px 18px rgba(0,0,0,.22)}}
  .badge{{border-radius:16px;background:#fff;display:flex;align-items:center;justify-content:center;box-shadow:0 14px 30px rgba(0,0,0,.28);position:absolute;pointer-events:none}}
  .b1{{animation:bob1 5.5s ease-in-out infinite}}
  .b2{{animation:bob2 6.5s ease-in-out infinite}}
  .b3{{animation:bob3 5s ease-in-out infinite}}
  .b4{{animation:bob4 7s ease-in-out infinite}}
  @keyframes floatCard{{0%,100%{{transform:translateY(0) rotate(-2deg)}}50%{{transform:translateY(-16px) rotate(1deg)}}}}
  .chart-card{{position:absolute;background:#fff;border-radius:28px;box-shadow:0 26px 54px rgba(0,0,0,.3);animation:floatCard 7s ease-in-out infinite;overflow:hidden}}
  @media (max-width:900px){{
    .wrap{{min-width:0 !important}}
    .hide-mobile{{display:none !important}}
    .grid-hero,.grid-lecturer,.grid-career,.grid-cta{{grid-template-columns:1fr !important}}
    .grid-audience{{grid-template-columns:1fr !important}}
    .grid-modules{{grid-template-columns:1fr 1fr !important}}
    .grid-steps{{grid-template-columns:1fr 1fr !important}}
    .grid-bonus2{{grid-template-columns:1fr !important}}
    .grid-reviews{{grid-template-columns:1fr !important}}
  }}
</style>
</head>
<body>
<div class="wrap" style="min-width:1440px;background:#ffffff">

<div class="sweep-line hide-mobile"></div>

<section style="position:relative;background:{ACCENT};overflow:hidden">
  <div class="blob blob-a" style="width:620px;height:620px;left:-120px;top:-160px"></div>
  <div class="blob blob-b" style="width:600px;height:600px;right:-80px;top:-160px"></div>
  <div class="blob blob-c" style="width:380px;height:380px;left:36%;bottom:-200px"></div>
  <div class="badge b1 hide-mobile" style="left:-14px;top:40px;width:54px;height:54px">
    <svg width="26" height="26" viewBox="0 0 24 24" fill="none"><rect x="4" y="2" width="16" height="20" rx="2" stroke="{ACCENT}" stroke-width="1.6"/><path d="M7 6h10M7 10h2M11 10h2M15 10h2M7 14h2M11 14h2M15 14h2" stroke="{ACCENT}" stroke-width="1.6" stroke-linecap="round"/></svg>
  </div>
  <div class="badge b2 hide-mobile" style="left:1370px;top:26px;width:50px;height:50px">
    <span style="font:800 22px/1 'Onest',sans-serif;color:{ACCENT}">₸</span>
  </div>
  <div class="badge b3 hide-mobile" style="left:24px;top:500px;width:54px;height:54px">
    <svg width="26" height="26" viewBox="0 0 24 24" fill="none"><circle cx="12" cy="13" r="8" stroke="{ACCENT}" stroke-width="1.6"/><path d="M9 3.5c1 1 1 2.3 0 3.4M15 3.5c-1 1-1 2.3 0 3.4" stroke="{ACCENT}" stroke-width="1.6" stroke-linecap="round"/></svg>
  </div>
  <div class="badge b4 hide-mobile" style="left:1390px;top:500px;width:50px;height:50px">
    <svg width="24" height="24" viewBox="0 0 24 24" fill="none"><path d="M3 17l5-5 4 4 8-9" stroke="{ACCENT}" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/><path d="M15 7h5v5" stroke="{ACCENT}" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>
  </div>
  <div class="grid-hero" style="max-width:1240px;margin:0 auto;padding:56px 40px 96px;position:relative;display:grid;grid-template-columns:minmax(0,1fr) 460px;gap:64px;align-items:center">
    <div>
      <div class="logo-chip" style="margin:0 0 48px">
        <img src="images/resto-logo.png" alt="Resto kz calculator" style="height:26px;display:block;border-radius:3px" />
      </div>
      <h1 style="font:800 46px/1.16 'Onest',sans-serif;letter-spacing:-.01em;text-transform:uppercase;color:#fff;margin:0 0 26px">Бухгалтер-калькулятор с нуля до уверенной работы в ресторане</h1>
      <div style="display:flex;gap:10px;margin:0 0 30px;flex-wrap:wrap">
        <span style="border:1px solid rgba(255,255,255,.42);border-radius:20px;padding:9px 18px;font:600 13px/1 'Onest',sans-serif;color:#fff">практическое обучение</span>
        <span style="border:1px solid rgba(255,255,255,.42);border-radius:20px;padding:9px 18px;font:600 13px/1 'Onest',sans-serif;color:#fff">9 модулей</span>
        <span style="border:1px solid rgba(255,255,255,.42);border-radius:20px;padding:9px 18px;font:600 13px/1 'Onest',sans-serif;color:#fff">HoReCa</span>
      </div>
      <div style="display:flex;gap:14px;align-items:flex-start;margin:0 0 40px;max-width:46ch">
        <span class="dash" style="color:rgba(255,255,255,.9)">—</span>
        <p style="font:500 18px/1.55 'Onest',sans-serif;margin:0;color:rgba(255,255,255,.92)">Практическое обучение калькуляции, технологическим картам, себестоимости, производственному и складскому учёту в HoReCa.</p>
      </div>
      <div style="display:flex;gap:14px;flex-wrap:wrap">
        <a href="#cta" class="btn" style="background:#14171c;color:#fff;min-height:60px;padding:0 34px;font-size:16px">Записаться на курс</a>
        <a href="#program" class="btn btn-outline" style="border:1px solid rgba(255,255,255,.5);color:#fff;min-height:60px;padding:0 34px;font-size:16px">Посмотреть программу</a>
      </div>
    </div>
    <div>
      <div style="border:2px solid rgba(255,255,255,.5);border-radius:22px;padding:14px">
        <div style="position:relative;border-radius:14px;overflow:hidden;aspect-ratio:4/5">
          <img src="images/murat.webp" alt="Видео о курсе" style="width:100%;height:100%;object-fit:cover;object-position:50% 8%;display:block" />
          <div style="position:absolute;inset:0;background:linear-gradient(0deg,rgba(0,0,0,.45) 0%,transparent 40%)"></div>
          <div style="position:absolute;inset:0;display:flex;align-items:center;justify-content:center">
            <span style="width:76px;height:76px;border-radius:50%;background:rgba(20,23,28,.85);display:flex;align-items:center;justify-content:center">
              <svg width="22" height="26" viewBox="0 0 22 26" fill="none"><path d="M21 13L0 25.7V.3L21 13z" fill="#fff"/></svg>
            </span>
          </div>
        </div>
      </div>
      <p style="text-align:right;margin:14px 8px 0;font:600 13px/1.4 'Onest',sans-serif;color:rgba(255,255,255,.85)">Узнайте о курсе <span style="color:#fff;font-weight:800">за 60 секунд</span></p>
    </div>
  </div>
</section>

<section style="position:relative;overflow:hidden;border-bottom:1px solid #e9eaed">
  <div class="blob-soft blob-soft-b hide-mobile" style="width:420px;height:420px;left:-140px;top:-180px"></div>
  <div class="blob-soft blob-soft-a hide-mobile" style="width:360px;height:360px;right:-120px;bottom:-160px"></div>
  <div style="max-width:1240px;margin:0 auto;padding:88px 40px;position:relative">
    <h2 style="font:800 54px/1.1 'Onest',sans-serif;letter-spacing:-.01em;margin:0 0 48px">
      <span style="color:#14171c">Кому подходит</span><br><span style="color:{ACCENT}">этот курс</span>
    </h2>
    <div class="grid-audience" style="display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:44px 32px">
      {audience_html}
    </div>
  </div>
</section>

<section style="position:relative;overflow:hidden;border-bottom:1px solid #e9eaed;background:#f5f5f5">
  <div class="blob-soft blob-soft-a hide-mobile" style="width:480px;height:480px;right:-140px;top:-200px"></div>
  <div class="blob-soft blob-soft-b hide-mobile" style="width:380px;height:380px;left:-120px;bottom:-180px"></div>
  <div style="max-width:1240px;margin:0 auto;padding:88px 40px;position:relative">
    <h2 style="font:800 54px/1.1 'Onest',sans-serif;letter-spacing:-.01em;margin:0 0 40px">
      <span style="color:#14171c">Что вы</span><br><span style="color:{ACCENT}">научитесь делать:</span>
    </h2>
    <div style="display:flex;flex-wrap:wrap;gap:14px;max-width:1080px;margin:0 0 36px">
      {skills_html}
    </div>
    <a href="#program" class="btn" style="background:{ACCENT};color:#fff;min-height:52px;padding:0 26px;font-size:14px">Посмотреть программу</a>
  </div>
</section>

<section id="program" style="position:relative;overflow:hidden;border-bottom:1px solid #e9eaed">
  <div class="blob-soft blob-soft-a hide-mobile" style="width:460px;height:460px;right:-150px;top:-190px"></div>
  <div class="blob-soft blob-soft-b hide-mobile" style="width:400px;height:400px;left:-130px;bottom:-170px"></div>
  <div style="max-width:1240px;margin:0 auto;padding:96px 40px;position:relative">
    <div style="display:flex;align-items:center;gap:18px;margin:0 0 24px">
      <h2 style="font:800 54px/1.1 'Onest',sans-serif;letter-spacing:-.01em;color:#14171c;margin:0">Программа<br>курса</h2>
      <svg width="44" height="44" viewBox="0 0 24 24" fill="none" style="flex:none;margin-top:10px"><circle cx="12" cy="12" r="11" stroke="{ACCENT}" stroke-width="1.4"/><path d="M9 8l4 4-4 4" stroke="{ACCENT}" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>
    </div>
    <p style="font:500 15px/1.6 'Onest',sans-serif;color:#8a8a8a;margin:0 0 40px;max-width:64ch">[ Темы и практические задания каждого модуля уточняются — программа будет опубликована перед стартом потока ]</p>
    <div class="grid-modules" style="display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:22px;margin:0 0 40px">
      {modules_html}
    </div>
    <a href="#cta" class="btn" style="background:{ACCENT};color:#fff;min-height:54px;padding:0 28px;font-size:14px">Записаться на курс</a>
  </div>
</section>

<section id="lecturer" style="position:relative;background:{ACCENT};overflow:hidden">
  <div class="blob blob-b hide-mobile" style="width:600px;height:600px;left:-180px;top:-160px"></div>
  <div class="blob blob-a hide-mobile" style="width:460px;height:460px;right:-160px;bottom:-200px"></div>
  <div class="grid-lecturer" style="max-width:1240px;margin:0 auto;padding:96px 40px;position:relative;display:grid;grid-template-columns:400px minmax(0,1fr);gap:64px;align-items:start">
    <div style="position:relative;width:400px;height:520px">
      <div style="position:absolute;left:0;bottom:0;width:100%;height:520px;background:#14171c;border-radius:18px"></div>
      <img src="images/murat.webp" alt="Мурат Ибрагимов" style="position:absolute;left:0;bottom:0;width:100%;height:auto;display:block" />
    </div>
    <div>
      <h2 style="font:800 42px/1.12 'Onest',sans-serif;letter-spacing:-.01em;color:#fff;margin:0 0 40px">Знакомьтесь — ваш<br>лектор на курсе</h2>
      <h3 style="font:800 28px/1.2 'Onest',sans-serif;letter-spacing:-.005em;text-transform:uppercase;color:#fff;margin:0 0 12px">Мурат Ибрагимов</h3>
      <p style="font:500 16px/1.5 'Onest',sans-serif;color:rgba(255,255,255,.8);margin:0 0 30px">Бухгалтер-калькулятор / эксперт по производственному и складскому учёту в HoReCa / преподаватель</p>
      <div style="display:flex;gap:56px;margin:0 0 34px">
        <div>
          <p style="font:800 40px/1 'Onest',sans-serif;color:#14171c;margin:0 0 8px">15 лет</p>
          <p style="font:600 14px/1.3 'Onest',sans-serif;color:rgba(255,255,255,.75);margin:0">практического опыта</p>
        </div>
        <div>
          <p style="font:800 40px/1 'Onest',sans-serif;color:#14171c;margin:0 0 8px">Resto</p>
          <p style="font:600 14px/1.3 'Onest',sans-serif;color:rgba(255,255,255,.75);margin:0">Calculator — учредитель</p>
        </div>
      </div>
      <div style="display:flex;flex-direction:column;gap:16px;max-width:56ch">
        {lecturer_facts_html}
      </div>
    </div>
  </div>
</section>

<section style="position:relative;overflow:hidden;border-bottom:1px solid #e9eaed;background:#f5f5f5">
  <div class="blob-soft blob-soft-b hide-mobile" style="width:440px;height:440px;right:-150px;top:-180px"></div>
  <div class="blob-soft blob-soft-a hide-mobile" style="width:360px;height:360px;left:-110px;bottom:-160px"></div>
  <div style="max-width:1240px;margin:0 auto;padding:88px 40px;position:relative">
    <h2 style="font:800 42px/1.12 'Onest',sans-serif;letter-spacing:-.01em;margin:0 0 40px">
      <span style="color:#14171c">Бонусы</span><br><span style="color:{ACCENT}">для учеников</span>
    </h2>
    <div style="background:{ACCENT};border-radius:18px;padding:44px 48px;display:grid;grid-template-columns:220px minmax(0,1fr);gap:36px;align-items:center;margin:0 0 20px">
      <p style="font:800 96px/.8 'Onest',sans-serif;color:#14171c;margin:0">30</p>
      <div>
        <h3 style="font:800 24px/1.2 'Onest',sans-serif;color:#fff;margin:0 0 12px;text-transform:uppercase">iiko на 30 дней</h3>
        <p style="font:500 15.5px/1.55 'Onest',sans-serif;margin:0;color:rgba(255,255,255,.88);max-width:56ch">Установка программы iiko на ваш компьютер на 30 дней — практика в настоящей базе, а не на скриншотах.</p>
      </div>
    </div>
    <div class="grid-bonus2" style="display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:20px;margin:0 0 20px">
      <div style="background:#fff;border-radius:18px;padding:36px 32px">
        <svg width="30" height="30" viewBox="0 0 24 24" fill="none" style="margin:0 0 18px"><rect x="3" y="5" width="18" height="15" rx="2" stroke="{ACCENT}" stroke-width="1.6"/><path d="M3 9h18M8 3v4M16 3v4" stroke="{ACCENT}" stroke-width="1.6" stroke-linecap="round"/></svg>
        <h3 style="font:800 21px/1.2 'Onest',sans-serif;color:#14171c;margin:0 0 12px">4 Zoom-встречи с лектором</h3>
        <p style="font:500 15px/1.5 'Onest',sans-serif;margin:0;color:#4a4a4a">По 60 минут каждая — разбираем ваши рабочие вопросы после прохождения курса.</p>
      </div>
      <div style="background:#fff;border-radius:18px;padding:36px 32px">
        <svg width="30" height="30" viewBox="0 0 24 24" fill="none" style="margin:0 0 18px"><circle cx="12" cy="12" r="9" stroke="{ACCENT}" stroke-width="1.6"/><path d="M12 7v5l3.2 2" stroke="{ACCENT}" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>
        <h3 style="font:800 21px/1.2 'Onest',sans-serif;color:#14171c;margin:0 0 12px">Записи на 6 месяцев</h3>
        <p style="font:500 15px/1.5 'Onest',sans-serif;margin:0;color:#4a4a4a">Все занятия проходят в Zoom и записываются. Пересматривайте уроки в удобное время.</p>
      </div>
    </div>
    <div style="background:#fff;border:1.5px solid {ACCENT};border-radius:18px;padding:36px 32px">
      <span style="display:block;font:700 12px/1 'Onest',sans-serif;letter-spacing:.1em;text-transform:uppercase;color:{ACCENT};margin:0 0 16px">доп. услуга</span>
      <h3 style="font:800 21px/1.2 'Onest',sans-serif;color:#14171c;margin:0 0 22px">Сопровождение после курса</h3>
      <div style="display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:10px 32px">
        {support_items_html}
      </div>
    </div>
  </div>
</section>

<section style="position:relative;overflow:hidden;border-bottom:1px solid #e9eaed">
  <div class="blob-soft blob-soft-a hide-mobile" style="width:400px;height:400px;left:-130px;top:-170px"></div>
  <div class="blob-soft blob-soft-b hide-mobile" style="width:340px;height:340px;right:-110px;bottom:-150px"></div>
  <div class="grid-career" style="max-width:1240px;margin:0 auto;padding:96px 40px;position:relative;display:grid;grid-template-columns:minmax(0,1fr) 460px;gap:64px;align-items:center">
    <div>
      <h2 style="font:800 42px/1.12 'Onest',sans-serif;letter-spacing:-.01em;margin:0 0 34px">
        <span style="color:{ACCENT}">Карьера</span><br><span style="color:#14171c">после курса</span>
      </h2>
      <div style="display:flex;flex-direction:column;gap:16px;max-width:46ch">
        {career_points_html}
      </div>
    </div>
    <div class="hide-mobile" style="position:relative;height:340px">
      <div style="position:absolute;left:36px;top:26px;width:320px;height:220px;background:#f5f5f5;border:1px solid #e0dede;border-radius:14px;transform:rotate(-4deg);box-shadow:0 18px 40px rgba(20,23,28,.08)"></div>
      <div style="position:absolute;left:0;top:0;width:320px;height:220px;background:{ACCENT};border-radius:14px;transform:rotate(3deg);box-shadow:0 18px 40px rgba(20,23,28,.14);display:flex;flex-direction:column;justify-content:center;align-items:center;gap:8px;padding:24px;box-sizing:border-box">
        <span style="font:700 10px/1 'Onest',sans-serif;letter-spacing:.14em;text-transform:uppercase;color:rgba(255,255,255,.7)">Сертификат</span>
        <span style="font:800 17px/1.25 'Onest',sans-serif;color:#fff;text-align:center;text-transform:uppercase">Бухгалтер-калькулятор</span>
        <span style="font:500 11px/1.4 'Onest',sans-serif;color:rgba(255,255,255,.6);text-align:center">[ макет предоставит заказчик ]</span>
      </div>
    </div>
  </div>
</section>

<section style="position:relative;overflow:hidden;border-bottom:1px solid #e9eaed;background:#f5f5f5">
  <div class="blob-soft blob-soft-b hide-mobile" style="width:420px;height:420px;right:-140px;top:-170px"></div>
  <div class="blob-soft blob-soft-a hide-mobile" style="width:340px;height:340px;left:-110px;bottom:-150px"></div>
  <div style="max-width:1240px;margin:0 auto;padding:96px 40px;position:relative">
    <h2 style="font:800 42px/1.12 'Onest',sans-serif;letter-spacing:-.01em;color:#14171c;margin:0 0 48px">Отзывы<br>от учеников</h2>
    <div class="grid-reviews" style="display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:20px">
      {reviews_html}
    </div>
  </div>
</section>

<section id="cta" style="position:relative;background:{ACCENT};overflow:hidden">
  <div class="blob blob-c hide-mobile" style="width:400px;height:400px;left:-140px;top:-160px"></div>
  <div class="blob blob-b hide-mobile" style="width:560px;height:560px;right:-200px;bottom:-220px"></div>
  <div class="grid-cta" style="max-width:1240px;margin:0 auto;padding:100px 40px;position:relative;display:grid;grid-template-columns:minmax(0,1fr) 420px;gap:40px;align-items:center">
    <div>
      <h2 style="font:800 60px/1.02 'Onest',sans-serif;letter-spacing:-.01em;text-transform:uppercase;color:#fff;margin:0 0 30px">Остались<br>вопросы?</h2>
      <div style="display:flex;gap:14px;align-items:flex-start;max-width:52ch;margin:0 0 40px">
        <span class="dash" style="color:#14171c">—</span>
        <p style="font:500 18px/1.6 'Onest',sans-serif;margin:0;color:rgba(255,255,255,.92)">Чтобы узнать подробнее о курсе «Бухгалтер-калькулятор», оставляйте заявку — расскажем про даты старта, формат обучения и стоимость.</p>
      </div>
      <a href="https://wa.me/77715427246" class="btn" style="background:#14171c;color:#fff;min-height:58px;padding:0 32px;font-size:15px;margin-bottom:44px">Записаться на курс</a>
      <div style="display:flex;gap:48px;flex-wrap:wrap;border-top:1px solid rgba(255,255,255,.25);padding-top:32px">
        <div><span style="display:block;font:600 12px/1 'Onest',sans-serif;letter-spacing:.1em;text-transform:uppercase;color:rgba(255,255,255,.6);margin:0 0 8px">Телефон</span><span style="font:700 19px/1 'Onest',sans-serif;color:#fff">+7 (771) 542-72-46</span></div>
        <div><span style="display:block;font:600 12px/1 'Onest',sans-serif;letter-spacing:.1em;text-transform:uppercase;color:rgba(255,255,255,.6);margin:0 0 8px">Instagram</span><span style="font:700 19px/1 'Onest',sans-serif;color:#fff">@resto_calculator_kz</span></div>
      </div>
    </div>
    <div class="hide-mobile" style="position:relative;height:420px">
      <div class="chart-card" style="left:90px;top:44px;width:240px;height:240px">
        <svg width="100%" height="100%" viewBox="0 0 220 220" fill="none">
          <circle cx="34" cy="34" r="7" fill="{ACCENT}"/>
          <circle cx="54" cy="34" r="7" fill="#14171c"/>
          <circle cx="74" cy="34" r="7" fill="#d9a45c"/>
          <rect x="38" y="140" width="24" height="52" rx="7" fill="#f0dcdc"/>
          <rect x="72" y="108" width="24" height="84" rx="7" fill="#f0a98f"/>
          <rect x="106" y="66" width="24" height="126" rx="7" fill="{ACCENT}"/>
          <rect x="140" y="118" width="24" height="74" rx="7" fill="#5c0101"/>
          <path d="M28 150 L92 82 L128 116 L192 34" stroke="#14171c" stroke-width="8" stroke-linecap="round" stroke-linejoin="round"/>
          <path d="M160 30 L196 36 L188 68 Z" fill="#14171c"/>
        </svg>
      </div>
      <div class="badge b2" style="left:300px;top:6px;width:88px;height:88px;border-radius:22px">
        <span style="font:800 36px/1 'Onest',sans-serif;color:{ACCENT}">₸</span>
      </div>
      <div class="badge b3" style="left:0px;top:302px;width:84px;height:84px;border-radius:20px">
        <svg width="40" height="40" viewBox="0 0 24 24" fill="none"><path d="M6 2h12v18l-2-1.3-2 1.3-2-1.3-2 1.3-2-1.3-2 1.3V2z" stroke="{ACCENT}" stroke-width="1.5" stroke-linejoin="round"/><path d="M8.5 7h7M8.5 10.5h7M8.5 14h4" stroke="{ACCENT}" stroke-width="1.5" stroke-linecap="round"/></svg>
      </div>
      <div class="badge b4" style="left:312px;top:300px;width:76px;height:76px;border-radius:18px">
        <svg width="36" height="36" viewBox="0 0 24 24" fill="none"><circle cx="12" cy="13" r="8" stroke="{ACCENT}" stroke-width="1.5"/><path d="M9 3.5c1 1 1 2.3 0 3.4M15 3.5c-1 1-1 2.3 0 3.4" stroke="{ACCENT}" stroke-width="1.5" stroke-linecap="round"/></svg>
      </div>
    </div>
  </div>
</section>

<footer style="background:#14171c">
  <div style="max-width:1240px;margin:0 auto;padding:48px 40px;display:flex;align-items:center;gap:40px;flex-wrap:wrap">
    <div style="display:flex;flex-direction:column;gap:16px;max-width:260px">
      <img src="images/resto-logo.png" alt="Resto kz calculator" style="height:34px;display:block;border-radius:4px" />
      <p style="font:500 13px/1.5 'Onest',sans-serif;color:rgba(255,255,255,.5);margin:0">Практическое обучение профессии бухгалтера-калькулятора для ресторанного бизнеса.</p>
      <a class="link" href="https://www.instagram.com/resto_calculator_kz/" style="font:500 13px/1 'Onest',sans-serif;color:rgba(255,255,255,.55)">instagram</a>
    </div>
    <div style="display:flex;gap:56px;margin-left:24px">
      <div style="display:flex;flex-direction:column;gap:10px">
        <a class="link" href="#program" style="font:500 14px/1.4 'Onest',sans-serif;color:rgba(255,255,255,.65)">Программа курса</a>
        <a class="link" href="#lecturer" style="font:500 14px/1.4 'Onest',sans-serif;color:rgba(255,255,255,.65)">Лектор</a>
      </div>
      <div style="display:flex;flex-direction:column;gap:10px">
        <a class="link" href="https://restocalculator.kz" style="font:500 14px/1.4 'Onest',sans-serif;color:rgba(255,255,255,.65)">restocalculator.kz</a>
        <a class="link" href="#" style="font:500 14px/1.4 'Onest',sans-serif;color:rgba(255,255,255,.65)">политика конфиденциальности</a>
      </div>
    </div>
    <div style="margin-left:auto;display:flex;align-items:center;gap:28px">
      <span style="font:800 38px/1 'Onest',sans-serif;color:#fff;letter-spacing:-.01em">+7 (771) 542-72-46</span>
      <a href="#cta" class="btn btn-outline" style="border:1px solid rgba(255,255,255,.35);color:#fff;min-height:48px;padding:0 24px;font-size:13px">заказать звонок</a>
    </div>
  </div>
  <div style="max-width:1240px;margin:0 auto;padding:0 40px 32px"><p style="font:500 12.5px/1.5 'Onest',sans-serif;color:rgba(255,255,255,.32);margin:0;border-top:1px solid rgba(255,255,255,.1);padding-top:20px">© 2026 Resto.kz calculator. Все права защищены.</p></div>
</footer>

<a href="https://wa.me/77715427246" style="position:fixed;right:32px;bottom:32px;z-index:40;width:58px;height:58px;border-radius:50%;background:#25d366;display:flex;align-items:center;justify-content:center;box-shadow:0 8px 20px rgba(0,0,0,.25)">
  <svg width="28" height="28" viewBox="0 0 24 24" fill="none"><path d="M12 2C6.48 2 2 6.48 2 12c0 1.85.5 3.58 1.36 5.07L2 22l5.06-1.33A9.94 9.94 0 0 0 12 22c5.52 0 10-4.48 10-10S17.52 2 12 2z" fill="#fff"/><path d="M17.2 14.35c-.28-.14-1.64-.81-1.9-.9-.25-.1-.44-.14-.62.14-.19.28-.72.9-.88 1.08-.16.19-.32.21-.6.07-.28-.14-1.18-.44-2.24-1.39-.83-.74-1.39-1.65-1.55-1.93-.16-.28-.02-.43.12-.57.13-.13.28-.33.42-.5.14-.16.19-.28.28-.47.09-.19.05-.35-.02-.5-.07-.14-.62-1.51-.85-2.06-.22-.54-.45-.47-.62-.48-.16-.01-.35-.01-.53-.01-.19 0-.5.07-.76.35-.26.28-1 1-1 2.42 0 1.43 1.03 2.82 1.18 3.01.14.19 2.03 3.11 4.93 4.36.69.3 1.22.48 1.64.61.69.22 1.31.19 1.81.11.55-.08 1.64-.67 1.87-1.32.23-.65.23-1.2.16-1.32-.07-.12-.25-.19-.53-.33z" fill="{ACCENT}"/></svg>
</a>

</div>
</body>
</html>
"""

html_out = TEMPLATE.format(
    ACCENT=ACCENT,
    audience_html=audience_html,
    skills_html=skills_html,
    modules_html=modules_html,
    lecturer_facts_html=lecturer_facts_html,
    support_items_html=support_items_html,
    career_points_html=career_points_html,
    reviews_html=reviews_html,
)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_out)

print("wrote index.html,", len(html_out), "bytes")
