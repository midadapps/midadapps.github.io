// روابط تحميل ملفات الأندرويد. غيّر DL_BASE إذا رفعت الملفات بمكان ثاني.
const DL_BASE = 'https://github.com/midadapps/midadapps.github.io/releases/latest/download/';
document.querySelectorAll('[data-apk]').forEach(a => { a.href = DL_BASE + 'midad-' + a.dataset.apk + '.apk'; });
