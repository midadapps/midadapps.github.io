# يولّد صفحات موقع مِداد (الرئيسية + صفحة لكل وجه). شغّله بعد أي تعديل بالنصوص:  python build_site.py
import html, os

HERE = os.path.dirname(os.path.abspath(__file__))
WA = "9647738181860"  # واتساب المبيعات

FACES = [
    dict(id="clinic", name="مِداد عيادات", short="العيادات والأطباء",
         tag="عيادتك منظّمة من هاتفك", sub="الدور بلا ازدحام، وملف كامل لكل مريض، والوصفة والتذكير يصلان إلى هاتفه.",
         price="جرّبه أسبوعاً مجاناً، ثم 12$ شهرياً أو 120$ سنوياً.",
         feats=[("calendar", "الدور والمواعيد", "من وصل ومن ينتظر ومن انتهى، وتضيف السكرتيرة المراجع بضغطة فيأخذ رقم دوره."),
                ("doc", "ملف كامل لكل مريض", "الزيارات السابقة والتشخيص والوصفات، وصور التحاليل والأشعة وفيديو العمليات."),
                ("warn", "تنبيه الحساسية", "إذا كان لدى المريض حساسية من دواء يظهر تنبيه واضح في ملفه."),
                ("rx", "الوصفة على هاتف المريض", "يصله تشخيصه ووصفته عبر تطبيق مِداد أو الواتساب."),
                ("chat", "المحادثة مع المريض", "رسائل مباشرة بين العيادة والمريض داخل التطبيق."),
                ("clock", "تذكير المواعيد", "رسالة تذكير للمراجع قبل موعده، وتذكير بالمبالغ المتبقية."),
                ("calplus", "الحجز من التطبيق", "يطلب المريض موعداً، والعيادة توافق أو تقترح وقتاً آخر."),
                ("users", "لكل موظف صلاحياته", "تسجّل السكرتيرة المواعيد والدفع، ولا ترى الملاحظات الطبية."),
                ("chart", "الحسابات والتقارير", "أجور المعاينات والمستلم والمصاريف وصافي كل شهر.")],
         video=None, video2=None,
         who="يستعمل الطبيب والسكرتيرة «مِداد عيادات»، ويستعمل المراجع تطبيق «مِداد»."),
    dict(id="generator", name="مِداد مولّدات", short="أصحاب المولّدات",
         tag="مولّدتك في جيبك", sub="المشتركون والأمبيرات والجباية، وتذكير غير المسددين بالواتساب بضغطة واحدة.",
         price="جرّبه أسبوعاً مجاناً، ثم 12$ شهرياً أو 120$ سنوياً.",
         feats=[("users", "المشتركون والأمبيرات", "كل مشترك بخطوطه وأمبيراته ومنطقته وعنوانه."),
                ("money", "الجباية الشهرية", "تسجيل التسديد في ثوانٍ، ومعرفة من سدّد ومن بقي عليه."),
                ("wa", "تذكير غير المسددين", "إرسال متتابع بالواتساب لكل غير المسددين، مع علامة «أُرسل» لكل واحد."),
                ("edit", "تعديل سعر الشهر", "تغيير سعر الأمبير لجميع المشتركين دفعة واحدة."),
                ("wallet", "فاتورة الشهر والمصاريف", "الوقود والصيانة والرواتب، والصافي الحقيقي لكل شهر."),
                ("megaphone", "تبليغ المشتركين", "إطفاء أو صيانة أو تغيير في التشغيل، يصل إلى جميع المشتركين."),
                ("chart", "التقارير الشهرية", "الجباية والديون والصافي لكل شهر."),
                ("eye", "المشترك يرى حسابه", "يتابع المشترك اشتراكه وديونه من تطبيق «مِداد».")],
         video=None, video2=None,
         who="يستعمل صاحب المولّدة والجابي «مِداد مولّدات»، ويستعمل المشترك تطبيق «مِداد»."),
    dict(id="installments", name="مِداد أقساط", short="محلات الأقساط",
         tag="أقساطك منظّمة، ولا يضيع دينار", sub="الزبائن والكفلاء وخطط الأقساط، وتذكير المتأخرين بالواتساب.",
         price="جرّبه أسبوعاً مجاناً، ثم 12$ شهرياً أو 120$ سنوياً.",
         feats=[("user", "الزبائن والكفلاء", "الاسم والهاتف والعنوان والكفيل والدين السابق."),
                ("calendar", "خطط الأقساط", "السعر الكلي والمقدّمة وعدد الأقساط، شهرياً أو أسبوعياً، وتاريخ أول قسط."),
                ("money", "تسديد القسط", "سجّل الدفعة في ثوانٍ، ويتحدّث الحساب تلقائياً."),
                ("warn", "المتأخرون بوضوح", "يظهر المتأخر بلون واضح، فتعرف من تتابع اليوم."),
                ("wa", "تذكير المتأخرين بالواتساب", "رسالة تذكير لكل متأخر بضغطة واحدة."),
                ("doc", "البيع بالدَّين والنقد", "كل حركة مسجّلة: بيع وتسديد ودَين."),
                ("list", "المخزون", "البضاعة والكميات وأسعار البيع."),
                ("users", "لكل موظف صلاحياته", "يرى كل موظف ويعمل ما تسمح له به فقط.")],
         video=None, video2=None,
         who="يستعمل صاحب المحل وموظفوه «مِداد أقساط»، ويستعمل الزبون تطبيق «مِداد»."),
    dict(id="hajj", name="مِداد حج وعمرة", short="حملات الحج والعمرة",
         tag="حملتك معك في كل خطوة", sub="الحجاج والغرف والمجموعات والبرنامج اليومي، والبث الصوتي المباشر، وزر «أنا تائه»، بواجهة واضحة لكبار السن.",
         price="جرّبه أسبوعاً مجاناً، ثم 17$ شهرياً أو 170$ سنوياً.",
         feats=[("pilgrim", "ملف كامل لكل حاج", "الهاتفان والصورة والجواز والتأشيرة والمحرم ورقم السوار والمعلومات الصحية."),
                ("bed", "الغرف والمجموعات والحافلات", "كل حاج في غرفته ومجموعته، وعدّ الحجاج عند الحافلة بضغطة."),
                ("calendar", "برنامج الرحلة ونقاط التجمع", "يوماً بيوم، ويعرف الحاج الفقرة القادمة ويصل إلى نقطة التجمع بالخريطة."),
                ("live", "بث مباشر مثل الراديو", "يتكلم المرشد فيسمعه الحجاج في اللحظة نفسها، حتى وهواتفهم في جيوبهم."),
                ("siren", "زر «أنا تائه»", "يصل موقع الحاج إلى الحملة فوراً، وإذا ضعف الإنترنت تُجهَّز رسالة نصية للمرشد."),
                ("question", "الأسئلة والطلبات", "يسأل الحاج المرشد كتابةً أو بصوته، ولا يرى سؤاله غيره."),
                ("megaphone", "الإعلانات", "إعلان مثبّت في الأعلى، والبقية تُحذف بعد 24 ساعة، وتعرف من اطّلع عليها."),
                ("idcard", "بطاقة الحاج", "بطاقة فيها الفندق والغرفة وهاتف الحملة إذا تاه."),
                ("eye", "خصوصية", "الملاحظات الصحية والداخلية تراها الإدارة فقط.")],
         video=None, video2=None,
         who="يستعمل صاحب الحملة والمرشد والحاج «مِداد حج وعمرة». يبحث الحاج عن حملته في التطبيق ويرسل طلب الانضمام، وتوافق الحملة بضغطة."),
    dict(id="school", name="مِداد مدارس", short="المدارس والروضات",
         tag="المدرسة والأهل في مكان واحد", sub="الحضور والدرجات والواجبات والتبليغات، ويتابع ولي الأمر ابنه من هاتفه.",
         price="جرّبه أسبوعاً مجاناً، ثم 17$ شهرياً أو 170$ سنوياً.",
         feats=[("users", "الصفوف والطلاب", "كل صف بطلابه وموادّه وجدوله الأسبوعي."),
                ("check", "التحضير اليومي", "يحضّر المعلم الصف في ثوانٍ، ويعرف الأهل فوراً."),
                ("doc", "الدرجات وبطاقة التقرير", "الدرجات لكل مادة، وبطاقة تقرير جاهزة."),
                ("list", "الواجبات ونشاطات الصف", "ينشر المعلم الواجب، ويطّلع عليه الأهل."),
                ("megaphone", "التبليغات", "عطلة أو اجتماع أو تنبيه، يصل إلى جميع أولياء الأمور، وتعرف من قرأه."),
                ("chat", "ملاحظات المعلم والشكاوى", "تواصل منظّم بين المدرسة والأهل."),
                ("money", "الأقساط المدرسية", "من سدّد ومن بقي عليه."),
                ("user", "لكل معلم صلاحياته", "يرى كل معلم صفوفه فقط.")],
         video=None, video2=None,
         who="تستعمل الإدارة والمعلمون وأولياء الأمور «مِداد مدارس»، ويطلب ولي الأمر الانضمام إلى مدرسة ابنه من التطبيق."),
]

