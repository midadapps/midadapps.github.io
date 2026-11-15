# يولّد صفحات موقع مِداد (الرئيسية + صفحة لكل وجه). شغّله بعد أي تعديل بالنصوص:  python build_site.py
import html, os

HERE = os.path.dirname(os.path.abspath(__file__))
WA = "9647738181860"  # واتساب المبيعات

FACES = [
    dict(id="clinic", name="مِداد عيادات", short="العيادات والأطباء",
         tag="عيادتك مرتّبة من تلفونك", sub="الدور بدون زحمة، ملف كامل لكل مريض، والوصفة والتذكير يوصلون لتلفونه.",
         price="جرّبه أسبوعاً مجاناً. بعدها 12$ شهرياً، أو 120$ سنوياً.",
         feats=[("🔢", "الدور والمواعيد", "منو وصل، منو ينتظر، ومنو خلص — والسكرتيرة تضيف المراجع بضغطة وياخذ رقم دوره."),
                ("🗂", "ملف كامل لكل مريض", "الزيارات السابقة، التشخيص، الوصفات، وصور التحاليل والأشعة."),
                ("⚠️", "تنبيه الحساسية", "إذا المريض عنده حساسية من دواء يطلع تنبيه واضح بملفه."),
                ("🦷", "خريطة الأسنان", "لأطباء الأسنان: كل سن وشنو انسوّى بيه."),
                ("💊", "الوصفة على تلفون المريض", "تشخيصه ووصفته يوصلون إله بتطبيق مِداد."),
                ("⏰", "تذكير المواعيد", "رسالة تذكير للمراجع قبل موعده، وتذكير بالمبالغ المتبقية."),
                ("📲", "حجز من التطبيق", "المريض يطلب موعد، والعيادة توافق أو تقترح وقت ثاني."),
                ("👩‍💼", "السكرتيرة بحسابها", "كل موظف بصلاحياته: تسجّل المواعيد والدفع، وما تشوف الملاحظات الطبية."),
                ("📊", "الحسابات والتقارير", "الكشفيات، المستلم، المصاريف، وصافي كل شهر.")],
         video="media/clinic.mp4", video2=None,
         who="الطبيب والسكرتيرة يستعملون «مِداد عيادات». المراجع يستعمل تطبيق «مِداد»."),
    dict(id="generator", name="مِداد مولّدات", short="أصحاب المولّدات",
         tag="مولّدتك بجيبك", sub="المشتركين والأمبيرات والجباية، وتذكير غير المسددين بالواتساب بضغطة.",
         price="جرّبه أسبوعاً مجاناً. بعدها 12$ شهرياً، أو 120$ سنوياً.",
         feats=[("👥", "المشتركين والأمبيرات", "كل مشترك بخطوطه وأمبيراته، والخط الذهبي، والمنطقة والعنوان."),
                ("💵", "الجباية الشهرية", "تسديد من مشترك بثواني، وتعرف منو سدد ومنو باقي عليه."),
                ("📲", "تذكير غير المسددين", "إرسال متتابع بالواتساب لكل غير المسددين، وكل واحد يتعلّم «أُرسل»."),
                ("✏️", "تعديل سعر الشهر", "غيّر سعر الأمبير لكل المشتركين مرة وحدة."),
                ("🧾", "فاتورة الشهر والمصاريف", "الوقود والصيانة والرواتب، وصافي الشهر الحقيقي."),
                ("📢", "تبليغ المشتركين", "إطفاء، صيانة، أو تغيير بالتشغيل — يوصل لكل المشتركين."),
                ("📊", "التقارير الشهرية", "الجباية والديون والصافي لكل شهر."),
                ("👀", "المشترك يشوف حسابه", "المشترك يتابع اشتراكه وديونه من تطبيق «مِداد».")],
         video=None, video2=None,
         who="صاحب المولّدة والجابي يستعملون «مِداد مولّدات». المشترك يستعمل تطبيق «مِداد»."),
    dict(id="installments", name="مِداد أقساط", short="محلات الأقساط",
         tag="أقساطك مرتّبة، وما يضيع دينار", sub="الزبائن والكفلاء وخطط الأقساط، وتذكير المتأخرين بالواتساب.",
         price="جرّبه أسبوعاً مجاناً. بعدها 12$ شهرياً، أو 120$ سنوياً.",
         feats=[("👤", "الزبائن والكفلاء", "الاسم والهاتف والعنوان والكفيل والدين السابق."),
                ("🧮", "خطط الأقساط", "السعر الكلي، المقدمة، عدد الأقساط، شهري أو أسبوعي، وتاريخ أول قسط."),
                ("💵", "تسديد القسط", "سجّل الدفعة بثواني، والحساب يتحدّث وحده."),
                ("🔴", "المتأخرين بوضوح", "المتأخر يطلع بلون واضح، وتعرف منو لازم تتابعه اليوم."),
                ("📲", "تذكير المتأخرين بالواتساب", "رسالة تذكير لكل متأخر بضغطة."),
                ("🧾", "البيع بالدين والنقدي", "كل حركة مسجّلة: بيع، تسديد، ودين."),
                ("📦", "المخزون", "البضاعة والكميات وأسعار البيع."),
                ("👥", "الموظفين بصلاحياتهم", "كل موظف يشوف ويسوي اللي تسمحله بيه.")],
         video=None, video2=None,
         who="صاحب المحل وموظفينه يستعملون «مِداد أقساط». الزبون يستعمل تطبيق «مِداد»."),
    dict(id="hajj", name="مِداد حج وعمرة", short="حملات الحج والعمرة",
         tag="حملتك ويّاك بكل خطوة", sub="الحجاج والغرف والأفواج والجدول، والبث الصوتي، وزر «أنا ضايع» — وواجهة كبيرة وواضحة لكبار السن.",
         price="جرّبه أسبوعاً مجاناً. بعدها 17$ شهرياً، أو 170$ سنوياً.",
         feats=[("🧕", "ملف كامل لكل حاج", "الهاتفين، الصورة، الجواز والفيزا، المحرم، رقم السوار، والمعلومات الصحية."),
                ("🛏", "الغرف والأفواج والباصات", "كل حاج بغرفته وفوجه، وعدّ الحجاج بالباص بضغطة."),
                ("🗓", "جدول الرحلة ونقاط التجمع", "يوم بيوم، والحاج يعرف الجاي ويوصل لنقطة التجمع بالخريطة."),
                ("🔴", "بث مباشر مثل الراديو", "المرشد يحچي والحجاج يسمعونه بنفس اللحظة، حتى وتلفوناتهم بجيوبهم والشاشة مطفية."),
                ("🆘", "زر «أنا ضايع»", "موقع الحاج يوصل للحملة فوراً، وإذا النت ضعيف يتجهز مسج للمرشد."),
                ("🙋", "الأسئلة والطلبات", "الحاج يسأل المرشد بالكتابة أو بصوته، ومحد يشوف سؤاله غيره."),
                ("🪪", "بطاقة الحاج", "بطاقة بيها الفندق والغرفة وهاتف الحملة وكود QR إذا ضاع."),
                ("🔒", "خصوصية", "الحالة النفسية والملاحظات الداخلية تشوفها الإدارة بس."),
                ("🌍", "العراق والكويت والخليج", "يدعم الدينار العراقي والكويتي وعملات الخليج وأرقامها.")],
         video="media/hajj-owner.mp4", video2="media/hajj-pilgrim.mp4",
         who="صاحب الحملة والمرشد والحاج كلهم يستعملون «مِداد حج وعمرة». الحاج يبحث عن حملته بالتطبيق ويكتب اسمه ورقمه، والحملة توافق بضغطة — بدون أكواد."),
    dict(id="school", name="مِداد مدارس", short="المدارس والروضات",
         tag="المدرسة والأهل بمكان واحد", sub="الحضور والدرجات والواجبات والتبليغات، وولي الأمر يتابع ابنه من تلفونه.",
         price="جرّبه أسبوعاً مجاناً. بعدها 17$ شهرياً، أو 170$ سنوياً.",
         feats=[("🏫", "الصفوف والطلاب", "كل صف بطلابه وموادّه وجدوله الأسبوعي."),
                ("✅", "التحضير اليومي", "المعلم يحضّر الصف بثواني، والأهل يعرفون."),
                ("📝", "الدرجات وبطاقة التقرير", "الدرجات لكل مادة، وبطاقة تقرير جاهزة."),
                ("📚", "الواجبات ونشاطات الصف", "المعلم ينشر الواجب، والأهل يشوفوه."),
                ("📢", "التبليغات", "عطلة، اجتماع، أو تنبيه — يوصل لكل أولياء الأمور، وتعرف منو قراه."),
                ("💬", "ملاحظات المعلم والشكاوى", "تواصل مرتّب بين المدرسة والأهل."),
                ("💵", "الأقساط المدرسية", "منو سدد ومنو باقي عليه."),
                ("👩‍🏫", "المعلم بصلاحياته", "كل معلم يشوف صفوفه بس.")],
         video=None, video2=None,
         who="الإدارة والمعلمين وأولياء الأمور كلهم يستعملون «مِداد مدارس»، وولي الأمر يدخل بكود من المدرسة."),
]

