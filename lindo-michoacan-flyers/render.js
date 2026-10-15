// Renderiza cada flyer de src/*.html a png/*.png
const { chromium } = require('playwright');
const fs = require('fs'), path = require('path');
(async () => {
  const src = path.join(__dirname, 'src'), out = path.join(__dirname, 'png');
  const browser = await chromium.launch();
  for (const f of fs.readdirSync(src).filter(f => f.endsWith('.html'))) {
    const h = f.includes('story') ? 1920 : 1350;
    const page = await browser.newPage({ viewport: { width: 1080, height: h } });
    await page.goto('file://' + path.join(src, f), { waitUntil: 'networkidle' });
    await page.evaluate(() => document.fonts.ready);
    await page.screenshot({ path: path.join(out, f.replace('.html', '.png')) });
    await page.close();
  }
  await browser.close();
})();