CSS = """
:root{--bg:#110d07;--bg2:#17120a;--card:#1c1710;--line:#3a3220;--gold:#e3b75a;--gold2:#f2d589;--gold3:#b8862f;--ink:#f4efe2;--muted:#b7b2a4}
*{box-sizing:border-box;margin:0;padding:0}
html{scroll-behavior:smooth}
body{font-family:Tajawal,system-ui,sans-serif;background:var(--bg);color:var(--ink);line-height:1.7;overflow-x:hidden}
a{color:inherit}
.wrap{max-width:1080px;margin:0 auto;padding:0 18px}
header{position:sticky;top:0;z-index:5;background:#110d07e6;backdrop-filter:blur(10px);border-bottom:1px solid #2a2418}
header .wrap{display:flex;align-items:center;justify-content:space-between;height:64px}
.brand{display:flex;align-items:center;gap:10px;text-decoration:none;font-weight:800;font-size:22px}
.brand img{width:38px;height:38px;border-radius:10px;box-shadow:0 0 0 1.5px #e3b75a77}
nav{display:flex;align-items:center;gap:18px}
nav a{text-decoration:none;color:var(--muted);font-weight:700;font-size:15px;display:inline-block;unicode-bidi:isolate;white-space:nowrap}
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
.feat .e{width:48px;height:48px;border-radius:50%;border:1px solid #d9b868aa;display:grid;place-items:center;background:#14100a}
.feat .e img{width:26px;height:26px}
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
<nav><a href="index.html#apps">التطبيقات</a><a class="hide" href="index.html#customers">للزبائن</a><a href="https://wa.me/{wa}">تواصل معنا</a></nav></div></header>
"""
FOOT = """<footer><div class="wrap">
<p>مِداد — عملك كله في جيبك</p>
<p style="margin-top:6px">للاستفسار والعروض: <a href="https://wa.me/{wa}">واتساب</a></p>
</div></footer>
<script src="site.js"></script>
</body></html>"""