CSS = """
:root{--bg:#0b1310;--bg2:#101b17;--card:#13211b;--line:#3a3220;--gold:#e3b75a;--gold2:#f2d589;--gold3:#b8862f;--ink:#f4efe2;--muted:#b7b2a4}
*{box-sizing:border-box;margin:0;padding:0}
html{scroll-behavior:smooth}
body{font-family:Tajawal,system-ui,sans-serif;background:var(--bg);color:var(--ink);line-height:1.7;overflow-x:hidden}
a{color:inherit}
.wrap{max-width:1080px;margin:0 auto;padding:0 18px}
header{position:sticky;top:0;z-index:5;background:#0b1310e6;backdrop-filter:blur(10px);border-bottom:1px solid #2a2418}
header .wrap{display:flex;align-items:center;justify-content:space-between;height:64px}
.brand{display:flex;align-items:center;gap:10px;text-decoration:none;font-weight:800;font-size:22px}
.brand img{width:38px;height:38px;border-radius:10px;box-shadow:0 0 0 1.5px #e3b75a77}
nav a{text-decoration:none;color:var(--muted);font-weight:700;margin-inline-start:18px;font-size:15px}
nav a:hover{color:var(--gold)}
.hero{padding:64px 0 40px;text-align:center;background:radial-gradient(ellipse 700px 380px at 50% 0,#3a2c0e88,transparent 70%)}
.hero h1{font-size:clamp(34px,6vw,58px);font-weight:800;line-height:1.2;background:linear-gradient(90deg,var(--gold2),var(--gold));-webkit-background-clip:text;background-clip:text;color:transparent}
.hero p{font-size:clamp(17px,2.4vw,21px);color:var(--muted);max-width:720px;margin:16px auto 0}
.hero .icon{width:110px;height:110px;border-radius:28px;box-shadow:0 18px 50px #0008,0 0 0 2px #e3b75a99;margin-bottom:18px}
.btn{display:inline-flex;align-items:center;justify-content:center;gap:8px;font-weight:800;font-size:17px;padding:14px 26px;border-radius:16px;text-decoration:none;border:0;cursor:pointer}
.gold{background:linear-gradient(135deg,var(--gold2),var(--gold3));color:#241a05;box-shadow:0 10px 30px #e3b75a33}
.ghost{border:1.5px solid var(--gold);color:var(--gold);background:transparent}
.soon{border:1.5px dashed #5a5140;color:#8d8676;background:transparent;cursor:default}
.dl{display:flex;flex-wrap:wrap;gap:12px;justify-content:center;margin-top:26px}
.note{font-size:13.5px;color:var(--muted);margin-top:12px}
h2{font-size:clamp(26px,4vw,34px);font-weight:800;text-align:center;margin-bottom:8px}
.lead{text-align:center;color:var(--muted);margin-bottom:28px}
section{padding:48px 0}
.grid{display:grid;gap:16px;grid-template-columns:repeat(auto-fill,minmax(250px,1fr))}
.face{background:var(--card);border:1px solid var(--line);border-radius:22px;padding:22px;text-decoration:none;display:flex;flex-direction:column;gap:10px;transition:transform .2s,border-color .2s}
.face:hover{transform:translateY(-3px);border-color:var(--gold)}
.face img{width:68px;height:68px;border-radius:18px;box-shadow:0 0 0 1.5px #e3b75a77}
.face b{font-size:21px;font-weight:800}
.face span{color:var(--muted);font-size:15px}
.face em{font-style:normal;color:var(--gold);font-weight:800;margin-top:auto}
.feat{background:var(--card);border:1px solid var(--line);border-radius:18px;padding:18px}
.feat .e{font-size:26px}
.feat b{display:block;font-size:18px;font-weight:800;margin:4px 0 2px}
.feat p{color:var(--muted);font-size:15px}
.band{background:var(--bg2);border-top:1px solid #2a2418;border-bottom:1px solid #2a2418}
.vids{display:flex;flex-wrap:wrap;gap:22px;justify-content:center}
.vid{width:min(300px,100%);text-align:center}
.vid video{width:100%;border-radius:22px;border:1.5px solid var(--line);background:#000}
.vid b{display:block;margin-top:8px;color:var(--muted)}
.steps{display:grid;gap:14px;grid-template-columns:repeat(auto-fill,minmax(230px,1fr));counter-reset:s}
.step{background:var(--card);border:1px solid var(--line);border-radius:18px;padding:20px 18px;position:relative}
.step:before{counter-increment:s;content:counter(s);position:absolute;top:-14px;right:18px;width:32px;height:32px;border-radius:50%;background:linear-gradient(135deg,var(--gold2),var(--gold3));color:#241a05;font-weight:800;display:grid;place-items:center}
.step b{display:block;font-size:17px;margin-top:6px}
.step p{color:var(--muted);font-size:15px}
.pill{display:inline-block;background:#e3b75a1f;border:1px solid #e3b75a66;color:var(--gold2);padding:8px 18px;border-radius:30px;font-weight:700;margin-top:18px}
.why{display:grid;gap:14px;grid-template-columns:repeat(auto-fill,minmax(220px,1fr))}
.cust{display:flex;gap:18px;align-items:center;background:var(--card);border:1px solid var(--gold);border-radius:22px;padding:22px;flex-wrap:wrap}
.cust img{width:76px;height:76px;border-radius:20px;box-shadow:0 0 0 1.5px #e3b75a77}
.cust div{flex:1;min-width:200px}
.cust b{font-size:21px}
footer{padding:34px 0 46px;text-align:center;color:var(--muted);font-size:14px}
footer a{color:var(--gold);text-decoration:none;font-weight:700}
@media (max-width:640px){nav a.hide{display:none}.hero{padding:42px 0 26px}section{padding:36px 0}}
"""

HEAD = """<!doctype html>
<html lang="ar" dir="rtl"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta property="og:title" content="{title}"><meta property="og:description" content="{desc}"><meta property="og:image" content="img/{img}.png">
<link rel="icon" href="img/{img}.png">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Tajawal:wght@500;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="site.css">
</head><body>
<header><div class="wrap"><a class="brand" href="index.html"><img src="img/midad.png" alt="">مِداد</a>
<nav><a href="index.html#apps">التطبيقات</a><a class="hide" href="index.html#customers">للزبائن</a><a href="https://wa.me/{wa}">تواصل</a></nav></div></header>
"""
FOOT = """<footer><div class="wrap">
<p>مِداد — شغلك كله بجيبك</p>
<p style="margin-top:6px">للاستفسار والعروض: <a href="https://wa.me/{wa}">واتساب</a></p>
</div></footer>
<script src="site.js"></script>
</body></html>"""

def e(s): return html.escape(s, quote=True)

def dl_buttons(face_id, label_app):
    return f"""<div class="dl">
<a class="btn gold" data-apk="{face_id}" href="#">⬇ تحميل للأندرويد</a>
<span class="btn soon">🍎 آيفون — قريباً</span>
<span class="btn soon">🖥 ويندوز — قريباً</span>
</div>
<p class="note">إذا طلب الهاتف السماح بالتثبيت من «مصادر غير معروفة»، وافق مرة وحدة وكمّل التثبيت.</p>"""