def e(s): return html.escape(s, quote=True)

def dl_buttons(face_id, label_app):
    return f"""<div class="dl">
<a class="btn gold" data-apk="{face_id}" href="#">تحميل للأندرويد</a>
<span class="btn soon">آيفون — قريباً</span>
<span class="btn soon">ويندوز — قريباً</span>
</div>
<p class="note">إذا طلب الهاتف السماح بالتثبيت من «مصادر غير معروفة»، فوافق مرة واحدة وأكمل التثبيت.</p>"""

def face_page(f):
    feats = "".join(f'<div class="feat"><div class="e"><img src="img/i/{x}.svg" alt=""></div><b>{e(t)}</b><p>{e(d)}</p></div>' for x, t, d in f["feats"])
    vids = ""
    if f["video"]:
        items = [(f["video"], "شرح لصاحب النشاط" if f["id"] != "clinic" else "جولة بالتطبيق")]
        if f["video2"]: items.append((f["video2"], "شرح للحاج"))
        vids = '<section class="band"><div class="wrap"><h2>شاهده بنفسك</h2><p class="lead">فيديو قصير بشاشات التطبيق الحقيقية</p><div class="vids">' + \
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
<section><div class="wrap"><h2>ماذا يقدّم {e(f['name'])}؟</h2><p class="lead">ميزات حقيقية موجودة في التطبيق اليوم</p><div class="grid">{feats}</div></div></section>
{vids}
<section><div class="wrap"><h2>كيف تبدأ؟</h2><p class="lead">{e(f['who'])}</p><div class="steps">
<div class="step"><b>حمّل التطبيق</b><p>من الزر في الأعلى، وثبّته على هاتفك.</p></div>
<div class="step"><b>أنشئ حسابك</b><p>برقم هاتفك، ثم أنشئ نشاطك باسمه.</p></div>
<div class="step"><b>أضف فريقك</b><p>يطلب كل موظف أو زبون الانضمام من التطبيق، وتوافق عليه بضغطة.</p></div>
</div>
<div class="dl" style="margin-top:30px"><a class="btn ghost" href="https://wa.me/{WA}?text={e('السلام عليكم، أودّ معرفة المزيد عن ' + f['name'])}">اسألنا بالواتساب</a></div>
</div></section>
</main>"""
    page += FOOT.format(wa=WA)
    return page

def index_page():
    cards = "".join(f'<a class="face" href="{f["id"]}.html"><img src="img/{f["id"]}.png" alt=""><b>{e(f["name"])}</b><span>{e(f["tag"])} — {e(f["short"])}</span><em>التفاصيل والتحميل ←</em></a>' for f in FACES)
    why = [("live", "يعمل بلا إنترنت", "تعمل كالمعتاد، وعند عودة الإنترنت يتحدّث كل شيء تلقائياً."),
           ("users", "فريقك بصلاحياته", "لكل موظف حسابه، وأنت تحدد ما يراه وما يعمله."),
           ("wa", "واتساب وإشعارات", "تذكير الزبائن والمتأخرين بضغطة، وإشعارات فورية."),
           ("check", "عربي ومن بيئتنا", "مصمم لأعمالنا وأسعارنا، وسهل حتى لكبار السن.")]
    whyh = "".join(f'<div class="feat"><div class="e"><img src="img/i/{x}.svg" alt=""></div><b>{e(t)}</b><p>{e(d)}</p></div>' for x, t, d in why)
    page = HEAD.format(title="مِداد — عملك كله في جيبك", desc="تطبيقات عربية لإدارة العيادات والمولّدات ومحلات الأقساط وحملات الحج والمدارس.", img="midad", wa=WA)
    page += f"""<main>