def face_page(f):
    feats = "".join(f'<div class="feat"><div class="e">{x}</div><b>{e(t)}</b><p>{e(d)}</p></div>' for x, t, d in f["feats"])
    vids = ""
    if f["video"]:
        items = [(f["video"], "شرح لصاحب النشاط" if f["id"] != "clinic" else "جولة بالتطبيق")]
        if f["video2"]: items.append((f["video2"], "شرح للحاج"))
        vids = '<section class="band"><div class="wrap"><h2>شوفه بعينك</h2><p class="lead">فيديو قصير بشاشات التطبيق الحقيقية</p><div class="vids">' + \
            "".join(f'<div class="vid"><video src="{v}#t=2" controls preload="metadata" playsinline></video><b>{e(t)}</b></div>' for v, t in items) + \
            "</div></div></section>"
    page = HEAD.format(title=f"{f['name']} — {f['tag']}", desc=e(f["sub"]), img=f["id"], wa=WA)
    page += f"""<main>
<section class="hero"><div class="wrap">
<img class="icon" src="img/{f['id']}.png" alt="{e(f['name'])}">
<h1>{e(f['tag'])}</h1>
<p>{e(f['sub'])}</p>
{dl_buttons(f['id'], f['name'])}
<span class="pill">{e(f['price'])}</span>
</div></section>
<section><div class="wrap"><h2>شنو يسوي {e(f['name'])}؟</h2><p class="lead">ميزات حقيقية موجودة بالتطبيق اليوم</p><div class="grid">{feats}</div></div></section>
{vids}
<section><div class="wrap"><h2>شلون تبدي؟</h2><p class="lead">{e(f['who'])}</p><div class="steps">
<div class="step"><b>حمّل التطبيق</b><p>من الزر فوگ، ونصّبه على تلفونك.</p></div>
<div class="step"><b>سوّي حسابك</b><p>برقم هاتفك وكلمة سر، وبعدين أنشئ نشاطك باسمه.</p></div>
<div class="step"><b>ادعُ فريقك</b><p>كل موظف أو زبون ينضم بكود ترسله إله بالواتساب.</p></div>
</div>
<div class="dl" style="margin-top:30px"><a class="btn ghost" href="https://wa.me/{WA}?text={e('السلام عليكم، أريد أعرف أكثر عن ' + f['name'])}">💬 اسألنا بالواتساب</a></div>
</div></section>
</main>"""
    page += FOOT.format(wa=WA)
    return page