<section class="hero"><div class="wrap">
<img class="icon" src="img/midad.png" alt="مِداد">
<h1>عملك كله في جيبك</h1>
<p>تطبيقات عربية لإدارة العيادات والمولّدات ومحلات الأقساط وحملات الحج والمدارس، كل تطبيق مصمم لعملك بالضبط، ويعمل حتى بلا إنترنت.</p>
<div class="dl"><a class="btn gold" href="#apps">اختر تطبيقك</a></div>
</div></section>
<section id="apps"><div class="wrap"><h2>اختر تطبيقك</h2><p class="lead">كل تطبيق مصمم لنوع عمل واحد، بمصطلحاته وشاشاته</p><div class="grid">{cards}</div></div></section>
<section class="band" id="customers"><div class="wrap">
<div class="cust"><img src="img/midad.png" alt=""><div><b>مِداد — للزبائن</b><p style="color:var(--muted)">مراجع عيادة أو مشترك مولّدة أو زبون أقساط؟ حمّل «مِداد» وتابع مواعيدك ووصفاتك وحسابك، وكل الجهات التي تتعامل معها في مكان واحد.</p></div>
<a class="btn gold" data-apk="midad" href="#">تحميل للأندرويد</a></div>
</div></section>
<section><div class="wrap"><h2>لماذا مِداد؟</h2><p class="lead">الأساس القوي نفسه في جميع التطبيقات</p><div class="why">{whyh}</div>
<div class="dl"><span class="btn soon">آيفون — قريباً</span><span class="btn soon">ويندوز — قريباً</span></div></div></section>
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