def index_page():
    cards = "".join(f'<a class="face" href="{f["id"]}.html"><img src="img/{f["id"]}.png" alt=""><b>{e(f["name"])}</b><span>{e(f["tag"])} — {e(f["short"])}</span><em>التفاصيل والتحميل ←</em></a>' for f in FACES)
    why = [("📶", "يشتغل بدون إنترنت", "تشتغل عادي، ومن يرجع النت يتحدّث كل شي وحده."),
           ("👥", "فريقك بصلاحياته", "كل موظف بحسابه، وإنت تحدد شنو يشوف وشنو يسوي."),
           ("📲", "واتساب وإشعارات", "تذكير الزبائن والمتأخرين بضغطة، وإشعارات فورية."),
           ("🤝", "عربي ومن بيئتنا", "مصمم لشغلنا وأسعارنا ولهجتنا، وسهل حتى لكبار السن.")]
    whyh = "".join(f'<div class="feat"><div class="e">{x}</div><b>{e(t)}</b><p>{e(d)}</p></div>' for x, t, d in why)
    page = HEAD.format(title="مِداد — شغلك كله بجيبك", desc="تطبيقات عربية لإدارة العيادات والمولّدات ومحلات الأقساط وحملات الحج والمدارس.", img="midad", wa=WA)
    page += f"""<main>
<section class="hero"><div class="wrap">
<img class="icon" src="img/midad.png" alt="مِداد">
<h1>شغلك كله بجيبك</h1>
<p>تطبيقات عربية لإدارة العيادات والمولّدات ومحلات الأقساط وحملات الحج والمدارس — كل تطبيق مصمم لشغلك بالضبط، ويشتغل حتى بدون إنترنت.</p>
<div class="dl"><a class="btn gold" href="#apps">اختار تطبيقك</a></div>
</div></section>
<section id="apps"><div class="wrap"><h2>اختار تطبيقك</h2><p class="lead">كل تطبيق مسوّى لنوع شغل واحد، بكلماته وشاشاته</p><div class="grid">{cards}</div></div></section>
<section class="band" id="customers"><div class="wrap">
<div class="cust"><img src="img/midad.png" alt=""><div><b>مِداد — للزبائن</b><p style="color:var(--muted)">مراجع عيادة، مشترك مولّدة، أو زبون أقساط؟ حمّل «مِداد» وشوف مواعيدك ووصفاتك وحسابك، وكل الجهات اللي تتعامل وياها بمكان واحد.</p></div>
<a class="btn gold" data-apk="midad" href="#">⬇ تحميل للأندرويد</a></div>
</div></section>
<section><div class="wrap"><h2>ليش مِداد؟</h2><p class="lead">نفس الأساس القوي بكل التطبيقات</p><div class="why">{whyh}</div>
<div class="dl"><span class="btn soon">🍎 آيفون — قريباً</span><span class="btn soon">🖥 ويندوز — قريباً</span></div></div></section>
</main>"""
    page += FOOT.format(wa=WA)
    return page

JS = """// روابط تحميل ملفات الأندرويد. غيّر DL_BASE إذا رفعت الملفات بمكان ثاني.
const DL_BASE = 'https://github.com/midadapps/midadapps.github.io/releases/latest/download/';
document.querySelectorAll('[data-apk]').forEach(a => { a.href = DL_BASE + 'midad-' + a.dataset.apk + '.apk'; });
"""

open(os.path.join(HERE, "site.css"), "w", encoding="utf-8").write(CSS)
open(os.path.join(HERE, "site.js"), "w", encoding="utf-8").write(JS)
open(os.path.join(HERE, "index.html"), "w", encoding="utf-8").write(index_page())
for f in FACES:
    open(os.path.join(HERE, f["id"] + ".html"), "w", encoding="utf-8").write(face_page(f))
print("ok")
